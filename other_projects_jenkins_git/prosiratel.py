import datetime
d1 = datetime.date.today()
print('d1:',d1)
d2 = d1.replace(year=int(input("enter year of birth:")),month=int(input("enter month of birth:")), day=int(input("enter birth day:")))
print('d2:',d2)
print("stolko vremeni prosrano", d1-d2)
input()
