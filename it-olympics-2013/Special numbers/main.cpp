#include <iostream>
#include <vector>

using namespace std;

int main()
{
    long long m;
    long long n;
    cin>>m;
    cin>>n;
    int counter = 0;

    for (long long i=m;i<n;i++)
    {
        vector<int> tall;
        int a = 0;
        long long k = i;
        while(k>0)
        {
            tall.push_back(k%10);
            //cout<<tall[k];
            k = k/10;
            a++;
        }
        //cout<<tall.size()<<endl;

       /* for(int j = 0;j<tall.size();j++)
        {
           cout<<tall[j];
        }*/
        //cout<<endl;
        long long multi = tall[0];
        for(int l = 0;l<tall.size()-1;l++)
        {
            multi = multi * tall[l+1];
        }
        //cout<<multi<<endl;

        long long addi = tall[0];
        for(int l = 0;l<tall.size()-1;l++)
        {
            addi = addi + tall[l+1];
        }
        //cout<<addi<<endl;
        if(addi == multi)
        {
            counter++;
        }

    }
    cout<<counter;

    return 0;
}
