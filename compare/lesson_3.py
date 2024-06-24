def compare_data(data_old, data_new, condition=None):
    data_change = False

    # วนลูปผ่านทุกข้อมูลใน data_old
    for item_old in data_old:
        id_to_check = item_old["id"]
        found = False

        # ตรวจสอบเงื่อนไขของ condition (ถ้ามี)
        if condition:
            should_compare = True
            for key, value in condition.items():
                if item_old.get(key) != value:
                    should_compare = False
                    break
            if not should_compare:
                continue  # ข้ามไปยังรอบถัดไปในลูป

        # ค้นหาข้อมูลใน data_new ที่มี id เท่ากับ id ใน data_old
        for item_new in data_new:
            if item_new["id"] == id_to_check:
                # เปรียบเทียบข้อมูลระหว่าง item_old กับ item_new
                if item_old != item_new:
                    data_change = True
                found = True
                break

        # หากพบข้อมูลที่ตรงกัน จะหยุดการวนลูป
        if found:
            break

    return data_change


# ตัวอย่างการใช้งาน
data_old = [
    { "id": 1, "data": None, "type": "HOTEL", "status": 50 },
    { "id": 2, "data": None, "type": "LUNCH", "status": 30 },
    { "id": 3, "data": None, "type": "HOTEL", "status": 40 },
]

data_new = [
    { "id": 1, "data": None, "type": "HOTEL", "status": 50 }, 
    { "id": 2, "data": None, "type": "LUNCH", "status": 30 },
    { "id": 3, "data": None, "type": "HOTEL", "status": 45 },
]

change_detected_all = compare_data(data_old, data_new)
change_detected_hotel = compare_data(data_old, data_new, {"type": "HOTEL"})

print(f"Data change detected (all objects): {change_detected_all}")
print(f"Data change detected (type HOTEL): {change_detected_hotel}")
