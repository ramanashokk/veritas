# Project Roadmap

Version: 1.0

Last Updated: 2026-07-19

---

# Purpose

This document defines the long-term development roadmap for Project Veritas.

It tracks major milestones and strategic priorities.

It intentionally avoids implementation details.

Implementation details belong in Architecture documents and ADRs.

---

# Guiding Principle

Build vertical slices.

Deliver usable functionality early.

Architecture must remain stable while implementations evolve.

---

# Current Status

Current Phase:

Core Platform

Latest Completed Milestone:

IMP-008 — Provider SDK & PubMed Provider

Current Version:

Development (post-v0.1.0)

Latest Git Tag:

v0.1.0

---

# Phase 1 — Core Platform

Status: Complete

## Completed

✅ IMP-001 Backend Scaffold

✅ IMP-002 Domain Models

✅ IMP-003 Source Registry

✅ IMP-004 Evidence Builder

✅ IMP-005 Consensus Engine

✅ IMP-006 Verification Engine

✅ IMP-007 Research Search Engine

✅ IMP-008 Provider SDK + PubMed Provider

Goal:

Build a deterministic, modular evidence evaluation platform.

---

# Phase 2 — First Working Product

Status: Next

## Planned

⬜ IMP-009 REST API

Expose Veritas through a public HTTP interface.

---

⬜ IMP-010 Minimal Web Interface

Allow users to submit a claim and receive evidence-backed verification.

---

Goal:

Deliver the first complete end-to-end user experience.

---

# Phase 3 — Research Expansion

Planned

⬜ OpenAlex Provider

⬜ Crossref Provider

⬜ Europe PMC Provider

⬜ Semantic Scholar Provider

Goal:

Increase evidence coverage while preserving provider independence.

---

# Phase 4 — Advanced Evidence Assessment

Planned

⬜ Evidence Weighting Framework

⬜ Reproducibility Assessment

⬜ Recency Assessment

⬜ Quality Assessment

⬜ Source Reliability Assessment

Goal:

Replace Version 1 consensus with a richer evidence methodology.

---

# Phase 5 — AI Assistance

Planned

⬜ Claim Extraction

⬜ Passage Extraction

⬜ AI Summarization

⬜ AI Explanation

Goal:

Use AI only where deterministic methods are insufficient.

AI remains an assistant—not the authority.

---

# Phase 6 — Platform

Planned

⬜ Authentication

⬜ Caching

⬜ Observability

⬜ Deployment

⬜ Monitoring

⬜ Performance Optimization

Goal:

Prepare Veritas for production usage.

---

# Success Criteria

Veritas should:

• Retrieve evidence

• Explain methodology

• Preserve provenance

• Handle conflicting evidence

• Produce reproducible conclusions

• Remain independent of any AI model

---

# Roadmap Rules

New milestones should:

- preserve architecture
- include tests
- include documentation
- avoid unnecessary coupling
- improve long-term maintainability

---

# Long-Term Vision

Veritas becomes the infrastructure layer for evidence-backed decision making.

Applications should be able to build on top of Veritas without depending on a specific AI model.