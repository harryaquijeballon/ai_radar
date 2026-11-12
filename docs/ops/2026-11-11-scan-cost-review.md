# Scan cost review, 2026-09-02 → 2026-11-11

Asked on 2026-11-11: cost per scan looked as if it was rising, from about $1.60 on 10-18 to $6.09 on 11-10. Is it, and what drives it? Source: the result block (`num_turns`, `total_cost_usd`, `duration_ms`) and the job summary of all 71 scheduled runs since 2026-09-02, read with `gh run view --log`.

The dollar figure is the CLI's `total_cost_usd`, an API-price equivalent. The run authenticates with a subscription token, so it is a measure of usage, not an invoice.

## Answer

1. **Cost is not drifting upward.** It moves with how much work the scan does. The apparent rise starts from an unusually cheap fortnight.
2. **Turns explain most of it:** about 3 cents per turn. Each new entry adds about 3.5 cents more.
3. **The step up after 10-27 is the window fix doing its job:** four times more entries per day for 22% more cost. Cost per entry fell from $1.19 to $0.35.
4. **No growth effect is visible yet** from the library getting larger, but the files the scan consults are growing fast and this is the thing to watch.
5. **What a scan's cost is made of (input, cache, output; which model) could not be read from the logs.** Two rows added today will show it from the next run.

## The four periods

| Period | Runs | Scan cost, mean (median, max) | Turns | $ per turn | New entries per run | $ per new entry |
|---|---|---|---|---|---|---|
| A. 09-02 → 09-28, `claude-sonnet-5` | 27 | $3.08 ($2.99, $4.64) | 109 | 0.028 | 2.6 | 1.19 |
| X. 09-29 → 10-16, collapse on `claude-sonnet-5-5` | 18 | $0.40 ($0.37, $0.68) | 32 | 0.013 | 0.8 | 0.48 |
| B. 10-17 → 10-26, model pinned, old window rule | 10 | $2.28 ($2.38, $3.28) | 91 | 0.025 | 2.8 | 0.81 |
| C. 10-27 → 11-11, new window rule | 16 | $3.76 ($3.61, $6.09) | 124 | 0.030 | 10.7 | 0.35 |

- Period C costs 22% more per scan than September, not four times more. The "$1.60 → $6.09" comparison set the cheapest day of period B against the dearest day of period C.
- Period B was cheap because the scans were short (91 turns), not because the price per turn was lower.
- All invocations included (repairs, second attempts), period C averages $3.98 per run, about **$119 per 30 days** for the two domains. Repairs are 5% of that.
- The eight red runs since 09-02 spent $30.87 and delivered nothing: 17% of the $181 total.

## What drives cost

Least-squares fit over the 53 runs on `claude-sonnet-5`:

```
scan cost ($) = -0.33 + 0.030 × turns + 0.036 × new entries        R² = 0.72
```

- Turns alone give R² = 0.68.
- Adding the calendar day as a third variable changes nothing (coefficient -0.001 per day): once turns and entries are held fixed, **there is no time trend**.
- Rejections logged add nothing measurable.

Price per turn rose slightly, from $0.028 (A) to $0.030 (C), about 7%. The days with the highest price per turn are heavy writing days: 11-10 ($0.041, the dedup-miss day that rewrote entries), 10-30, 11-11, 11-04, 10-29 (all about $0.035, with 10 to 18 new entries). That is consistent with output tokens, the dearest kind, but the logs cannot confirm it.

The 11-10 run ($6.09) was an outlier for two reasons at once: many turns (147) and the highest price per turn. It is also the run that regenerated two existing entries and wrote three duplicates.

## The growth risk

What the scan must consult grows with the library:

| File | 09-02 | 10-17 | 11-10 |
|---|---|---|---|
| `library/INDEX.md` | 46 kB (246 entries) | 59 kB (315) | 88 kB (465) |
| `library/rejections.md` | 39 kB | 153 kB | 187 kB |

Together they are now about 275 kB, in the order of 70,000 tokens if read whole. If the agent read both in full, every later turn would carry them, and price per turn would climb with the library. It has not: the rejection log grew fourfold between September and October while price per turn went down. The likely reason is that the agent searches these files instead of reading them (9 and 12 `Grep` calls in the two runs whose tool counts were kept, 11-10 and 11-11). That is behaviour, not a guarantee.

[interpretation] The structural protection is the same as for dedup: do the lookup in a script. The entry write guard already checks identifiers at write time. If the token rows show the index or the rejection log being read whole, the next step is to stop the agent needing them: a harness-side lookup for candidates, and no more date-only rejection lines (already stopped on 10-27).

## For planning another radar or more categories

- Budget by turns. A two-domain scan here runs 110 to 125 turns and costs $3 to $4. The split between the two domains was not measured.
- A category adds cost in proportion to the sources it fetches and the candidates it reviews, not to the size of the library, as long as dedup stays a search.
- Accepting more per day is cheap: about 4 cents per extra entry on top of the turns it takes.
- Failed runs are the avoidable cost: 17% here. In-run checks (the write guard, and the proposed coverage check in `docs/ops/2026-11-11-coverage-floor-incident.md`) recover that spend as delivered days.
- The alarm ceiling of $8.00 per scan stays: no run has passed $6.09, and nothing here argues for a lower or higher one.

## What was not measurable, and the fix

The job log carries total cost only. It does not say how much was fresh input, cache writes, cache reads or output, or how much went to the small model that summarises fetched pages. Added today (`scripts/run_metrics.py`, `scripts/make_run_summary.py`): when the transcript's result block carries them, the run summary shows

- `scan tokens (input / cache write / cache read / output)`
- `scan cost by model (USD)`

Whether the CLI writes these fields into the transcript the harness reads is not yet verified; the rows appear only if it does. Review again after about seven runs with the rows present.

## Verification

- All 71 scheduled runs from 09-02 to 11-11 are in the table; none was dropped. For runs with several invocations, the scan is the invocation with the most turns.
- Figures recomputed from the logs by script on 2026-11-11.
- Not verified: the token composition of cost; why price per turn is higher on heavy writing days.

## Update 2026-11-12: first token breakdown

Run 43224490117 (delivered, 141 turns, $3.61) is the first with the token rows.

| Measure | Value |
|---|---|
| Fresh input tokens | 108 |
| Cache-write tokens | 243,640 |
| Cache-read tokens | 8,912,673 |
| Output tokens | 72,216 |
| Cost by model | `claude-sonnet-5` $3.48, `claude-haiku-5-5` $0.14 |

- The small model that summarises fetched pages is 4% of the cost. Fetching is not the cost driver.
- Cache reads are 97% of all tokens. Divided by the 141 turns, each turn re-reads about 63,000 tokens of accumulated context. That is why cost follows turns: every extra turn pays again for the whole conversation so far.
- [interpretation] Under the usual price ratios (cache read 0.1, cache write 1.25, output 5, relative to input), cache reads would be a little over half the cost, output about a quarter and cache writes about a fifth. The actual prices were not checked.
- This sharpens the growth risk above: anything that enlarges the context early in the run (reading the index or the rejection log whole, long engine files) is paid for on every later turn. One day of data; review after about seven runs.
