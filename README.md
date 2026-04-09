> ** AI Declaration: This document was formatted and organized using AI assistance(ChatGPT) to enhance readability, structure, and visual presentation.

# โปรเจกต์นี้เป็นส่วนหนึ่งของวิชา CP353004 Software Engineering  
กิจกรรม Lab 3.3: Configuration Management using Git  
ภาคการศึกษา 2/2568

---

## สมาชิกทีม
- **ณัฐพัฒน์ แสนตรี (663380012-6)** : รับผิดชอบส่วน Main Program
- **ธิติวุฒิ ศรีอมรรัตน์ (663380213-6)** : รับผิดชอบส่วน Algorithm Quick Sort
- **ณัฐรภา ศรีวิชา (663380504-5)** : รับผิดชอบส่วน Algorithm Bubble Sort

---

## โครงสร้างโปรเจกต์
```
configuration-management-using-git-soften888/
│── Project/
│   │── BubbleSort.py      \# ฟังก์ชันการทำงานของ Bubble Sort Algorithm
│   └── quicksort.py       \# ฟังก์ชันการทำงานของ Quick Sort Algorithm
│── AboutMyTeam/           \# ข้อมูลรายละเอียดของสมาชิกในทีม
│── main.py                \# โปรแกรมหลัก สำหรับรับค่า input และแสดงผลลัพธ์
└── README.md              \# คำอธิบายโปรเจกต์
```

---

## ขั้นตอนการรันทดสอบโปรแกรม

**1. ให้ทำการ clone repository ลงไปในเครื่อง โดยใช้คำสั่ง**

```
git clone https://github.com/kku-computer-science/configuration-management-using-git-soften888.git
```

-----

**2. เข้าไปในโฟลเดอร์โปรเจ็ค**

```
cd configuration-management-using-git-soften888
```

-----

**3. การรันโปรแกรมหลัก**
รันไฟล์ `main.py` ใน Terminal จะปรากฏข้อความให้ผู้ใช้ป้อนข้อมูลตัวเลข

```
python main.py
```

  * **Input:** กรอกตัวเลขจำนวนเต็มหลายๆ ตัว โดย**เว้นวรรค**ระหว่างตัวเลข (เช่น `10 5 2 8 7`)

-----

**4. เลือกวิธีการเรียงลำดับ (Sorting Method)**
หลังจากใส่ค่าตัวเลขแล้ว ระบบจะให้เลือกเมนู ดังนี้:

  * พิมพ์ 1 : เพื่อเลือกการเรียงลำดับแบบ Quick Sort
  * พิมพ์ 2 : เพื่อเลือกการเรียงลำดับแบบ Bubble Sort

*เมื่อเลือกเสร็จสิ้น โปรแกรมจะแสดงผลลัพธ์ของอาเรย์ที่เรียงลำดับเรียบร้อยแล้ว*

-----
