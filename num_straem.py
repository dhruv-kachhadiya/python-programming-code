#simple numeric stream....
print('simple numeric stream...')
a=range(100)
b=(x for x in a)
print(list(b))

#odd number stream....
print('\nodd number stream...')
a=range(1,100,2)
b=(x for x in a)
print(list(b))

#even number stream.....
print('\neven number stream....')
a=range(2,100,2)
b=(x for x in a)
print(list(b))
