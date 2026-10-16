---
slug: 2026-korinek-economic-scenarios-transformative-ai
title: "Economic Scenarios for Transformative AI"
status: accepted
domains: [social_science]
source_type: academic
source_url: https://www-cdn.anthropic.com/files/4zrzovbb/website/cf58f84d46a4a76bf5a5b039ac695fba6b80041c.pdf
canonical_ids: ["anthropic-institute-wp:2026-02"]
publisher_or_author: "Anton Korinek, Charles I. Jones, Szymon Sacher, Tess Cotter, Peter McCrory — The Anthropic Institute Working Paper No. 2026-02"
published: 2026-09
captured: 2026-10-16
relevance:
  social_science: high
  ai_engineering: n/a
verification: verified
rationale: >-
  Squarely on lens 1 (growth and productivity): a calibrated task-based macro
  model that maps explicit assumptions about AI capability, diffusion and
  automation into 2026–2030 paths for GDP, the labor share, wages and
  unemployment, benchmarked against the published forecast range. Also on
  lens 4 (public policy), since it sizes the transfers the extreme scenario
  would require. Deliberate user save.
---

# Economic Scenarios for Transformative AI

## Summary

A working paper that builds a framework for assessing the economic consequences of AI between 2026 and 2030, implemented in a public scenario explorer (anthropic.com/institute/econ-scenarios). The authors state that the scenarios "are not predictions" and carry no probabilities; the purpose is to make the consequences of different assumptions comparable.

**Model.** A standard task-based model in which AI automates or augments a growing share of tasks. Workers are in cognitive occupations (management, professional, sales, office), which are directly exposed, or in all other occupations, which are not. AI raises productivity but displaces cognitive workers, who must search for jobs elsewhere under frictions (a search-and-matching labour block with a discount on cross-occupation search effort, plus real-wage rigidity). AI also raises demand for capital and speeds up idea discovery through a semi-endogenous (Jones 1995) innovation block. The inputs are the share of tasks AI can do, diffusion, the productivity gain per task, the automation-versus-augmentation split, and new-task reinstatement.

**Three scenarios, 2030 outcomes (US, versus the no-AI path):**

| | Modest | Substantial | Extreme |
|---|---|---|---|
| Tasks impacted by AI | 4% | 12% | 30% |
| GDP above no-AI path | 1.6% | 8.3% | 32.4% |
| GDP growth, % per year | 2.4 | 5.4 | 15.4 |
| Labor share (from 60%) | 59.4% | 56.1% | 45.2% |
| Cognitive employment vs. mid-2026 | −0.5% | −3.9% | −21.5% |
| Unemployment, cognitive workers | 2.9% | 4.5% | 17.9% |
| Unemployment, all workers | 3.9% | 4.6% | 11.9% |

The modest scenario sits close to Acemoglu (2025) and the OECD estimates of Filippucci, Gal and Schief. The substantial scenario matches the 2023 financial and consulting forecasts (about 1.5 percentage points of annual labour-productivity growth). The extreme scenario is benchmarked against the AGI-acceleration literature. In the extreme case, cognitive wages are 11.5% below the no-AI path while wages in all other occupations are 33.6% above it. Almost all divergence between scenarios comes after 2027.

**Findings the authors flag:**
- The growth contribution of AI-driven innovation is minor. It raises labour productivity by well under one percent in all three scenarios, because research stays bottlenecked by physical tasks. The authors call this a likely lower bound, since the model omits research–automation feedbacks.
- In the extreme scenario, total labour income in 2030 is almost exactly what it would have been without AI, so all of the GDP gain accrues as capital income. A transfer of about 9% of GDP (roughly Social Security plus Medicare) would hold cognitive workers' income at its no-AI level.

**Survey.** A representative survey of 10,980 US adults asked when AI will do eight cognitive tasks, how widely it will be used, the productivity gains, automation versus augmentation, and re-employment time. Run through the model, the median answers (3,259 respondents answered all five items) imply outcomes close to the substantial scenario: GDP 8.6% above the no-AI path and cognitive employment down 4.2% by 2030.

**Caveats the authors state:** the model omits catastrophic risk, political economy, business cycles, financial disruption and demand-side feedbacks. It uses only two coarse worker groups, a single capital good (compute is not distinguished), and cognitive tasks only (no robotics), which is why it stops at 2030.

## Why it matters

The paper is useful less for its numbers than as a translation device. It makes explicit which capability, diffusion and automation assumptions separate a "1.6% of GDP" forecast from a "32%" one, and it places the existing forecast literature on one calibrated scale. For digital-economy and policy analysis, the public explorer offers a way to stress-test any AI-impact claim against its implied inputs. Two results are worth carrying into debates. First, the innovation channel adds little within this horizon. Second, the distributional problem in a high-impact case is a labour-to-capital shift of about 15% of GDP, not a fall in total output. The labour-market block (cross-occupation search frictions) is a reusable modelling template. Readers should note that the paper is published by Anthropic's research institute; the authors state the views are their own, not Anthropic's, and that Claude was used as a research and writing assistant.

## Verification notes

Full PDF fetched (2026-10-16, 656 KB, LaTeX source) and its text extracted. Every figure in the Summary was traced to the paper: the abstract, the Introduction (pp. 3–5), Section 4.1 (modest), Section 4.3 (extreme, including the labour-income and 9%-of-GDP transfer calculation), and Table 4 (scenario and survey-implied outcomes, including the 3,259 complete-response count). The survey size of 10,980 is from the Introduction. Bibliographic identity (title, five authors, Working Paper No. 2026-02, September 2026) is from the title page and suggested-citation line. It was corroborated against the publisher's scenario-explorer page (anthropic.com/institute/econ-scenarios, explorer v1.0, September 2026), which links this exact PDF and reproduces the GDP and labor/capital-share figures for all three scenarios. That corroboration is same-publisher, not independent. The model outputs are, by construction, the authors' own results; the underlying calibration and survey microdata were not re-examined. No DOI or SSRN/NBER identifier was found; the working-paper number is recorded as the canonical id.

## Updates

- None yet.

## Related entries

[2017-aghion-jones-jones-ai-growth](2017-aghion-jones-jones-ai-growth.md) — cited as the singularity case this model's innovation block deliberately cannot generate; shares an author (Jones).
[2025-oecd-filippucci-ai-productivity-g7](2025-oecd-filippucci-ai-productivity-g7.md) — OECD estimate the paper uses to benchmark its modest scenario.
[2026-blumenfeld-ai-software-engineering-macro](2026-blumenfeld-ai-software-engineering-macro.md) — another 2026 macro sizing of AI effects, through a single-sector channel.
[2026-imas-ai-productivity-paradox](2026-imas-ai-productivity-paradox.md) — the micro–macro gap this paper addresses by modelling diffusion and frictions explicitly.
[2026-massenkoff-economic-index-cadences](2026-massenkoff-economic-index-cadences.md) — Economic Index release sharing two authors (Sacher, McCrory).
[2026-favaro-clark-when-ai-builds-itself](2026-favaro-clark-when-ai-builds-itself.md) — Institute essay arguing that the AI-research channel, small in this model by 2030, may be strengthening.
