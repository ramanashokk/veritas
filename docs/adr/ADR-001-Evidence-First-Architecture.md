# ADR-001: Evidence-First Architecture

- Status: Accepted
- Date: 2026-07-19

## Context

Veritas is being built as an evidence infrastructure platform, not as a general-purpose conversational system. The core risk of such a platform is that conclusions may become detached from the underlying facts that support them. In high-stakes domains, this creates a trust problem: users cannot tell whether a conclusion is grounded in evidence or merely generated fluently.

For that reason, the platform must place evidence at the center of its design. The system should be able to explain why a conclusion was reached, which facts were considered, and what remains uncertain.

## Decision

Veritas will be evidence-first rather than AI-first. AI may assist with extraction or analysis, but it is never the authority. Evidence is the source of truth.

Every conclusion must be traceable to underlying observations, documents, and sources. The platform will preserve the distinction between facts, interpretations, and synthesized judgments. This keeps the system aligned with the principle that explanation must be grounded in evidence rather than in the persuasive power of generated language.

## Consequences

This decision makes trust and explainability foundational. It ensures that users can inspect the chain from claim to observation to document to source. It also creates a clear boundary for AI: useful as a tool for processing, but never as a substitute for the evidence itself.

The tradeoff is that the platform must invest in structured evidence handling, provenance, and traceability. However, this creates a more robust foundation for future automation and auditability.

## Alternatives Considered

- AI-first architecture: prioritize fluent generation over evidence traceability.
- Opinion-driven architecture: allow conclusions to be presented as assertions without clear grounding.
- Evidence-only architecture without any assistive automation: more rigid and harder to scale, but conceptually clean.

The chosen approach preserves the strengths of automation without sacrificing verifiability.
