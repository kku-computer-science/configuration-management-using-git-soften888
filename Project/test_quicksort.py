#Unit Test ถ้าตรวจสอบแล้ว ลบไฟล์นี้ทิ้งได้
#import quicksort
from quicksort import quick_sort
#test ลิสต์ว่าง
def test_empty_list():
    assert quick_sort([]) == []
#test ลิสต์มีตัวเดียว
def test_only_element():
    assert quick_sort([5]) == [5]
#test เรียงมาแล้ว
def test_sorted():
    assert quick_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
#test กลับหลัง
def test_reverse_order():
    assert quick_sort([4, 3, 2, 1]) == [1, 2, 3, 4]
#test ซ้ำกัน
def test_duplicate():
    assert quick_sort([3, 1, 2, 3, 3]) == [1, 2, 3, 3, 3]
#test ติดลบ
def test_negativenumbers():
    assert quick_sort([-1, -5, 0, 3]) == [-5, -1, 0, 3]
