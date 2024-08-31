from models.client import Client
from models.count import Count

felicity: Client = Client('Felicity Jones',
                          'felicity@gmail.com',
                          '123.456.789-01',
                          '02/09/1987')

angelina: Client = Client('Angelina Jolie',
                          'angelina@gmail.com',
                          '234.567.898-02',
                          '08/07/1978')

# print(30*'-')
#
# print(felicity)
#
# print(30*'-')
#
# print(angelina)

# print(30*'-')

count_felicity: Count =Count(felicity)
count_angelina: Count =Count(angelina)

# print(30*'-')
#
# print(count_felicity)
#
# print(30*'-')
#
# print(count_angelina)
#
# print(30*'-')
