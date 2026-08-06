
## Technical Progress

✅ Development environment checked  
✅ Git configured  
✅ GitHub account connected  
✅ SSH authentication configured  
✅ First repository created and pushed  
✅ Understood local vs remote repositories  
✅ Learned push, pull, remote, upstream concepts  
✅ Learned basic Unix command structure

---

## Problems Solved

### SSH Authentication

**Error:**

```
Permission denied (publickey)
```

**Learned:**  
Authentication is separate from repository configuration.

---

### Missing Remote

**Problem:**

```
git remote -v
```

returned nothing.

**Learned:**  
A local repository does not automatically know where GitHub is.

---

### Repository Not Found

**Problem:**

GitHub could authenticate me but could not find the repository.

**Learned:**  
The remote destination must actually exist.

---

### Missing Upstream

**Problem:**

```
fatal: The current branch main has no upstream branch
```

**Learned:**  
Branches can have relationships with remote branches.

---

# Core Concepts

## Git Mental Model

```
Working files
      ↓
git add
      ↓
Staging area
      ↓
git commit
      ↓
Local history
      ↓
git push
      ↓
Remote repository
```

---

## Unix Philosophy

Main idea:

> Programs should do one thing well and communicate with other programs.

This concept interested me because it shows a different way of designing systems.

---

## Shell Understanding

Learned:

- Commands
- Subcommands
- Flags
- Arguments
- Pipes
- Command substitution

Example:

```
git push -u origin main
```

---

# Learning Behavior Analysis

## Strengths Observed

### 1. Systems thinking

I naturally try to understand relationships between components instead of isolated commands.

Example:

SSH key → ssh-agent → authentication → GitHub

---

### 2. Curiosity-driven learning

I don't only want the solution. I want the mechanism behind the solution.

Example:

Instead of memorizing:

```
eval "$(ssh-agent -s)"
```

I investigated how every piece works.

---

### 3. Creating mental models

I use analogies to understand abstract concepts:

- Remote = destination
- Push = shipping
- Upstream = default shipping route

---

# Weaknesses Observed

## 1. Going too deep too early

Risk:

Spending too much time understanding one detail before building.

Growth strategy:

Learn → Build → Return deeper later.

---

## 2. Low confidence while debugging

Observation:

The reasoning was often correct, but confidence was lower than ability.

Growth strategy:

Create hypotheses before asking for solutions.

---

## 3. Risk of depending too much on AI

Observation:

I recognized that AI can generate things I don't understand.

Growth strategy:

Use AI as a teacher, not as an answer machine.

---

# Final Reflection

Day 1 was about learning that software engineering is not mainly about memorizing commands.

It is about understanding systems, communication between components, and developing the ability to investigate unknown problems.

The biggest lesson:

> A good engineer does not know every answer. A good engineer knows how to find the answer and understand why it works.

---

# Next Day Focus

## Day 2 — Unix Fundamentals

Topics:

- Filesystem structure
- Home directory
- Absolute vs relative paths
- Environment variables
- `$PATH`
- Processes
- Permissions
- Shell behavior