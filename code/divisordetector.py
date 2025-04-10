number = int(input("Enter a number"))
var = number
a = []
while var>=1:
  x=(number/var)
  if x%1 == 0:
    a.append(x)
  var = var-1
print(a)
