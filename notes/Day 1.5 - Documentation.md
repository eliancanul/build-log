# Day 1.5 — Python Functions, Testing, Collections, and GitHub

> This session became the effective first programming day after the roadmap and study plan were updated. The work continued from the initial environment and Git setup documented in `Day 01 - Documentation.md`.

---

## Session Summary

### Main objective

Recover Python fluency through small, testable functions and connect the work to Study's future evidence model.

### Reported duration

Approximately 5 hours total:

- First block: functions, exceptions, and pytest.
- Second block: lists, dictionaries, sets, loops, filtering, and collection tests.
- Final block: documentation, Git commits, GitHub push, and retrospective.

### Verified final state

- 7 Python functions implemented.
- 25 tests executed.
- 25 tests passed.
- 6 files changed and published.
- 2 logical commits created.
- Working tree clean after push.
- GitHub remote: `git@github.com:eliancanul/build-log.git`.

Final test command:

```bash
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q
```

Final result:

```text
25 passed in 0.03s
```

---

# Technical Progress

## Python functions implemented

### `is_even(number)`

Returns whether an integer is even:

```python
return number % 2 == 0
```

Key learning:

- `%` returns the remainder.
- `==` compares values.
- `=` assigns a value.

### `percentage(part, total)`

Calculates a percentage and raises `ValueError` when `total` is zero.

```python
if total == 0:
    raise ValueError
```

Key learning:

- The formula is `(part * 100) / total`.
- `raise ValueError` raises an exception.
- `return ValueError` would only return the exception class as a value; it would not signal an error.

### `clamp_score(score)`

Normalizes scores to the range `0–100`:

- values below `0` become `0`;
- values above `100` become `100`;
- values inside the range remain unchanged.

### `classify_mastery(scorem)`

Uses composition:

```python
scorem = clamp_score(scorem)
```

Then classifies the normalized score:

```text
0–39    → unknown
40–69   → developing
70–89   → proficient
90–100  → advanced
```

Important concept:

> A function that returns a value can be used as the input to another function.

The original attempt called `clamp_score(scorem)` but discarded the returned value. Reassigning it made the composition work.

---

## Python testing with pytest

### `assert`

`assert` checks whether a condition is true:

```python
assert percentage(1, 4) == 25.0
```

If the condition is true, the test passes. If it is false, pytest reports a failure.

### `pytest.raises`

Used when the expected behavior is an exception:

```python
with pytest.raises(ValueError):
    percentage(5, 0)
```

The test passes only if the code inside the block raises `ValueError`.

### Parametrization

`pytest.mark.parametrize` was used to run the same test against multiple input/expected-value pairs.

Example:

```python
@pytest.mark.parametrize("a, expected", [
    (2, True),
    (3, False),
    (0, True),
])
def test_is_even(a, expected):
    assert is_even(a) == expected
```

### Arrange → Act → Assert

The test structure became clearer through this model:

```text
Arrange: prepare the input.
Act: call the function.
Assert: compare the result with the expectation.
```

For example:

```python
def test_count_correct_attempts_empty_list():
    result = count_correct_attempts([])
    assert result == 0
```

No interactive `input()` is necessary. The function argument is the test input.

---

# Collections and Data Structures

## List

A list is an ordered collection:

```python
concepts = ["functions", "testing", "python"]
```

Access uses an index:

```python
concepts[0]
```

Lists preserve order and can contain duplicate values.

## Dictionary

A dictionary stores values under named keys:

```python
attempt = {
    "concept": "functions",
    "correct": True,
    "assistance": 0,
}
```

Access uses a key:

```python
attempt["concept"]
```

## List of dictionaries

Study evidence can be represented as a list of dictionaries:

```python
attempts[0]["concept"]
```

This means:

```text
list → item at index 0 → dictionary → value under "concept"
```

Inside a loop:

```python
for attempt in attempts:
    print(attempt["concept"])
```

The loop variable already refers to the current dictionary, so the list name and index are no longer needed.

Important refinement:

> A loop iterates over each element of a list, not necessarily each number. The element can be an integer, string, dictionary, or another object.

## Set

A set stores unique values:

```python
concepts = set()
concepts.add("functions")
```

Sets are useful when duplicate concepts should be removed.

## List versus set operations

```python
result.append(value)  # add to a list
result.add(value)     # add to a set
```

---

# Collection Functions Implemented

## `count_correct_attempts(attempts)`

Returns an integer count.

```text
list of attempts → integer
```

For an empty list, it returns `0` because the counter starts at zero and the loop runs zero times.

Important syntax lesson:

```python
counter += 1
```

increments the current value.

```python
counter =+ 1
```

assigns positive one and resets the counter to `1`; it does not increment.

## `concepts_attempted(attempts)`

Returns a set of unique concept names.

```text
list of attempt dictionaries → set of strings
```

For an empty list, it returns `set()`.

## `independent_attempts(attempts)`

Returns a list containing complete attempt dictionaries where:

```python
attempt["assistance"] == 0
```

For an empty list, it returns `[]`.

The complete record must be appended:

```python
independent.append(attempt)
```

not only the concept name.

---

# Problems Solved

## Python syntax recovery

Initial problems included:

- missing function parameters;
- missing colons;
- using `=` instead of `==`;
- using an undefined variable name;
- declaring a variable with invalid syntax such as `float percentage = ...`;
- mixing `input()` into functions that should receive parameters.

Resolution:

