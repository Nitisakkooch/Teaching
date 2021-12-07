#---การอ่านข้อมูลจาก Text file---
f = open('t1.txt', 'r')
s = f.read()
f.close()
print(s)

#---การอ่านข้อมูลจาก Binary file---
# writing to binary file
f = open('data', 'wb')
f.write(b'marcuscode')
f.close()

# reading from binary file
f = open('data', 'rb')
print(f.read(3))
print(f.read(3))
print(f.read(4))

f.seek(0)
print(f.read(1))

f.seek(-4, 2)
print(f.read())

f.close()