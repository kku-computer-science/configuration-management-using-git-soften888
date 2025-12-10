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
#เรียก quicksort และเรียง
    return quick_sort(left) + mid + quick_sort(right)
