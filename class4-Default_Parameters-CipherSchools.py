# Default Parameters

def user_info(first_name,last_name = 'unknown' ,age = None):    # You have to write default parameters at last inside the function brackets to avoid error
    print(f"Your first name is {first_name}")
    print(f"Your last name is {last_name}")
    print(f"You age is {age}")
    
user_info("Shivam","Singh",19)