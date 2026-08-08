def is_even(number):
    return number % 2 == 0

def percentage(part, total): 

    if total == 0: 
        raise ValueError
    else: 
        percentage = (part * 100) / (total)  
        return percentage

def clamp_score(score): 
    if score < 0: 
        return 0 
    if score > 100: 
        return 100
    else: 
        return score


def classify_mastery(scorem):
    scorem = clamp_score(scorem)

    if 0 <= scorem < 40: 
        return "unknown"
    elif 40 <= scorem <= 69: 
        return "developing"
    elif 70 <= scorem <= 89: 
        return "proficient"
    elif 90 <= scorem <= 100: 
        return "advanced"
