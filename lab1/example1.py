print("Hello, World!")

animals = 10
chickens = 6
roosters = animals-chickens
print(roosters)

x = 1
y = 4
z = 0.25
expression = (((2*x+y)**2)*(z**0.5))/(x**0.5 + y**0.5)
print(expression)

a = 2
b = 6
c = -20
d = (b**2) - (4*a*c)
root1 = (-b-d**0.5)/(2*a)
root2 = (-b+d**0.5)/(2*a)
print(root1 , "," , root2)


temperature_celcius = input("What is the temparature?")
temperature_fahrenhait = (int(temperature_celcius)*1.8 + 32)
print(temperature_fahrenhait)


edge1 = input("What is the length of the first perpendicular edge?")
edge2 = input("What is the length of the second perpendicular edge?")
hypo = (int(edge1)**2 + int(edge2)**2)**0.5
print(hypo)


vehicle1 = 80
vehicle2 = 70
beginning = 490
end = 150
time = 60 * (beginning - end) / (vehicle1 + vehicle2)
print(time)