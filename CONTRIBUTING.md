# Contributing to Project Veritas

Thank you for contributing.

Before writing code, read:

1. PROJECT_INDEX.md
2. PROJECT_STATE.md
3. PROJECT_IDENTITY.md
4. docs/PROJECT_CONSTITUTION.md
5. docs/ARCHITECTURE.md
6. ENGINEERING_PRINCIPLES.md

---

# Development Workflow

Every feature follows the same lifecycle.

Design

↓

Implementation

↓

Tests

↓

Documentation

↓

Architecture Review

↓

Git Commit

---

# Engineering Rules

Always:

- preserve architecture
- write deterministic code where possible
- keep responsibilities separated
- update documentation
- add tests

Never:

- place business logic inside engines
- introduce hidden global state
- tightly couple providers
- bypass interfaces

---

# Coding Standards

Prefer:

- composition
- dependency injection
- interfaces
- immutable data where practical

Avoid:

- deep inheritance
- duplicated logic
- provider-specific code outside providers

---

# Pull Request Checklist

Before submitting:

✓ Tests pass

✓ Documentation updated

✓ Architecture preserved

✓ Public interfaces stable

✓ No unnecessary coupling

✓ Code reviewed

---

# Documentation Requirements

Major architecture decisions:

→ ADR

Project progress:

→ PROJECT_STATE.md

Milestone completion:

→ IMPLEMENTATION_HISTORY.md

Future work:

→ PROJECT_ROADMAP.md

---

# Philosophy

Implementation is temporary.

Architecture is long-term.

Protect the architecture.