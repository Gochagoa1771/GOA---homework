def calculate(x, y):
    addition = x + y
    subtraction = x - y
    multiplication = x * y
    division = x // y  # მთელი ნაწილის გაყოფა

    return addition, subtraction, multiplication, division

result = calculate(10, 3)
print(f"ჯამი: {result[0]}, გამოკლება: {result[1]}, გამრავლება: {result[2]}, გაყოფა: {result[3]}")

def greet_user(ნიკა):
    message = f"გამარჯობა {"ნიკა"}, კეთილი იყოს შენი მობრძანება, გისურვებ წარმატებას და წინ სვლას"
    return message
print(greet_user("ნიკა"))
def love_letter(ნიკა):
    letter = f"ძვირფასო {"ნიკა"},\nმინდა გაგიზიაროთ ჩემი გულწრფელი გრძნობები და გულითადი სურვილები შენთან მიმართებაში. შენი არსებობა ჩემს ცხოვრებაში საოცარი ბედნიერებაა. \nსიყვარულით {name}"
    return letter

def find_max(num1, num2):
    # შეადარეთ ორი რიცხვი და დააბრუნეთ მაქსიმალური
    if num1 > num2:
        return num1
    else:
        return num2
    
    # განსაზღვრეთ ორი რიცხვი
number1 = 7
number2 = 12

# გამოძახეთ ფუნქცია და მიიღეთ მაქსიმალური რიცხვი
max_number = find_max(number1, number2)
print(f"მაქსიმალური რიცხვი არის: {max_number}")

def check_even_or_odd(number):
    if number % 2 == 0:
        return "ლუწი"
    else:
        return "კენტი"
    # განსაზღვრეთ რიცხვი
num = 7

# გამოძახეთ ფუნქცია და მიიღეთ ინფორმაცია რიცხვის ტიპზე
result = check_even_or_odd(num)
print(f"რიცხვი {num} არის: {result}")