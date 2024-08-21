# Brilliant challenge about loops 4 flames difficult
# number = 3
# steps = 0

# for i in range(200):
#     if number == 1:
#         break
#     # fill in the rest of this program
    
# if number == 1:
#     print("It took", steps, "steps")
# else:
#     print("The number didn't reach 1 yet")

number = 3
steps = 0

for i in range(200):
    if number%2 == 0:
        number = number/2
    else:
        number = (number*3) + 1
    print(number)
    steps += 1
    if number == 1:
        break

print('it took',steps,'steps to reach into 1')
    