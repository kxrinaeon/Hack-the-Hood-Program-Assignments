# Ticket 1
ages = [17, 11, 25, 13, 9]

for item in ages:
    if item >= 13:
        print(f"Age {item}: Access Granted.")
    else:
        print(f"Age {item}: Too young")
# PREDICT: 17, 25, 13: access granted, 11, 9: access denied
# EXPLAIN: Age holds each individual age that is trying to sign up

# Ticket 2
keep_checking = "yes"

while keep_checking == "yes":
    age = int(input("Enter an age to check: "))

    if age >= 13:
        print("Access Granted.")
    else:
        print("Too young")

    keep_checking = input("Do you want to check another age? (yes/no) ")
# PREDICT: it'll run at least once because of the control variable
# EXPLAIN: A while loop is the best option because it can be stopped based on input while a for loop takes a an already set amount of items without the extra input.

# Ticket 3
while True:
    age = input("Enter an age or stop: ")

    if age == "stop":
        print("Exiting the age checker, goodbye!")
        break

    age = int(age)

    if age >= 13:
        print("Access Granted.")
    else:
        print("Too young")
# PREDICT: if i forgot the break, i think it would loop infinitely
# EXPLAIN: The difference in ticket 2's loop and this one is that we are utilizing strings and integers instead of just integers.

# Ticket 4
def can_access(age):
    return age >= 13

for age in ages:
    if can_access(age):
        print(f"Age {age}: Access Granted.")
    else:
        print(f"Age {age}: Too young")
# PREDICT: The difference is that it's reuseable and a lot easier to fix code if there's something wrong with it.
# EXPLAIN: Putting the check inside a function is better than writing the if/else directly in every loop because as I mentioned before, it's easier to check the code and troubleshoot.

# Ticket 5
def signup_report(ages_list):
    approved = 0
    total = len(ages_list)
    
    for index, age in enumerate(ages_list, start=1):
        if can_access(age):
            status = "Access Granted."
            approved += 1
        else:
            status = "Too Young"
            
        print(f"Signup #{index} (Age {age}): {status}")
        
    print(f"Report Summary: {approved} out of {total} people were approved.")

signups = [22, 10, 15, 8, 19, 13]
print(" - - - StreamPass Signup Report - - - ")
signup_report(signups)
# PREDICT: I expect for 4/6 people to be approved, only ones not approved would be 10 and 8.
# EXPLAIN: I used: functions, parameters, lists, integers, for loops, loop configuration, conditionals, booleans, operators, f-strings, and len.