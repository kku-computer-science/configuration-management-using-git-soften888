import Project.BubbleSort as BubbleSort
import Project.quicksort as QuickSort

array = list(map(int, input("ป้อนลำดับตัวเลขที่ต้องการจัดเรียง: ").split()))
print("เลือกวิธีการเรียงลำดับ\n1. Quick Sort\n2. Bubble Sort")

choice = input("ป้อนตัวเลือก: ")
if choice == "1":
    result = BubbleSort.bubble_sort(array)
    print("Bubble Sort Result : " + result)

elif choice == "2":
    result = QuickSort.quick_sort(array)
    print("Quick Sort Result : " + result)

else:
    print("ตัวเลือกไม่ถูกต้อง")