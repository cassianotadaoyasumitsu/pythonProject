from helper import validation_type, user_input_message
# from helper import * 'will import all'

# comments
user_input = ""
while user_input != "exit":
    user_input = input(user_input_message)
    days_and_unity = user_input.split(":")
    days_and_unity_dict = {"days": days_and_unity[0], "unity": days_and_unity[1]}
    validation_type(days_and_unity_dict)


