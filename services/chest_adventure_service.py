import random

def roll_d20():
    """Roll d20 dice"""
    return random.randint(1,20)
    
    
def chest_challenge():
    """Verify if it's mimic or chest"""
    result = roll_d20()
    print (f"Dice result: {result}")
    
    if result <=2:
        print ("WARNING! A mimic has appeared!")
        return False
    
    else:
        print("It´s a chest! Try to open it.")
        return True

def try_open_chest():
    """Three chances to open the chest"""
    
    tries = 3
    for chance in range(1, tries + 1):
        print (f"Try: {chance}")
        result = roll_d20()
        print(f"Rolled D20 dice for open the chest: {result}")
        
        if result <= 9:
            print("Fail! You didn´t open the chest")
        else:
            print("Sucess! You opened the chest!")
            print("You obtained a health potion !")
            return True
            """Add function to up health to + 50%"""
    
    print("All chances have been used. The chest is now gone.")
    return False

"""Add function to link to the main app and run the game"""