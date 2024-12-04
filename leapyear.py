a=int(input("Enter Starting Year"))
b=int(input("Enter Last Year"))
if a>b:
    print("wrong input")
    exit()
print(f"leap year from {a} to {b} are:")
for x in range(a,b+1):
    if(x%4==0 and x%100!=0) or (x%400==0):
       print(x)