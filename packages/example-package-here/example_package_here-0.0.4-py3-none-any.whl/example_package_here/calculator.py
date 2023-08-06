# logic functions

def add_one(number):
    return number + 1 

# calci 
class Calculator:
    def add_nums(self, num1, num2):
        return num1 + num2 
    
    def divide_nums(self, numerator, denominator):
        if denominator == 0:
            return "Denominator cannot be zero"
        return numerator / denominator

    def multiply_nums(self, num1, num2):
        return num1 * num2 
    
    def subtract_nums(self, num1, num2):
        return num1 - num2 


def add_two(number):
    return number + 2

def add_three(number):
    return number + 3