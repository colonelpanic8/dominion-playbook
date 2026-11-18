---
name: play-turn
description: Choose plays in a Dominion game in progress, including play order, which cards to play or hold, what to buy or gain, when to change plan, the endgame, and responses to attacks (e.g. what to discard to Militia). Use for every decision while playing or advising on a game, each turn and each prompt, not only when asked; also when given a hand and game state and asked what to do, or when reviewing a played turn.
---

# Play a turn

Turn the current game state into plays and a buy. Briefly explain important
choices using the relevant game facts: nothing for routine moves such as
playing Treasures, a line or two for an Action play, and a short gain
explanation for every buy or gain (step 6). Report the choice and the
evidence supporting it, rather than a running account of the deliberation.
The sections cited below are in `context/strategy.md`, which `play-game`
has you read before the first decision. If you haven't read it in this game,
read it whole now, once; don't re-read it each turn.

Decide one play at a time. Work out what the hand could do, then look at
the state again after anything that draws, reveals or asks for a choice.
Only moves that can't change what you know, such as playing Treasures, can
be decided together.

## 1. Read the situation

- Get the hand, cards in play, Durations and mats, and whatever is known
  about your deck and discard pile: their size, what's left in the deck
  since the last shuffle, and good cards waiting in the discard.
- Get the scores, the pile counts (Provinces/Colonies and any pile close to
  empty), and your available Actions, Buys, $, Coffers, Villagers and
  Favors.
- Use the card text supplied with the state. Don't reconstruct it from
  memory. If something needed is missing, say what you assumed.
- Decide what this turn is for: building, greening, ending the game, or
  several of these. Name the price or gains it needs (e.g. "$8 + a Buy",
  "gain 2 villages"). A good draw can make room for both an engine piece
  and a Duchy; a bad one can make the best play a modest gain and a strong
  next hand.
- Ask what your deck is most short of right now, and let the answer guide
  every gain, trash and choice this turn, not only the buy. It is often
  not a missing card but a balance: Actions spent faster than they come
  in, trash fodder running out, draw that finds nothing to play. Revisit it
  after each draw: what the deck lacks can change in the middle of a turn.
- When a card that wasn't part of the plan shows up (a Black Market reveal,
  a Loot, a Reward, a card an attack hands you, something the opponent just
  started buying), check it against the board before judging it: what here
  supplies what it wants, and what wants what it supplies? See
  "Interactions to look for" in `context/strategy.md`. A card that is weak
  on most boards can be the best buy on this one.

## 2. Order the plays

- Play draw first, so later choices are made with the most information.
  Play villages before terminals as needed to keep Actions.
- Play cards that trash from your hand last, so you've seen the most
  targets.
- Hold Throne Room or King's Court until you know what you lack. The best
  target is often another multiplier, or a card that produces what this
  turn still needs.
- Play a gainer just before a reshuffle if you want the gained card soon,
  and late if you don't.
