# Engineering Principles

Version: 1.0

---

# Purpose

This document defines the engineering principles that govern Project Veritas.

Architecture decisions should follow these principles before considering implementation convenience.

These principles are expected to evolve slowly.

Implementations may evolve rapidly.

---

# Principle 1

Architecture is a Product.

Architecture is not temporary.

Architecture is part of the value delivered by Veritas.

Every major architectural decision should improve:

- clarity
- maintainability
- extensibility
- explainability

---

# Principle 2

Interfaces are Long-Lived.

Implementations are Replaceable.

Every subsystem should communicate through stable interfaces.

Changing implementations should not require changing public interfaces.

Examples:

SearchProvider

ConsensusStrategy

VerificationRule

---

# Principle 3

Engines Orchestrate.

Strategies Decide.

Engines coordinate workflows.

Strategies contain business logic.

Never place decision-making logic directly inside an engine.

Good:

SearchEngine

ConsensusEngine

VerificationEngine

Bad:

Large conditional blocks inside engines.

---

# Principle 4

Dependency Injection by Default.

Subsystems receive dependencies.

They do not create them internally.

Avoid hidden dependencies.

Avoid global state.

---

# Principle 5

Composition over Inheritance.

Prefer assembling small components over extending deep inheritance trees.

Small focused objects are easier to replace.

---

# Principle 6

Deterministic Core.

Whenever deterministic algorithms solve a problem, they are preferred.

AI belongs at the edges of the system—not at its core.

Core reasoning should remain reproducible.

---

# Principle 7

Evidence Before AI.

Evidence is authoritative.

AI assists with:

- retrieval
- extraction
- summarization
- explanation

AI must not silently invent evidence.

---

# Principle 8

Explainability is Mandatory.

Every important decision should be explainable.

Users should understand:

- what happened
- why it happened
- where the conclusion came from

---

# Principle 9

Tests are Architecture.

Tests protect architecture.

Every milestone should include:

- unit tests
- boundary tests
- failure tests

A feature is not complete until its tests pass.

---

# Principle 10

Documentation is Part of the Product.

Documentation should evolve alongside code.

Architecture without documentation eventually disappears.

---

# Principle 11

Single Responsibility.

Each module should have one reason to change.

Examples:

Client

↓

Parser

↓

Mapper

↓

Provider

Each layer has one responsibility.

---

# Principle 12

Provider Isolation.

SearchEngine must never contain provider-specific logic.

Provider implementations must remain isolated.

Adding a provider should never require changing SearchEngine.

---

# Principle 13

Business Logic Lives in Domain Layers.

Networking belongs in providers.

Evidence evaluation belongs in Evidence Builder.

Consensus belongs in Consensus Engine.

Verification belongs in Verification Engine.

Never mix responsibilities.

---

# Principle 14

Fail Gracefully.

Failures should remain isolated.

One provider failing should not prevent the entire system from functioning.

Errors should be meaningful.

---

# Principle 15

Optimize for Evolution.

Write software that welcomes future changes.

Adding new providers, algorithms or interfaces should require extension—not modification.

---

# Engineering Checklist

Before every commit verify:

✓ Tests pass

✓ Documentation updated

✓ Public interfaces remain stable

✓ Responsibilities remain separated

✓ No unnecessary coupling introduced

✓ Architecture preserved

✓ Dependency injection maintained

✓ Replaceability maintained

---

# Final Rule

When two implementations are technically correct,

choose the one that makes the architecture simpler.

Long-term simplicity always wins over short-term convenience.