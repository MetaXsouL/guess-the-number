import math
import random
ascii_art = """⋱ ⋮ ⋰
⋯ ◯ ⋯ ︵ 　　　　　　^v^
¸︵︵( ░░ )︵.︵.︵　　
(´░░░░░░ ') ░░░' )
`´︶´¯`︶´`︶´︶´`　^v^　　^v^
╔┓┏╦━━╦┓╔┓╔━━╗╔╗
║┗┛║┗━╣┃║┃║╯╰║║║
║┏┓║┏━╣┗╣┗╣╰╯║╠╣
╚┛┗╩━━╩━╩━╩━━╝╚╝
♪♫•*¨*•.¸¸❤¸¸.•*¨*•♫♪
"""


lines = ascii_art.split('\n')

for line in lines:
    print(line.center(80))
print("Input the range of number:")
first = int(input("The first number:"))
last = int(input("Input the last number:"))
number = random.randint(first,last)
# print(number)
user =int(input(f"Guess the nuber which is between {first} and {last}: "))
if user==number:
    print("Hurray ! you gotted a first\nʕ•ᴥ•ʔ")
else:
    while number!=user:
        user1=int(input("Try again :"))
        if user1<number:
            print("Too Low Input Again ")
        elif user1>number:
            print("Too High Input Again ")
        elif user1==number:
            print("Gotted")
            print("""(\____/)
( ͡ ͡° ͜ ʖ ͡ ͡°)
\╭☞ \╭☞

""")


            break
