import os
import shutil

# # Find the current directory
current_directory = os.getcwd()
current_directory = current_directory + "\\output"
# # Get a list of all files in the current directory
# files = os.listdir(current_directory)
print(current_directory)

files = os.listdir(current_directory)
# Print the names of all files
print("List of all files in the current directory:")
for file in files:
    print(file)
    # print(os.path.isfile(file))

# Select only files that are actual files and not the file of this program
# file_list = [file for file in files if os.path.isfile(file) and file != os.path.basename(__file__)]
file_list = [file for file in files]

# Create input.txt file and write the names of all files into it
print(file_list)
with open('input.txt', 'w') as input_file:
    for file in file_list:
        print('save file: ' + file)
        input_file.write(file + '\n')

# Print confirmation message
print("Completed writing file names into input.txt")
