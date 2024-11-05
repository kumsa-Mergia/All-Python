num = int(input("Enter a number : "))

print("Factors of ",num," are : ")
a = 1
for a in range(1, num+1):
  if num % a == 0:
    print(a)
  a += 1
