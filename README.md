# Workflow Opportunity Auditor

Most businesses do not need another automation project. They need to know which part of a workflow is worth changing, what already exists, and whether the expected outcome justifies the cost and risk.

Workflow Opportunity Auditor is a free, open-source agent skill from [1stStep.ai](https://1ststep.ai). It maps a repetitive workflow, records an honest baseline, researches current alternatives, and returns one evidence-backed decision:

- `reuse`
- `configure`
- `integrate`
- `extend`
- `experiment`
- `build`
- `do not automate`

It prefers removing unnecessary work and using existing capabilities before recommending custom software.

## What you receive

- A current-state workflow map
- Measured facts separated from estimates and unknowns
- A review of existing tools, native features, APIs, plugins, MCP servers, and open-source options
- A deterministic time, cost, and payback calculation when enough data exists
- A reversible first experiment with success measures and stop conditions
- The precise unmet requirement when custom development is justified

## Install

### Claude Code

```text
/plugin marketplace add 1ststepai/workflow-opportunity-auditor
/plugin install workflow-opportunity-auditor@workflow-opportunity-auditor
```

### Codex

```text
codex plugin marketplace add 1ststepai/workflow-opportunity-auditor
codex plugin add workflow-opportunity-auditor@workflow-opportunity-auditor
```

### Cursor

Import `https://github.com/1ststepai/workflow-opportunity-auditor` from **Dashboard → Plugins & MCPs**, or copy the plugin directory into your local plugin setup.

## Try it

Ask your agent:

```text
Audit our weekly lead follow-up workflow. Map the current process, identify missing baseline data, research what our existing stack and current products can already do, and recommend whether we should remove, reuse, configure, integrate, experiment, build, or leave it alone. Do not invent costs or savings.
```

The included calculator can also be run directly:

```powershell
python plugins/workflow-opportunity-auditor/scripts/workflow_economics.py examples/sample-workflow.json --format markdown
```

## Operating boundaries

The skill performs diagnosis, research, and planning. It does not connect accounts, purchase or install software, alter production systems, send messages, or publish content unless the user separately authorizes that action.

It treats absent facts as `unknown`, distinguishes estimates from measurements, and describes labor savings as capacity unless the business can show an actual cash reduction.

## Repository layout

```text
.agents/plugins/marketplace.json          Codex marketplace
.claude-plugin/marketplace.json           Claude Code marketplace
.cursor-plugin/marketplace.json           Cursor marketplace
plugins/workflow-opportunity-auditor/     Portable plugin
examples/sample-workflow.json             Calculator example
tests/                                    Deterministic calculator tests
docs/BUILD-IN-PUBLIC.md                   Public demo material
```

## Status

Version `0.1.0` is an early public release. It is useful for structured workflow discovery and build-versus-reuse decisions, but every recommendation still depends on the completeness and quality of the supplied business facts and current research.

## License

MIT. See [LICENSE](LICENSE).
