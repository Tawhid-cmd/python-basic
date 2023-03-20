mass1 = float(input('First mass :'))
mass2 = float(input('second mass :'))

d = float(input('Distance between the objects:'))

G= 6.673*(10**-11)

force= (G*mass1*mass2)/(d**2)

print('The gravitational force is :', force, 'N')