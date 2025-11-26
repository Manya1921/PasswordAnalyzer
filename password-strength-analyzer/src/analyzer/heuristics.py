def check_common_patterns(password):
    common_patterns = ['123456', 'password', 'qwerty', 'abc123', 'letmein']
    return password in common_patterns

def check_leetspeak_variations(password):
    leetspeak_dict = {
        'a': '4', 'b': '8', 'e': '3', 'g': '9', 'i': '1', 'o': '0', 's': '5', 't': '7'
    }
    leetspeak_variations = set()
    
    for char, leet_char in leetspeak_dict.items():
        variation = password.replace(char, leet_char)
        leetspeak_variations.add(variation)
    
    return leetspeak_variations

def evaluate_password_strength(password):
    strength = 0
    
    if len(password) >= 8:
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.islower() for char in password):
        strength += 1
    if any(not char.isalnum() for char in password):
        strength += 1
    
    return strength

def analyze_password(password):
    if check_common_patterns(password):
        return "Weak: Common pattern detected."
    
    leetspeak_variations = check_leetspeak_variations(password)
    if password in leetspeak_variations:
        return "Weak: Leetspeak variation detected."
    
    strength_score = evaluate_password_strength(password)
    if strength_score < 3:
        return "Weak: Consider using a stronger password."
    elif strength_score == 3:
        return "Moderate: Your password is decent, but could be improved."
    else:
        return "Strong: Your password is strong."