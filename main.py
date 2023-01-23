def p4(n):
  if type(n) != int or n <= 0:
    return Flase
  while n % 4 == 0:
    n= n/4
  return n == 1
print(p4(1024))
print(p4(55))
print(p4("Cuatro"))
print(p4(0))
print(p4(-4))
    