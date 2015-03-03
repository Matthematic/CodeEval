#include <iostream>
#include <fstream>
using namespace std;


int main(int argc, char* argv[])
{
    ifstream file;
    string test;
    file.open(argv[1]);
    char delimiter = ' ';
    while (!file.eof()) 
    {
        int count = 0;
        getline(file, test);
        if (test.length() == 0)
            continue; //ignore all empty lines
        else 
        {
                test.erase(test.find_last_not_of(" \n\r\t")+1); //trim whitespace from ends of the string
            //counts number of spaces after trimming, so the number of words is count+1
                for (unsigned int i = 0;i < test.length();i++) {
                    if (test[i] == delimiter) {
                        count++;
                    }
                }
                
                string words[count+1];

                for (signed int i = 0; i < count+1; i++) {
                    words[i] = test.substr(0, test.find(delimiter));
                    test.erase(0, test.find(delimiter) + 1);
                }
                
                for (signed int i = count; i >= 0; i--) {
                    cout << words[i] << " ";
                }
        }
        cout << endl;
    }
    
    
    return 0;
}

