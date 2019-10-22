a=34
if a==3:
    print("a=3")
else:
    print("a not equal to 3")
#elif a>3:
#    print("NADA")
for i in range(3):
    print("Hello world!",i)
    
arr = [1.0, 2, "Test", 5,3.1415926,16]
print(arr[2])
arr[4] = 10
print(arr)
print(len(arr)) 

for i in range(len(arr)):
    print("i = ", i, "arr[i] = ", arr[i])
    
for i in range(11):
    print(i*i)

for a in arr:
    print(a)