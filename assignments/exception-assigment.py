try:
    num1 = float(input(" ตัวเลขที่ 1: "))
    num2 = float(input(" ตัวเลขที่ 2: "))
    operator = input("เครื่องหมาย (+, -, *, /): ")
    result = 0
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    if operator == "*":
            result = num1 * num2
    elif operator == "/":
            result = num1 / num2
    else:
        raise ValueError("เครื่องหมายต้องเป็น +,-,*,/ เท่านั้น")
    print(f"{num1} {operator} {num2} = {result}")

except ValueError: #กรณีผู้ใช้ไม่พิมตัวเลข
     print("กรุณาใส่ตัวเลขเท่านั้น")

except ZeroDivisionError: #กรณีผู้ใช้ใส่ตัวหารเป็น0
     print("ไม่สามารถหารด้วย0ได้")

except Exception: #กรณีอื่น
     print("ทำอะไรไม่ได้บางอย่างแต่ไม่แน่ใจว่าคืออะไร")

else: #จะทำที่นี่ก็ต่อเมื่อไม่มี exception
     print("คำนวณข้อมูลเรียบร้อยแล้ว")

finally: 
     print("จบการทำงาน")
        