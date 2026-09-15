# 1. รับค่า N (จำนวนชุดข้อมูล) บรรทัดแรก
N = int(input())

# 2. วนลูปรับค่าวินาทีจำนวน N ครั้ง
for _ in range(N):
    total_seconds = int(input())
    
    # 3. คำนวณชั่วโมง (1 ชั่วโมง = 3600 วินาที)
    hours = total_seconds // 3600
    
    # 4. คำนวณนาที (หาเศษจากชั่วโมง แล้วหารด้วย 60)
    minutes = (total_seconds % 3600) // 60
    
    # 5. คำนวณวินาทีที่เหลือ (หาเศษจาก 60)
    seconds = total_seconds % 60
    
    # 6. แสดงผลลัพธ์คั่นด้วยช่องว่างตามรูปแบบโจทย์
    print(f"{hours} {minutes} {seconds}"