import json
import random

def randomname():
    # สร้างชื่อสุ่ม
    names = ['John', 'Emma', 'Michael', 'Sophia', 'William']
    return random.choice(names)

def convert_to_js_variable(json_data):
    # แปลง JSON เป็นรูปแบบตัวแปรใน JavaScript
    js_variable = "const data = " + json.dumps(json_data, indent=4)
    return js_variable

def generate_json(input_data, loop):
    json_list = []
    for i in range(loop):
        json_dict = {}
        for line in input_data:
            parts = line.split('|')
            key = parts[0] + str(i+1)  # เพิ่มเลขลงไปใน key
            value = None
            if len(parts) > 1:
                if parts[1] == "randomname()":
                    value = randomname()
                else:
                    value = parts[1]
            json_dict[key] = value
        json_list.append(json_dict)
    return json_list

def main():
    input_data = [
        "key",
        "name|randomname()",
        "col|'test'",
        "none",
        "none"
    ]
    loop = 3  # กำหนดจำนวนรอบที่ต้องการทำซ้ำ
    json_data = generate_json(input_data, loop)
    
    print("JSON:")
    print(json.dumps(json_data, indent=4))
    js_variable = convert_to_js_variable(json_data)
    print("\nJavaScript variable:")
    print(js_variable)

if __name__ == "__main__":
    main()
