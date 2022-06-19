import random, sys

print("Heyyyyyyyyy, I am thinking of a number between 1 and 20\n")
print("Type your guess here: ")

n = int(input())

rand = random.randint(1,10)

while n != rand:
    if n > rand:
        print("\nOop your guess is to high!" * 5)
        sys.exit();
    elif n < rand:
        print("\nNah your guess is too low!" * 5)
        sys.exit();

print("\nNice Job You Got It!!!!")
sys.exit();
