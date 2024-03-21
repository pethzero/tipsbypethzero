#การเขียน ข้อความ text แล้วเติมให้ อัตโนมัติ
filename = 'input.txt'  # ชื่อไฟล์ที่มีข้อมูลตัวอักษร
output_filename = 'output.txt'  # ชื่อไฟล์ที่ต้องการสร้างและเขียนข้อมูล

with open(filename, 'r', encoding='utf-8') as input_file, open(output_filename, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        line = line.strip()  # ลบช่องว่างหรือตัวขึ้นบรรทัดในท้ายสตริง
        output_file.write(f" <td>{line}</td> \n")  # เขียนข้อมูลลงในไฟล์ใหม่
       
       
SELECT ORDERHD.RECNO, ORDERHD.DOCDATE, ORDERHD.DOCNO, ORDERHD.CUSTORDERNO, CUST.CODE, CUST.SNAME, CUST.NAME, CUSTCONT.CONTNAME, EMPL.EMPNAME, ORDERDT.DETAIL, ORDERDT.QUANDLY, ORDERDT.UNITAMT, ORDERDT.TOTALAMT FROM ORDERHD LEFT JOIN CUST ON (ORDERHD.CUST = CUST.RECNO) LEFT JOIN CUSTCONT ON (ORDERHD.CONT = CUSTCONT.RECNO) LEFT JOIN EMPL ON (ORDERHD.SALES = EMPL.RECNO) LEFT JOIN ORDERDT ON (ORDERHD.RECNO = ORDERDT. ORDERHD) WHERE (ORDERHD.DOCDATE BETWEEN :ABEGIN AND :AEND)  AND  (ORDERDT.DETAIL <> '')  AND (ORDERHD.STATUS <> 'C') ORDER BY ORDERHD.RECNO       