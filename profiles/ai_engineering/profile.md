# AI-engineering interest profile

> **Strawman draft — edit me.** Drafted by the agent from the project's requirements; the user's editing pass is the quality gate. Scoring behavior changes only when this file changes.

Scope: technical practice for building **reliable** AI-powered research and policy products — not model research for its own sake, not AI business news. Audience for outputs: data-scientist and AI-builder colleagues. A standing generic lens: techniques that would inform an *agentic simulation of policy interventions* — multi-step agent systems whose outputs must be validated, reproducible, and defensible.

## How tiers are decided

- **high** — squarely on at least one lens below AND practically usable: a pattern, tool, eval method, or failure-mode analysis a builder could apply to a research/policy product this quarter.
- **medium** — on-lens but early, unvalidated, or framework-specific context worth knowing.
- **low** — adjacent background (model releases, benchmarks without engineering lessons).
- **n/a** — off-profile. Model announcements and funding news never score above low without an engineering lesson attached.

## Relevance lenses

1. **Agent architecture and orchestration** — captures: single- vs multi-agent designs, planning, delegation, workflow engines, subagent isolation, failure recovery. *High* for patterns with stated trade-offs and evidence; *medium* for architecture opinion pieces.

2. **Harness and context engineering** — captures: context management (memory, compaction, progressive disclosure), skill/prompt design as engineering artifacts, harness design that constrains model behavior. *High* when it names mechanisms and when to use them.

3. **Tool use and MCP** — captures: tool-interface design, Model Context Protocol servers/clients, function-calling reliability, tool-permission models. *High* for interoperable, reusable integration knowledge.

4. **Evaluation, validation and deterministic guardrails** — captures: eval design, LLM-as-judge validity, structured outputs, schema enforcement, deterministic checks around stochastic components. *High* for methods that make agent output trustworthy enough for research/policy use — the core lens for the policy-simulation interest.

5. **Observability and debugging** — captures: tracing multi-step agent runs, failure taxonomy, logging/replay, cost and latency monitoring. *High* for approaches transferable across frameworks.

6. **Reproducibility, security and governance** — captures: versioning of prompts/models/data, run reproducibility, prompt injection and tool-abuse defenses, sandboxing, audit trails, model governance for institutional use. *High* for concrete controls; *medium* for governance commentary.

7. **AI-assisted software development** — captures: coding agents in real SDLC use, code review by/of AI, testing AI-written code, team practices with evidence. *High* for measured results or transferable practices.

8. **Reliable research and policy products** — captures: RAG and document-grounding done rigorously, citation verification, data-analysis agents with validation, simulation harnesses, human-in-the-loop review patterns. *High* whenever the technique moves an AI research product from demo to defensible.
