def count(value):
    pass
s=input("Enter the string :")
# s="aabbc"
result=[]
for i in s:
    if s.count(i)==1:
       result.append(i) 
if len(result)==0:
    print(None)
else:
    print("The first non repeated value is :",result[0])