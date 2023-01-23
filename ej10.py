def poder(base, exponente):
  if exponente < 0:
  result = 1
  for i in range(exponente):
        result *= base
    return result 
    