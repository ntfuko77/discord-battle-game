import random

def generate_character(name:str):
    """Generate a character with random attributes and skills."""
    seed = sum([ord(char) for char in name])
    random.seed(seed)  # Set the seed for reproducibility
    attributes = {
        "mhp": random.randint(1, 10),
        "agility": random.randint(1, 10),
        "attack": random.randint(1, 10),
        "defense": random.randint(1, 10),
        "speed": random.randint(1, 10),
    }
    character = {
        "name": name,
        "attributes": attributes,
    }
    random.seed()  # Reset the seed for future random operations
    return character