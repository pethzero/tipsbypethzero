from ctypes import cdll

def main():
    my_dll = cdll.LoadLibrary('.\\EXAMPLE.dll')

    # Call the add_numbers function from the DLL
    result_add = my_dll.add_numbers(5, 7)
    print("Result from add_numbers DLL:", result_add)

    # Call the subtract_numbers function from the DLL
    result_subtract = my_dll.subtract_numbers(10, 4)
    print("Result from subtract_numbers DLL:", result_subtract)

    # Call the multiply_numbers function from the DLL
    result_multiply = my_dll.multiply_numbers(3, 8)
    print("Result from multiply_numbers DLL:", result_multiply)

    # Call the divide_numbers function from the DLL
    result_divide = my_dll.divide_numbers(20, 4)
    print("Result from divide_numbers DLL:", result_divide)

if __name__ == "__main__":
    main()
