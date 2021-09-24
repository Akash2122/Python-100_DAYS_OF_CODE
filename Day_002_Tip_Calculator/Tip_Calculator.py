import os
def ask_and_check_numeric(question):
        try:
            x = float(input(question))
            return x
        except ValueError:
            print("Please gives the input only in numbers!")
            ask_and_check_numeric(question)

def tip_calculator():
    print("Welcome to the tip Calculator.")

    question1 = "What is the total bill? "
    total_bill = ask_and_check_numeric(question1)

    question2 = "How many people to split the bill?"
    members = ask_and_check_numeric(question2)

    question3 = "What percentage tip would you like to give? 10% \or 12% \or 15% "
    percentage = ask_and_check_numeric(question3)

    each_pay = (total_bill + (total_bill*(percentage/100)))/members
    print(f"Each person should pay : {each_pay}")

tip_calculator()


