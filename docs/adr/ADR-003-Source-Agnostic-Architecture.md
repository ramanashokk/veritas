# ADR-003: Source-Agnostic Architecture

- Status: Accepted
- Date: 2026-07-19

## Context

Veritas must work with many kinds of evidence providers. These may include PubMed, OpenAlex, Crossref, Europe PMC, user-uploaded PDFs, or enterprise repositories. Each source exposes information differently, but the platform must treat them as interchangeable providers of documents and evidence.

If downstream processing depends on a specific source implementation, the system becomes brittle. Adding a new provider would force changes in the evidence pipeline and weaken the integrity of the platform.

## Decision

All external providers will be abstracted behind a Source Registry. The registry is the canonical catalog of known sources, while adapters remain responsible only for translating provider-specific data into the platform’s shared document model.

This means that PubMed, OpenAlex, Crossref, Europe PMC, user PDFs, and enterprise repositories are all treated as interchangeable sources of documents. Downstream evidence processing should work with the same domain concepts regardless of which provider supplied the material.

## Consequences

This decision keeps the evidence pipeline stable and source-independent. It allows the platform to add or retire providers without rewriting the logic that turns documents into observations and evidence links. It also makes testing easier because source-specific behavior can be isolated from core reasoning.

The tradeoff is that a shared abstraction layer must be maintained. That cost is justified because it protects the platform from integrating too tightly with any one provider.
