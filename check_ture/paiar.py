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
        # print(key,value)
        if data[key]:  # Check if material status is True
            # print(data[key])
            if not data[value]:
                arr_false.append(key)
            else:
                print('True')
                arr_true.append(key)
        else:
            print('None')

    return arr_true,arr_false

# Example usage
data_record = {
    'data_1': 'some_value',  # Example value, can be any non-None value
    'data_2': 'some_value',
    'data_3': None,
    'status_1': True,
    'status_2': False,
    'status_3': False,
}


obj_pair = pair_check(data_record)
print(obj_pair)



process = {
    'status_1': True,
    'status_2': False,
    'status_3': False,
}
