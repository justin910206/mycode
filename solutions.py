# Ricky, Jane
for i in range(10):
    if i <=5:
        print("* "*i)
    else:
        print("* "*(10-i))

# Hunter
for i in range(10):
    print("* "*i if i <= 5 else "* "*(5-i%5))

# Luke
stars = ["*", "* *", "* * *", "* * * *", "* * * * *", "* * * *", "* * *", "* *", "*"]
for each in stars:
    print(f"{each}")

# Maya
snowflakes = [1, 2, 3, 4, 5, 4, 3, 2, 1]
for x in snowflakes:
    print(x*"* ")

# Joe
for x in range(1, 11):
    print("* " * x) if x < 5 else print("* " * (10-x))

# Marcelo
line= ["*","* *","* * *","* * * *","* * * * *"];
for x in line:
    print(x)
    if x == line[-1]:
        newline = reversed(line)
        for x in newline:
            print(x)

# Danny
star = "* "
for i in range(6):
    print(star * i)
for j in range(6, 0, -1):
    print(star * j)

# Chris
for x in range(5):
    for i in range(x):
        print("* ", end="")
    print("")
for x in range(5, 0, -1):
    for i in range(x):
        print("* ", end="")
    print("")

# Hunter mk2
a = [print( (("*"*(5-i%5)),"*"*i) [i <= 5]  ) for i in range(10)]

# Levi
for count in (*range(1,6), *range(4,0,-1)): print("* " * count)

# Jeffrey
starStr = ""
for row in range(10):
    if row < 5:
        starStr += "*"
    else:
        starStr = starStr[:-1]
    print(starStr)

# Wonil
asterisk = '* '
for i in range(10):
    if i < 5:
        print(asterisk * i)
    else:
        print(asterisk * (10 - i))

# Michael
string = ""
x=0
y=10
while x < 9:
    x += 1
    y -= 1
    if x < 6:
        string += "* "
        print(string)
    else:
        print(string[0:(y*2)])
