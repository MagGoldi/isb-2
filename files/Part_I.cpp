#include <iostream>
 
int main(int argc, char *argv[])
{
    srand(time(0));
    int x = std::rand() % 12347;
 
    int N = 128;
    bool b;
 

    for(int i = 0; i < N; i++)
    {
        x = (x * 222 + 4) % 12347;
        b = x % 2;
        std::cout << b;
    }
 
    return 0;
}


// 01001010000011001100111011001001111110100100110000100010010001100100000111100110110100100010110001101111000111111001011110011101