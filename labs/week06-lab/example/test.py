"""

เขียน FUNCTION แปลงหน่วยเงิน ที่สามารถแปลงเงินจาก
THB <-> USD .. 1 USD = 32 THB

โดยใช้ชื่อและการใช้งาน
function convert_currency(100, "USD")

แสดงผลออกทางหน้าจอ
100 THB = 3.3 USD

และทดสอบการใช้งาน function ที่ตัวเองเขียนด้วย

"""

def convert_currency(amount, currency):
    if   currency == "USD":
        return amount / 32
    elif currency == "THB":
        return amount * 32
    

result = convert_currency(100, "USD")
print(f"100 THB = {result:.1f} USD")