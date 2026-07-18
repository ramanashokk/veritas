# Veritas Architecture

Veritas is an evidence infrastructure platform.

> AI is not the authority. The evidence is.

This document defines the first-principles domain model and request flow. It establishes the language of Veritas — not its implementation.

---

## Design Principles

- **Evidence before explanation** — conclusions are built from traceable facts, not generated narratives.
- **Every conclusion must be traceable** — users can follow the chain from claim back to source documents.
- **Facts must be separated from interpretations** — observations state what was found; claims and consensus interpret what it means.
- **Uncertainty is information** — inconclusive or conflicting evidence is preserved, not hidden.
- **Consensus is computed, not stored as truth** — scientific understanding evolves; Veritas reflects current evidence, not permanent verdicts.

---

## Core Domain Model

### Source

Represents where information originates.

Examples: PubMed, OpenAlex, ClinicalTrials.gov, USPTO, WHO.

A source is an external system or corpus. It does not contain interpretations — only the origin of raw material.

---

### Document

A paper, patent, trial, guideline, report, or judgment retrieved from a source.

Documents are the primary artifacts of evidence. Every observation must trace back to a document, and every document must trace back to a source.

---

### Observation

A factual observation extracted from a document.

Observations remain **neutral**. They describe what the document states or what was measured — without inference, opinion, or evaluative language.

Examples:
- "The trial reported a 12% reduction in primary endpoint."
- "The abstract states n=1,842 participants."

Observations are **facts**, not conclusions.

---

### Claim

A proposition that can be evaluated using observations.

A claim is what the user (or system) asks Veritas to assess. Claims are evaluable statements — they can be supported, contradicted, or left inconclusive by the evidence.

Examples:
- "Does caffeine improve cognitive performance?"
- "Is metformin effective for type 2 diabetes?"

Claims are **propositions**, not facts.

---

### EvidenceLink

Represents the relationship between an Observation and a Claim.

An evidence link connects a single neutral observation to a single claim and records how that observation bears on the claim.

Allowed relationships:

| Relationship   | Meaning                                              |
|----------------|------------------------------------------------------|
| **SUPPORTS**   | The observation is consistent with the claim         |
| **CONTRADICTS**| The observation conflicts with the claim             |
| **NEUTRAL**    | The observation is relevant but neither supports nor contradicts |

Evidence links are **relationships**, not summaries. They preserve traceability from claim → observation → document → source.

---

### Consensus

Computed from multiple EvidenceLinks.

Consensus synthesizes the pattern of supporting, contradicting, neutral, and inconclusive links for a claim. It is a **derived view** — never stored or presented as fixed truth.

Consensus may change as:
- new documents are indexed,
- new observations are extracted,
- or existing evidence is re-evaluated.

---

## Domain Relationships

```
Source
  └── Document
        └── Observation
              └── EvidenceLink ──→ Claim
                                        └── Consensus (computed)
```

Facts flow upward from sources. Interpretation happens only at the claim and consensus layers.

### First-Principles Domain Model

The backend now includes a small domain layer under the app models package for the core concepts that Veritas reasons about:

- Source captures the origin of information.
- Document captures the artifact retrieved from that source.
- Observation captures neutral factual content extracted from a document.
- Claim captures a proposition that can be evaluated.
- EvidenceLink captures how an observation bears on a claim.
- Consensus captures the aggregate evaluation of a claim from multiple links.

These models are intentionally pure and immutable. They describe what Veritas knows and how it relates, without embedding APIs, persistence, or external integration details.

---

## Request Flow

```
Frontend
  → API
    → Workflow
      → Evidence Engine
        → Sources
```

| Layer            | Responsibility                                              |
|------------------|-------------------------------------------------------------|
| **Frontend**     | Collects user input; displays traceable results             |
| **API**          | HTTP boundary; validates requests and serializes responses  |
| **Workflow**     | Orchestrates a use case (e.g. verify a question)            |
| **Evidence Engine** | Domain model and evidence logic (claims, links, consensus) |
| **Sources**      | Retrieves documents from external systems (PubMed, etc.)    |

The frontend is a client. Business logic lives in the Evidence Engine. Workflows coordinate the engine and sources; the API exposes workflows to clients.

---

## What This Document Does Not Cover

The following are intentionally out of scope for this document:

- Database persistence
- External source integration (PubMed, OpenAlex, etc.)
- AI summarization or extraction
- Confidence scoring algorithms
- Authentication and authorization

Those concerns are implemented in later milestones on top of this domain model.
