from cgi import print_arguments


print('Hello there')

print('''            __.-._
            '-._"7'
             /'.-c
             |  /T
        snd _)_/LI''')

print("\nWhat is your name young one?")
name = input() 
# takes users name as input

print("\nGood to me you it is, young " + name)
# concats the input to a string

print("\nThe length of your name is: " + str(len(name)))
# makes the input into a string and determins its length

print("\nWhat is your age?")
age = input()
# takes users age as input

print("\nHmmm you will be " + str(int(age) + 400) + " a long time from now.")
# changes that input to a int adds it to 400 and changes the sum to a string

'''
test = round(3.1415926535457)

print(test)

exit()
'''
