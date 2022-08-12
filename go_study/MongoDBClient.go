package main

import (
	"bufio"
	"crypto/md5"
	"encoding/hex"
	"flag"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
	"time"

	"github.com/golang/glog"
	"github.com/weilaihui/fdfs_client"
	"gopkg.in/mgo.v2"
	"gopkg.in/mgo.v2/bson"
)

const dbName string = "meizu-image"

type image struct {
	ID         bson.ObjectId `bson:"_id"`
	BizID      string        `bson:"name"`
	StorageID  int           `bson:"storageId"`
	URL        string        `bson:"url"`
	Size       int           `bson:"size"`
	Files      []file        `bson:"files"`
	UpdateTime time.Time     `bson:"updateTime"`
}

type file struct {
	Model string `bson:"model"`
	MD5   string `bson:"md5"`
	Path  string `bson:"path"`
	Size  int    `bson:"size"`
}

type ucDel struct {
	mongoClient *mgo.Session
	fdfsClient  *fdfs_client.FdfsClient
}

func getURLFromUID(uid string) string {
	//根据uid获取URL
	tempUID := uid
	// if len(tempUID)%2 == 1 {
	// 	tempUID += "0"
	// }

	for len(tempUID) < 10 {
		tempUID += "0"
	}

	var url string
	for i := 0; i < len(tempUID); i += 2 {
		url += tempUID[i:i+2] + "/"
	}
	url = "uc:/" + url + uid
	return url
}

func getUIDFromURL(url string) string {
	//获取uid
	stringList := strings.Split(url, "/")
	return stringList[len(stringList)-1]
}

func getFdfsPath(path string) string {
	//获取path
	return strings.Join(strings.Split(path, "@"), "/")
}

func getImageID(uid string) string {
	//计算id
	url := getURLFromUID(uid)
	md5Ctx := md5.New()
	md5Ctx.Write([]byte(url))
	return hex.EncodeToString(md5Ctx.Sum(nil))
}

func getUIDFromFile(fileName string) ([]string, error) {
	file, err := os.Open(fileName)
	defer file.Close()
	if err != nil {
		glog.Errorf("open file %s faild", fileName)
		return []string{}, err
	}
	glog.Infof("open file %s success, try to read uid", fileName)

	var uidList []string
	reader := bufio.NewReader(file)
	for {
		line, err := reader.ReadString('\n')
		if err == io.EOF {
			break
		} else if err != nil {
			glog.Errorf("read file %s error", fileName)
			return []string{}, err
		} else {
			uidList = append(uidList, strings.Split(line, "\n")[0])
		}
	}
	glog.Infof("read uid success")

	return uidList, nil
}

func (p ucDel) getImageInfo(uid string) (image, error) {
	id := getImageID(uid)
	url := getURLFromUID(uid)

	var imageInfoList []image
	col := p.mongoClient.DB(dbName).C("image")
	err := col.FindId(id).All(&imageInfoList)
	if err != nil {
		glog.Warningf("get uid %s id %s image info fail", uid, id)
		return image{}, err
	}

	//根据id获取，有且仅有一个
	if len(imageInfoList) > 1 {
		return image{}, fmt.Errorf("uid %s url %s id %s image info more than 1", uid, url, id)
	}

	//没有数据的情况
	if len(imageInfoList) < 1 {
		return image{}, fmt.Errorf("uid %s url %s id %s not found image info", uid, url, id)
	}
	imageInfo := imageInfoList[0]

	//去掉在2018-03-01之后更新头像的
	lastUpadetTime := time.Date(2018, 3, 1, 0, 0, 0, 0, time.Local)
	if imageInfo.UpdateTime.After(lastUpadetTime) {
		return image{}, fmt.Errorf("uid %s id %s url %s image UpdateTime %s after 2018-03-01", uid, id, imageInfo.URL, imageInfo.UpdateTime.String())
	}

	glog.Infof("get uid %s, id %s, url %s, image info success, have %d image", uid, id, imageInfo.URL, len(imageInfo.Files))
	for _, v := range imageInfo.Files {
		glog.Infof("uid %s id %s have image path %s model %s", uid, id, v.Path, v.Model)
	}
	return imageInfo, nil
}

func (p ucDel) downloadImage(imageInfo image) error {
	var err error
	failNumber := 0
	for _, v := range imageInfo.Files {
		fileName := "image_" + v.MD5 + "_" + v.Model
		response, err := p.fdfsClient.DownloadToFile(fileName, getFdfsPath(v.Path), 0, 0)
		if err != nil {
			glog.Errorf("download uid %s, image fail", getUIDFromURL(imageInfo.URL))
			failNumber++
			continue
		}
		glog.Infof("download uid %s, image success, fileID %s", getUIDFromURL(imageInfo.URL), response.RemoteFileId)
	}
	if failNumber > 0 {
		return err
	}
	return nil
}

func (p ucDel) deleteImage(imageInfo image) error {
	err := p.deleteFdfsImage(imageInfo)
	if err != nil {
		return err
	}

	err = p.deleteMongoImage(imageInfo)
	if err != nil {
		return err
	}
	return nil
}

func (p ucDel) deleteFdfsImage(imageInfo image) error {
	var err error
	for _, v := range imageInfo.Files {
		path := getFdfsPath(v.Path)
		err = p.fdfsClient.DeleteFile(path)
		if err != nil {
			glog.Errorf("delete uid %s path %s model %s image from fdfs fail", getUIDFromURL(imageInfo.URL), path, v.Model)
			glog.Errorln(err)
			return err
		}
		glog.Infof("delete uid %s path %s model %s image from fdfs success", getUIDFromURL(imageInfo.URL), path, v.Model)
	}
	return nil
}

func (p ucDel) deleteFdfsImageByStr(path string) error {
	err := p.fdfsClient.DeleteFile(path)
	if err != nil {
		glog.Errorf("delete path %s image from fdfs fail", path)
		glog.Errorln(err)
		return err
	}
	return nil
}

func (p ucDel) deleteMongoImage(imageInfo image) error {
	col := p.mongoClient.DB(dbName).C("image")
	uid := getUIDFromURL(imageInfo.URL)
	id := getImageID(uid)
	err := col.RemoveId(id)
	if err != nil {
		glog.Errorf("delete uid %s id %s image info from mongo fail", uid, id)
		return err
	}
	glog.Infof("delete uid %s id %s image info from mongo success", uid, id)
	return nil
}

func main() {
	flag.Parse()
	defer glog.Flush()

	fileName := "./image"
	uidList, err := getUIDFromFile(fileName)
	if err != nil {
		glog.Fatal(err)
		return
	}

	// mgoClient, err := mgo.Dial("10.3.172.97:28030,10.3.172.99:28030")
	mgoClient, err := mgo.Dial("172.16.177.147:21001")
	defer mgoClient.Close()
	if err != nil {
		glog.Fatal(err)
		return
	}

	fdfsClient, err := fdfs_client.NewFdfsClient("./client.conf")
	if err != nil {
		glog.Fatal(err)
		return
	}
	ucDeler := ucDel{mgoClient, fdfsClient}
	for _, uid := range uidList {
		uidNum, err := strconv.Atoi(uid)
		if uidNum < 600000 || uidNum > 150100705 {
			glog.Warningf("uid %s not between 600000 and 150100705", uid)
			continue
		}

		imageInfo, err := ucDeler.getImageInfo(uid)
		if err != nil {
			glog.Warningln(err)
			continue
		}
		err = ucDeler.downloadImage(imageInfo)
		// err = ucDeler.deleteImage(imageInfo)
		if err != nil {
			glog.Warningln(err)
			continue
		}
	}
}
