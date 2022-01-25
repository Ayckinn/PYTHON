from os import system

count = 1
width = 20

system("clear")
print("\033[0;32m") #-- GREEN

for i in range(10):
    print(("*" * count).center(width))
    count += 2

print("\033[1;31m", end = "") #-- RED
print("| |".center(width))
print("\033[1;m")
