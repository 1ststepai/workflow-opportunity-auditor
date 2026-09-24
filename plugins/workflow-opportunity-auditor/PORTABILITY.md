# Runtime Portability Contract

`skills/workflow-opportunity-auditor/SKILL.md` and its references are the canonical behavior. Runtime adapters must load those files without weakening their research, evidence, supervision, or approval boundaries.

## Supported package surfaces

- Agent Plugins v1 and compatible future clients: `plugin.json`
- Codex: `.codex-plugin/plugin.json`
- Claude Code: `.claude-plugin/plugin.json`
- Cursor: `.cursor-plugin/plugin.json`
- Gemini CLI: `gemini-extension.json` plus `GEMINI.md`
- Grok Build: the portable skill and Claude-compatible plugin manifest, discovered through `~/.grok/plugins/workflow-opportunity-auditor`
- Grok Bot: `GROK-BOT.md` is the account-level private-skill handoff

Future adapters must preserve current primary-source research, explicit unknowns, build-versus-reuse ordering, reversible experiments, accountable approval, and the prohibition on unapproved account connections, purchases, installs, production changes, sends, or publishing. Validate fresh-session discovery before claiming activation.
