# while loop
i=10
while i<20:
    print(i)
    i+=1

for i in range(5):
    if i==3:
        break
    print(i)

#grade calculator
a=int(input("Enter marks: "))
if 90<=a and a<=100:
    print("A")
elif 75<=a and a<90:
    print("B")
elif 50<=a and a<75:
    print("C")
elif 100<a:
    print("Error!")
else:
    print("Fail")

text=" python language  "
res1=text.upper()
print(res1)
res2=res1.lower()
print(res2)
res3=text.title()
print(res3)
res4=text.capitalize()
print(res4)
res5=text.strip()
print(res5)
res6=text.lstrip()
print(res6)
res7=text.rstrip()
print(res7)
res8=text.replace("python","java")
print(res8)
res9=text.split()
print(res9)
