import os

# Specify the directory containing files
folder_path = 'output'  # Change to the actual directory you want to use

# Create a dictionary to store the key-value pairs between old names and new names
# file_mapping = {
#     'test.txt': 'oo.txt',
#     'name.zip': 'ex.zip'
#     # Add more as needed
# }

file_mapping = {}
with open('input.txt', 'r') as f:
    for line in f:
        old_name, new_name = line.strip().split(':')
        file_mapping[old_name.strip()] = new_name.strip()
        
# Rename files
for filename in os.listdir(folder_path):
    if filename in file_mapping:
        old_filepath = os.path.join(folder_path, filename)
        new_filename = file_mapping[filename]
        new_filepath = os.path.join(folder_path, new_filename)
        os.rename(old_filepath, new_filepath)
        print(f"Renamed file {filename} to {new_filename}")
