import random

class Species:
  def __init__(self, name, biome, consumer, diet, population):
    self.name = name
    self.biome = biome
    self.consumer = consumer
    self.diet = diet
    self.population = population

points = 0
wave = 0

Zebra = Species("Zebra", "plains", 1, "herbivore", 0)
Lion = Species("Lion", "plains", 3, "carnivore", 0)
Cheetah = Species("Cheetah", "plains", 2, "carnivore", 0)
B = "Plains"
Grass = Species("Grass", "plains", 0, "producer", 0)

print("Welcome! An ecosystem in your hands, President Joe Bison!")
print("The biome for this game is " + B)
print("Created by Rick Feng, Anderson Liu, Ethan Wang, and Sean Xing")

Lion.population = random.randrange(2, 4)
Zebra.population = random.randrange(200, 300)
Cheetah.population = random.randrange(20, 30)
Grass.population = random.randrange(2500, 3500)

print("\n")
print("Lion: " + str(Lion.population))
print("Zebra: " + str(Zebra.population))
print("Cheetah: " + str(Cheetah.population))
print("Grass: " + str(Grass.population))

print("\n")

while (Lion.population > 0 and Zebra.population > 0 and Cheetah.population > 0):
  prey = Zebra.population + Cheetah.population
  for x in range(Lion.population):
    x += 2
    if(prey > 0):
      rnum = random.randrange(0, prey)
      if(rnum > Zebra.population):
        Cheetah.population -= 1
        newnum = random.randrange(0,4)
        if newnum == 2:
          Lion.population += random.randrange(0, 4)
      else :
        Zebra.population -= 1
        newnum = random.randrange(0,4)
        if newnum == 2:
          Lion.population += random.randrange(0, 4)
  Lion.population -= (Lion.population/10)
  for x in range(Cheetah.population):
    x+=3
    if(Zebra.population > 0):
      Zebra.population-=1
      newnum = random.randrange(0,4)
      if newnum == 2:
          Cheetah.population += random.randrange(0, 8)
  Cheetah.population -= (1+Cheetah.population/5)
  for x in range(Zebra.population):
     if(Grass.population >= 10):
      Grass.population -=10;
      newnum = random.randrange(0,3)
      if newnum == 2:
          Zebra.population += random.randrange(0, 5)
  Zebra.population -= (2 + Zebra.population/4)
  points += 50
  wave += 1
  Grass.population += 1000
  Lion.population = round(Lion.population)
  Zebra.population = round(Zebra.population)
  Cheetah.population = round(Cheetah.population)
  waveprompt = print("You are on Round " + str(wave))
  pointsprompt = print("You have " + str(points) + " points.")
  print("\n")
  popcheck = input("Do you want to view the population for each animal? Type y or n. ")
  if(popcheck == "y"):
    print("\n")
    print("Lion: " + str(Lion.population))
    print("Zebra: " + str(Zebra.population))
    print("Cheetah: " + str(Cheetah.population))
    print("Grass: " + str(Grass.population))
  shopprompt = input("Do you want to view the store? Type y or n. ")
  if(shopprompt == "y"):
    solditem = input("Store: Type '1' for 3-6 Zebras (25 points). Type '2' for 2-4 Cheetahs (40 points). Type '3' for 1-2 Lions (80 points). ")
    if(int(solditem) == 1):
      points-=25
      Zebra.population += random.randrange(2, 7)
      pointsprompt = print("\nYou have " + str(points) + " points.")
    elif (int(solditem) == 2):
      points-=40
      Cheetah.population += random.randrange(1, 5)
      pointsprompt = print("\n You have " + str(points) + " points.")
    else: 
      points-=80
      Lion.population += random.randrange(0,3)
      pointsprompt = print("\n You have " + str(points) + " points.")
  Lion.population = round(Lion.population)
  Zebra.population = round(Zebra.population)
  Cheetah.population = round(Cheetah.population)
  
  print("\n Round is over. \n")
print("Well Done! :D You have lasted " + str(wave) + " waves. Your final point total was " + str(points) + " points.")