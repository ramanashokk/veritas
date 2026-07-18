# Project Veritas

Last Updated: 2026-07-19

---

# Current Status

Phase: Core Platform

Status: Active Development

Current Version: v0.1.0

Current Milestone:

IMP-009 (In Progress)

---

# Mission

Build the world's most trusted Evidence Intelligence Platform.

AI assists.

Evidence decides.

---

# Current Architecture

User

↓

Search Engine

↓

Providers

↓

Evidence Builder

↓

Consensus Engine

↓

Verification Engine

↓

REST API (Planned)

↓

Frontend (Planned)

---

# Completed Milestones

✅ IMP-001 Backend Scaffold

✅ IMP-002 Domain Models

✅ IMP-003 Source Registry

✅ IMP-004 Evidence Builder

✅ IMP-005 Consensus Engine

✅ IMP-006 Verification Engine

✅ IMP-007 Search Engine

✅ IMP-008 Provider SDK + PubMed Provider

---

# In Progress

None

---

# Next Milestone

IMP-009

REST API (Minimal)

Goal:

Expose the first public endpoint that allows users to submit a scientific claim and receive a structured verification result.

---

# Long-Term Roadmap

Phase 1

Core Platform

Phase 2

User Experience

Phase 3

Advanced Evidence Assessment

Phase 4

AI Assistance

Phase 5

Scale & Optimization

---

# Architecture Principles

Evidence First

Deterministic Core

Source Agnostic

AI Optional

Dependency Injection

Replaceable Components

Explainability

Traceability

---

# Technical Debt

Known limitations:

• PubMed is the only provider.

• Evidence weighting is intentionally simple.

• Consensus uses Version 1 scoring.

• Verification uses Version 1 thresholds.

• No REST API.

• No frontend.

• No caching.

• No authentication.

---

# Design Philosophy

Business logic belongs in strategies.

Engines orchestrate.

Providers retrieve data.

AI augments.

Evidence remains authoritative.

---

# Repository Structure

backend/

docs/

tests/

providers/

search/

evidence/

consensus/

verification/

---

# Immediate Goal

Deliver the first end-to-end vertical slice:

Browser

↓

REST API

↓

Search

↓

Evidence

↓

Consensus

↓

Verification

↓

JSON Response