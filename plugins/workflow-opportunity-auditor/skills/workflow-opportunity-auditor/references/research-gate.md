# Build-versus-reuse research gate

Research on the date of the audit because product capabilities, pricing, licenses, and maintenance change.

## Search order

1. Capabilities already present in the user's current systems.
2. Platform-native features, templates, and automations.
3. Maintained commercial products.
4. Maintained APIs, plugins, MCP servers, and open-source projects.
5. Adjacent products that solve the outcome through a different workflow.

Use primary sources for factual claims. Community reports can establish pain or implementation experience but should not replace current product documentation.

## Minimum comparison

Compare at least three credible options when available:

| Field | What to capture |
| --- | --- |
| Outcome fit | Which required outcome and workflow steps it covers |
| Missing requirement | Exact verified gap |
| Price | Current public price or `unknown` |
| License | Proprietary or license identifier |
| Data | What is sent, stored, retained, or used for training |
| Access | Permissions, authentication, and approval model |
| Maintenance | Maintainer, release activity, deprecation state |
| Integration | Supported systems and implementation effort |
| Portability | Export, lock-in, and migration path |
| Operations | Hosting, monitoring, support, and failure recovery |

## Disqualifiers

Reject an option when a verified hard constraint fails. Do not reject it for superficial differences that do not affect the outcome.

## Build threshold

A build recommendation requires all of the following:

- a measurable outcome worth changing;
- a current landscape review;
- an exact unmet requirement after configuration or extension;
- evidence that the gap matters to the outcome;
- a smallest owned layer with a defined boundary;
- a reversible experiment and maintenance owner;
- kill criteria.

If the research is incomplete, choose `experiment` or defer the decision instead of choosing `build`.
