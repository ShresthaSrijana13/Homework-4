# Srijana Shrestha
# 1918305

def get_age():
    age = int(input())

    # TODO: Raise exception for invalid ages
    if 18 <= age <= 75:
        return age
    else:
        raise ValueError("Invalid age.")


# TODO: Complete fat_burning_heart_rate() function

def fat_burning_heart_rate(age):

    return 0.7 * (220 - age)
    return heart_rate


if __name__ == "__main__":

    try:
        # TODO: Modify to call get_age() and fat_burning_heart_rate()
        #       and handle the exception

        age = get_age()
        fatBurningHeartRate = fat_burning_heart_rate(age)
        print("Fat burning heart rate for a", age, "year-old:", fatBurningHeartRate, "bpm")

    except ValueError as error:

        print(error.args[0])
        print("Could not calculate heart rate info.")
        print()



