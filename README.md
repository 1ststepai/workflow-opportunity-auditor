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

### Gemini CLI

Link the repository extension during local development, or copy `plugins/workflow-opportunity-auditor/skills/workflow-opportunity-auditor` into `.agents/skills/` or `.gemini/skills/`. Start a new trusted session and verify the skill appears before relying on it.

### Grok Build and Grok Bot

Grok Build can discover the portable skill from `.agents/skills/` or a local plugin directory. Grok Bot private skills are account-managed: use `plugins/workflow-opportunity-auditor/GROK-BOT.md` as the reviewed handoff and verify the saved skill in the signed-in Bot account.

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
  gemini-extension.json                   Gemini extension metadata
  GEMINI.md                               Gemini context gateway
  GROK-BOT.md                             Grok Bot private-skill handoff
  PORTABILITY.md                          Runtime portability contract
examples/sample-workflow.json             Calculator example
tests/                                    Deterministic calculator tests
docs/BUILD-IN-PUBLIC.md                   Public demo material
```

## Status

Version `0.2.0` adds cross-model packaging while retaining the evidence-first workflow and supervised operating boundaries. Every recommendation still depends on the completeness and quality of the supplied business facts and current research.

## License

MIT. See [LICENSE](LICENSE).
