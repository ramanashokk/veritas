# Veritas

> **The Evidence Engine**

Veritas is an open platform that helps people understand what the scientific evidence actually says.

Instead of relying on a single study or AI-generated opinion, Veritas retrieves published research, constructs structured evidence, evaluates the collective strength of that evidence, and produces transparent, explainable conclusions.

**AI is not the authority. The evidence is.**

---

# Vision

To become the world's most trusted platform for understanding scientific evidence.

Our long-term goal is to build the infrastructure for evidence-backed decision making that can be used by researchers, clinicians, organizations, and AI systems alike.

---

# Core Principles

- Evidence over opinion
- Transparency by default
- Every conclusion is traceable
- Uncertainty is shown, not hidden
- Science evolves, so Veritas evolves
- Architecture evolves slowly; implementations evolve rapidly

---

# Current Status

🚧 Active Development

Current milestone:

**IMP-009 — REST API**

Completed milestones:

- ✅ Backend Scaffold
- ✅ Domain Model
- ✅ Source Registry
- ✅ Evidence Builder
- ✅ Consensus Engine
- ✅ Verification Engine
- ✅ Search Engine
- ✅ Provider SDK
- ✅ PubMed Provider

---

# Architecture

```
User
  │
  ▼
Search Engine
  │
Providers
  │
Evidence Builder
  │
Consensus Engine
  │
Verification Engine
  │
Structured Result
```

For full details, see:

- docs/ARCHITECTURE.md

---

# Project Book

The Project Book documents the philosophy, architecture, engineering practices, and evolution of Veritas.

Recommended reading order:

1. PROJECT_INDEX.md
2. PROJECT_STATE.md
3. PROJECT_IDENTITY.md
4. PROJECT_ROADMAP.md
5. docs/PROJECT_CONSTITUTION.md
6. docs/ARCHITECTURE.md
7. ENGINEERING_PRINCIPLES.md
8. IMPLEMENTATION_HISTORY.md
9. DECISION_LOG.md
10. AI_CONTEXT.md
11. CONTRIBUTING.md

The repository—not previous conversations—is the source of truth.

---

# Roadmap

### Phase 1 — Core Platform ✅

- Backend
- Domain Model
- Search Engine
- Evidence Builder
- Consensus
- Verification
- Provider SDK
- PubMed

### Phase 2 — Product

- REST API
- Minimal Web UI

### Phase 3 — Research Expansion

- OpenAlex
- Crossref
- Europe PMC
- Semantic Scholar

### Phase 4 — Advanced Evidence Assessment

- Evidence weighting
- Recency assessment
- Quality assessment
- Reproducibility assessment

### Phase 5 — AI Assistance

- Claim extraction
- Passage extraction
- Scientific summarization
- Explainable responses

---

# Repository Structure

```
.
├── backend/
├── frontend/
├── tests/
├── docs/
│   ├── ARCHITECTURE.md
│   ├── PROJECT_CONSTITUTION.md
│   └── adr/
│
├── README.md
├── PROJECT_INDEX.md
├── PROJECT_STATE.md
├── PROJECT_IDENTITY.md
├── PROJECT_ROADMAP.md
├── ENGINEERING_PRINCIPLES.md
├── IMPLEMENTATION_HISTORY.md
├── DECISION_LOG.md
├── AI_CONTEXT.md
└── CONTRIBUTING.md
```

---

# Contributing

Before contributing, please read:

- PROJECT_INDEX.md
- PROJECT_STATE.md
- PROJECT_IDENTITY.md
- docs/PROJECT_CONSTITUTION.md
- docs/ARCHITECTURE.md
- ENGINEERING_PRINCIPLES.md

See **CONTRIBUTING.md** for the complete workflow.

---

# Guiding Principle

> Build trust through evidence, not assertions.

**Veritas — The Evidence Engine**