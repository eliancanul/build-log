# Day 02 — Python Collections, Testing, and Debugging

> **Date:** August 11, 2026  
> **Earliest verifiable start:** 2:58 pm EST  
> **Documentation close:** 5:44 pm EST  
> **Verified active window:** approximately 2 hours 46 minutes

## Time-recording note

The start time is the creation timestamp of `excercises/audit_attempts.py` (2:58:03 pm EST). The close time is the time this documentation was prepared (5:44 pm EST). These are evidence-based timestamps from the project files and environment, not a manually tracked timer; study or reflection before the first file was created is not included.

---

## Session objective

Practice Python collections by building a small Study-related audit function.

The task was to receive a list of student attempt records and return a summary containing:

- the total number of attempts;
- the number of attempts that passed;
- the unique students who required significant support;
- the unique concepts observed.

This exercise connected basic Python data structures to a real future subsystem of **Study / Hermes Learning Layer**: an evidence audit that can inform a teaching policy.

---

## Final artifact

### Production file

```text
excercises/audit_attempts.py
```

Public function:

```python
audit_attempts(attempts: list[dict]) -> dict
```

### Test file

```text
excercises/audit_attempts_test.py
```

### Verified test result

```text
4 passed in 0.00s
```

Focused verification command:

```bash
cd "/Users/dojo/Desktop/2026 PROGRAMACIÓN/build-log"
.venv/bin/python -m pytest excercises/audit_attempts_test.py -q
```

A Python compilation check also succeeded:

```bash
.venv/bin/python -m py_compile excercises/audit_attempts.py
```

The implementation and tests were committed during the session:

```text
feat: add day 2 python exercises and test
```

---

## Data model

Each learning attempt is represented as a dictionary:

```python
{
    "student": "Elian",
    "concept": "python-collections",
    "passed": True,
    "help_level": 1,
}
```

The function receives a **list of dictionaries** because:

- a **list** preserves every attempt record, including repeated attempts;
- a **dictionary** gives each field a meaningful name;
- a **set** is used when the output must contain unique values.

---

## Final output contract

The function returns one dictionary:

```python
{
    "total_attempts": 3,
    "passed_attempts": 2,
    "students_needing_support": {"Maya", "Elian"},
    "concepts_seen": {"python-collections", "python-functions"},
}
```

| Key | Type | Meaning |
|---|---|---|
| `total_attempts` | `int` | Every record received in the input list. |
| `passed_attempts` | `int` | Records where `passed` is `True`. |
| `students_needing_support` | `set[str]` | Unique students where `help_level >= 3`. |
| `concepts_seen` | `set[str]` | Unique concept values seen in all records. |

The function makes one pass through the input list and does not mutate it.

---

## Behaviors proved by tests

### 1. Normal audit summary

A multi-record input produces the expected counters and unique sets.

### 2. Empty input

An empty list returns:

```python
{
    "total_attempts": 0,
    "passed_attempts": 0,
    "students_needing_support": set(),
    "concepts_seen": set(),
}
```

This proves that counters and sets are initialized correctly before the loop.

### 3. Boundary rule: `help_level == 3`

The support rule uses:

```python
attempt["help_level"] >= 3
```

A student who receives exactly level `3` support must be included. This test distinguishes `>= 3` from `> 3`.

### 4. Repeated concept values

Several attempts can contain the same concept. The output set must contain that concept only once.

This proves the purpose of:

```python
concepts_seen.add(attempt["concept"])
```

A set removes duplicates automatically; a list would preserve them.

---

## Debugging timeline and lessons

### Import error: project location matters

Initial error:

```text
ModuleNotFoundError: No module named 'excercises'
```

Cause: pytest was started from `/Users/dojo`, while the project package existed inside the `build-log` folder.

Resolution: run pytest from the repository root so Python can resolve:

```python
from excercises.audit_attempts import audit_attempts
```

Lesson:

> Python imports depend on the interpreter's import path, which normally includes the current project directory.

### Pytest fixture error

Initial test shape:

```python
def test_audit_attempts(attempts):
```

Pytest treated `attempts` as a fixture and raised:

```text
fixture 'attempts' not found
```

Resolution: remove the parameter from the test function and define the test data inside the test or at module level.

Lesson:

> Parameters in pytest test functions request fixtures. Normal input data must not accidentally be written as a test parameter.

### Calling a function versus referring to it

An early test used the function name without calling it.

```python
result = audit_attempts
```

A function must be called with parentheses and input data:

```python
result = audit_attempts(attempts)
```

Lesson:

> A function name is a reference to a function object. Parentheses execute the function and produce its return value.

### Output-shape contract

An early version returned a list containing one dictionary. Its matching test also expected a list, so the test passed.

The required contract, however, was one dictionary directly.

Lesson:

> A passing test proves the code matches the assertion. It does not prove the assertion matches the requested behavior. Check value, type, and structure.

---

## Performance review

### Strengths demonstrated

- **Persistence through initial frustration:** the session began with difficulty reading conditions and combining several collection operations, but the work continued through multiple revisions rather than stopping at the first error.
- **Conceptual recovery:** counters, conditions, function calls, and `.add()` were initially rusty but became understandable after practical repetition.
- **Incremental debugging:** import errors, pytest fixtures, function invocation, output shape, thresholds, and duplicate behavior were handled one at a time.
- **Test-driven reasoning:** the final artifact tests normal behavior, empty input, an exact threshold, and duplicate elimination.
- **Growing data-shape awareness:** the difference between a dictionary and a list containing a dictionary became a concrete debugging lesson.
- **Good help calibration:** when a test felt confusing, reducing it from multiple students to one focused behavior made the condition understandable.

### Growth areas

- Build descriptive variable names from the start rather than temporary letters.
- Keep test indentation and code formatting consistent.
- Prefer idiomatic boolean checks:

  ```python
  if attempt["passed"]:
  ```

  instead of:

  ```python
  if attempt["passed"] == True:
  ```

- Before writing a test, state the exact input shape and expected output shape in plain language.
- Continue practicing small conditional exercises. The main gap was not lack of reasoning ability; it was retrieval fluency after time away from Python.

---

## Learning conclusion

The main result of the day was not only a passing test suite. The important shift was moving from initial confusion around conditions and collection operations to being able to explain the logic as a sequence:

```text
iterate over one attempt
→ inspect its fields
→ update the appropriate counter or set
→ return one structured summary
```

The exercise showed that a difficult-looking program becomes manageable when its behaviors are separated, tested, and debugged one at a time.

---

## Next session recommendation

Do one short transfer exercise without copying this implementation:

- use a list of track metadata or student evidence records;
- count one condition;
- collect one unique field in a set;
- write an empty-input test and one boundary test.

The goal is to reinforce the mental pattern, not introduce more tools yet.
