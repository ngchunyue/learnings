lunch_option = {"japanese": "sushi",
                "chinese": "noodles",
                "thai": "soup"}
inverted_lunch_option = {}

print(lunch_option.items())

# def invert_dict(lunch_option: dict) -> dict:
#     for old_key in lunch_option:
#         old_value = lunch_option[old_key]

#         new_value = old_key
#         new_key = old_value

#         inverted_lunch_option[new_key] = new_value

#     return inverted_lunch_option







# def invert_dict(lunch_option: dict) -> dict:
#     for old_key in lunch_option.keys():
        
#         inverted_lunch_option[lunch_option[old_key]] = old_key
    
#     return inverted_lunch_option




def invert_dict(lunch_option: dict) -> dict:
    inverted_lunch_option = {val: key for (key, val) in lunch_option.items()}


    return inverted_lunch_option





print(invert_dict(lunch_option))