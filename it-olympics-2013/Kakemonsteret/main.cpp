#include <iostream>
#include <string>
#define ARRAY_SIZE(array) (sizeof((array))/sizeof((array[0])))

using namespace std;

int main()
{
    unsigned long long tid = 0;
    int kakerTopp = 0;
    int antallNaboer;//N
    int antallKaker;//K
    int etasjeKakemonster;//E
    cin>>antallNaboer>>antallKaker>>etasjeKakemonster;
    //SO FAR SO GOOD
    int naboArray[antallNaboer][3];
    char charHolder; //n = 110, o = 111
    int etasjeHolder;
    for(int i = 0;i<antallNaboer;i++)
    {
        cin>>etasjeHolder>>charHolder;
        naboArray[i][0] = etasjeHolder-1;
        naboArray[i][1] = (int)charHolder;
        naboArray[i][2] = 0;
        //naboArray[i][3] = 0;
        //cout<<naboArray[i][1]<<endl;
    }
    //PRINT
    /*for (int i=0; i<antallNaboer; i++)
    {
        for (int j=0; j<3; j++)
        {
            cout<<naboArray[i][j]<<" ";
        }
        cout<<endl;
    }*/

    //SORTER
    for(int rad = 0; rad <antallNaboer;rad++)
    {
        for(int rad2 = 0; rad2 < antallNaboer;rad2++)
        {
            if(naboArray[rad][0] < naboArray[rad2][0])
            {
                swap(naboArray[rad][0],naboArray[rad2][0]);
                swap(naboArray[rad][1],naboArray[rad2][1]);
                swap(naboArray[rad][2],naboArray[rad2][2]);
                /*int temp[3]=naboArray[rad];
                naboArray[rad] = naboArray[rad2];
                naboArray[rad2] = temp;*/
            }
        }
    }
    //SORT OPP/NED
    for (int i = 0; i<antallNaboer-1;i++)
    {
        if(naboArray[i][1] == 111 && naboArray[i+1][1] == 110 && naboArray[i][0] == naboArray[i+1][0])
        {
            naboArray[i][1] = 110;
            naboArray[i+1][1] = 111;
        }
    }

    //PRINT ETTER SORT
    /*cout<<endl;
    for (int i=0; i<antallNaboer; i++)
    {
        for (int j=0; j<3; j++)
        {
            cout<<naboArray[i][j]<<" ";
        }
        cout<<endl;
    }*/

    while(kakerTopp < antallKaker)
    {
        //BYTTER PLASSER HVIS DET TRENGS
        for(int i = 0; i<antallNaboer;i++)
        {
            if(naboArray[i][0] + 1 == naboArray[i+1][0] && naboArray[i][1]==111&&naboArray[i+1][1]==110)
            {
                swap(naboArray[i],naboArray[i+1]);
            }
        }
        for(int i = 0; i<antallNaboer;i++)
        {
            //GÅ!
            switch(naboArray[i][1])
            {
            case 110:
                naboArray[i][0]--;
                break;
            case 111:
                naboArray[i][0]++;
                break;
            }
        }

        //SJEKKER TOPP/BUNN
        /*if(naboArray[0][0]== 0)
        {
            naboArray[0][2] = 1;
            naboArray[0][1] = 111;
        }
        if(naboArray[antallNaboer-1][0] == etasjeKakemonster-1)
        {
            if(naboArray[antallNaboer-1][2]==1)
            {
                naboArray[antallNaboer-1][2] = 0;
                kakerTopp++;
            }
            naboArray[antallNaboer-1][1] = 110;
        }*/

        for(int i = 0;i<antallNaboer;i++)
        {
            if (naboArray[i][0] == etasjeKakemonster - 1)
            {
                if (naboArray[i][2] == 1)
                {
                    naboArray[i][2] = 0;
                    kakerTopp++;
                }
                naboArray[i][1] = 110;
            }
            else if (naboArray[i][0] == 0)
            {
                naboArray[i][2] = 1;
                naboArray[i][1] = 111;
            }
        }
        tid += 10;
        /*cout<<endl;
        for (int i=0; i<antallNaboer; i++)
        {
            for (int j=0; j<3; j++)
            {
                cout<<naboArray[i][j]<<" ";
            }
            cout<<endl;
        }*/
    }
    cout<<tid;

    return 0;
}

