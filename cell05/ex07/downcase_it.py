#!/usr/bin/env python3
import sys

# ตรวจสอบว่าจำนวนพารามิเตอร์ (ไม่นับชื่อไฟล์) เท่ากับ 1 หรือไม่
if len(sys.argv) == 2:
    # ดึงพารามิเตอร์ตัวแรก (index 1) มาทำให้เป็นตัวพิมพ์เล็กทั้งหมด
    result = sys.argv[1].lower()
    print(result)
else:
    # หากไม่มีพารามิเตอร์ หรือมีมากกว่า 1 ให้แสดง none
    print("none")