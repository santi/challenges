#include <iostream>
//#include <cstdlib>
#include <cstring>

using namespace std;

int mult(int x,int y);
int addi(int x,int y);
int subt(int x,int y);
int divi(int x,int y);
int kalkulator();

int tall1;
int tall2;
char funksjon;
string valg;

int main()
{
    cout<<"Velkommen til min kalkulator!"<<endl;
    kalkulator();
}
int kalkulator()
{
    cout<<"Vennligst oppgi tall nr 1:"<<endl;
    cin>>tall1;
    cout<<"Vennligst oppgi tall nr 2:"<<endl;
    cin>>tall2;
    cout<<"Hva ønsker du å gjøre med disse tallene?\na=Addisjon, s=Subtraksjon, m=Multiplikasjon, d=Divisjon"<<endl;
    cin>>funksjon;

    switch(funksjon){
    case 'a':
        cout<<"Svaret blir:"<<endl;
        cout<<addi(tall1,tall2)<<endl;
        break;
    case 's':
        cout<<"Svaret blir:"<<endl;
        cout<<subt(tall1,tall2)<<endl;
        break;
    case 'm':
        cout<<"Svaret blir:"<<endl;
        cout<<mult(tall1,tall2)<<endl;
        break;
    case 'd':
        cout<<"Svaret blir:"<<endl;
        cout<<divi(tall1,tall2)<<endl;
        break;
    default:
        cout<<"Vennligst oppgi en gyldig bokstav:"<<endl;
        cin>>funksjon;
    }
    cout<<"Vil du utføre en ny operasjon?"<<endl;
    cin>>valg;
    if(valg=="ja"||valg=="Ja"||valg=="JA"){
        kalkulator();
    }
    else
        return 0;
}
/*int recieveTall1()
{
    cin>>tall1;
    if(tall1!=int)
        recieveTall1();
}*/

int addi(int x,int y)
{
    return x+y;
}
int subt(int x,int y)
{
    return x-y;
}
int mult(int x,int y)
{
    return x*y;
}
int divi(int x,int y)
{
    return x/y;
}
