data_sql = "recno, lastupd, created, code, sname, name, year, itemno, detail"

# ใช้ split() เพื่อแยกสตริงเป็นรายการของฟิลด์
array_sql = data_sql.split(', ')
array_sql = [f'"{item}"' for item in array_sql]

# print(data_sql)

for i in array_sql:
    print(i)
