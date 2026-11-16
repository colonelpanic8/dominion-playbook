# dominion-playbook

Agent context and skills for the deck-building card game Dominion. This repo
targets Claude (Claude Code) and OpenAI (Codex) agents, and both share the
same files.

## Always

- Card text overrides general rules. When a question hinges on exact card
  wording, quote or ask for the card text rather than reciting it from memory.

## What to read when

Nothing else is loaded for you. Read each of these whole, once, when a task
first needs it, and don't read it again in the same task unless a specific
question sends you back to it. The skills say which file and section each
step needs.

- `context/strategy.md`: strategy fundamentals. Read it before analysing a
  kingdom or planning a game.
- `context/combos.md`: known game-deciding combos. Read it with
  `context/strategy.md` when analysing a kingdom.
- `context/card-power.md`: what the community ratings mean and how to look
  them up. Read it before using them.
- `context/rules.md`: the rules reference. Read it when a question turns on a
  rule you aren't sure of (timing, triggers, setup, how the game ends).
- `data/card-ratings.jsonl`: never read whole. Look cards up with
  `python3 data/card-ratings.py "Card One" "Card Two"`.

## Layout

- `context/`: reference material agents read when a task needs it. Every
  file here is listed under "What to read when". `context/rules.md` is the
  canonical rules reference, and other files should point to it, not
  restate the rules.
- `data/`: data agents query rather than read whole.
  `data/card-ratings.jsonl` is generated from the Card Glicko sheet by
  `just refresh-power`. Don't edit it by hand. `data/card-ratings.py`
  looks cards up in it.
- `skills/<name>/SKILL.md`: optional, task-specific workflows (YAML
  frontmatter with `name` and `description`, then instructions). Supporting
  material goes in `skills/<name>/references/`.
- `protocol/`: the agent-view@2 protocol. `agent-view.schema.json` is canonical;
  `README.md` is its spec (fields, knowledge, answers, text rendering);
  `tools.md` specifies dominion/play@1, the MCP tools every producer serves;
  `examples/` holds a view, its text rendering and an answer, produced by
  dominion-engine. Change the schema here first; producers (dominion-engine's
  `just sync-protocol`, dominion-navigator) vendor it. Keep it producer- and
  provider-neutral.
- Evals live in [dominion-bench](https://github.com/colonelpanic8/dominion-bench),
  not here: kingdoms with answer keys built from expert analysis.
- `.agents/skills` (Codex) and `.claude/skills` (Claude Code) are both
  symlinks to `skills/`. Never put files in them directly.
- `CLAUDE.md` holds only `@AGENTS.md`, so Claude Code loads this file. It
  is the repo's only include.

## Invariants

- Keep content provider-neutral. Don't use tool names, slash commands or
  frontmatter fields that only one agent understands, unless they are optional
  extras the other agent safely ignores.
- No includes (`@path`) or other loader features in shared files: Codex has
  none, and reference material should be read when it's needed, not loaded
  at every start. `CLAUDE.md` is the one exception.
- Keep this file short: every agent loads it at start. Reference material
  goes in `context/` and is listed under "What to read when"; a skill names
  the file and section at the step that needs it. Use a skill only for a
  workflow that some tasks need.
- Keep a skill's `name` equal to its directory name. Write descriptions that
  say when to use the skill, since that is what triggers it.
- Keep the rules reference concise: mechanics and edge cases, not card
  lists. Card-specific data belongs in a separate data file.
- Work on `master` and push there. Don't create branches or worktrees
  unless the user asks for one.

## Writing skills and context

Working guidelines from one round of Kingdom of the Week checks and four
dominion-bench runs of 16 kingdoms (`results/2026-11-11-opus-5-5-0c0c5b7`
there). One rewrite they led to scored 0.56 against 0.53 and 0.49 for the
rules before it, which is inside the run-to-run noise, so treat them as
hypotheses:

- Put the questions that narrow the search first, then a cheap sweep over
  everything the narrowing skipped. A focused search alone misses the
  unexpected card, and an exhaustive one is slow and shallow.
- Don't rely on a list of patterns to match. Agents treat a list as
  complete, so say that it isn't, and give a question to ask of each card.
- Make the cheap version the default and the thorough one opt-in.
- When a step needs a number (a turn count, a VP rate), ask for the worked
  line that produces it. An estimate with no working behind it is a guess.
- End with a step that attacks the conclusion: the cards that were skipped
  and the plan that was rejected.
- Apply the worked-line rule to the plan that is hardest to estimate, not
  the easiest. Agents put numbers on money plans, guess at engines, and
  then trust the plan that has numbers.
- Use ratings and tier lists as a check after the agent has its own view.
  Withholding them did not fix any missed interaction, so don't blame or
  remove them when an analysis goes wrong.
- Give the output format a slot for everything the procedure asks for,
  including assumptions.
- A warning doesn't move a default. The skill already said that a guessed
  engine loses to a worked money line, and analysts still picked money on
  boards where experts built engines. Say which plan gets the benefit of
  the doubt and what evidence overturns it.
- A list of conditions that must all hold gets used as a list of reasons to
  say no. Keep the real requirements few, and give the rest as obstacles
  with ways round them.
- Give reference numbers for whatever agents have to estimate (how long
  games last, how fast each kind of deck is). Without them they guess
  cautiously.
- Don't hand an analyst a simulator to compare plans with. Analysts given
  `dominion solo` (dominion-engine) to play lines out scored lower and
  recommended money on 12 of 16 boards, against 5 without it: they play
  the simple plan well and the hard plan once, badly, and then trust the
  comparison.
- Rules like these move which plan gets picked. They haven't made an
  analyst find an interaction it didn't see. The same tricks were missed
  before and after the rewrite.
- Card names used as examples steer analyses of boards that contain them.
  Prefer a general statement plus one example.
- dominion-bench runs are for occasional checks, not every edit. A blind
  run costs roughly 100k tokens and five minutes per kingdom.

## Checks

`just check` validates the shared symlinks and `CLAUDE.md`, that every
context file is listed here and nothing uses an include, skill frontmatter, the protocol schema (and that the example view matches it), and
checks Nix formatting. Run it inside the dev shell
(`direnv allow`, or `nix develop -c just check`).
