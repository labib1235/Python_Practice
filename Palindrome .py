#a = [22, 42, 22, 77, 67, 45, 67, 56, 12, 10, 10, 42]
#my_list = []
#for i in a:
#    if i not in my_list:
#        my_list.append(i)
#print(my_list)


#print("Please input the number: ")
#number = int(input())
#temp = number
#while number > 0:
#    count = temp
#    while count > 0 :
#        print('*', end='')
#        count -= 1
#    print()
#    number -= 1


print("please input your word: ")
word = input()
word = word.casefold() 
reversed_word = word[::-1]

if word == reversed_word:
    print('Great! It is a palindrome.' )
else:
    print('LOL! It is  not a palindrome.' )