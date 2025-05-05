choise = input("This is a prime number checker. Do you want to check a range or a single value?")
def prime_check(check):
  clist = list(range(2,check))
  divisibility = []
  for x in clist:
    if check%x != 0: 
      divisibility.append(True)
    else:
      divisibility.append(False)
  if check == 1:
    return "This number is neither prime nor composite."
  elif all(z == True for z in divisibility):
    return "This number is prime."
  else:
    return "This number is not prime."
def prime_check_list(start, end):
  num_2_check = list(range(start, end+1))
  prime = []
  for a in num_2_check:
    
    clist = list(range(2,a))
    divisibility = []
    for x in clist:
      if a%x != 0: 
        divisibility.append(True)
      else:
        divisibility.append(False)
    if all(z == True for z in divisibility) and a != 1:
      prime.append(a)
  return prime
if choise == "single value":
  check = int(input("Enter a number to check:"))
  print(prime_check(check))
else:
  start = int(input("Enter start number:"))
  end = int(input("Enter end number:"))
  print(prime_check_list(start, end))