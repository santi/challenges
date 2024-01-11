#include <iostream>

using namespace std;

int main()
{
    cout << "Hello Hyperion!" << endl;
    int bredde;
    int hoyde;

    cin>>bredde>>hoyde;

    char labyrinthArr[hoyde][bredde];

    for(int i = 0; i<hoyde;i++)
    {
        for(int j = 0;j<bredde;j++)
        {
            cin>>labyrinthArr[i][j];
        }
    }
    int startX=0;
    int startY=0;

    int malX=0;
    int malY=0;

    //FINNER VIKTIGE POSISJONER
    for(int i = 0; i<hoyde;i++)
    {
        for(int j = 0;j<bredde;j++)
        {
            if(labyrinthArr[i][j] == 'M')
            {
                malX = j;
                malY = i;
            }
            else if(labyrinthArr[i][j] == 'S')
            {
                startX = j;
                startY = i;
            }

        }
    }


    /*cout<<malX<<" "<<malY<<endl;
    cout<<startX<<" "<<startY<<endl;



    //PRINTING ARRAY
    for(int i = 0;i<bredde;i++)
    {
        for(int j = 0;j<hoyde;j++)
        {
            cout<<labyrinthArr[i][j]<<" ";
        }
        cout<<endl;
    }*/

    //REGNER UT MANHATTAN-AVSTAND


    return 0;
}
