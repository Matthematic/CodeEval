#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <cstdlib>
#include <iomanip>
using namespace std;


void BubbleSort(vector<float> & values);
vector<float> PutInSingleArray(string & input);
template<typename T> ostream& operator<< (ostream& out, const vector<T> v);
int main(int argc, char* argv[])
{
        ifstream file;
        string input;
        vector<float> values;
        file.open(argv[1]);


        while (!file.eof()) {

                getline(file, input);
                input.erase(input.find_last_not_of(" \n\r\t")+1); //erase whitespace



                values = PutInSingleArray(input);
                BubbleSort(values);
                cout << values << endl;
        }
        file.close();

        return 0;
}







template<typename T>
ostream& operator<< (ostream& out, const vector<T> v) {
    for(unsigned int i = 0; i < v.size(); i++)
        out << std::fixed << std::setprecision(3) << v[i] << " ";
    return out;
}


vector<float> PutInSingleArray(string & input)
{
        vector<float> values;
        istringstream iss(input);
        string sub;

        while (iss >> sub)
        {
                //iss >> sub;
                values.push_back(atof(sub.c_str()));
        }

        return values;
}


void BubbleSort(vector<float> & values)
{
  float temp;

      unsigned int i, j;
      for(i = 1; i < values.size(); i++)
      {
       for (j=0; j < values.size()-1; j++)
       {
           if (values[j+1] < values[j])
           {
               temp = values[j];
               values[j] = values[j+1];
               values[j+1] = temp;
           }
       }
     }
}

