# รายการ data
data = [
"Wraehouse",
"Production",
"HR",
"Facility",
]

# ชื่อของตาราง
table_name = "OP_DOC_CTRL.dbo.op_asset_config"

# สร้าง string ของคำสั่ง INSERT
insert_query = f"INSERT INTO {table_name} ([type], is_active, name) VALUES "

# สร้างค่าที่จะแทรก
values = ", ".join([f"('A', 1, '{itme}')" for itme in data])

# รวมคำสั่ง INSERT และค่าต่าง ๆ
insert_query += values + ";"

# แสดงผลลัพธ์
print(insert_query)
