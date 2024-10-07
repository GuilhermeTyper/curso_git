class Animal():
  def falar(self):
   pass

class Cachorro(Animal):
  def falar(self):
   print('latindo...')

class Gato(Animal):
  def falar(self):
    print('miando...')

gato = Gato()
cachorro = Cachorro()

mamiferos = [gato, cachorro]

for animais in mamiferos:
    animais.falar()