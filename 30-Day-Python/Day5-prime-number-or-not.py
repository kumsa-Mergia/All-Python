num = int(input("Enter a Number : "))
f = 0
if num == 1:
  print("1 is nor prime")
else:
  for a in range(2,num):
    if num % a == 0:
      print(num," is not a Prime number")
      break
  else:
    print(num," is a prime number")
