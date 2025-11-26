def calculate_entropy(password):
    import math
    unique_characters = len(set(password))
    password_length = len(password)
    if password_length == 0:
        return 0
    entropy = password_length * math.log2(unique_characters)
    return entropy

def calculate_character_diversity(password):
    character_types = {
        'lowercase': any(c.islower() for c in password),
        'uppercase': any(c.isupper() for c in password),
        'digits': any(c.isdigit() for c in password),
        'special': any(not c.isalnum() for c in password),
    }
    diversity_score = sum(character_types.values())
    return diversity_score

def calculate_metrics(password):
    return {
        'entropy': calculate_entropy(password),
        'character_diversity': calculate_character_diversity(password),
    }