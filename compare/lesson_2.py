class DataItem:
    def __init__(self, id, data, type, status):
        self.id = id
        self.data = data
        self.type = type
        self.status = status

    def __repr__(self):
        return f"{{ id: {self.id}, data: {self.data}, type: '{self.type}', status: {self.status} }}"


class HotelDataItem(DataItem):
    def __init__(self, id, data, status):
        super().__init__(id, data, "HOTEL", status)


def compare_data(data_old, data_new, condition=None):
    data_change = False

    # วนลูปผ่านทุกข้อมูลใน data_old
    for item_old in data_old:
        id_to_check = item_old.id
        found = False

        # ตรวจสอบเงื่อนไขของ condition (ถ้ามี)
        if condition:
            should_compare = True
            for key, value in condition.items():
                if getattr(item_old, key, None) != value:
                    should_compare = False
                    break
            if not should_compare:
                continue  # ข้ามไปยังรอบถัดไปในลูป

        # ค้นหาข้อมูลใน data_new ที่มี id เท่ากับ id ใน data_old
        for item_new in data_new:
            if item_new.id == id_to_check:
                # เปรียบเทียบข้อมูลระหว่าง item_old กับ item_new
                if not objects_are_equal(item_old, item_new):
                    data_change = True
                found = True
                break

        # หากพบข้อมูลที่ตรงกัน จะหยุดการวนลูป
        if found:
            break

    return data_change


# เช็คว่าอ็อบเจกต์สองตัวเท่ากันหรือไม่
def objects_are_equal(obj1, obj2):
    # แปลง Object เป็น JSON String แล้วเปรียบเทียบ
    return obj1.__dict__ == obj2.__dict__


# ตัวอย่างการใช้งาน
data_old = [
    HotelDataItem(1, None, 50),
    DataItem(2, None, "LUNCH", 30),
    HotelDataItem(3, None, 40),
    # อ็อบเจกต์เพิ่มเติมใน data_old
]

data_new = [
    HotelDataItem(1, None, 50),  # เปลี่ยนแปลงที่นี่
    DataItem(2, None, "LUNCH", 30),
    HotelDataItem(3, None, 45),
    # อ็อบเจกต์เพิ่มเติมใน data_new
]

  


change_detected_all = compare_data(data_old, data_new)
change_detected_hotel = compare_data(data_old, data_new, {'type': 'HOTEL'})

print(f"Data change detected (all objects): {change_detected_all}")
print(f"Data change detected (type HOTEL): {change_detected_hotel}")
