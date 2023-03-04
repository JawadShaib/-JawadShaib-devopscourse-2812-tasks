# Exercise 1

X = int(input("please enter the fist Number: "))
Y = int(input("please enter the second Number: "))

if X > Y:
    print("BIG")
elif X < Y:
    print("SMALL")
else:
    print("Not Relevant")

# Exercise 2

for i in range(5):
    print(i)

# Exercise 3

season = int(input(" Enter a Number between 1-4 "))
season_num = [1, 2, 3, 4]

if season not in season_num:
    print("Error the number you entered is not in range ")
else:
    if season == 1:
        print(" the season is Summer !")
    elif season == 2:
        print(" the season is fall ")

    elif season == 3:
        print(" the season is fall ")

    elif season == 4:
        print(" the season is fall ")

# Exercise 4

"a: the while loop will be executed  10 times "
"b: the last num printed  will be 10 "

# Exercise 5

info = {
    "age": 24,
    "first letter": "J",
    " Nis -> dollars": 3.51,
    " fly aboard ?": True,
    " apt number": 1,
}

for i in info:
    print(i, info[i])

print(
    "results of adding age to cuurency: ", float(info["age"]) + info[" Nis -> dollars"]
)

# Exercise 6

phone_number = int(input("please write your phone number: "))
print("phone number: ", phone_number)


# Exercise 7


def print_hello():
    print("hello !")


def calculate():
    print("the result is: ", 5 + 3.2)


print_hello()
calculate()


# Exercise 8
def get_name(name):
    print(name)


def get_div(num):
    print(round(num / 2, 2))


name = input(" welcome , enter your name: ")
num = int(input("please enter a number: "))

get_name(name)

get_div(num)


# Exercise 9


def calc_sum(x, y):
    return x + y


def new_string(str1, str2):
    return str1 + " " + str2


x = int(input("enter your first num: "))
y = int(input("enter your second num: "))
print(calc_sum(x, y))

a = input("enter your first string: ")
b = input("enter your first string: ")
print(new_string(a, b))

# Exercise 10 creating a triangle option 1

sum = ""
for i in range(5):
    for j in range(i + 1):
        sum += "*"

    print(sum)
    sum = ""

# Exercise 10 creating a triangle option 2

for i in range(5):
    print((i + 1) * "*")
