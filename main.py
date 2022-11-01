
def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} {conversion_unit}"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} {conversion_unit}"
    else:
        return "Unsupported unity"


def validation_type():
    try:
        # comments
        user_input_num = int(days_and_unity_dict["days"])
        if user_input_num > 0:
            calculate = days_to_units(user_input_num, days_and_unity_dict["unity"])
            print(calculate)
        elif user_input_num == 0:
            print("0 is not a valid input!")
        else:
            print("Negative number not allowed!")
    except ValueError:
        print("Don't ruin my program!")


# comments
user_input = ""
while user_input != "exit":
    user_input = input("Enter values of days:unit type:\n")
    days_and_unity = user_input.split(":")
    print(days_and_unity)
    days_and_unity_dict = {"days": days_and_unity[0], "unity": days_and_unity[1]}
    print(days_and_unity_dict)
    print(type(days_and_unity_dict))
    validation_type()


