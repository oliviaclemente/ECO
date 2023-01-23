def valor(palabra):
  palabra= palabra.upper()
  palabra_lista= list(permutaciones(palabra))
  palabra_lista sorted(palabra_lista)
  return palabra_lista.index(tuple(palabra)) +1