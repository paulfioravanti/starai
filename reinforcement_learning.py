# This script created as part of the application process for
# the Star AI course.
# python 3.7.0
message = (
    "How many times do you want to display the message "
    "\"Reinforcement Learning\" on screen? "
    )
user_input = input(message)
try:
    times = int(user_input)
    for _ in range(times):
        print("Reinforcement Learning")
except ValueError:
    print(f"You inputted \"{user_input}\", but you need to provide an integer.")
