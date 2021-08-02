n_one = int(input("Give me a number."))
n_two = int(input("Give me a different number."))
n_three = int(input("Give me a different number."))

def sum (n_one, n_two, n_three):
    answer = n_one + n_two + n_three
    print ("The sum of your three numbers is " + str(answer) + ".")
sum(n_one, n_two, n_three)

def average (n_one, n_two, n_three):
    average_answer=((n_one + n_two + n_three) /3)
    print ("The average of your three numbers is " + str(average_answer) + ".")
    
average (n_one, n_two, n_three)

#Basic
n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))
n3 = int(input("Enter a third number: "))
def sum(x,y,z):
    sum = x + y + z
    return sum

def avg(x,y,z):
    avg = sum(x,y,z)/3
    return avg

print("Your original numbers were " + str(n1) + ", " + str(n2) + ", and " + str(n3) + ". The sum of your numbers was " + str(sum(n1,n2,n3)) + " and the average was " + str(avg(n1,n2,n3)) + ".")


# Version 2: Advanced

num = int(input("Enter how many numbers you have: "))
numbers = []

for i in range(num):
    x = int(input("Enter your number: "))
    numbers.append(x)

def sum(lst):
    sum = 0
    for i in range(len(lst)):
        sum += numbers[i]
    return sum

def avg (lst):
    average = sum(lst) / len(lst)
    return average

print("You entered the list " + str(numbers) + ". The sum of your numbers is " + str(sum(numbers)) + " and the average is " + str(avg(numbers)) + ".") 
    

