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
        
        if len(data_dulpicate):
            
        else:
            filtered_data = [data for data in data_management 
                            if (data['gender'] == 'T' or data['gender'] == gender) 
                                and data['count'] < data_count
                                and data['plant'] == plant]
            
            if filtered_data:
                # สุ่มเลือกข้อมูลจาก filtered_data
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


data_management = [ 
{'id': 1, 'plant':'SVI2A','gender': 'T', 'count': 0}, 
{'id': 2, 'plant':'SVI2A','gender': 'T', 'count': 0}, 
{'id': 3, 'plant':'SVI2A','gender': 'T', 'count': 0}, 
{'id': 4, 'plant':'SVI2A','gender': 'T', 'count': 0}, 
{'id': 5, 'plant':'SVI2A','gender': 'T', 'count': 0}, 
{'id': 6, 'plant':'SVI2A','gender': 'T', 'count': 0}, 
{'id': 7, 'plant':'SVI2A','gender': 'T', 'count': 0}, 
{'id': 8, 'plant':'SVI2A','gender': 'T', 'count': 0}, 
{'id': 9, 'plant':'SVI2A','gender': 'T', 'count': 0}, 
{'id': 10,'plant':'SVI2A', 'gender': 'T', 'count': 0}, 
{'id': 11,'plant':'SVI2A', 'gender': 'T', 'count': 0}, 
{'id': 12,'plant':'SVI2B', 'gender': 'T', 'count': 0}, 
{'id': 13,'plant':'SVI2B', 'gender': 'T', 'count': 0}, 
{'id': 14,'plant':'SVI2B', 'gender': 'T', 'count': 0}, 
{'id': 15,'plant':'SVI2B', 'gender': 'T', 'count': 0}, 
{'id': 16,'plant':'SVI2B', 'gender': 'T', 'count': 0}, 
{'id': 17,'plant':'SVI2B', 'gender': 'T', 'count': 0}, 
{'id': 18,'plant':'SVI2B', 'gender': 'T', 'count': 0}, 
{'id': 19,'plant':'SVI2C', 'gender': 'T', 'count': 0}, 
{'id': 20,'plant':'SVI2C', 'gender': 'T', 'count': 0}, 
{'id': 21,'plant':'SVI2C', 'gender': 'T', 'count': 0}, 
{'id': 22,'plant':'SVI2C', 'gender': 'T', 'count': 0}, 
{'id': 23,'plant':'SVI2C', 'gender': 'T', 'count': 0}, 
{'id': 24,'plant':'SVI2C', 'gender': 'T', 'count': 0}, 
{'id': 25,'plant':'SVI2C', 'gender': 'T', 'count': 0}, 
{'id': 26,'plant':'SVI2A', 'gender': 'T', 'count': 0}, 
{'id': 27,'plant':'SVI2A', 'gender': 'T', 'count': 0}, 
{'id': 28,'plant':'SVI2A', 'gender': 'T', 'count': 0}, 
{'id': 29,'plant':'SVI2A', 'gender': 'T', 'count': 0},
{'id': 30,'plant':'SVI2A', 'gender': 'T', 'count': 0}
]


