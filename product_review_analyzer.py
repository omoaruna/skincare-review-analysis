# Program to review beauty products and conduct analysis
# CORE FUNCTIONS
# Create product review
# Show all product reviews
# Filter through products that have positive and negative ratings
# Filter through products based on keywords like lightweight, greasy, moisturizing etc 

#FUNCTION TO CREATE REVIEWS
def create_review(product_name,brand_name,age_group,rating,review_text=None):
    product_review = {}
    #Product name
    if product_name:
        product_review["product_name"] = product_name.lower()
    else:
        raise Exception("Product name field cannot be empty.")
    
    #Brand name
    if brand_name:
        product_review["brand_name"] = brand_name.lower()
    else:
        raise Exception("Brand name field cannot be empty.")
    
    #Age group logic
    #Create ages dictionary to provide mapping
    age_groups = [(13,18),(19,24),(25,34),(35,44),(45,55),(56,64),(65,)]
    ages = {}
    for index, age_range in enumerate(age_groups,start=1):
        ages[index] = age_groups[index - 1]
    # print(ages) **logging**
    
    # selected_age_group = ages[age_group]
    product_review["age_group"] = (ages[age_group])

    #Rating logic
    if rating:
        product_review["rating"] = int(rating)
    else:
        raise Exception("Rating field must be provided.")
    
    #Review text logic
    if not review_text:
        product_review["review_text"] = None
    else:
        product_review["review_text"] = review_text

    return product_review

#FUNCTION TO SHOW REVIEWS
def show_reviews(all_product_reviews):
    # all_reviews is a list with multiple dictionaries
    if not all_product_reviews:
        print("No reviews made yet")
    else:
        for i in range(len(all_product_reviews)):
            product_review = all_product_reviews[i]
            for field, value in product_review.items():
                print(f"{field.title()}: {value}")
            print()
            
    

   




    
    
    
    



    
