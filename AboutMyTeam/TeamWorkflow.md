> ** AI Declaration: This document was formatted and organized using AI assistance(ChatGPT) to enhance readability, structure, and visual presentation.

## Team Workflow – Lab 03: Project Management

## สมาชิกทีม
- **ณัฐพัฒน์ แสนตรี (663380012-6)** : รับผิดชอบส่วน Main Program
- **ธิติวุฒิ ศรีอมรรัตน์ (663380213-6)** : รับผิดชอบส่วน Algorithm Quick Sort
- **ณัฐรภา ศรีวิชา (663380504-5)** : รับผิดชอบส่วน Algorithm Bubble Sort

---

## วัตถุประสงค์ของโครงการ (Objective)
โปรเจกต์นี้มีเป้าหมายเพื่อพัฒนาโปรแกรมภาษา Python ที่สามารถ:

1. รับค่าจำนวนเต็มจากผู้ใช้
2. เก็บข้อมูลในลิสต์
3. จัดเรียงข้อมูลด้วยสองอัลกอริทึม ได้แก่
    -    Quick Sort
    -    Bubble Sort
4. แสดงผลข้อมูลที่จัดเรียงแล้ว พร้อมระบุชื่ออัลกอริทึมที่ใช้

--- 

# โครงสร้างโปรเจกต์ (Project Structure)
```
configuration-management-using-git-soften888/
│── Project/
│   │── BubbleSort.py      \# ฟังก์ชันการทำงานของ Bubble Sort Algorithm
│   └── quicksort.py       \# ฟังก์ชันการทำงานของ Quick Sort Algorithm
│── AboutMyTeam/           \# ข้อมูลรายละเอียดของสมาชิกในทีม
│── main.py                \# โปรแกรมหลัก สำหรับรับค่า input และแสดงผลลัพธ์
└── README.md              \# คำอธิบายโปรเจกต์
```
## แนวทางการทำงาน (Workflow)

1. การตั้งค่า Repository

- Thitiwut245 สร้าง Team Repository บน GitHub
- จัดโครงสร้างไฟล์ตามรูปแบบที่กำหนด
- เพิ่มสมาชิกทีมให้สามารถร่วมพัฒนาได้

2. การสร้าง Branch (Branching Strategy)
| งานที่รับผิดชอบ | ชื่อ Branch |
|-----|-------------|
| Quick Sort | `Thitiwut_2136` |
| Bubble Sort | `Natrapa_5045` |
| Main Program | `nattaphat010447` |

## ข้อกำหนด:

- ไม่ push เข้าbranch main โดยตรง
- สมาชิกแต่ละคนทำงานเฉพาะบน branch ของตัวเอง
- เมื่อทำงานเสร็จ ให้เปิด Pull Request
- รอตรวจสอบและอนุมัติ ก่อน merge เข้าสู่ branch main

## รายละเอียดตามบทบาทของสมาชิกทีม
1. Main Program

ผู้รับผิดชอบ: ณัฐพัฒน์ แสนตรี 
หน้าที่:

- เขียนไฟล์ main.py ให้สามารถ

    - รับค่า input จากผู้ใช้
    - แสดงเมนูเลือกอัลกอริทึม
    - เรียกใช้ฟังก์ชัน quick_sort หรือ bubble_sort ตามที่เลือก
    - แสดงผลข้อมูลที่เรียงแล้ว
    - ตรวจสอบและ review Pull Request จากสมาชิกทีม

---

2. Quick Sort

ผู้รับผิดชอบ: ธิติวุฒิ ศรีอมรรัตน์
หน้าที่:
- เขียนฟังก์ชัน quick_sort()
- ดูแลการประมวลผล input และ output ให้ถูกต้อง
- สามารถเพิ่มข้อความอธิบายขั้นตอนภายในฟังก์ชัน เช่น การเลือก pivot, การแบ่งกลุ่มข้อมูล

---
3. Bubble Sort

ผู้รับผิดชอบ: ณัฐรภา ศรีวิชา
หน้าที่:
- เขียนฟังก์ชัน bubble_sort()
- ทดสอบการทำงานด้วยชุดข้อมูลหลากหลายรูปแบบ
- ปรับปรุงโค้ดให้มีความชัดเจนและอ่านง่าย

---
## Main Program Flow

1. โปรแกรมเริ่มทำงาน
2. แสดงเมนูให้ผู้ใช้เลือกอัลกอริทึม
3. รับจำนวนข้อมูลจากผู้ใช้
4. รับค่าข้อมูลเข้า list
5. เรียกใช้อัลกอริทึมที่เลือก
6. แสดงผลลัพธ์
7. สิ้นสุดโปรแกรม

## Git Workflow Summary
```
1. Clone repository
   git clone <repository-url>

2. Checkout branch ที่รับผิดชอบ
   git checkout -b <branch-name>

3. เขียนโค้ดและทดสอบ

4. Commit การเปลี่ยนแปลง
   git add .
   git commit -m "<commit message>"

5. Push branch
   git push origin <branch-name>

6. เปิด Pull Request บน GitHub
   จาก <branch-name> → main หรือ staging (ตามที่กำหนด)

7. Reviewer ตรวจสอบและ merge
```