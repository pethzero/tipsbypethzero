import random

def get_filtered_data(data_list, gender, plant, data_count):
    return [
        data for data in data_list
        if (data['gender'] == 'T' or data['gender'] == gender)
        and data['count'] < data_count
        and data['plant'] == plant
        and data['process'] == 'F'
    ]

def update_locker_data(data_list, gender):
    chosen_data = random.choice(data_list)
    chosen_data['count'] += 1
    chosen_data['gender'] = gender
    return chosen_data

def generate_locker_id_prepare(data_management, data_count, data_request):
    output = []
    data_duplicate = []

    for item in data_request:
        gender = item['gender']
        plant = item['plant']
        lk_id = None

        if data_management:
            filtered_data_duplicate = get_filtered_data(data_duplicate, gender, plant, data_count)
            
            if filtered_data_duplicate:
                get_locker_data = max(filtered_data_duplicate, key=lambda x: x['count'])
                get_locker_data['count'] += 1
                lk_id = get_locker_data['id']
            else:
                filtered_data_new = get_filtered_data(data_management, gender, plant, data_count)
                if filtered_data_new:
                    locker_data = update_locker_data(filtered_data_new, gender)
                    lk_id = locker_data['id']
                    data_duplicate.append(locker_data)
                    data_management.remove(locker_data)
        item['locker_id'] = lk_id
        output.append(item)
    return output

data_management = [ 
    {'id': 1, 'plant':'SVI2A','gender': 'T', 'count': 0,'process':'F'}, 
    {'id': 2, 'plant':'SVI2A','gender': 'T', 'count': 0,'process':'F'}, 
    {'id': 3, 'plant':'SVI2A','gender': 'T', 'count': 0,'process':'F'}, 
    {'id': 4, 'plant':'SVI2A','gender': 'T', 'count': 0,'process':'F'}, 
    {'id': 5, 'plant':'SVI2B','gender': 'T', 'count': 0,'process':'F'}, 
    {'id': 6, 'plant':'SVI2B','gender': 'T', 'count': 0,'process':'F'}, 
    {'id': 7, 'plant':'SVI2B','gender': 'T', 'count': 0,'process':'F'}, 
    {'id': 8, 'plant':'SVI2B','gender': 'T', 'count': 0,'process':'F'}, 
    {'id': 9, 'plant':'SVI2C','gender': 'T', 'count': 0,'process':'F'}, 
    {'id': 10,'plant':'SVI2C', 'gender': 'T', 'count': 0,'process':'F'}, 
    {'id': 11,'plant':'SVI2C', 'gender': 'T', 'count': 0,'process':'F'}, 
    {'id': 12,'plant':'SVI2C', 'gender': 'T', 'count': 0,'process':'F'}
]

data_request = [ 
    {'name': 'A','plant':'SVI2A', 'gender': 'M', 'en': 11100},
    {'name': 'B','plant':'SVI2A', 'gender': 'F', 'en': 11101},
    {'name': 'C','plant':'SVI2A', 'gender': 'M', 'en': 11102},
    {'name': 'D','plant':'SVI2A', 'gender': 'F', 'en': 11103},
    {'name': 'E','plant':'SVI2A', 'gender': 'M', 'en': 11104},
    {'name': 'F','plant':'SVI2A', 'gender': 'F', 'en': 11105},
    {'name': 'G','plant':'SVI2B', 'gender': 'M', 'en': 11106},
    {'name': 'H','plant':'SVI2B', 'gender': 'F', 'en': 11107},
    {'name': 'I','plant':'SVI2B', 'gender': 'M', 'en': 11108},
    {'name': 'J','plant':'SVI2B', 'gender': 'F', 'en': 11109},
    {'name': 'K','plant':'SVI2B', 'gender': 'M', 'en': 11110},
    {'name': 'L','plant':'SVI2B', 'gender': 'F', 'en': 11111},
    {'name': 'M','plant':'SVI2B', 'gender': 'M', 'en': 11112},
    {'name': 'N','plant':'SVI2B', 'gender': 'F', 'en': 11113},
    {'name': 'O','plant':'SVI2C', 'gender': 'M', 'en': 11114},
    {'name': 'P','plant':'SVI2C', 'gender': 'F', 'en': 11115},
    {'name': 'Q','plant':'SVI2C', 'gender': 'M', 'en': 11116},
    {'name': 'R','plant':'SVI2C', 'gender': 'F', 'en': 11117},
    {'name': 'S','plant':'SVI2C', 'gender': 'M', 'en': 11118},
    {'name': 'T','plant':'SVI2C', 'gender': 'F', 'en': 11119},
    {'name': 'U','plant':'SVI2D', 'gender': 'M', 'en': 11120},
    {'name': 'V','plant':'SVI2D', 'gender': 'F', 'en': 11121},
    {'name': 'W','plant':'SVI2D', 'gender': 'M', 'en': 11122},
    {'name': 'X','plant':'SVI2D', 'gender': 'F', 'en': 11123},
    {'name': 'Y','plant':'SVI2D', 'gender': 'M', 'en': 11124},
    {'name': 'Z','plant':'SVI2D', 'gender': 'F', 'en': 11125}
]

data_count = 3
output = generate_locker_id_prepare(data_management, data_count, data_request)

# Write the output to a text file with each item on a new line
with open('locker_output.txt', 'w') as file:
    for item in output:
        file.write(f"{item}\n")

print(output)
