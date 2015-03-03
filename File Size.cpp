#include <iostream>

int main(int argc, char* argv[]) {
    FILE * test;
    long size;

    test = fopen (argv[1],"rb");
    if (test != NULL)
    {
        fseek (test, 0, SEEK_END);
        size = ftell(test);
        fclose (test);
        std::cout << size;
    }
    
    return 0;
}