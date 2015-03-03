#include <iostream>
#include <cctype>
#include <fstream>
using namespace std;



int main(int argc, char* argv[])
{
    ifstream file;
    string lineBuffer;
    file.open(argv[1]);
    while (!file.eof()) 
    {
        getline(file, lineBuffer);
        if (lineBuffer.length() == 0)
            continue; //ignore all empty lines
        else 
        {
            lineBuffer = lineBuffer.c_str();
            for (signed int i = 0;i < lineBuffer.length();i++) {
                lineBuffer[i] = tolower(lineBuffer[i]);
                cout << lineBuffer[i];
           }
           cout << endl;
        }
    }
    
    
    return 0;
}