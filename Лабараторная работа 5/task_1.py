# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
table = list()
for i in range (0,16):
    a = {'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct' : oct(i)}
    table.append(a)
pprint(table)
#так нужно делать?