- parameters became the source of function input;
- functions returned values instead of printing them;
- syntax was checked with `py_compile`;
- behavior was verified with pytest.

## Input versus function arguments

A function test does not need interactive input:

```python
count_correct_attempts(attempts)
```

The `attempts` variable is the input. This is preferable because tests are deterministic and do not wait for a person to type data.

## Expected type mismatch in tests

A major debugging lesson came from `independent_attempts`.

The implementation returned:

```python
[{...}]
```

but the test expected:

```python
{...}
```

The first value is a list containing one dictionary. The second value is a dictionary. They are different types and different structures.

Correct expectation:

```python
assert result == [{
    "concept": "functions",
    "correct": True,
    "assistance": 0,
}]
```

General rule:

> Tests must match the complete return contract: value, type, and structure.

## Test naming and function shadowing

A test initially overwrote the imported production function by using the same function name:

```python
def count_correct_attempts():
```

The test needed the `test_` prefix:

```python
def test_count_correct_attempts():
```

Tests should call the production function, not call themselves.

## Pytest environment issue

The local Python environment used Python 3.9. Pytest attempted to load an external Hermes `anyio` plugin built for Python 3.11, causing an import error.

The project-specific workaround is:

```bash
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q
```

This disables unrelated external pytest plugins and keeps the test run focused on the project.

---

# Learning Behavior Analysis

## Strengths observed

### 1. Fast syntax recovery

The initial syntax was rusty after several years away from Python, but the core mental models returned quickly once the errors were explained.

### 2. Mechanism-oriented questions

The learner consistently asked why a solution worked instead of only accepting a patch.

Examples:

- why `raise` differs from `return`;
- why `+=` differs from `=+`;
- how a function passes a value to another function;
- how a list of dictionaries is traversed;
- why the expected test type must match the returned type.

### 3. Debugging persistence

The learner repeatedly revised the code, ran tests, inspected failures, and continued instead of abandoning the exercise.

### 4. Appropriate use of assistance

Visual Studio Code provided a solution for handling `ValueError`, but the learner paused to understand the pattern afterward. The important requirement was satisfied: the code was explained and understood rather than merely copied.

### 5. Public evidence discipline

The work was documented, tested, committed in logical units, pushed to GitHub, and verified with a clean working tree.

## Weaknesses and growth areas

### 1. Retrieval fluency

Python syntax and collection operations were rusty. The solution is repeated small exercises, not more passive reading.

### 2. Data-shape awareness

The next growth area is reasoning about the exact shape of data:

```text
integer
string
list
set
 dictionary
list of dictionaries
```

Before writing a test, explicitly state the expected type and structure.

### 3. Test design precision

A test can pass while testing the wrong function. Tests must be reviewed for:

- correct imported function;
- correct input;
- correct expected type;
- correct expected structure;
- correct edge case.

### 4. Pace calibration

The first plan underestimated the learner's capacity. The session was expanded from a small function exercise into a longer five-hour block. Future sessions should track elapsed time and continue through additional meaningful blocks instead of closing after one milestone.

---

# Git and GitHub Evidence

## Repository hygiene

Added `.gitignore` rules for:

```text
__pycache__/
*.py[cod]
.pytest_cache/
.venv/
.DS_Store
.obsidian/
```

## Logical commits

```text
47d4f4a feat: add day 1 Python exercises and tests
ce70be0 docs: add day 1.5 study journal
```

## Published files

```text
.gitignore
excercises/day_01_functions_01.py
excercises/test_study_session_01.py
excercises/day_01_collections.py
excercises/day_01_collections_test.py
notes/Day 1.5 - Journal.md
notes/Day 1.5 - Documentation.md
```

The implementation and tests were pushed to `origin/main`.

---

# Current Competency Snapshot

This is a provisional baseline using the roadmap's 0–4 scale.

| Area | Provisional level | Evidence |
|---|---:|---|
| Python syntax and functions | 2 | Implemented and corrected four functions |
| Testing and pytest | 2 | Wrote parametrized tests and used `pytest.raises` |
| Debugging | 2 | Diagnosed syntax, runtime, naming, and type-shape problems with guidance |
| Collections | 1–2 | Rebuilt list, dictionary, set, loop, and filtering concepts |
| Git/GitHub workflow | 2 | Created logical commits, pushed, and verified clean status |
| Technical English | 2 | Wrote a journal and discussed technical concepts in English |

These levels are a starting point, not a final evaluation. The next target is independent implementation and explanation at level 3.

---

# Key Takeaways

1. A function's return type is part of its contract.
2. `return` provides a value; `raise` interrupts execution with an exception.
3. `assert` checks an expected condition.
4. `pytest.raises` checks expected failure behavior.
5. Lists are ordered collections; dictionaries map keys to values; sets contain unique values.
6. A list of dictionaries requires reasoning about both levels of structure.
7. `+=` increments; `=+` assigns positive one.
8. Tests must match the returned type and complete data shape.
9. Empty-input behavior should be intentional and tested.
10. AI assistance is useful when the learner can explain and reproduce the result.

> The most important lesson from this session: working code is only half the job. The expected data shape, tests, documentation, and version history must all agree with the implementation.

---

# Next Session Focus

Continue Day 1 rather than advancing the roadmap prematurely.

Suggested next blocks:

- add tests for more collection edge cases;
- practice dictionaries and nested data structures;
- introduce file handling and JSON persistence;
- use the collection functions on a small evidence-like dataset;
- review Git status, diff, and commit boundaries;
- finish with an English technical explanation.
