n1 = int(input("Enter The First Number : "))
n2 = int(input("Enter The Second Number : "))

while n1 % n2 != 0:
  rem = n1 % n2
  n1 = n2
  n2 = rem

print("HCF is : ",n2)