- Some costs depend on what you gained this turn (a card that copies the
  last gain's cost, one that gets cheaper per gain). Then the order and
  choice of gains is part of the play: a cheap gain first can make the
  card you want affordable, and a gainer can take a cheap card to set the
  price the Buy can pay.
- With more than one Buy, or before buying an Event or Project, play all
  the Treasures you mean to use before the first purchase. Buying anything
  ends Treasure play for the turn (`context/rules.md`, "Buy phase"), so
  paying for one purchase with just the Treasures it needs strands the
  rest. Hold back only a Treasure that hurts you to play.
- Play the Treasures all at once only when neither their order nor which
  ones you play can matter. Otherwise play them one at a time:
  - a Treasure that counts or multiplies what is already in play goes
    last (Bank, Fortune);
  - a Treasure that asks a question or plays another Treasure (Loan,
    Crown, Counterfeit, Venture) needs its answer chosen with the rest in
    view;
  - hold back a Treasure that costs you to play when you don't need its $
    (Capital's Debt, Contraband letting the opponent name a card), or
    that blocks the buy you want (Copper in play stops a Grand Market
    buy).

## 3. Control the reshuffle

- Cards in your hand or in play when you reshuffle miss that whole pass
  through your deck. Trigger a reshuffle when your discard pile is strong
  and your hand is weak, not right after a big turn put your best cards in
  play. Drawing is a choice too: when a draw would reshuffle with your best
  cards in play, look for a way not to draw (take $ instead of cards,
  stop playing draw) if the turn already has what it needs.
- Don't fill your discard with junk (Cellar, Warehouse) just before you
  draw into a reshuffle.
- Cards that reveal or look at several cards (Sentry) reshuffle as soon as
  fewer cards are left than they look at.
- When buying: if a few cards remain in your deck, your next hand is mostly
  those cards plus the top of the new shuffle. Buy what improves that hand.
  Early in the game, buy what improves your very next shuffle.

## 4. Check in on the position

On the first turn after you reshuffle, write a short read of where you
stand. Also check when an attack, contested pile, unexpected deck problem
or signal from the plan could change a decision; don't wait for the next
shuffle. Usually one to three sentences cover the position, bottleneck
and response together. If unchanged, one line is enough. Expand only when
the evidence changes the read or the decision needs a closer comparison.
Use the state already available; fetch more only if missing information
could change the decision.

- **Position**: ahead, even, behind or unclear, with confidence and the
  evidence. "I'm clearly ahead: same engine, but mine is thinned and has
  spare draw" is stronger than "I think I'm behind: theirs looks faster,
  but I haven't established its reliability." Judge it as in "Who's
  ahead" in `context/strategy.md`, mainly from the decks, clocks and
  control of the ending. Near the end, calculate finishing scores.
- **Deck**: the one thing most likely to stop your deck doing its job next
  shuffle, and whether it is on pace for the plan's payoff before the
  opponent's clock runs out: count the pieces the plan's deck needs
  against the ones you own. Give the evidence: "4 terminals, 1 village:
  over-terminaled", "stalled twice because the only village missed the
  starting hand: needs reliability", "nothing at $5 yet". A shortage can be
  a rate rather than a count: "2 Villagers banked, spending 3 a turn,
  earning 3 only when Recruiter finds a Silver: short of Recruiter food".
  Count what comes in and goes out each turn. Distinguish a
  composition problem from an unlucky hand. Use observed counts or a
  worked estimate, not an invented success rate. If no bottleneck needs
  fixing, say so briefly. Once the deck draws most of itself, the limit
  is usually what it makes, not what it draws: give its total $ and Buys
  with every card played, against the price the plan needs
  (`context/strategy.md`, "Count what the deck makes").
- **So**: what the read changes: the next buys, how much risk to take
  (`context/strategy.md`, "Risk and luck"), when to green, a branch to
  choose. Being behind on score while building is expected. Change plan
  when you won't reach your payoff before the opponent's clock runs out,
  or when the opponent's choices make another plan better. A new plan
  starts from the deck you have.

Later gain checks (step 6) start from this assessment, updated for any
cards gained or removed since it. Don't repeat the check-in at each prompt.

## 5. Don't play everything

- Skip plays that hurt you, such as forced trashing of a card you need, or
  that help the opponent, such as a "steal or swap" attack while they hold a
  Province, or effects that give them cards.
- With one Buy, once you've reached your price, consider stopping so good
  cards stay in your deck for next turn.
- Don't play dead cards that only reveal information to the opponent.

## 6. Choose the buy or gains

For every buy or gain, briefly explain how it serves the deck, including
one the plan seems to settle, gains from Action cards, and buying nothing.
Summarize the relevant points below, usually in two to four lines:

- **Composition**: look at the whole deck as it is now, not just this
  hand, and say what it is most short of right now, with the counts that
  show it, and only those. This is the main question for every gain: the
  best gain is usually whatever relieves the shortage that will stop the
  next shuffle. "3 villages,
  Militia, Smithy: Actions to spare, short of draw" is enough. Early, deck
  control and thinning usually beat payload; once the deck is reliable,
  payload usually wins. A card that is strong in general can be wrong for
  this deck, such as more draw with nothing to play it with.
- **Candidates**: the card the plan names, and the best other card at each
  price you can pay.
- **Pick**: the gain, and what it is for: the next shuffle, the finished
  deck, or a pile that decides the game. The plan gives direction, not a
  shopping list. Any card that gives the deck what it needs serves it,
  and a chance the plan didn't foresee can be worth taking: a price you
  rarely hit, a pile about to run out, a card the opponent's play made
  stronger. When the pick doesn't address what the deck needs, or
  isn't what the plan would take, say why in a line. What to avoid is a
  gain with no reason behind it, such as Silver by default, or a card
  that is good in general but does nothing for this deck. If no reason
  holds up, take what the plan says.

Choosing what to trash or Exile gets the same check in short form: what
leaves, and what the deck needs after. Which way the doubt goes depends
on the deck:

- **While a hand is a sample of the deck**, removing its worst cards is
  the default, Coppers included.
- **Once the deck draws most of itself**, a card that makes $ stays by
  default. Give the deck's total $ before and after the trash
  (`context/strategy.md`, "Count what the deck makes") and the price the
  turns left need. Trash it when the total after still clears that price
  with $1–2 spare, when the same turn replaces it, or when the game ends
  before it would be played again. A bonus for trashing it (VP, Villagers,
  a gain) is weighed against the $ it would make on each turn left.
- **A mandatory trash is part of the cost of the play that forces it.**
  Count it before playing that card. Choose the order and target that
  take least from the total, and skip the play if the turn doesn't need
  what it gives.

Also:

- Read the plan as adjusted to what has happened since the kingdom
  analysis: did the opponent commit to a plan, did a key pile run low?
- When asked whether one buy is right ("is Silver right here?"), don't
  confirm it from the plan alone. Compare it with the best other card at
  each price you can pay, and work out the next hand for any candidate that
  changes it (gained to hand, a when-gain effect, a Night card). If the
  comparison shows the plan misread a card, say so and redo the plan.
- Before buying or gaining a terminal, count the terminals in your deck
  including this one. Without villages, keep to roughly one per 8–10
  cards, fewer once the deck draws, and one in all once it draws itself
  (`context/strategy.md`, "Terminal slots and collision"). Past that, a new
  terminal collides often enough that Treasure or a non-terminal is
  usually the better buy.
- Before a scoring buy, check the endgame (`context/strategy.md`, "Greening
  and the endgame"). Before gaining a Victory card, weigh its VP against
  the later hands it will land in. A rough read is enough: how many
  shuffles are left, and how much slack the deck has to hit its prices. A
  spare Buy with leftover $ isn't a free point: before the endgame, a
  useful card or nothing usually beats an Estate or an early Duchy. Once either player could end the game within a turn
  or two, work out the scores after each option and what the opponent
  would need on their next turn to win. Then apply:
  - the Penultimate Province Rule and its exceptions, to those numbers;
  - the opponent's whole next turn: unused extra turns, stored Coffers,
    Villagers or Favors, cards on mats, and the +Buys and Golds left in
    their current shuffle;
  - three-pile risk: how many gains each player needs to end the game.
- Decide whether to spend or keep Coffers and Villagers for a later price
  point or a bigger turn.

## 7. Responding to attacks

- **Discard attacks** (Militia): keep the best three-card *hand*, not the
  three best cards. A deck that draws can keep Village + Smithy and discard
  Golds.
- **Junking**: when given a choice (e.g. Torturer), don't always take the
  option that keeps your deck clean if it costs you your own key plays.
- Reveal Reactions only when the benefit beats keeping the card's normal
  use.

## Output format

```markdown
**Goal this turn:** <e.g. "$8 + Buy for Province + Duchy">
**Play:** 1. <card> — <why, if not obvious> 2. ...
**Buy/gain:** <what the deck needs now, with the counts that show it ·
candidates · pick, and the reason for any departure; for a terminal, the
count against the terminal budget>
**Trash/Exile:** <what leaves, and what the deck needs after; once the
deck draws itself, total $ before → after and the price still needed>
**Check-in:** <when due: position and confidence · deck bottleneck and
evidence · response; combine into a sentence if little changed>
**Endgame:** <once the game could end: scores after each option, and what
the opponent would need>
```

If the best line depends on unknown information, give the line for the
likely case and say what would change it.
