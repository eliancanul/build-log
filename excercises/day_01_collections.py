

    
attempts = [
    {
        "concept": "functions",
        "correct": True,
        "assistance": 0,
    },
    {
        "concept": "testing",
        "correct": False,
        "assistance": 1,
    },
]

def count_correct_attempts(attempts):
    counter = 0
    for attempt in attempts:
        if attempt["correct"] == True: 
            counter += 1
    return counter


def concepts_attempted(attempts):
    concepts = set()
    for attempt in attempts:
        concepts.add(attempt["concept"])
    return concepts 

def independent_attempts(attempts):
    independent = []
    for attempt in attempts:
        if attempt["assistance"] == 0: 
            independent.append(attempt)
    return independent 
