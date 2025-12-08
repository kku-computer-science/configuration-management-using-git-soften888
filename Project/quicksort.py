#Quick Sort by Thitiwut2136 Date: 9/12/2568

#base case ถ้าจำนวนสมาชิกน้อยกว่า 2 ไม่ต้องเรียงเพราะเรียงอยู่แล้ว
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
#ใช้ pivot เป็นค่าตรงกลางของ list 
    pivot = arr[len(arr) // 2]
#แยกleft/mid/right ตอนtest จะได้เห็นชัด
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
#เรียกquicksort + เอาผลลัพธ์มาต่อกัน
    return quick_sort(left) + mid + quick_sort(right)
#รันtest แบบไม่ผ่าน main ถ้า ไม่conflict แล้วลบข้างล่างทิ้งได้เลย
if __name__ == "__main__":
    data = [42, 71, 84, 91, 11, 5]
    print("Original:", data)
    print("Sorted:", quick_sort(data))
#Unit Test ผ่าน ทั้ง 6ตัว น่าจะไม่มีปัญหา(ตอนนี้)