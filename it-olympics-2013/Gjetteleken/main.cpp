#include <iostream>

using namespace std;

int main()
{
    int svar;
    int antallGjetninger;
    int gjetning;

    cin>>svar>>antallGjetninger;

    for(int u=0;u<antallGjetninger;u++)
    {
        cin>>gjetning;
        if(gjetning>svar){
            cout<<"FOR MYE\n";//<<endl;
        }
        else if(gjetning<svar){
            cout<<"FOR LITE\n";//<<endl;
        }
        else{
            cout<<"RIKTIG\n";//<<endl;
        }
    }
    return 0;
}
