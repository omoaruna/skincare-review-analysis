def get_user_skin_type():
    user_input = input("What's your skin type? DRY, OILY, COMBINATION, NORMAL: ").lower().strip()
# dictionary that stores skin types and product recommendations based on them
    types_and_products = {
    "dry":["cream cleanser","hydrating toner","lactic acid","cream moisturizer",
           "sunscreen"],
    "oily" : ["foaming gel cleanser","hydrating toner","salicylic acid","gel moisturizer",
           "sunscreen"],
    "combination" : ["gel cleanser","hydrating toner","mandelic acid","gel moisturizer",
           "sunscreen"],
    "normal" : ["gel cleanser","hydrating toner","mandelic acid","gel moisturizer",
           "sunscreen"],
}
# validation loop
    while True:
        if user_input not in types_and_products:
            print("Please enter a valid skin type")
            print("DRY, OILY, COMBINATION, NORMAL")
            user_input = input().lower().strip()
        else:
            break

    return {user_input : types_and_products[user_input]}



# user_input = input("What's your skin type? DRY, OILY, COMBINATION, NORMAL: ").lower().strip()
user_results = get_user_skin_type()


# types_and_products = {
#     "dry":["cream cleanser","hydrating toner","lactic acid","cream moisturizer",
#            "sunscreen"],
#     "oily" : ["foaming gel cleanser","hydrating toner","salicylic acid","gel moisturizer",
#            "sunscreen"],
#     "combination" : ["gel cleanser","hydrating toner","mandelic acid","gel moisturizer",
#            "sunscreen"],
#     "normal" : ["gel cleanser","hydrating toner","mandelic acid","gel moisturizer",
#            "sunscreen"],
# }

# while True:
#     if user_skin_type not in types_and_products:
#         print("Please enter a valid skin type")
#         print("DRY, OILY, COMBINATION, NORMAL")
#         user_skin_type = input().lower().strip()
#     else:
#         break

for skin_type, product_recs in user_results.items():
    # if user_skin_type == skin_type:
    print(f"PRODUCT RECOMMENDATIONS FOR {skin_type.upper()} SKIN")
    for products in product_recs:
        print(f"- {products.capitalize()}")

