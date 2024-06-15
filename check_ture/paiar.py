# Example usage
example_data = {
    'data_1': 'some_value',  # Example value, can be any non-None value
    'data_2': 'some_value',
    'data_3': None,
    'status_1': True,
    'status_2': False,
    'status_3': False,
}
process = {
    'status_1': True,
    'status_2': False,
    'status_3': False,
}




def pair_check(data):
    # Define pairs to check
    pairs = {
        'data_1': 'status_1',
        'data_2': 'status_2',
        'data_3': 'status_3'
    }

    # Initialize a list to store the statuses that need to be updated
    arr_true = []
    arr_false = []

    # Check and update statuses
    for key, value in pairs.items():
        if data[key]:  # Check if material status is True
            if not data[value]:
                arr_false.append(key)
            else:
                print('True')
                arr_true.append(key)
        else:
            print('None')

    return arr_true,arr_false


def mutiple_check(data, process):
    # Define pairs to check
    pairs = {
        'data_1': ('status_1', 'process_1'),
        'data_2': ('status_2', 'process_2'),
        'data_3': ('status_3', 'process_3')
    }
    
        # Initialize a list to store the statuses that need to be updated
    to_update = []

    # Check and update statuses
    for key, (status_value, process_value) in pairs.items():
        if data[key] is not None:  # Check if material status is not None
            if not data[status_value]:  # Check if the status is False
                if process[status_value]:  # Check the process status
                    to_update.append((key, process[status_value]))  # Add to the update list with process status
                else:
                    to_update.append((key, process[status_value]))  # Even if process is False, add to the list
                    
    print(to_update)
    return to_update

    

# obj_pair = pair_check(example_data)
obj_mutiple = mutiple_check(example_data,process)
print(obj_mutiple)



