# task n1
agr = 'word'
doc = 24

print(doc)
print(agr)

doc_init = int(input('write number'))
agr_init = input('write any text')

print(agr_init)
print(doc_init)

# task n2

DayTime = int(input('write the number of second you need'))
s = int('00')
m = int('00')
h = int('00')

while DayTime >= 59:
    if DayTime >= 3600:
        DayTime -= 3600
        h += 1
    elif DayTime < 3600:
        DayTime -= 60
        m += 1
else:
    s += DayTime

print(str(h) + ':' + str(m) + ':' + str(s))


# task n3

a = int(input('write the number'))
b = str(a) + str(a)
c = str(a) + str(a) + str(a)
print(int(a) + int(b) + int(c))

# task n4

bite = int(input('write the number'))





