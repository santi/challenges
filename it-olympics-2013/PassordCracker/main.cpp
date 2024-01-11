#include <iostream>
#include <string>

using namespace std;

//NOTES:
// 48 - 57 ER 0 - 9
//97 - 122 ER a - z



int main()
{
    int tall = 122;
    char chChar = tall;
    char chChar2 = 'g';
    char chArr[2] = {chChar,chChar2};
    chArr[0] = chChar;
    chArr[1] = chChar2;
    //cout<<chArr<<endl;
    std::string tekst;
    tekst = {chChar,chChar2};
    cout<<tekst<<endl;


    string password = "c";






    cout<<password << endl;

    int counter = 0;

    /*for(int i6 = 48;i6<123;i6++)
    {
        for(int i5 = 48;i5<123;i5++)
        {
            for(int i4 = 48;i4<123;i4++)
            {
                for(int i3 = 48;i3<123;i3++)
                {*/
                    /*for(int i2 = 48;i2<123;i2++)
                    {
                        for(int i1 = 97;i1<123;i1++)
                        {

                            char c1 = i1;
                            string solution;
                            solution = c1;
                            if (password ==solution)
                            {
                                cout<<counter;
                                i1 = 123;
                            }
                            counter++;
                        }
                        char c2 = i2;

                    }

                /*}

            }

        }

    }*/




    return 0;
}
