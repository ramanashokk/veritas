# ADR-002: Layered Verification Pipeline

- Status: Accepted
- Date: 2026-07-19

## Context

Verification is a complex activity that involves many distinct concerns: identifying a claim, gathering candidate evidence, turning raw material into observations, assembling evidence relationships, and producing a final judgment. If these responsibilities are mixed together, the system becomes difficult to reason about and harder to evolve.

A platform like Veritas needs a structure that supports careful evaluation, replacement of individual components, and strong testing at each stage.

## Decision

Veritas will use a layered verification pipeline with a single responsibility at each stage:

Claim → Search → Documents → Observations → Evidence Builder → Evidence Summary → Consensus → Verification → Explanation

Each layer is responsible for one part of the reasoning chain. The claim layer defines what is being evaluated. The search and document layers identify candidate material. The observation layer captures neutral facts. The evidence builder creates evidence relationships. The summary and consensus layers synthesize the evidence. Verification and explanation interpret the final outcome.

This structure makes it possible to replace any layer independently. A new search strategy, a new extraction method, or a new consensus approach can be introduced without forcing changes across the entire system.

## Consequences

This decision improves testing by allowing each layer to be exercised in isolation. It also improves maintainability because changes are localized and easier to understand. Over time, it supports extensibility as new evidence sources, extraction techniques, or evaluation strategies are introduced.

The main tradeoff is that the architecture requires clear interfaces between layers. That discipline is worthwhile because it preserves modularity and reduces coupling.
