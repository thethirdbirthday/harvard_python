#In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

#First take
#Create function
#def energy():
#Take input
  #string = input()
#Convert string input to integer
  #int(string) = mass
#Apply integer to formula
  #result = mass * 300000000 ** 2
  #print(result)

#Second take 
m = int(input("mass: "))
c= 300000000
E = m * (c ** 2)
print(E)
