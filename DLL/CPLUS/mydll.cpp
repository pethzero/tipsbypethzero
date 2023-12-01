// mydll.cpp
#include <iostream>

extern "C" __declspec(dllexport) void HelloWorld() {
    std::cout << "Hello, World from DLL!" << std::endl;
}
