from product_review_analyzer import create_review, show_reviews

#List that stores all reviews
all_product_reviews = []
count = 0 #New variable that tracks how many times a user has made a product review
done_adding_reviews =  False #flag that controls logic flow when prompting the user for
# more product reviews

while True: #Loop goes back here if user decides to review another product

    #Prompt user for product name
    print("Enter the product name: ")
    while True:
        product_name = input(">> ").strip().lower()
        if not product_name:
            print("This is a required field.")
            continue
        else:
            break


    #Prompt user for brand name
    print("Enter the brand name: ")
    while True:
        brand_name = input(">> ").strip().lower()
        if not brand_name:
            print("This is a required field")
            continue
        else:
            break

    #Display age group menu and prompt user for their age group
    #Age group logic
    #Create ages dictionary to map user input (key) to their respective age group(value)
    age_groups = [(13,18),(19,24),(25,34),(35,44),(45,55),(56,64),(65,)]
    ages = {}
    for index, age_range in enumerate(age_groups,start=1):
        ages[index] = age_groups[index - 1]
    # print(ages) logging
    print("Pick your age group: ")
    for option, age_group in ages.items():
        if len(age_group) > 1:
            print(f"{option}: {age_group[0]}-{age_group[1]}")
        else:
            print(f"{option}: {age_group[0]}")

    ## age_group validation logic       
    while True:
        age_group_response = input(">> ")
        try:
            age_group_response = int(age_group_response)
        except (ValueError,TypeError):
            print("Enter a valid option")
            continue
        else:
            if age_group_response < 1 or age_group_response > len(age_groups):
                print(f"Pick an option between 1 and {len(age_groups)}")
                continue
            else:
                selected_age_group = ages[age_group_response]
                break

    #Rating logic
    print("Enter a rating for this product (On a scale of 1 to 5): ")
    while True:
        rating = input(">> ")
        try:
            rating = int(rating)
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
    print("Would you like to review this product (y/n)")
    review_text = ""
    while True:
        review_response = input(">> ").strip().lower()
        if review_response == "y":
            print("Enter your review: ")
            review_text = input(">> ")
            break
        elif review_response == "n":
            review_text = None
            break
        else:
            print("Please enter a valid response")
            print("Would you like to review this product (y/n)")
            continue

    product_review = create_review(product_name,brand_name,age_group_response,
                                   rating,review_text)
    all_product_reviews.append(product_review)

    #Prompt user if they want to make another review
    print("Do you want to add another product review? (y/n)")
    while True:
        more_reviews = input(">> ").strip().lower()
        if more_reviews == "y":
            count += 1
            # add_more_reviews = True
            break
        elif more_reviews == "n":
            done_adding_reviews = True
            break
        else:
            print("Enter a valid response: ")
            continue

    if done_adding_reviews: #this should evaluate to true if user is done
        break

# print(all_product_reviews)
show_reviews(all_product_reviews)


  















