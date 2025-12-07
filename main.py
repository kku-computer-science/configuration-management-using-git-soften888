array = list(map(int, input("ป้อนลำดับตัวเลขที่ต้องการจัดเรียง: ").split()))
print("เลือกวิธีการเรียงลำดับ\n1. Quick Sort\n2. Bubble Sort")

choice = input("ป้อนตัวเลือก: ")
if choice == "1":
    result = array
    #ทำการ เรียงลำดับด้วย Quick Sort
    print(result)

elif choice == "2":
    result = array
    #ทำการ เรียงลำดับด้วย Bubble Sort
    print(result)

else:
    print("ตัวเลือกไม่ถูกต้อง")