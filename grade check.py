print("Enter Your marks:")
sub1= int(input('1st subject:'))
sub2= int(input('2nd subject'))
sub3= int(input('3rd subject'))
sub4= int(input('4th subject'))
sub5= int(input('5th subject'))

avg= (sub1 +sub2 +sub3 +sub4 +sub5 )/5

if avg>=90:
    print('Grade A')
elif avg>=70:
    print('Grade B')
elif avg>=60:
    print('Grade C')
elif avg>=40:
    print('Grade D')
else:
    print('Grade F')