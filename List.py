# Declare lists
numbers = [1, 2, 4, 6, 8, 19]
names = ["Mateo", "Danny", "James", "Thomas", "Luke"]
mixed = [-2, 5, 84.2, "Mountain", "Python"]

# Display lists using the for loops

for n in numbers:
    print(n, end=" ")
print()

for n in names:
    print(n, end=" ")
print()

for n in mixed:
    print(n, end=" ")
print()

'''
Lists นั้นทำงานกับ Index ดังนั้นเราสามารถเข้าถึงข้อมูลของ List 
โดยการใช้ Index ของมันได้ ในตัวอย่างเป็นการเข้าถึงข้อมูลภายใน Index ซึ่ง Index ของ List 
นั้นจะเริ่มจาก 0 ไปจนถึงจำนวนทั้งหมดของมันลบด้วย 1 ในตัวอย่างเราได้แสดงผลข้อมูลของสอง List 
ในตำแหน่งแรกและในตำแหน่งที่ 4 ด้วย Index 0 และ 3 ตามลำดับ หลังจากนั้นเราเปลี่ยนค่าของ List 
ที่ตำแหน่งแรกเป็น "Scalar" 
'''
languages = ["C", "C++", "Java", "Python", "PHP"]

print("Index at 0 = ", languages[0])
print("Index at 3 = ", languages[3])
languages[0] = "Scalar" #เป็นการเปลี่ยนค่าใน list ตำแหน่ง 0
print("Index at 0 = ", languages[0])
