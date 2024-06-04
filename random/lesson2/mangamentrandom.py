import random

def generate_locker_id(data_management, data_count, data_request):
    output = []
    for item in data_request:
        gender = item['gender']
        
        # เลือกข้อมูลที่มี gender เป็น 'T' และ count < 2
        filtered_data = [data for data in data_management 
                         if (data['gender'] == 'T' or data['gender'] == gender) and data['count'] < data_count]
        
        if filtered_data:
            random_data = random.choice(filtered_data)
            locker_id = random_data['id']
            random_data['count'] += 1
            random_data['gender'] = gender
        else:
            locker_id = None
        
        # เพิ่มข้อมูลลงใน output พร้อมกับ locker_id ที่สร้างขึ้น
        item['locker_id'] = locker_id
        output.append(item)
    return output


def generate_locker_id_new(data_management, data_count, data_request):
    output = []
    data_dulpicate = []
    for item in data_request:
        gender = item['gender']
        plant = item['plant']
        # print('DATA',item['name'])
        
        # if len(data_dulpicate) > 0:
        #     # เลือกข้อมูลที่มี gender เป็น 'T' เติม  และ count < 2
        #     filtered_data_temp = [data for data in data_dulpicate 
        #                     if (data['gender'] == 'T' or data['gender'] == gender) 
        #                         and data['count'] < data_count
        #                         and data['plant'] == plant]
        #     # if()
        #     print(filtered_data_temp)
        # else:
        #     filtered_data = [data for data in data_management 
        #                     if (data['gender'] == 'T' or data['gender'] == gender) 
        #                         and data['count'] < data_count
        #                         and data['plant'] == plant]
            
        #     if filtered_data:
        #         random_data = random.choice(filtered_data)
        #         random_data['count'] += 1
        #         random_data['gender'] = gender
        #         locker_id = random_data['id']
        #         data_dulpicate.append(random_data)
        #         print('PP',data_dulpicate)
        #     else:
        #         locker_id = None
                
        filtered_data = [data for data in data_management 
                            if (data['gender'] == 'T' or data['gender'] == gender) 
                                and data['count'] < data_count
                                and data['plant'] == plant
                                and data['exit'] == 'F'
                                ]
        if filtered_data:
            random_data = random.choice(filtered_data)
            random_data['count'] += 1
            random_data['gender'] = gender
            locker_id = random_data['id']
        else:
            locker_id = None
        
        # เพิ่มข้อมูลลงใน output พร้อมกับ locker_id ที่สร้างขึ้น
        item['locker_id'] = locker_id
        output.append(item)
        
        # print('Oput',output)
    print(data_management)
    return output


data_management = [ 
{'id': 1, 'plant':'SVI2A','gender': 'T', 'count': 0,'exit':'F'}, 
{'id': 2, 'plant':'SVI2A','gender': 'T', 'count': 0,'exit':'F'}, 
{'id': 3, 'plant':'SVI2A','gender': 'T', 'count': 0,'exit':'F'}, 
{'id': 4, 'plant':'SVI2A','gender': 'T', 'count': 0,'exit':'F'}, 
# {'id': 5, 'plant':'SVI2B','gender': 'T', 'count': 0}, 
# {'id': 6, 'plant':'SVI2B','gender': 'T', 'count': 0}, 
# {'id': 7, 'plant':'SVI2B','gender': 'T', 'count': 0}, 
# {'id': 8, 'plant':'SVI2B','gender': 'T', 'count': 0}, 
# {'id': 9, 'plant':'SVI2C','gender': 'T', 'count': 0}, 
# {'id': 10,'plant':'SVI2C', 'gender': 'T', 'count': 0}, 
]


data_request = [ 
 {'name': 'A','plant':'SVI2A', 'gender': 'M', 'en': 11100}
,{'name': 'B','plant':'SVI2A', 'gender': 'F', 'en': 11101}
,{'name': 'C','plant':'SVI2A', 'gender': 'M', 'en': 11102}
,{'name': 'D','plant':'SVI2A', 'gender': 'F', 'en': 11103}
,{'name': 'E','plant':'SVI2A', 'gender': 'M', 'en': 11104}
,{'name': 'F','plant':'SVI2A', 'gender': 'F', 'en': 11105}
# ,{'name': 'G','plant':'SVI2B', 'gender': 'M', 'en': 11106}
# ,{'name': 'H','plant':'SVI2B', 'gender': 'F', 'en': 11107}
# ,{'name': 'I','plant':'SVI2B', 'gender': 'M', 'en': 11108}
# ,{'name': 'J','plant':'SVI2B', 'gender': 'F', 'en': 11109}
# ,{'name': 'K','plant':'SVI2B', 'gender': 'M', 'en': 11110}
# ,{'name': 'L','plant':'SVI2B', 'gender': 'F', 'en': 11111}
# ,{'name': 'M','plant':'SVI2B', 'gender': 'M', 'en': 11112}
# ,{'name': 'N','plant':'SVI2B', 'gender': 'F', 'en': 11113}
# ,{'name': 'O','plant':'SVI2C', 'gender': 'M', 'en': 11114}
# ,{'name': 'P','plant':'SVI2C', 'gender': 'F', 'en': 11115}
# ,{'name': 'Q','plant':'SVI2C', 'gender': 'M', 'en': 11116}
# ,{'name': 'R','plant':'SVI2C', 'gender': 'F', 'en': 11117}
# ,{'name': 'S','plant':'SVI2C', 'gender': 'M', 'en': 11118}
# ,{'name': 'T','plant':'SVI2C', 'gender': 'F', 'en': 11119}
# ,{'name': 'U','plant':'SVI2D', 'gender': 'M', 'en': 11120}
# ,{'name': 'V','plant':'SVI2D', 'gender': 'F', 'en': 11121}
# ,{'name': 'W','plant':'SVI2D', 'gender': 'M', 'en': 11122}
# ,{'name': 'X','plant':'SVI2D', 'gender': 'F', 'en': 11123}
# ,{'name': 'Y','plant':'SVI2D', 'gender': 'M', 'en': 11124}
# ,{'name': 'Z','plant':'SVI2D', 'gender': 'F', 'en': 11125}
]

data_count = 2
output = generate_locker_id_new(data_management, data_count, data_request)
# print(output)
