# AI Context

Version: 1.0

---

# Purpose

This document is the onboarding guide for any AI assistant contributing to Project Veritas.

Read this document before proposing architecture, writing code, or modifying existing functionality.

The goal is to ensure all AI systems contribute consistently, regardless of model or vendor.

---

# Required Reading Order

Before making any changes, read these documents in order:

1. README.md
2. PROJECT_INDEX.md
3. PROJECT_STATE.md
4. PROJECT_IDENTITY.md
5. docs/PROJECT_CONSTITUTION.md
6. docs/ARCHITECTURE.md
7. docs/adr/
8. ENGINEERING_PRINCIPLES.md
9. IMPLEMENTATION_HISTORY.md
10. ROADMAP.md

Never skip the Constitution or Architecture documents.

---

# Project Vision

Veritas is an Evidence Intelligence Platform.

Its purpose is to explain:

- what evidence exists
- how strong the evidence is
- why conclusions are reached

AI assists the process.

Evidence remains authoritative.

---

# Core Philosophy

AI is never the authority.

Evidence is.

Every conclusion should be:

- explainable
- reproducible
- traceable
- transparent

---

# Engineering Philosophy

Architecture is designed by humans.

AI implements approved designs.

AI should not invent architecture.

When uncertain, preserve existing architecture.

---

# Development Workflow

Every milestone follows this process:

1. Architecture design
2. Implementation
3. Unit tests
4. Documentation
5. Architecture review
6. Git commit

Never skip tests.

Never skip documentation.

---

# Coding Principles

Prefer:

- interfaces
- dependency injection
- composition
- deterministic behavior
- modularity

Avoid:

- hidden globals
- tight coupling
- duplicated logic
- provider-specific code inside engines

---

# Layer Responsibilities

Search Engine

Responsible for:

- coordinating providers
- merging results
- deduplication

Not responsible for:

- networking
- parsing
- provider-specific behavior

---

Providers

Responsible for:

- retrieval
- parsing
- mapping

Not responsible for:

- evidence evaluation
- consensus
- verification

---

Evidence Builder

Responsible for converting observations into structured evidence.

---

Consensus Engine

Responsible for evaluating evidence.

Not responsible for determining user-facing verdicts.

---

Verification Engine

Responsible for translating consensus into user-facing verification results.

Not responsible for evidence assessment.

---

# Documentation Rules

Every architectural decision should be documented.

Major decisions belong in ADRs.

Project status belongs in PROJECT_STATE.md.

Long-term philosophy belongs in the Constitution.

---

# Code Review Checklist

Before considering any implementation complete, verify:

- Tests pass
- Documentation updated
- Public interfaces remain stable
- No hidden coupling introduced
- Dependency injection preserved
- Deterministic behavior maintained

---

# Long-Term Goal

The repository—not the conversation—is the source of truth.

Any AI assistant should be able to contribute successfully after reading the Project Book.

No implementation should depend on prior chat history.