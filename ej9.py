class guerrero:
  def n (self, nombre):
    self.nombre= nombre
    self.sano= 100
    self.ataque= 5
    self.bloque= 0
    self.zombie= False
    self.muerte= False
  def ataque(self, enemigo, posicion):
    