---
name: play-game
description: Play a whole game of Dominion as one seat through a `dominion` MCP server (dominion-engine or dominion-navigator), from the kingdom plan through every decision to a review afterwards. Use when asked to play a game, play against a bot or another agent, or carry on with a game in progress.
---

# Play a game

Play one seat from the first decision to the result. The server's tools are the
same on every producer and are specified in `protocol/tools.md`. The view and
its decisions are specified in `protocol/README.md`. This skill is the loop
around them: `kingdom-analysis` makes the plan, `play-turn` decides the hard
turns, and this skill decides how much thought each decision gets.

## Ground rules

- Know only what your seat may know. Never call a debugging tool (`inspect`
  or anything that says it reads hidden state), and never use another seat's
  token, even one `new_game` handed you.
- Don't sit down against human opponents unless the operator said to. A
  `REFUSED` error is the server enforcing that, so report it and stop.
- Trust the view over your memory. It tracks every card you could know about,
  including your own deck. Your notes only need to hold the plan and the
  deck it is building toward.

## 1. Start or rejoin

Call `state` first. If you already have a game in progress, carry on with it.
Otherwise call `new_game` with what the operator asked for (kingdom, bots,
seats). Its result is your first full view.

## 2. Make the plan

Before answering the first decision, do these in order, every game:

1. Look up the ratings of every Kingdom card and landscape on the board, all
   in one command:

       python3 data/card-ratings.py "Card One" "Card Two" ...

   If you can't run it, say so in the plan; don't guess ratings from memory.
2. Read `context/strategy.md` whole and once if you haven't yet. Read
   `context/rules.md` too if a card on the board turns on a rule you aren't
   sure of. Don't
   read them again later in the game unless a specific question sends you
   back to one.
3. Run `kingdom-analysis` on the kingdom in the first view, every step of
   it, the sweep of every card included, comparing your view with the
   ratings from step 1 where the skill says to. The `CARDS` block has the
   text of every card.
4. Before the first decision, share a short game plan: the recommended
   strategy, opening, and the key game facts that support them.

The first decision looks routine (a $3 or $4 buy), and that is when the
plan gets skipped; the opening is where the plan matters most. Keep the
result as a short game plan, about ten lines:

- the plan and the reason it beats Big Money here, with its loop when it
  has one: what feeds what, and which side runs short;
- the opening for each split;
- the deck you are building toward, in a line: its shape and the
  balances that matter (e.g. "a village per Smithy, 2 +Buys, Estates
  gone"), and what it needs first. This is a direction, not an order of
  buys: each gain is judged from the deck's composition at the time, and draws, prices and the opponent will call for changes;
- when you start greening;
- the parts of the plan the analysis was unsure of, and for each the
  options and what decides between them, by when;
- the signals that would change the plan (the opponent's attacks or plan,
  your pace, key or contested piles), each with when it shows and the
  response.

`skills/kingdom-analysis/references/example-recruiter-wayfarer.md` ends with a
plan written in this spirit: ideas and trade-offs, not a list of rules.

The plan is the only thing you carry between decisions. If the game is past
its opening when you join, still write the plan, from the current view.

## 3. Answer decisions

Each `step` result shows what changed and your next decision. A game has
roughly 30–60 decisions. Most are routine, but the gains and a few plays
decide the game, and those are where a deck drifts away from its plan.

Before a nonroutine decision, briefly explain your choice using the game
facts that matter. Give the conclusion and supporting evidence, such as
deck counts or finishing scores. Summarize the choice rather than narrating
the deliberation. Use the levels below to choose what to report, then call
`step`.

- **Routine**: no other answer could change the deck or this turn's
  result. Examples are playing Treasures when no card reacts to their
  order, ending a phase with nothing worth playing, or the only legal
  answer. Answer it straight away, several in one call where allowed. If
  you aren't sure a decision is routine, it isn't.
- **Play**: which Action to play, in what order, which card to hold. Write
  a line or two: what the hand could do this turn, and which play gets
  there. Use `play-turn`: make each decision as it comes, and look at the
  state again after every draw or reveal. Answer several moves in one call
  only when nothing between them draws, reveals or asks for a choice.
- **Deck change**: every buy or gain, including buying nothing and gains
  from a card such as Workshop, and every choice of what to trash, Exile or
  otherwise remove for good. These shape every hand for the rest of the
  game, so even one the plan seems to settle gets `play-turn`'s short
  gain explanation (step 6): what the deck's composition needs now, the
  candidates, and the pick. Read the composition from your player view's
  `owns` line (`owned` in JSON), which lists every card you own. It usually takes two to four lines. A choice that is close to this, such as a Throne Room target, a
  Reaction to reveal or Coffers to spend, gets the same care.
- **Full check**: also run `play-turn`'s endgame and attack-response steps,
  and write out their numbers, when the decision is any of these:
  - a buy or gain once the game could end within two turns;
  - a response to an attack;
  - a choice involving a card you haven't judged yet (new `CARDS` lines, an
    unplanned Loot or Reward, a card the opponent just started buying).

