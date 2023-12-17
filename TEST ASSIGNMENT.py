# Question no:1 
import random
num = random.randint(1, 100)
guesses=0
while guesses < 5:
    guess = int(input("guess the number between 1 and 100:"))
    guesses += 1
    if guess < num:
        print("too low.")
    elif guess > num:
        print("too high")
    else:
        print("congratulations! You guessed the number in", guesses, "guesses!")
        break
    if guesses == 5:
        print("Game over! you ran out of guesses.")


# Question No.2
num1=int(input("enter a number:"))
num2=int(input("Enter a number:"))
if num1 %2 ==1 and num2 %2==1:
    result=(num1*num1)+(num2*num2)
    print(result)
else:
    print("calculation is not performed")



#Question no.3
#Factorial
i=int(input("enter a number"))
fac=1
while i>0:
    fac=fac*i
    i=i-1
    print("the factorial of",fac)



#Question no.4
#Resturant bill Calculator
number_of_people=int(input("Enter a number:"))
Cost_of_each_meat=float(input("Enter a Number:"))
Sales_tax_persentage=10
Tip_persentage=5
Total_cost_of_food=(Cost_of_each_meat+Sales_tax_persentage+Tip_persentage)
print(Total_cost_of_food)
Total_Sales_tax=(Total_cost_of_food % Sales_tax_persentage)
print(Total_Sales_tax)
Total_tip_amount=(Total_cost_of_food % Tip_persentage)
print(Total_tip_amount)
Total_bill_amount_per_person=(Total_cost_of_food % number_of_people)
print(Total_bill_amount_per_person)