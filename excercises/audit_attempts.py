
def audit_attempts(attempts: list[dict]) -> dict: 
    total_attempts, passed_attempts = 0, 0
    students_needing_support, concepts_seen = set(), set()

    for attempt in attempts: 
        
        total_attempts += 1
        if attempt["passed"]: 
            passed_attempts += 1
        if attempt["help_level"] >= 3: 
            students_needing_support.add(attempt["student"])
        if attempt["concept"] != "": 
            concepts_seen.add(attempt["concept"])
    audit = {
    "total_attempts": total_attempts,
    "passed_attempts": passed_attempts,
    "students_needing_support": students_needing_support,
    "concepts_seen": concepts_seen,
    }
    return audit