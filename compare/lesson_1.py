def compare_data(data_old, data_new):
    data_change = False
    
    for item_old in data_old:
        id_to_check = item_old['id']
        found = False
        
        for item_new in data_new:
            if item_new['id'] == id_to_check:
                if item_new != item_old:
                    data_change = True
                found = True
                break
        
        if found:
            break
    
    return data_change

# ตัวอย่างการใช้งาน
data_old = [
    { "id": 1, "data": None },
    { "id": 2, "data": 'A' }
]

data_new = [
    { "id": 1, "data": None },  # เปลี่ยนแปลงที่นี่
    { "id": 2, "data": 'A' }
]

change_detected = compare_data(data_old, data_new)
print("Data change detected:", change_detected)
