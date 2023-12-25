a = 10
def something(k):
    k = 15
    global a
    a = 200
    print('In function')
    print(a)
    print(k)
    print('End function')

print('Out of function')

print(a)
something(a)
print(a)
    