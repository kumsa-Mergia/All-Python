a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))

if a > b:
  g = a
else:
  g = b
for n in range(g, a*b + 1):
  if n % a == 0 and n % b ==0:
    print("LCM of ",a," and ",b," is ",n)
    break
