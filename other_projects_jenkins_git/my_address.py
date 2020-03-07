class Envelope():
    def __init__(self, to,address,city,state,zipcode, street,suite):
        self.to = to
        self.address = address
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.suite = suite

    def mail(self):
        print('Recipients Name')
letter = Envelope(to = 'Azizbek Gapurov', address = 1101, street = 'Columbia ave',suite=209,city = 'Chicago', state = 'Illinos', zipcode = 60626)

print(letter.mail())        
print(letter.to)
print(letter.address)
print(letter.street)
print(letter.suite)
print(letter.city)
print(letter.state)
print(letter.zipcode)