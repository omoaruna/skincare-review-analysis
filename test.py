# age group logic
age_groups = [(13,18),(19,24),(25,34),(35,44),(45,55),(56,64),(65,)]
ages = {}
for index, age_range in enumerate(age_groups,start=1):
    ages[index] = age_groups[index - 1]
print(ages)
print("Pick your age group: ")
for option, age_group in ages.items():
    if len(age_group) > 1:
        print(f"{option}: {age_group[0]}-{age_group[1]}")
    else:
        print(f"{option}: {age_group[0]}")

## age_group validation logic       
while True:
    user_response = input(">> ")
    try:
        user_response = int(user_response)
    except (ValueError,TypeError):
        print("Enter a valid option")
        continue
    else:
        if user_response < 1 or user_response > len(age_groups):
            print(f"Pick an option between 1 and {len(age_groups)}")
            continue
        else:
            selected_age_group = ages[user_response]
            break
#Rating logic
print("Enter a rating for this product (On a scale of 1 to 5): ")
while True:
    rating = input(">> ")
    try:
        rating = float(rating)
    except(ValueError,TypeError):
        print("Enter a valid rating: ")
        continue
    else:
        if rating > 5 or rating < 1:
            print("Enter a rating from 1 to 5: ")
            continue
        else:
            break

#Review text logic
# review_text = None
# if not review_text:
#     print("review text is empty")

#Review text logic
print("Would you like to review this product (y/n)")
while True:
    review_response = input(">> ").strip().lower()
    if review_response == "y":
        review_text = input(">> ")
    elif review_response == "n":
        break
    else:
        print("Please enter a valid response")
        print("Would you like to review this product (y/n)")
        continue

all_reviews = []

    

