#Compound interest
p= float(input('Money you borrowed:'))
r= float(input('Interest rate (per year):'))
t=float(input('Overall duration:'))

A=p*(1+r/100)**t
print(' interest amount is :', A)