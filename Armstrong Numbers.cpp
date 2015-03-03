#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;




int main(int argc, char* argv[])
{
    string test;
    ifstream file;
    file.open(argv[1]);
    
    while (!file.eof())
    {
        int sum = 0;
        getline(file, test); //read the line
        test.erase(test.find_last_not_of(" \n\r\t")+1); //trim whitepace
        test = test.c_str();
        for (unsigned int i = 0;i < test.length();i++)
        {
            sum = sum + pow(test[i] - '0', test.length());
        }
        if (atoi(test.c_str()) == sum) cout << "True" << endl;
        else cout << "False" << endl;
    }
    
    
    
    
    
    
    
    
    
    return 0;
}