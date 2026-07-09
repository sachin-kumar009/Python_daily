str1="Hello World"
str2="12345"
str3="1hello"
res1=str1.find("Wor") #it is used to find the characters in string
print(res1)
res2=str1.index("Wo")
print(res2)
res3=str1.index(".") #same as find but it produce error instead of -1
print(res3)
res4=str1.startswith("He") #checks if it starts with the given char
print(res4)
res5=str1.endswith("ld") #checks if it ends with the given char
print(res5)
res6=str1.count("l") #checks the count of given char in string
print(res6)
res7=d.isalpha() #checks if the string contains only alphabets(no digits,no spaces)
print(res7)
res8=str2.isdigit() #checks if the string contains only digits(no alphabets,no spaces)
print(res8)
res9=str3.isalnum() #checks if the string contains digits and alphabets(no spaces)
print(res9)
res10=d.swapcase() #swaps lower with upper and vice versa
print(res10)
res11=d.center(20,"-") #it centers with width
print(res11)
res12=str2.zfill(5) #fills '0' at start
print(res12)
print("my statement is {} and age is {}".format(d,str2)) #format is used to format the string
print(f"my statement is {d} and second is {str2}") #fstring is another way to format the string
print("my name is",d," age is",str2)

#list

num=[1,2,3]
num.append(4) #adds the number to last of list
print(num)
num.extend([5,5,6]) #could add multiple numbers
print(num)
num.insert(0,0) #inserts the number at given index(index,number)
print(num)
num.remove(5) #remove first matching element from list
print(num)
items=num.pop() # items will display the popped element.If given no value it pops last element
print(num)
print(items)
num1=[1,2,3,4]
num1.clear() #clears the list
print(num1)
l1=['a','b','c','d'] 
res=l1.index('b') #points the position
print(res)
res1=l1.count('b') #repetition of given char in list
print(res1)
print("".join(l1)) #joins list into string

num2=[2,33,3]
num2.sort() #sorts in ascending order
print(num2)
num2.sort(reverse=True) #sorts in descending order
print(num2)
num2.reverse() #reverses the list
print(num2)
num3=num2.copy() #copies the data into another list
print(num3)
print(len(num3)) #returns the number of elements
print(max(num3)) #returns largest element in the list
print(min(num3)) #returns smallest element in the list
print(sum(num3)) #returns sum of all elements in the list
print(sorted(num3)) #returns a new list with elements sorted in ascending order
