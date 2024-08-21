# # Fibonnaci Sequence
# a = 1
# b = 1
# for i in range(1,16):
#     sum = a + b
#     a = b
#     b = sum
#     i += 1
#     print('A soma desses termos é:', sum,'O valor a é:',a,' e o valor b é :',b)
# print('número de termos: ',i)
# Fibonnaci Sequence 2,5
a = 2
b = 5
for i in range(1,4):
    print('a value before sum:', a)
    print('b value before sum:', b)
    sum = a + b
    print('the sum is:', sum)
    a = b
    b = sum
    print('a after sum:', a)
    print('b after sum:,', b)