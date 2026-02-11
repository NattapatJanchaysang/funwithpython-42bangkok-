#!/usr/bin/env python3
import sys

# 1. ตรวจสอบว่ามีพารามิเตอร์ส่งมาครบ 2 ตัวหรือไม่ (sys.argv ต้องมี 3 ตัวรวมชื่อไฟล์)
if len(sys.argv) == 3:
    keyword = sys.argv[1]
    text = sys.argv[2]
    
    # 2. นับจำนวนครั้งที่ keyword ปรากฏใน text
    occurrence = text.count(keyword)
    
    # 3. ตรวจสอบว่าพบคำนั้นหรือไม่ (ต้องมากกว่า 0)
    if occurrence > 0:
        print(occurrence)
    else:
        print("none")
else:
    # หากพารามิเตอร์ไม่ครบหรือเกิน ให้แสดง none
    print("none")