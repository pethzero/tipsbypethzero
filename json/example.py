import json
import random

def randomname():
    # สร้างชื่อสุ่ม
    names = ['John', 'Emma', 'Michael', 'Sophia', 'William']
    return random.choice(names)

def read_txt_name(filename):
    try:
        with open(filename, 'r') as file:
            names = file.readlines()
            # ลบช่องว่างหรือขึ้นบรรทัดใหม่ที่อาจมีอยู่ในแต่ละชื่อ
            names = [name.strip() for name in names]
            # กรองชื่อที่ไม่เป็นชื่อว่าง
            names = [name for name in names if name]
            if names:
                return random.choice(names)
            else:
                return None
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None


def generate_json(loop):
    json_list = []
    for i in range(1, loop + 1):
        json_dict = {}
        json_dict['key'] = i
        json_dict['name'] = read_txt_name("name.txt")
        json_dict['col'] = "'test'"
        json_dict['none'] = None
        json_list.append(json_dict)
    return json_list

def main():
    loop = 10  # กำหนดจำนวนรอบที่ต้องการทำซ้ำ
    json_data = generate_json(loop)
    
    print("JSON:")
    print(json.dumps(json_data, indent=4))

if __name__ == "__main__":
    main()