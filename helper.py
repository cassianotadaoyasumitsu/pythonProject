import logging


def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} {conversion_unit}"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} {conversion_unit}"
    else:
        return "Unsupported unity"


def validation_type(days_and_unity_dict):
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
        logging.error("Log Error")
        print("Don't ruin my program!")


user_input_message = "Enter values of days:unit type:\n"
