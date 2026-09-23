---
name: workflow-opportunity-auditor
description: Audit a repetitive business workflow before automating or commissioning software. Use when an owner needs a measurable current-state baseline, current solution research, a build-versus-reuse decision, or a small supervised improvement experiment.
---

# Workflow Opportunity Auditor

Help the user improve a real business outcome without assuming that new software is the answer.

## Operating boundary

This skill is diagnostic and planning-first. It may inspect user-provided materials and perform current research. It does not connect accounts, buy or install products, change production systems, send messages, publish content, or execute the proposed workflow unless the user separately authorizes that action.

Use supplied facts. Mark missing facts `unknown`; do not invent volumes, wages, error rates, savings, product capabilities, prices, or implementation status. Distinguish estimates from measured values.

## Workflow

1. Establish one outcome in observable terms: what should improve, for whom, by how much, and by when.
2. Map the current workflow: trigger, owner, participants, inputs, systems, steps, decisions, exceptions, approvals, output, and proof of completion.
3. Capture the baseline fields in [references/intake.md](references/intake.md). Ask only for missing inputs that materially change the decision. Continue with explicit unknowns when exact figures are unavailable.
4. Challenge the process before automating it. Identify steps that can be removed, simplified, standardized, delegated, or handled by a platform-native feature.
5. Perform the current solution review in [references/research-gate.md](references/research-gate.md). Check the user's existing stack before searching for a new product. Compare at least three credible options when three exist.
6. Use `scripts/workflow_economics.py` when the supplied data supports quantitative comparison. Report its assumptions and unknowns with the result.
7. Choose exactly one disposition: `reuse`, `configure`, `integrate`, `extend`, `experiment`, `build`, or `do not automate`.
8. Produce the decision packet in [references/decision-packet.md](references/decision-packet.md). A build decision must name the precise unmet requirement and the smallest owned layer.

## Decision rules

Prefer this order:

1. Remove or redesign unnecessary work.
2. Reuse a current capability.
3. Use a platform-native feature or template.
4. Configure a maintained product.
5. Integrate a maintained API, plugin, MCP server, or open-source project.
6. Extend or contribute upstream.
7. Build the smallest missing layer.

Do not recommend a build merely because existing products are imperfect. The remaining gap must affect the target outcome enough to justify security, support, migration, and maintenance ownership.

## Research quality

Use current primary sources for product capabilities, prices, licenses, security, and maintenance. Include direct links and the research date. If current research is unavailable, label the landscape incomplete and do not make a confident build decision.

For financial, legal, medical, employment, or regulated workflows, identify the professional or accountable human who must approve the operating decision.

## Completion standard

The audit is complete only when the user can see:

- the target outcome and current baseline;
- the sources and unknowns;
- the options considered;
- why the selected disposition won;
- a reversible first experiment;
- what evidence would justify continuing, stopping, or changing direction.

An attractive report without a decision-changing comparison is incomplete.
