def deposit(money):
    print(f"ยอดเงินเริ่มต้น: {money} บาท")
    try:
        amount = float(input("กรอกเงินที่ต้องการฝาก"))
        if amount <= 0:
            raise ValueError("จำนวนเงินฝากต้องมากกว่า 0")

    except ValueError as e:
        print(f"\nเกิดข้อผิดพลาด : {e}")

    else:
        print("\nฝากเงินสำเร็จ")
        print(f"ยอดเงินคงเหลือ: {money + amount:.2f}บาท")

    finally:
        print("สิ้นสุดการฝากเงิน")


deposit(1000)