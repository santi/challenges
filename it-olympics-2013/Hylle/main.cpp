#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    vector<int> tall;
    tall.push_back(4);
    tall.push_back(8);
    swap(tall[0],tall[1]);
    cout<<tall[1]<<endl;

    sort(tall.begin(),tall.end());
    cout<<tall[1]<<endl;

    int i = 0;
    do
    {
        i++;
    } while(i<5);
    cout<<i<<endl;

    return 0;
}
