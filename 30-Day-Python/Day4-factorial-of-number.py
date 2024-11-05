num = int(input("Enter a Number : "))
p = 1
for a in range(num,0,-1):
  p = p * a # p*= a

print("Factorial of ",num, " is ",p)
