#Celcious to Fahrenhite and Kelvin
celcious=float(input('Temparature in Celcious(deg)'))
fahrenhite=celcious*9*.2+32
kelvin=273.15+celcious
print('Temparature in Fahrenhite(deg)',fahrenhite)
print('Temparature in Kelvin',kelvin)

#Fahrenhite to Celcious and Kelvin
fahrenhite=float(input('Temparature in Fahrenhite(deg)'))
celcious=fahrenhite/9*.2+32
print('Temparature in Celcious(deg)', celcious)
kelvin=273.15+celcious
print('Temparature in Kelvin', kelvin)

#kelvin to Celcious and Fahrenhite
kelvin=float(input('Temparature in Kelvin'))
celcious=kelvin-273.15
print('Temparature in Celcious(deg)', celcious)
fahrenhite=celcious*9*.2+32
print('Temparature in Fahrenhite(deg)',fahrenhite)