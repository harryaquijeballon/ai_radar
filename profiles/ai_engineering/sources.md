# AI-engineering curated sources

> **Strawman draft — edit me.** Every source is public. Types: primary | academic | commentary. Discovery (ENGINE.md P6) checks the active lists first; the radar may append to "Proposed" with justification but never queries it.

> **`fetch hosts`** (added 2026-10-26, plan `docs/plans/2026-10-16-001-fix-discovery-coverage-plan.md` U12): the hosts — or `host/path-prefix` — where the unattended scan reads each source. The harness matches the run's actual fetches against this column to measure scan coverage (`scripts/validators/check_scan_coverage.py`). Hosts must be on `profiles/egress_allowlist.md`; `—` means the source is reachable only through search and is left out of the coverage ratio. Keep this column current when adding or editing a row.

## Practitioners (public blogs and posts)

| who | type | why included | fetch hosts |
|-----|------|--------------|-------------|
| Andrej Karpathy | commentary | Among the most trusted independent voices in the field: "English as a programming language", nanoGPT-style minimal pedagogy, coined "vibe coding"; shapes how the discipline thinks about building with LLMs — lenses 2, 7. | `karpathy.ai`, `github.com/karpathy` |
| Simon Willison | commentary | The most consistent public chronicler of LLM engineering practice; early, sceptical, hands-on — lenses 2, 3, 6, 7. | `simonwillison.net` |
| Hamel Husain | commentary | The reference practitioner voice on evals that actually work — lens 4. | `hamel.dev` |
| Eugene Yan | commentary | Applied LLM system patterns with literature grounding — lenses 1, 4, 5. | `eugeneyan.com` |
| Chip Huyen | commentary | Systematic AI-engineering treatments (books/posts); good architecture-level maps — lenses 1, 2, 5. | `huyenchip.com` |
| Lilian Weng | commentary | Deep technical surveys (agents, safety) bridging research and practice — lenses 1, 6. | `lilianweng.github.io` |

## Organizations, series and repositories

| source | type | why included | fetch hosts |
|--------|------|--------------|-------------|
| Anthropic engineering & research blog | primary | First-party depth on agent design, context engineering, MCP, agentic safety — lenses 1, 2, 3, 6. Vendor perspective: read accordingly. | `anthropic.com`, `www.anthropic.com/engineering`, `www.anthropic.com/news`, `www.anthropic.com/research` |
| OpenAI research blog & Cookbook | primary | First-party patterns and eval tooling; the other reference stack — lenses 1, 3, 4. Vendor perspective. | `openai.com` |
| Google DeepMind blog | primary | Agentic systems and evaluation research at scale — lenses 1, 4. Vendor perspective. | `deepmind.google` |
| Model Context Protocol (GitHub org + spec) | primary | The interoperability standard for tool use; spec changes are directly actionable — lens 3. | `modelcontextprotocol.io`, `github.com/modelcontextprotocol` |
| Hugging Face blog | primary | Open-source tooling, reproducible pipelines, eval leaderboard methodology — lenses 4, 6. | `huggingface.co/blog` |
| METR reports | academic | Independent evaluations of agentic capability and autonomy; antidote to vendor benchmarks — lenses 4, 6. | `metr.org` |
| Stanford HAI (incl. the AI Index) | academic | University-based independent measurement of AI capability, cost, and adoption trends; a second counterweight to vendor benchmarks — lenses 4, 6. | `hai.stanford.edu` |
| Epoch AI | academic | Independent data and analysis on AI capability and compute trends; evidence base for capability claims — lenses 4, 6. | `epoch.ai` |
| arXiv cs.MA / cs.CL / cs.SE (agent, eval, SE-with-LLM papers) | academic | Preprint pipeline for agent architecture, evaluation, and AI-assisted development research — lenses 1, 4, 7. | `arxiv.org/list/cs` |
| LangChain / LlamaIndex blogs | commentary | Framework-vendor posts; useful for ecosystem patterns, discounted for framework promotion — lenses 1, 3, 5. | `langchain.com`, `llamaindex.ai` |
| Towards Data Science | commentary | User's existing high-yield source; applied builds and post-mortems — lenses 1, 4, 5, 7. | `towardsdatascience.com` |

## Deliberately not covered

**Aniket Panjwani** — retired by user decision 2026-08-12 (no yield during
the pilot; rationale recorded in `profiles/social_science/sources.md`, where
the trail was cross-listed).

## Proposed (pending approval)

*(moved — proposals now live as pending records in `reviews/source_proposals/ai_engineering.md` (engine P6.5); only the user promotes one into the active lists above. No pending proposals existed at migration, 2026-07-23.)*
