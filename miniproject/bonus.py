import sys
from checkmate import checkmate

def solve():
    #ตรวจสอบว่ามีการส่งไฟล์เข้ามาไหม
    if len(sys.argv) < 2:
        print("Error: Please provide a board file.")
        return

    # วนลูปอ่านทีละไฟล์ (เผื่อส่งมาหลายไฟล์)
    # เริ่มที่ index 1 เพราะ index 0 คือชื่อโปรแกรม main.py
    for filename in sys.argv[1:]:
        try:
            # พยายามเปิดไฟล์ขึ้นมาอ่าน
            with open(filename, 'r') as f:
                board_content = f.read()
                
            # ส่งเนื้อหาในไฟล์ไปตรวจ
            print(f"--- Checking {filename} ---")
            checkmate(board_content)
            print("") 

        except FileNotFoundError:
            # ถ้าหาไฟล์ไม่เจอ
            print(f"Error: File '{filename}' not found.")
        except Exception as e:
            # ถ้าเกิด error อื่นๆ
            print(f"Error reading '{filename}': {e}")

if __name__ == "__main__":
    solve()