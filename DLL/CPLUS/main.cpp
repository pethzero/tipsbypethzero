// main.cpp
#include <iostream>
extern "C" __declspec(dllimport) void HelloWorld();

int main() {
    HelloWorld();
    return 0;
}
