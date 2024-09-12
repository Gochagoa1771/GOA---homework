def simple_calculator(num1, num2, operation):
    if operation == "დამატება":
        return num1 + num2
    elif operation == "გამოკლება":
        return num1 - num2
    elif operation == "გამრავლება":
        return num1 * num2
    elif operation == "გაყოფა":
        if num2 == 0:
            return "შეცდომა: ნულზე გაყოფა შეუძლებელია"
        else:
            return num1 / num2
    else:
        return "შეცდომა: უცნობი ოპერაცია"

# ფუნქციის გამოცდა სხვადასხვა ოპერაციებით
print(simple_calculator(10, 5, "დამატება"))       # უნდა დაბრუნდეს 15
print(simple_calculator(10, 5, "გამოკლება"))      # უნდა დაბრუნდეს 5
print(simple_calculator(10, 5, "გამრავლება"))     # უნდა დაბრუნდეს 50
print(simple_calculator(10, 5, "გაყოფა"))         # უნდა დაბრუნდეს 2.0
print(simple_calculator(10, 0, "გაყოფა"))         # უნდა დაბრუნდეს "შეცდომა: ნულზე გაყოფა შეუძლებელია"
print(simple_calculator(10, 5, "უცნობი"))          # უნდა დაბრუნდეს "შეცდომა: უცნობი ოპერაცია"