def compute_tax_breakdown(income):
    # กำหนดช่วงภาษี (ขอบเขตล่าง, ขอบเขตบน, อัตราภาษี)
    brackets = [
        (0, 150000, 0.00),
        (150000, 300000, 0.05),
        (300000, 500000, 0.10),
        (500000, 750000, 0.15),
        (750000, 1000000, 0.20),
        (1000000, 2000000, 0.25),
        (2000000, 5000000, 0.30),
        (5000000, float('inf'), 0.35)
    ]
    
    total_tax = 0
    details = []

    for min_inc, max_inc, rate in brackets:
        if income > min_inc:
            taxable = min(income, max_inc) - min_inc
            tax = taxable * rate
            total_tax += tax
            
            upper_bound = min(income, max_inc)
            lower_label = 0 if min_inc == 0 else min_inc + 1
            
            if min_inc == 5000000:
                label = "มากกว่า 5,000,000"
            else:
                label = f"{lower_label:,.0f} - {upper_bound:,.0f}"
                
            details.append((label, tax))
        else:
            break
            
    return total_tax, details

def show_text_graph(records):
    # แสดงกราฟเปรียบเทียบในรูปแบบตัวอักษร (ส่วนโบนัส ไม่ต้องใช้โมดูล)
    print("\n=== กราฟเปรียบเทียบรายได้และภาษี (Text Bar Chart) ===")
    max_val = max(r['income'] for r in records) if records else 1
    scale = 30 / max_val if max_val > 0 else 1  # กำหนดความยาวแท่งสูงสุด 30 ตัวอักษร
    
    for rec in records:
        inc_bar = "█" * int(rec['income'] * scale)
        tax_bar = "▒" * int(rec['tax'] * scale)
        print(f"\n[{rec['person_id']}]")
        print(f"  รายได้ : {inc_bar:<30} ({rec['income']:,.0f} บาท)")
        print(f"  ภาษี   : {tax_bar:<30} ({rec['tax']:,.0f} บาท)")

def save_report(records):
    # บันทึกผลลัพธ์ลงไฟล์ .txt ด้วยฟังก์ชัน open() พื้นฐาน (ส่วนโบนัส)
    f = open("tax_summary_report.txt", "w", encoding="utf-8")
    f.write("=== รายงานสรุปการคำนวณภาษี ===\n\n")
    for rec in records:
        f.write(f"รายการ: {rec['person_id']}\n")
        f.write(f"  - เงินได้สุทธิ: {rec['income']:,.2f} บาท\n")
        f.write(f"  - ภาษีรวม: {rec['tax']:,.2f} บาท\n")
        f.write(f"  - รายได้หลังหักภาษี: {rec['net']:,.2f} บาท\n")
        f.write(f"  - Effective Tax Rate: {rec['eff']:.2f}%\n")
        f.write("-" * 40 + "\n")
    f.close()
    print("\n[ระบบ] บันทึกรายงานลงไฟล์ tax_summary_report.txt เรียบร้อยแล้ว")

def process_tax_calculation(count):
    records = []
    
    for i in range(count):
        person_id = f"คนที่ {i + 1}"
        print(f"\n--- คำนวณรายการ {person_id} ---")
            
        income = float(input("กรอกเงินได้สุทธิ : "))
        
        tax, details = compute_tax_breakdown(income)
        net_income = income - tax
        eff_rate = (tax / income * 100) if income > 0 else 0

        print(f"\nรายละเอียดภาษี")
        for label, step_tax in details:
            print(f"{label:<25} {step_tax:,.0f} บาท")
            
        print(f"\nภาษีรวม {tax:,.0f} บาท")
        print(f"รายได้หลังหักภาษี {net_income:,.0f} บาท")
        print(f"Effective Tax Rate = {eff_rate:.2f}%")

        records.append({
            'person_id': person_id,
            'income': income,
            'tax': tax,
            'net': net_income,
            'eff': eff_rate
        })

    save_report(records)
    show_text_graph(records)

def main():
    print("==========================================")
    print("  โปรแกรมคำนวณภาษีเงินได้บุคคลธรรมดา")
    print("==========================================")
    print("1. คำนวณภาษี 1 คน")
    print("2. คำนวณภาษีหลายคน")
    choice = input("เลือกเมนู (1/2): ")

    if choice == "1":
        process_tax_calculation(1)
    elif choice == "2":
        num = int(input("ระบุจำนวนคนที่ต้องการคำนวณ: "))
        process_tax_calculation(num)
    else:
        print("ตัวเลือกไม่ถูกต้อง กรุณารันโปรแกรมใหม่อีกครั้ง")

if __name__ == "__main__":
    main()