These lists aren't complete. For any decision they don't name, ask whether
a different answer could change what your deck holds or what this turn
produces. If it could, treat it as a play or a deck change.

Mechanics:

- Read indices from the latest `DECISION` only. They change from one decision
  to the next: after a buy, the piles you can no longer afford are gone and
  the rest move up, so the number that was Silver can now be Curse.
- With every `indices`, give `expect`: the label each index is meant to
  choose, in the same order (`indices: [2], expect: ["Buy Silver"]`). An index
  that points at something else is then rejected instead of played.
- Check each group's `min` and `max`. `indices: []` chooses nothing. For an
  ordered decision, list the top card first.
- After a `REJECTED` error, read the reason and the decision that came with
  it, then answer that. Don't resend the same answer.
- In a Buy phase, `play_treasures` plays every Treasure the decision offers
  in one call. Use it when the order and which Treasures you play don't
  matter; otherwise play them one at a time with `step` (`play-turn`,
  "Order the plays").
- On `WAITING`, call `wait`. Call `state` only when you've lost track: it
  prints everything. Use `log` for older history.

## 4. Revisit the plan

Check the plan against the view, in a line or two, at each of these moments:

- the first turn after each of your reshuffles (`play-turn`, "Check in
  on the position");
- the opponent's opening is visible (after their second turn), and whenever
  they start buying something new: check whether their choices reopen a
  plan the analysis rejected;
- your deck starts drawing itself, so it is time to switch to payload;
- the deck stalls or misses an important price: check whether this was
  an unlucky hand or a composition problem;
- a pile you or they need runs low;
- a branch's decider or a signal from the plan shows up: choose the
  branch then, not later;
- someone buys the first Victory card.

Use `play-turn`'s short check-in for position, the deck's current bottleneck
and the response. In it, count the deck you are building toward against
what you own and name the next piece, in one line: "draw 0 of 3, payload
1 of 3: the next $5 is draw". Combine it with the gain check when they
coincide. If nothing changed, a line confirming that is enough. Rewrite
the compact plan after a material change, or when the previous version is
too far back to follow reliably; say what changed and why.

## 5. Finish and review

On `GAME OVER`, report to the operator:

- the result line (VP, turns, how the game ended);
- the plan you made, and whether you kept to it;
- the one or two turns or decisions that decided the game, each with what you
  would do differently, if anything;
- anything the server got wrong or showed confusingly (a missing card text, a
  decision you couldn't express), so the producer can be fixed.

Keep the report short. Don't write lessons into the repository unless asked.

## Talking to the operator during play

Keep reports short: the plan once it is made, brief explanations of
important choices, position check-ins, any change to the plan, and the
result. Combine a check-in with a gain explanation when they cover the same
facts. If the server breaks (errors that aren't about your answer, a
game that stops advancing), stop and report what you called and what came
back, rather than guessing around it.
