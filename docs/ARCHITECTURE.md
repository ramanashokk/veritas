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

### Source Registry

Veritas also includes an in-memory Source Registry under the app sources package. This layer is the canonical catalog of evidence sources the platform knows about.

Responsibilities of the registry:

- register sources
- retrieve source metadata by identifier
- list all available sources
- enable or disable sources
- look up a source by id

The registry is intentionally simple and replaceable. It stores metadata only, without fetching data, making API calls, or touching a database. Future adapters can plug into this catalog once they are implemented.

### Evidence Builder

The Evidence Builder is the first deterministic transformation step in the evidence pipeline. It takes a claim and a set of observations and turns them into evidence links.

The flow is:

```
Document
  ↓
Observation
  ↓
EvidenceBuilder
  ↓
EvidenceLink
  ↓
EvidenceSummary
```

Responsibilities of the builder:

- accept a claim and a list of observations
- evaluate each observation against the claim
- produce evidence links for later use by the verification engine
- derive a provisional evidence summary for the claim

The builder does not use AI, external APIs, or databases. It works entirely with in-memory demo data and keeps the evaluator replaceable so future strategies can be introduced without changing the surrounding architecture.

### Consensus Engine

The Consensus Engine is the next stage in the pipeline. It accepts an EvidenceSummary and produces a deterministic ConsensusResult that describes the current strength of the evidence for a claim.

The flow is:

```
EvidenceSummary
  ↓
Consensus Engine
  ↓
ConsensusResult
```

The engine is intentionally modular. The public interface remains stable while the underlying strategy can change over time. Version 1 uses a simple rule-based approach with no weighting beyond support and contradict counts. Future versions can incorporate evidence quality, source reliability, recency, and reproducibility without changing the public interface.

### Verification Engine

The Verification Engine translates the consensus output into a user-facing verdict. It takes a ConsensusResult and produces a VerificationResult that is easier to present to an end user.

The flow is:

```
EvidenceSummary
  ↓
Consensus Engine
  ↓
ConsensusResult
  ↓
Verification Engine
  ↓
VerificationResult
```

Consensus estimates what the evidence collectively indicates. Verification translates that consensus into a user-facing verdict. Future versions may incorporate jurisdiction-specific policies, domain-specific thresholds, regulatory verification rules, and configurable confidence thresholds without changing the engine interface.

### Search Engine

The Search Engine provides the first source-agnostic retrieval step in the evidence pipeline. A user query is passed into the engine, which distributes it to one or more search providers and merges their normalized results.

The flow is:

```
User Query
  ↓
Search Engine
  ↓
Search Providers
  ↓
Normalized Search Results
  ↓
Evidence Builder
```

The Search Engine never needs to know provider-specific implementation details. That separation allows PubMed, OpenAlex, Crossref, Europe PMC, user PDFs, and other future providers to be plugged in behind the same interface without changing the core architecture.

### Provider SDK

The provider SDK defines a reusable structure for implementing research-source integrations. Each provider is split into a small set of responsibilities so that networking, parsing, and mapping remain isolated.

The flow is:

```
Search Engine
  ↓
Provider
  ↓
Client
  ↓
Parser
  ↓
Mapper
  ↓
SearchResult
```

Responsibilities are intentionally narrow:

- The Search Engine remains provider-agnostic and only knows the shared interface.
- The Provider coordinates the flow and returns normalized results.
- The Client handles HTTP communication, timeouts, retries, and response retrieval.
- The Parser converts raw provider payloads into intermediate Python objects.
- The Mapper converts those objects into SearchResult instances.

This separation keeps provider implementations isolated and makes it straightforward to add new providers such as OpenAlex, Crossref, Europe PMC, or Semantic Scholar without changing the engine contract.

### Design Notes

Version 1 intentionally simplifies the verification process. It assumes that consensus confidence and a fixed threshold are sufficient for a first-pass verdict. It does not yet model evidence quality, source reliability, or domain-specific policy nuance. The main extension points for Version 2 are configurable thresholds, policy-driven rules, and richer evidence metadata.

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
