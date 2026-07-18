# Decision Log

Version: 1.0

---

# Purpose

This document records important architectural decisions.

Unlike ADRs, entries are intentionally brief.

---

## 2026-07-19

Created the Evidence Builder as a dedicated layer between observations and consensus.

Reason:

Separate evidence construction from evidence interpretation.

---

## 2026-07-19

Separated Consensus from Verification.

Reason:

Consensus evaluates evidence.

Verification communicates conclusions.

---

## 2026-07-19

Introduced Strategy pattern for Consensus.

Reason:

Consensus methodology will evolve.

The engine should remain stable.

---

## 2026-07-19

Introduced Rule abstraction for Verification.

Reason:

Verification policies may vary by domain.

---

## 2026-07-19

Search Engine made provider-independent.

Reason:

Support multiple scientific databases without changing the search engine.

---

## 2026-07-19

Created Provider SDK.

Reason:

Networking, parsing and mapping must remain isolated.

---

## 2026-07-19

Adopted deterministic-first architecture.

Reason:

Core reasoning should remain reproducible.

AI is used only where deterministic methods are insufficient.

---

## 2026-07-19

Project Book introduced.

Reason:

The repository—not chat history—should become the permanent memory of Veritas.

---

# Rule

If an architectural decision changes the long-term direction of Veritas:

Create an ADR.

Add a summary here.