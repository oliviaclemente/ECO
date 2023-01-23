def db(links):
  red= [[0 for i in range(3)] for i in range(3)]
  record= [0, 0]
  for l in links:
if l[0] ==  if l[0] == l[1] - 1:
  if red[l[0] // 3][l[0] % 3] == 0 and red[l[1] // 3][l[1] % 3] == 0:
    record[0] += 1
    record[1] += 1
  elif red[l[0] // 3][l[0] % 3] == 0:
    record[0] += 1
   elif red[l[1] // 3][l[1] % 3] == 0:
     record[1] += 1
    