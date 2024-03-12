data_sql = "code, sname, name, year, detail"

# ใช้ split() เพื่อแยกสตริงเป็นรายการของฟิลด์
array_sql = data_sql.split(', ')
array_sql = [f'{item}' for item in array_sql]

# print(data_sql)

# for i in array_sql:
#     print(f"$stmt->bindParam(':{i}', $data['{i}']);")

with open("aBindP.txt", "w") as file:
    # Using loop to write data to the file
    for i in array_sql:
        file.write(f"$stmt->bindParam(':{i}', $data['{i}']);" + "\n")