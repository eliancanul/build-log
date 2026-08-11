from excercises.audit_attempts import audit_attempts
attempts = [
    {
        "student": "Elian",
        "concept": "python-collections",
        "passed": True,
        "help_level": 1,
    },
    {
        "student": "Maya",
        "concept": "python-collections",
        "passed": False,
        "help_level": 3,
    },
    {
        "student": "Elian",
        "concept": "python-functions",
        "passed": True,
        "help_level": 4,
    },
]

def test_audit_attempts():
    result = audit_attempts(attempts)
    assert result == {
    "total_attempts": 3,
    "passed_attempts": 2,
    "students_needing_support": {"Maya", "Elian"},
    "concepts_seen": {"python-collections", "python-functions"},
    }
def test_empty_audit_attempts():
    result = audit_attempts([])
    assert result == {
    "total_attempts": 0,
    "passed_attempts": 0,
    "students_needing_support": set(),
    "concepts_seen": set(),
    }
def test_help_level_3():
        attempts = [
        {
        "student": "Elian",
        "concept": "python-functions",
        "passed": True,
        "help_level": 3,
        }
    ]
        result = audit_attempts(attempts)
        assert result["students_needing_support"] == {"Elian"}

def test_repeated_concept_is_seen_once():
        attempts = [
    {
        "student": "Elian",
        "concept": "python-collections",
        "passed": True,
        "help_level": 1,
    },
    {
        "student": "Maya",
        "concept": "python-collections",
        "passed": False,
        "help_level": 3,
    },
    {
        "student": "Elian",
        "concept": "python-functions",
        "passed": True,
        "help_level": 4,
    },

     {
            "student": "José",
            "concept": "python-functions",
            "passed": True,
            "help_level": 2,
        },
]
        result = audit_attempts(attempts)
        assert result["concepts_seen"] == {"python-collections", "python-functions"}
