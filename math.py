import random
import time

OPERATORS = ["+", "-", "*"]
min_operand = 3
max_operand = 10
total_problem = 5

def problem():
    left = random.randint(min_operand,max_operand)
    right = random.randint(min_operand,max_operand)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr,answer

wrong = 0

input("press any key to start")
print("-------------")

start_time = time.time()

for i in range(total_problem):
    expr,answer = problem()
    while True:
        guess = input("problem # " + str(i + 1) + " : " + expr + "=")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time)

print("-----------------")
print("nice work")
print(" u finshed in ", total_time, "seconds")


