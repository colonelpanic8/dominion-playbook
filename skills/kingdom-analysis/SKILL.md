---
name: kingdom-analysis
description: Analyze a Dominion kingdom before the game starts and recommend a plan. Use when given a set of kingdom cards, landscapes or a game setup (a typed list, screenshot or Dominion Online log) and asked what to do, how to open, which strategy wins, or how strong the board's cards are.
---

# Kingdom analysis

Turn a kingdom into a recommended plan, an opening for each split the
starting deck can produce, and the risks to watch. First read
`context/strategy.md` whole and once, unless you already have in this
task: the steps below cite their sections. Read `context/rules.md` when a
rule decides something. This skill adds the
procedure. Once the game starts, use the `play-turn` skill for each
decision.

The plan is a starting point, not a commitment. The analysis is worth
doing up front because it maps what the board allows: then, during the
game, you can see when the opponent's choices or your own draws make a
different plan better, and switch to it.

Defaults, unless the user says otherwise:

- Assume 2 players. Name what would change with more players.
- Work from card text. Community ratings come in at step 5, as a check on a
  view you have already formed.
- Keep the reasoning concise. Don't give a tutorial, assume an audience that is
  proficient in the game.
- Distinguish firm conclusions from tentative ones where it affects the
  plan. Name the uncertainty and what would resolve it; don't hedge clear
  conclusions or attach a confidence label to every line.

## 1. Inventory

- List every Kingdom pile with its cost, plus every landscape (Events,
  Projects, Ways, Landmarks, Traits, Allies, Prophecies) and any non-Supply
  piles they bring (Spoils, Horses, Loot, Rewards, Spirits, ...).
- Note setup effects: Colony/Platinum, Shelters, Heirlooms, Young Witch's
  Bane, a Prophecy and its Sun count, which pile a Trait is on, split piles,
  and added piles (Approaching Army, Ferryman, Riverboat, ...).
  Colony/Platinum changes the race clock for every plan. Read "Colony
  games" in `context/strategy.md` before comparing speeds.
- Note special rules in play: Debt, Potion, Night, Favors, Exile, Coffers,
  Villagers, Durations.
- Note the price points: which costs are crowded (every key card at $5) and
  which are empty (nothing worth buying at $2, nothing above $5).
- Write down the actual starting deck and the turn 1–2 splits it produces.
  The default is 4/3 or 5/2, but Heirlooms and Shelters change the deck, and
  some change the money.
- Get exact card text from the user, the log or the client. Never
  reconstruct it from memory. If text is missing, ask or state your
  assumption.

## 2. Interactions

Before judging plans, find what the board's cards do together. The tricks
no card announces often decide a board, and an analysis that goes straight
to plans misses them. Follow the `interaction-spotting` skill
(`skills/interaction-spotting/SKILL.md`) now, in full: every card read to
the bottom, what would make each one great or take its hidden costs away,
every candidate tested and, when it fails, rescued if the board allows,
then the second look. Write its output before reading on, and give this
step real effort.

The steps after this one build on that list. Every interaction in it is a
candidate engine piece, loop or plan, and one that could decide the board
must come back in step 6, as a plan or as the reason against one.

## 3. First read: what is this board about?

Answer these quickly from the card text, before studying any card in depth.
The answers decide where to look harder. "Payload" and "deck control" are
used as defined in "Payload and deck control" in `context/strategy.md`.

1. **Scoring and ending**: every way to score here (Provinces or Colonies,
   other Victory cards, VP tokens, Landmarks, Curses as minus points), and
   which of them add no card to the deck. Which piles will run out, and how
   does the game most likely end?
2. **Draw and Actions**: what increases hand size, and is it terminal or
   non-terminal (see "Draw and villages" in `context/strategy.md`)?
   What gives a spare Action: villages, including conditional ones,
   Actions that arrive at the start of the next turn, and Villagers?
3. **Thinning**: what takes cards out of your deck (trashing, Exile, mats,
   swapping a card for a better one), and how fast is it?
4. **+Buy and gaining**: where does +Buy come from (Kingdom cards, Events,
   tokens), and what gains cards or VP without a Buy? With none of these, a
   turn scores at most one card, so an engine can't outscore money (see
   "+Buy turns a big turn into points"). For each gainer, say what it
   consumes, whether the deck will make that every turn, and what a second
   and third copy add: a gainer with renewable fodder is a stacking +Buy.
5. **Attacks**: is there a junker? Can it be blocked, trashed away or
   outpaced? What do the other attacks hit?
