def rangetest():
    global i
    for i in range(1, 21, 2):
        print(i, end=' ')
    print()


rangetest()


def rangetest2():
    global i
    for i in range(0, 101, 10):
        print(i, end=' ')
    print()


rangetest2()


for i in range(20,0,-1):
    print(i, end=' ')
print()

stars = int(input("How many stars?: "))
for i in range(stars):
    print('*',end=' ')
print()



#I'm a little lost here
stars = int(input("How many stars?: "))
for i in range(stars):
    print('*' * (i + 1), end=' ')
    print()
print()
