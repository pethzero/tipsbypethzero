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

data_management = [ {'id': 1, 'gender': 'T', 'count': 0}, {'id': 2, 'gender': 'T', 'count': 0}, {'id': 3, 'gender': 'T', 'count': 0}, {'id': 4, 'gender': 'T', 'count': 0}, {'id': 5, 'gender': 'T', 'count': 0}, {'id': 6, 'gender': 'T', 'count': 0}, {'id': 7, 'gender': 'T', 'count': 0}, {'id': 8, 'gender': 'T', 'count': 0}, {'id': 9, 'gender': 'T', 'count': 0}, {'id': 10, 'gender': 'T', 'count': 0}, {'id': 11, 'gender': 'T', 'count': 0}, {'id': 12, 'gender': 'T', 'count': 0}, {'id': 13, 'gender': 'T', 'count': 0}, {'id': 14, 'gender': 'T', 'count': 0}, {'id': 15, 'gender': 'T', 'count': 0}, {'id': 16, 'gender': 'T', 'count': 0}, {'id': 17, 'gender': 'T', 'count': 0}, {'id': 18, 'gender': 'T', 'count': 0}, {'id': 19, 'gender': 'T', 'count': 0}, {'id': 20, 'gender': 'T', 'count': 0}, {'id': 21, 'gender': 'T', 'count': 0}, {'id': 22, 'gender': 'T', 'count': 0}, {'id': 23, 'gender': 'T', 'count': 0}, {'id': 24, 'gender': 'T', 'count': 0}, {'id': 25, 'gender': 'T', 'count': 0}, {'id': 26, 'gender': 'T', 'count': 0}, {'id': 27, 'gender': 'T', 'count': 0}, {'id': 28, 'gender': 'T', 'count': 0}, {'id': 29, 'gender': 'T', 'count': 0}, {'id': 30, 'gender': 'T', 'count': 0}]


data_request = [ 
 {'name': 'A', 'gender': 'M', 'en': 11100}
,{'name': 'B', 'gender': 'F', 'en': 11101}
,{'name': 'C', 'gender': 'M', 'en': 11102}
,{'name': 'D', 'gender': 'F', 'en': 11103}
,{'name': 'E', 'gender': 'M', 'en': 11104}
,{'name': 'F', 'gender': 'F', 'en': 11105}
,{'name': 'G', 'gender': 'M', 'en': 11106}
,{'name': 'H', 'gender': 'F', 'en': 11107}
,{'name': 'I', 'gender': 'M', 'en': 11108}
,{'name': 'J', 'gender': 'F', 'en': 11109}
,{'name': 'K', 'gender': 'M', 'en': 11110}
,{'name': 'L', 'gender': 'F', 'en': 11111}
,{'name': 'M', 'gender': 'M', 'en': 11112}
,{'name': 'N', 'gender': 'F', 'en': 11113}
,{'name': 'O', 'gender': 'M', 'en': 11114}
,{'name': 'P', 'gender': 'F', 'en': 11115}
,{'name': 'Q', 'gender': 'M', 'en': 11116}
,{'name': 'R', 'gender': 'F', 'en': 11117}
,{'name': 'S', 'gender': 'M', 'en': 11118}
,{'name': 'T', 'gender': 'F', 'en': 11119}
,{'name': 'U', 'gender': 'M', 'en': 11120}
,{'name': 'V', 'gender': 'F', 'en': 11121}
,{'name': 'W', 'gender': 'M', 'en': 11122}
,{'name': 'X', 'gender': 'F', 'en': 11123}
,{'name': 'Y', 'gender': 'M', 'en': 11124}
,{'name': 'Z', 'gender': 'F', 'en': 11125}
,{'name': '[', 'gender': 'M', 'en': 11126}
,{'name': '!', 'gender': 'F', 'en': 11127}
,{'name': ']', 'gender': 'M', 'en': 11128}
,{'name': '^', 'gender': 'F', 'en': 11129}
,{'name': '_', 'gender': 'M', 'en': 11130}
,{'name': '`', 'gender': 'F', 'en': 11131}
,{'name': 'a', 'gender': 'M', 'en': 11132}
,{'name': 'b', 'gender': 'F', 'en': 11133}
,{'name': 'c', 'gender': 'M', 'en': 11134}
,{'name': 'd', 'gender': 'F', 'en': 11135}
,{'name': 'e', 'gender': 'M', 'en': 11136}
,{'name': 'f', 'gender': 'F', 'en': 11137}
,{'name': 'g', 'gender': 'M', 'en': 11138}
,{'name': 'h', 'gender': 'F', 'en': 11139}
,{'name': 'i', 'gender': 'M', 'en': 11140}
,{'name': 'j', 'gender': 'F', 'en': 11141}
,{'name': 'k', 'gender': 'M', 'en': 11142}
,{'name': 'l', 'gender': 'F', 'en': 11143}
,{'name': 'm', 'gender': 'M', 'en': 11144}
,{'name': 'n', 'gender': 'F', 'en': 11145}
,{'name': 'o', 'gender': 'M', 'en': 11146}
,{'name': 'p', 'gender': 'F', 'en': 11147}
,{'name': 'q', 'gender': 'M', 'en': 11148}
,{'name': 'r', 'gender': 'F', 'en': 11149}
,{'name': 's', 'gender': 'M', 'en': 11150}]

# [{'name':'A', 'gender':'M', 'en':11111}, {'name':'B', 'gender':'M', 'en':11112},
#                 {'name':'C', 'gender':'F', 'en':11113}, {'name':'D', 'gender':'M', 'en':11114},
#                 {'name':'E', 'gender':'F', 'en':11115}, {'name':'F', 'gender':'M', 'en':11116},
#                 {'name':'G', 'gender':'M', 'en':11117}, {'name':'H', 'gender':'M', 'en':11118}]

data_count = 2
output = generate_locker_id(data_management, data_count, data_request)
print(output)
