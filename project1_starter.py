"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Joshua Evans]
Date: [10/20/2025]

AI Usage: AI gave an example on how to code the "Earthling" character class, which helped code the rest of the classes.

def create_character (name , character_class): #
    if character_class == "Earthling":
        return{"Physical_Damage": 50, "Ki_Damage": 50, "Health": 100, "Speed": 100}
    elif character_class == "Saiyan":
        return{"Physical_Damage": 75, "Ki_Damage": 35, "Health": 80, "Speed": 150 }
    elif character_class == "Namekian":
        return{"Physical_Damage": 65, "Ki_Damage": 45, "Health": 120, "Speed": 80}
    elif character_class == "Frieza":
        return{"Physical_Damage": 45, "Ki_Damage": 55, "Health": 70, "Speed": 200}
    else: return{"Pick a race: Earthling, Saiyan, Namekian, Frieza"}
    def create_character(name, character_class):
        stats = calculate_stats(charcacter_class)
        character = {
        "name": name,
        "class": character_class,
        "level": 1,
        "Physical_Damage": stats[Physical_Damage"],
        "Ki_Damage": stats["Ki_Damage"],
        "Health": stats["Health"],
        "Speed": stats["speed"],
        "zeni": 100
    }
    return character
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
    pass

def calculate_stats(character_class, level): #Calculates stats based on level and class and returns a tuple of all stats 
    if character_class == "Earthling": 
    Physical_Damage = 50 + (level * 3)
    Ki_Damage = 50 + (level * 3)
    Health = 100 + (level * 3)
    Speed = 100 + (level * 3)
    
    elif character_class == "Saiyan":
    Physical_Damage = 75 + (level * 4)
    Ki_Damage = 35 + (level * 2)
    Health = 80 + (level * 2)
    Speed = 150 + (level * 3)

    elif character_class == "Namekian":
    Physical_Damage = 65 + (level * 2)
    Ki_Damage = 45 + (level * 2)
    Health = 125 + (level * 4)
    Speed = 80 + (level * 2)

    elif character_class == "Freiza":
    Physical_Damage = 45 + (level * 2)
    Ki_Damage = 55 + (level * 2)
    Health = 70 + (level * 2)
    Speed = 100 + (level * 4)
    
    else:print("please choose a class: Earthling, Saiyan, Namekian, or Frieza")

    return (Physical_Damage, Ki_Damage, Health, Speed)
    
    
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """
    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)
    pass

def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    # TODO: Implement this function
    # Remember to handle file errors gracefully
    pass

def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    # TODO: Implement this function
    # Remember to handle file not found errors
    pass

def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    # TODO: Implement this function
    pass

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    pass

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