data_request = [ 
 {'name': 'A','plant':'SVI2A', 'gender': 'M', 'en': 11100}
,{'name': 'B','plant':'SVI2B', 'gender': 'F', 'en': 11101}
,{'name': 'C','plant':'SVI2B', 'gender': 'M', 'en': 11102}
,{'name': 'D','plant':'SVI2B', 'gender': 'F', 'en': 11103}
,{'name': 'E','plant':'SVI2C', 'gender': 'M', 'en': 11104}
,{'name': 'F','plant':'SVI2C', 'gender': 'F', 'en': 11105}
,{'name': 'G','plant':'SVI2A', 'gender': 'M', 'en': 11106}
,{'name': 'H','plant':'SVI2A', 'gender': 'F', 'en': 11107}
,{'name': 'I','plant':'SVI2A', 'gender': 'M', 'en': 11108}
,{'name': 'J','plant':'SVI2B', 'gender': 'F', 'en': 11109}
,{'name': 'K','plant':'SVI2A', 'gender': 'M', 'en': 11110}
,{'name': 'L','plant':'SVI2A', 'gender': 'F', 'en': 11111}
,{'name': 'M','plant':'SVI2A', 'gender': 'M', 'en': 11112}
,{'name': 'N','plant':'SVI2A', 'gender': 'F', 'en': 11113}
,{'name': 'O','plant':'SVI2A', 'gender': 'M', 'en': 11114}
,{'name': 'P','plant':'SVI2A', 'gender': 'F', 'en': 11115}
,{'name': 'Q','plant':'SVI2A', 'gender': 'M', 'en': 11116}
,{'name': 'R','plant':'SVI2A', 'gender': 'F', 'en': 11117}
,{'name': 'S','plant':'SVI2A', 'gender': 'M', 'en': 11118}
,{'name': 'T','plant':'SVI2A', 'gender': 'F', 'en': 11119}
,{'name': 'U','plant':'SVI2A', 'gender': 'M', 'en': 11120}
,{'name': 'V','plant':'SVI2A', 'gender': 'F', 'en': 11121}
,{'name': 'W','plant':'SVI2A', 'gender': 'M', 'en': 11122}
,{'name': 'X','plant':'SVI2A', 'gender': 'F', 'en': 11123}
,{'name': 'Y','plant':'SVI2A', 'gender': 'M', 'en': 11124}
,{'name': 'Z','plant':'SVI2A', 'gender': 'F', 'en': 11125}
,{'name': '[','plant':'SVI2A', 'gender': 'M', 'en': 11126}
,{'name': '!','plant':'SVI2A', 'gender': 'F', 'en': 11127}
,{'name': ']','plant':'SVI2A', 'gender': 'M', 'en': 11128}
,{'name': '^','plant':'SVI2A', 'gender': 'F', 'en': 11129}
,{'name': '_','plant':'SVI2A', 'gender': 'M', 'en': 11130}
,{'name': '`','plant':'SVI2A', 'gender': 'F', 'en': 11131}
,{'name': 'a','plant':'SVI2A', 'gender': 'M', 'en': 11132}
,{'name': 'b','plant':'SVI2A', 'gender': 'F', 'en': 11133}
,{'name': 'c','plant':'SVI2A', 'gender': 'M', 'en': 11134}
,{'name': 'd','plant':'SVI2A', 'gender': 'F', 'en': 11135}
,{'name': 'e','plant':'SVI2A', 'gender': 'M', 'en': 11136}
,{'name': 'f','plant':'SVI2A', 'gender': 'F', 'en': 11137}
,{'name': 'g','plant':'SVI2A', 'gender': 'M', 'en': 11138}
,{'name': 'h','plant':'SVI2A', 'gender': 'F', 'en': 11139}
,{'name': 'i','plant':'SVI2A', 'gender': 'M', 'en': 11140}
,{'name': 'j','plant':'SVI2C', 'gender': 'F', 'en': 11141}
,{'name': 'k','plant':'SVI2C', 'gender': 'M', 'en': 11142}
,{'name': 'l','plant':'SVI2C', 'gender': 'F', 'en': 11143}
,{'name': 'm','plant':'SVI2C', 'gender': 'M', 'en': 11144}
,{'name': 'n','plant':'SVI2C', 'gender': 'F', 'en': 11145}
,{'name': 'o','plant':'SVI2A', 'gender': 'M', 'en': 11146}
,{'name': 'p','plant':'SVI2A', 'gender': 'F', 'en': 11147}
,{'name': 'q','plant':'SVI2A', 'gender': 'M', 'en': 11148}
,{'name': 'r','plant':'SVI2A', 'gender': 'F', 'en': 11149}
,{'name': 's','plant':'SVI2A', 'gender': 'M', 'en': 11150}]

data_count = 2
output = generate_locker_id_new(data_management, data_count, data_request)
print(output)
