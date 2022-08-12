#include <iostream>
#define LISTLEN

using namespace std;

typedef struct{
    int *elem;
    int count;
}

int main(int argc, char *argv[])
{
    int i;
    int* j;
    i = 1;
    j = &i;
    cout << "i is " << *j << endl;
    return 0;
}
