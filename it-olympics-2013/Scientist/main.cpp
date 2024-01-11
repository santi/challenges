#include <iostream>
#include <cstdlib>

using namespace std;

void sorter(unsigned long long arrayet[],int str);

int main()
{
    int antallForskjellige;
    cin>>antallForskjellige;
    cout<<RAND_MAX<<"\n";
    unsigned long long ressurser[antallForskjellige];
    for(int i=0;i<antallForskjellige;i++)
    {
        //cin>>ressurser[i];
        ressurser[i]=100000000000;
        //ressurser[6] = 99999999999;
    }
    sorter(ressurser,antallForskjellige);
    //cout<<"SORTERT!\n";
   /* for(int h =0;h<antallForskjellige;h++)
    {
        cout<<ressurser[h]<<" "<<h<<"\n";
    }*/

    long long antallHus=0;
    while(ressurser[2] > 0)
    {
        antallHus += ressurser[2];
        ressurser[0]-=ressurser[2];
        ressurser[1]-=ressurser[2];
        ressurser[2]=0;

        sorter(ressurser,antallForskjellige);
    }
    cout<<antallHus;
    return 0;
}


void sorter(unsigned long long arrayet[], int str)
{
  int i, j, small;
  unsigned long long temp;

  for (i = str - 1; i > 0; i--)
   {
    small = 0;

    for (j = 1; j <= i; j++)
     {
      if (arrayet[j] < arrayet[small])
       {
        small = j;
       }
     }

    temp = arrayet[small];
    arrayet[small] = arrayet[i];
    arrayet[i] = temp;
   }
}
