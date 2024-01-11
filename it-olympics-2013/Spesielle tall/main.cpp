#include <iostream>
#include <sstream>
#include <string>


using namespace std;

int main()
{
    long long m = 20000;
    long long n = 30000;

    int o;

    string M;
    string N;
    ostringstream convertM;
    ostringstream convertN;
    convertM << m;
    convertN << n;
    M = convertM.str();
    N = convertN.str();


    int strM = sizeof(M)/sizeof(M[0]);
    int strN = sizeof(N)/sizeof(N[0]);

    cout<<M<<endl;
    cout<<N<<endl;
    cout<<M[0]<<endl;
    cout<<N[0]<<endl;


    /*for(int i = m;i<=n;i++)
    {
       long long multi = int(M[0]);
       long long addi = int(M[0]);

       // multi = int(M[0]) * int(M[1]);
        for(int k = 1;k<strM-1;k++)
        {
            multi = multi * int(M[k]);
        }
        for(int k = 1;k<strM-1;k++)
        {
            addi = addi + int(M[k]);
        }
        if (addi == multi)
            o++;


    }*/
    //cout<<o;
    /*cin>>m;
    cin>>n;*/
    int multi = M[0];
    cout<<"Multi: "<<multi<<endl;
    long long addi = M[0];
    cout<<"Addi:" <<addi<<endl;

    for(int k = 1;k<strM-1;k++)
        {
            multi = multi * int(M[k]);
        }
    cout<<multi<<endl;
    for(int k = 1;k<strM-1;k++)
        {
            addi = addi + int(M[k]);
        }
    cout<<addi<<endl;
    if (addi == multi)
            o++;





    return 0;
}
