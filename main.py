# print('Hello "world"!')
# print('test')
# print('one', 'two', 'three', sep='____', end=' ')
# print('hello')

# """ Task #1 """
# print('Enter three numbers for math operations: ')
# number1 = int(input('Enter first number: '))
# number2 = int(input('Enter second number: '))
# number3 = int(input('Enter third number: '))
#
# Answer = print('"+" = ', number1 + number2 + number3,'\n'
#                '"-" = ', number1 - number2 - number3,'\n'
#                '"*" = ', number1 * number2 * number3,'\n'
#                '"/" = ', number1 / number2 / number3,
#                )

# """ Task #1 """
# print('Input diagonales.')
# diagonal_1 = int(input('Enter first diagonale: '))
# diagonal_2 = int(input('Enter second diagonale: '))
#
# Answer = print('The area of the rhombus: ', (diagonal_1 * diagonal_2) /2 )
#
# """ Task #3 """
# number = int(input('Enter 4-digital number: '))
#
# n1 = number // 1000
# n2 = number // 100 % 10
# n3 = number // 10 % 10
# n4 = number % 10
#
# result = n1 + n2 + n3 + n4
#
# print(f"n1: {n1} n2: {n2} n3: {n3} n4: {n4}")
# print(f"Result: {result}")

# print('Hello world')
#
# """___________________________________"""
#
# n1 = 10
# n2 = 20
# n3, n4, n5 = 5, 12, 4
#
# print('hello' in 'hello world')

# hours = int(input('Enter time: '))
# if 24 < hours >= 12:
#     print('PM')
# elif 12 > hours >= 0:
#     print('AM')
# else: print('Incorrect time!')

"""new_task"""
ratio = int(input('Enter film ratio: '))
if 0 < ratio <= 5:
    if ratio == 4 or ratio == 5:
        print('Good film')
    else:
        print('Bad film!')