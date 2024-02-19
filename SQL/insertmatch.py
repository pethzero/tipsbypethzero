data_sql = "recno, lastupd, created, code, sname, name, year, itemno, detail"
data_now = "lastupd, created"
head = 'billdetail'

# ใช้ split() เพื่อแยกสตริงเป็นรายการของฟิลด์
array_sql = data_sql.split(', ')
array_sql = [f'"{item}"' for item in array_sql]

array_now = data_now.split(', ')
array_now = [f'"{item}"' for item in array_now]


print(array_sql)
print(array_now)

value_sql = ''
for i, field in enumerate(array_sql):
    if field in array_now:
        # print(field)
        value_sql += 'NOW()'
    else:
        value_sql += f':{field[1:-1]}'  # เอาออก " "
    
    if i < len(array_sql) - 1:
        value_sql += ', '

print(value_sql)

sql_result = f'INSERT INTO {head} ({data_sql}) VALUES ({value_sql})'
with open("astring.txt", "w") as file:
    file.write(sql_result)
