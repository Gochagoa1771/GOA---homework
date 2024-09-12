numbers = ['1', '2', '3', '4' ,'5' ,'6' ,'7' ,'8' ,'9' ,'10'] 
print(numbers[0:5])

numbers = ['1' , '2', '3', '4' ,'5' ,'6' ,'7' ,'8' ,'9' ,'10']
print(numbers[7:10])

numbers = ['1' , '2', '3', '4' ,'5' ,'6' ,'7' ,'8' ,'9' ,'10']
print(numbers[::2])

fruit = ['apple' ,'banana' ,'fig' ,'grapes' ,'cherry' ,'watermelon' ,'orange' ,'mellon' ,'pear']
print(fruit[::-1])

fruit = ['apple' ,'banana' ,'fig' ,'grapes' ,'cherry' ,'watermelon' ,'orange' ,'mellon' , 'pear']
fruit[4] = ['kiwi'] 
fruit[5] = ['lime']
print(fruit)