6. **Standouts**: a card the whole board bends around, an unusual setup, a
   landscape that changes scoring, a combo, or a way to end the game fast.

Then write one or two sentences: what the board is about, and what is still
open ("the only village is conditional", "no +Buy", "the payoff needs a
discard outlet"). Those open points are what step 4 goes looking for.

## 4. Is there an engine, and is it fast and reliable enough?

This is usually the question that decides the board. Money plus +Buy is
payload enough, so payload is rarely what's missing. What decides the
board is whether a deck here can draw itself, how soon, and how often.

- **Pieces**: the draw, the Actions its terminals need (none if draw and
  payload are non-terminal), thinning and +Buy the engine would use,
  the cheapest set of them, and their prices. If a piece is missing, name
  it.
- **Speed**: roughly when it first draws its deck, from the opening and
  the number of parts it must gain. Compare that with "How fast decks
  are" in `context/strategy.md`.
- **Reliability**: once built, how often does it draw its deck? Check what
  can stall it (see "Reliability" in `context/strategy.md`): copies of the
  key cards, Actions against terminals, spare draw, junk, and the
  opponent's attacks.
- **Resource loop**: when pieces feed each other (a card that gains what a
  trasher eats, Villagers that pay for terminal draw, tokens spent and
  earned each turn), write the loop with its rates: what each turn adds
  and spends. The engine works only while the loop balances, so the
  ratio of the pieces matters as much as their count, and the scarce side
  of the loop is what to buy next.
- **Ceiling**: the $ and Buys of a built turn, and how many Provinces (or
  other VP) that is per turn.
- **Payload**: now judge the payload cards for the deck this board wants.
  Note which pay off only when stacked (see "Payload depends on the
  deck"), and so matter only if the engine works.

When something stalls the engine (a missing or conditional village, no
+Buy, a key card not in hand every turn, a price that's hard to hit), look
for the card or landscape that fixes it. Do the same for any other scoring
route or combo from step 3. Read cards for what they **supply** and what
they **want**, not only for their role:

- Supplies: gains (and where they land: discard, hand, top of deck),
  discards from hand or deck, trashes, putting cards on top of the deck or
  ordering it, playing another card, extra Actions or Buys, tokens, anything
  carried to the next turn, forced discards or gains for the opponent.
- Wants: when-gained, when-discarded and when-trashed triggers; counts of
  cards, types or names; a particular cost or type in hand, in play or on
  top of the deck; an Action-dense hand; an Action already in play; a pile
  running out; the opponent doing something.

Consistency is a supply too. Cards that put cards on the deck, order it, set
cards aside or act at the start of the next turn can make one key card show
up every turn, and that is often what makes an awkward engine work.

Write each real interaction as a loop with numbers: "A does X, which
triggers B, for Y per turn, from about turn T".

## 5. Sweep what's left

Step 4 finds what you were looking for. This pass finds what you weren't.

- Go back to step 2's unpaired and rejected cards with the deck you now
  expect to build. A card that had no partner on a blank board may have
  one in this deck: does it create the situation the card needed, or take
  its cost away? "None" is an allowed answer only after checking it
  against each of the others.
- Check the patterns in `context/strategy.md` ("Interactions to look for").
  That list shows kinds of interaction and is not complete. Don't drop an interaction because it
  isn't listed.
- Look the board's cards up with `data/card-ratings.py`. Where your view
  and the rating differ by a lot, in either direction, take a second look
  and give the board-specific reason. A rating is never a reason to skip a card or
  to buy one. First-edition ratings carry little weight.

If the sweep turns up a new loop, take it back through step 4.

## 6. Decide

- **Candidates**: two or three plans that are realistic here. Always
  include the strongest Big Money + X as the baseline, the engine from
  step 4 if there is one, and one plan for each strong loop. Build the
  best version of each before judging it: the right opening, the cheapest
  set of pieces, every helper the board offers.
  For each, say how it works, what it needs by when (including the minimum
  number of copies of any scarce card, and whether the opponent wants them
  too), and its main weakness. Write every candidate down, even in a short
  write-up. A recommendation with no rivals beside it skipped this step.
- **No village**: when step 3 found no way to play two terminals in a turn,
  first check for non-terminal draw: with it, an engine of non-terminal
  draw and payload needs no village. Without it, the realistic plans are
  mostly money decks and the choice of X matters
  most, unless the board thins well: then work the thin deck's line (what
  leaves, how many cards remain by about turn 8, what that deck plays each
  turn) before picking money.
  Every such plan has one terminal slot a turn. For each candidate, count
  its terminals against the budget ("Terminal slots and collision" in
  `context/strategy.md`), and spend the slots on the best terminals, not
  on every good one.
  If the board has an attack, compare at least X as a draw card, X as
  the attack, and two copies of the attack. Estimate for each: the
  opening, the turns it first hits $6 and $8, and how often it plays its
  attack. k copies in an N-card deck reach a 5-card hand in at most
  5k/N of turns, less once copies collide (one copy in 15 cards: 1 turn in
  3; two copies: over half). Judge each against an opponent who also plays
  money (see "The Big Money baseline" in `context/strategy.md`).
- **Matchups**: name the opponent's best plan against your pick and
  against the runner-up. Check the race (does one plan end the game, or
  take an unbeatable lead, before the other comes online?), attacks that
  hit one plan much harder, contested piles and three-pile risk, and who
  controls when the game ends.
- **Pick** the plan with the best result against the opponent's best
  response. Against a strong opponent prefer a plan that holds up whatever
  they do.
- **The engine is the default.** If step 4 found draw that can reach most
  of the deck and the Actions to play it, pick the engine unless a
  compelling reason from "The engine gets the benefit of the doubt" in
  `context/strategy.md` holds, shown with worked lines for both plans.
  Engines usually beat money and good-stuff decks, and estimates of them
  run late, so between an engine and a rival that look close, pick the
  engine. An obstacle is a problem for the build to solve, not a reason
  to drop it.
- **Openings**: the best opening for each split from step 1, with one line
  of reasoning each. If a split leaves nothing worth buying at one price,
  say so.
- **Buy priorities** for the first two or three shuffles, and roughly when
  to start greening.
- **Ending**: which piles could empty, who benefits, and how the game ends.
- **Challenge the pick**: take one more look at the rejected plan with the
  highest ceiling, with every fix the board offers. Most wrong calls come
  from rejecting the stronger, harder plan after a shallow look. Then ask
  how your pick loses.
- **Least sure of**: the one conclusion most likely to be wrong, and what
  would show it. If the game itself will show it, make it a signal below.
- **Branches and signals**: for an uncertainty the game can resolve, name
  the preferred line, the observation that would change it, when to check,
  and the response. Consider your access to key prices, the deck's pace
  and reliability, the opponent's opening or attacks, and contested piles.
  The opponent's choices can reopen a plan you rejected: an engine their
  junker would have shut down may be best if they don't buy it.
  Use the worked line and the opponent's clock to set checkpoints, rather
  than a fixed turn to abandon the build. Prefer useful buys shared by
  the live options while waiting, but don't pay heavily to keep options
  open or build half of two incompatible decks. One bad draw alone needn't
  disprove the plan. Also name any split that changes the pick.

## Output format

`references/example-recruiter-wayfarer.md` is one board taken through this
analysis to a plan. Read it when you want to see the depth and shape
expected; its conclusions are that board's.

Keep branches and signals to those that could change a decision; combine
them when they describe the same contingency. State confidence where it
matters, especially for the recommendation and its weakest assumption.

```markdown
**Board:** <what it is about, from step 3, in 2–3 sentences>
**Engine:** <the pieces, when it draws its deck, how reliably, and a built
turn's $ and Buys; or the missing piece>
**Key interactions:**
- <A + B: the loop, with numbers; step 2's list, ranked, with anything
  later steps added>
**Rejected interactions:** <from step 2: the candidate and why it fails>
**Other cards:** <one line each: its best partner here, or "none">
**Plans considered:** <each in one line: how it works · rough line ($6 and
$8 turns, attack plays) · needs · weakness · what would make it the pick>
**Recommendation:** <plan, and why it holds up against the best response>
**Why not the engine:** <only if the board has one and the pick isn't it:
the compelling reason, with the worked lines for both plans>
**Against their best plan:** <the matchup for the pick and the runner-up>
**Open:** <split>: <cards> · <split>: <cards>
**Buy priorities:** <first two or three shuffles, per branch where they
differ, then when to green; without a village, the terminals the deck
holds and when it stops adding them>
**Ending:** <how it ends, which piles are at risk>
**Branches/signals:** <where needed: preferred line · what you see · when
to check · what you do then>
**Challenged:** <the rejected plan you re-tested, and how the pick loses>
**Least sure of:** <the conclusion most likely to be wrong, and the test>
**Assumed:** <rules readings or card text you weren't sure of, and anything
you needed that the repo context didn't cover>
```
