# dominion/events@1

A game of Dominion as a stream of **events**, each one precise statement about the game.
The events describe a **table**: where every card is, every counter and token, the turn,
the lasting effects, the piles. A reader who applies the events one after another has the
whole table, with no rules engine: **the table after event *n* is the fold of events
`0..=n`**. This document defines the table, every event, and exactly what each event does
to the table.

The same stream is how a game is talked about (by a program, a log, an agent), how it is
recorded (Arena records every game it hosts this way), and, later, what a client can be
sent to follow a live game. It also holds what caused the game: how it was set up, how
chance fell, and what each seat was asked and answered. So the engine that recorded a
stream can play the game again from the stream alone ([Replay](#replay)).

The format is a **model**: the types below and what they mean. An **encoding** writes
those types as bytes. JSON Lines is the reference encoding and CBOR is a second one
([Encodings](#encodings)). The JSON examples in this document illustrate the model in the
reference encoding; every one is real output of `dominion-engine`, from the complete
streams in [`examples/events/`](examples/events/).

Status: only the **full** stream exists: every card's face, every shuffle's order. The
versions for one seat and for the public are not specified
([Not specified yet](#not-specified-yet)).

## An example

The first turn of [`moat-chapel.events.jsonl`](examples/events/moat-chapel.events.jsonl),
a two-player game. The first record is the header; then come `setup` (here trimmed with
`…`), each player's opening shuffle and draw, and the first turn, with each question Ann
was asked (after the first, their options trimmed with `…`) and her answer:

```jsonl
{"schema":"dominion/events@1","viewer":"full","game":"g12"}
{"seq":0,"type":"setup","rules":{"implementation":"dominion-engine","version":"0.1.0"},"seats":["Ann","Bo"],"kingdom":["Throne Room","Wharf","Moat","Militia","Chapel","Fortress","Haven","Village","Smithy","Market"],"table":{"zones":{"0/deck":["Copper","Copper","Copper","Copper","Copper","Copper","Copper","Estate","Estate","Estate"],"1/deck":["Copper",…],"pile/Chapel":["Chapel",…],…},"piles":{"pile/Chapel":{"card":"Chapel","supply":true,"recipe":{"kind":"stacked","cards":[{"card":"Chapel","count":10}]}},…},"costs":{"Chapel":{"coins":2},"Copper":{"coins":0},…}},"config":{"colonies":false,"shelters":false,"turnLimit":40,"seed":189}}
{"seq":1,"type":"shuffle","player":0,"cards":["Estate","Copper","Estate","Copper","Copper","Estate","Copper","Copper","Copper","Copper"],"from":"0/deck","to":"0/deck","pos":[7,0,6,0,0,4,0,0,0,0]}
{"seq":2,"type":"draw","player":0,"cards":["Estate","Copper","Estate","Copper","Copper"],"from":"0/deck","to":"0/hand"}
{"seq":3,"type":"shuffle","player":1,"cards":["Copper","Copper","Copper","Copper","Copper","Estate","Estate","Estate","Copper","Copper"],"from":"1/deck","to":"1/deck","pos":[0,0,0,0,0,2,2,2,0,0]}
{"seq":4,"type":"draw","player":1,"cards":["Copper","Copper","Copper","Copper","Copper"],"from":"1/deck","to":"1/hand"}
{"seq":5,"type":"turn","player":0,"number":1,"kind":"regular"}
{"seq":6,"by":5,"type":"phase","phase":"action"}
{"seq":7,"by":5,"type":"phase","phase":"buy"}
{"seq":8,"by":7,"type":"ask","seat":0,"prompt":"Buy phase: choose a move","kind":"turn","purpose":"turn","phase":"buy","min":1,"max":1,"options":[{"index":0,"group":0,"action":"play","label":"Play Copper","card":"Copper","zone":"hand"},{"index":1,"group":0,"action":"play","label":"Play Copper","card":"Copper","zone":"hand"},{"index":2,"group":0,"action":"play","label":"Play Copper","card":"Copper","zone":"hand"},{"index":3,"group":0,"action":"buy","label":"Buy Copper ($0)","card":"Copper","cost":{"coins":0}},{"index":4,"group":0,"action":"buy","label":"Buy Curse ($0)","card":"Curse","cost":{"coins":0}},{"index":5,"group":0,"action":"end-phase","label":"End your Buy phase"}]}
{"seq":9,"by":7,"type":"answer","seat":0,"indices":[1]}
{"seq":10,"by":7,"type":"play","player":0,"card":"Copper","from":"0/hand","to":"0/play"}
{"seq":11,"by":10,"type":"counter","counter":"coins","delta":1,"value":1}
{"seq":12,"by":7,"type":"ask","seat":0,"prompt":"Buy phase: choose a move","kind":"turn","purpose":"turn","phase":"buy","min":1,"max":1,"options":[…]}
{"seq":13,"by":7,"type":"answer","seat":0,"indices":[0]}
{"seq":14,"by":7,"type":"play","player":0,"card":"Copper","from":"0/hand","to":"0/play"}
{"seq":15,"by":14,"type":"counter","counter":"coins","delta":1,"value":2}
{"seq":16,"by":7,"type":"ask","seat":0,"prompt":"Buy phase: choose a move","kind":"turn","purpose":"turn","phase":"buy","min":1,"max":1,"options":[…]}
{"seq":17,"by":7,"type":"answer","seat":0,"indices":[0]}
{"seq":18,"by":7,"type":"play","player":0,"card":"Copper","from":"0/hand","to":"0/play"}
{"seq":19,"by":18,"type":"counter","counter":"coins","delta":1,"value":3}
{"seq":20,"by":7,"type":"ask","seat":0,"prompt":"Buy phase: choose a move","kind":"turn","purpose":"turn","phase":"buy","min":1,"max":1,"options":[…]}
{"seq":21,"by":7,"type":"answer","seat":0,"indices":[1]}
{"seq":22,"by":7,"type":"buy","player":0,"card":"Silver"}
{"seq":23,"by":22,"type":"counter","counter":"buys","delta":-1,"value":0}
{"seq":24,"by":22,"type":"counter","counter":"coins","delta":-3,"value":0}
{"seq":25,"by":22,"type":"counter","counter":"bought","delta":1,"value":1}
{"seq":26,"by":22,"type":"gain","player":0,"cards":["Silver"],"from":"pile/Silver","to":"0/discard"}
{"seq":27,"by":5,"type":"phase","phase":"night"}
{"seq":28,"by":5,"type":"phase","phase":"cleanup"}
{"seq":29,"by":28,"type":"discard","player":0,"cards":["Copper","Copper","Copper"],"from":"0/play","to":"0/discard"}
{"seq":30,"by":28,"type":"discard","player":0,"cards":["Estate","Estate"],"from":"0/hand","to":"0/discard"}
{"seq":31,"by":28,"type":"draw","player":0,"cards":["Estate","Copper","Copper","Copper","Copper"],"from":"0/deck","to":"0/hand"}
{"seq":32,"by":5,"type":"turn-end","player":0}
```

After the header, each line is one event. `seq` numbers the events from 0. `by` names the event this one
happened inside: Copper's +$1 (11) is inside its play (10), which is inside the Buy phase
(7), which is inside the turn (5). The setup table lists each deck in no particular order;
the shuffle at seq 1 says which order it is in afterwards. Ann is asked for a move (8) and
answers with option 1, a Copper to play (9); the play that follows is inside the Buy
phase, not inside her answer: questions and answers are no causes.

## The table

The table is everything the events describe. Its parts:

| Part | |
| --- | --- |
| `zones` | the cards in every zone |
| `faceUp` | of the cards in set-aside zones and `looking`, those lying face up |
| `counters` | every counter that is not 0 |
| `turn` | the turn in progress, if any |
| `effects` | the lasting effects |
| `extraTurns` | the extra turns waiting |
| `ending` | once the game's end condition is met: why, and the final round still to play |
| `ended` | once the game is over: the result |
| `piles` | every pile's properties |
| `landscapes`, `prophecy`, `holdings` | the landscapes and Artifacts in the game, its Prophecy, who holds each Project cube, Artifact and State |
| `tokens` | the players' tokens that are out |
| `notes` | public state a card keeps that has no other place |
| `costs`, `types` | derived values: what each card costs now, and types that are not the printed ones |

### Cards

A card is its **name**: `Copper`, `King's Court`, `The Sea's Gift`. A viewer who doesn't
see a card's face writes it `?`. In the full stream every face is seen, so `?` never
appears there.

Nothing numbers the physical copy. Copies of a card are interchangeable under the rules;
what can tell two copies apart is something attached to one, and the stream says each of
those where it applies: a card's position in an ordered zone (`pos`), the effect that
keeps or holds it (the effect's `id`), the way it lies in a set-aside zone (`face`,
`fromFace`), which of the cards trashed or discarded together an ability answers
(`index`).

Boons and Hexes are cards like any other: they lie in zones and move.

### Zones

A zone holds cards. There are two kinds:

- **Ordered**: a sequence of cards, top first.
- **Bag**: how many of each card, with no order. A bag is listed sorted: `?` first, then
  by name in Unicode code-point order (the byte order of the names in UTF-8). So
  `["Copper","Copper","Estate","Silver"]` is the only way to list that hand.

| Zone | Kind | |
| --- | --- | --- |
| `<seat>/deck` | ordered | |
| `<seat>/discard` | ordered | |
| `<seat>/hand` | bag | |
| `<seat>/play` | bag | the cards in play |
| `<seat>/aside` | bag, with faces | set aside |
| `<seat>/looking` | bag, with faces | taken off the deck to be looked at or revealed |
| `<seat>/tavern`, `<seat>/island`, `<seat>/native-village`, `<seat>/exile` | bag | mats |
| `<seat>/boons` | bag | Boons the player took and has not discarded: being received, taken by Fool, held by Blessed Village for later, kept until Clean-up (The Field's Gift) |
| `<seat>/hexes` | bag | a Hex the player turned over, while it is received (by them, or by each other player for an Attack) |
| `pile/<card>` | ordered | a pile, named after the card or randomizer it is named after; a later pile of the same name (one joining after Divine Wind removed the first) is `pile/<card> (2)`, then `(3)` |
| `aside/<card>` | ordered | cards set aside for the game that are no pile by the rules: the Black Market deck, Riverboat's and Way of the Mouse's cards. Named and numbered as piles are |
| `trash` | ordered | |
| `boons/deck`, `boons/discard` | ordered | the Boons' draw and discard piles |
| `boons/druid` | ordered | Druid's three Boons, set aside for the game |
| `hexes/deck`, `hexes/discard` | ordered | the Hexes' draw and discard piles |

`<seat>` is a player's index in turn order, from 0. A pile is never identified by
parsing its zone's name: `piles` says which card it is named after.

**Which zones exist.** A seat's zones, the trash and the Boons' and Hexes' zones always
exist; while empty they are left out of `zones`. A pile or `aside/<card>` zone exists
from the moment it is in the table (in `setup`, or by a `pile` or `add` event) and is
listed even when empty.

**Faces.** A seat's `aside` and `looking` zones are bags whose cards each lie face up
(everyone sees them) or face down (their owner may look at them). `faceUp` maps each such
zone to the bag of its cards that lie face up; the rest of the zone lies face down. A
zone with no face-up card is left out of `faceUp`. A card's face is said by the move
that brings it in (`face`) and the move that takes it out (`fromFace`); a card stops
being face up when it leaves the zone.

```json
"zones": {"0/aside": ["Copper", "Copper", "Gold"]},
"faceUp": {"0/aside": ["Copper"]}
```

### Counters

A counter is an integer, 0 unless an event says otherwise. It is keyed by **whose** it
is and **which** of theirs:

| Whose | Text form | Which |
| --- | --- | --- |
| the turn | `<name>` | `actions`, `buys`, `coins`, `potions`, `next-hand`, `bought`, `hand-plays` |
| the game | `<name>` | `trade-route-mat`, `sun` |
| a seat | `<seat>/<name>` | `coffers`, `villagers`, `favors`, `debt`, `vp-tokens`, `pirate-ship`, `sinister-plot`, `skip-turns`, `turns-skipped` |
| a pile | `<pile>/<name>` | `vp`, `debt`, `embargo`, `trade-route`, `favors` |
| a landscape | `landscape/<card>/<name>` | `vp` |

`<pile>` is the pile's zone (`pile/Village/embargo`). The text form is the encoding's;
in the model a counter key is the pair (whose, which). Which owner a bare name belongs
to follows from the name: the first seven are the turn's, `trade-route-mat` and `sun`
the game's.

| Counter | |
| --- | --- |
| `actions`, `buys`, `coins`, `potions` | the turn's Actions, Buys, $ and Potions |
| `next-hand` | how many cards this turn's Clean-up draws: 5, Outpost's 3, more with Expedition or Flag |
| `bought` | 1 once something (a card, Event or Project) has been bought in this Buy phase, which ends playing Treasures; returning to the Action phase sets it back to 0 |
| `hand-plays` | the plays from the hand this turn, in a turn whose `limits` has `handPlays` (Voyage's); 0 otherwise |
| `trade-route-mat` | the coin tokens on the Trade Route mat |
| `sun` | the Sun tokens on the Prophecy |
| `<seat>/coffers`, `/villagers`, `/favors`, `/debt`, `/vp-tokens` | the player's |
| `<seat>/pirate-ship` | coin tokens on their Pirate Ship mat |
| `<seat>/sinister-plot` | their tokens on Sinister Plot |
| `<seat>/skip-turns` | the next turns the player will skip (Lich): the next ones they would take, of any kind |
| `<seat>/turns-skipped` | the regular turns they have skipped, which count for the tiebreaker |
| `<pile>/vp`, `/debt`, `/embargo`, `/trade-route` | tokens on the pile |
| `<pile>/favors` | Family of Inventors' Favor tokens on the pile |
| `landscape/<card>/vp` | VP tokens on a Landmark |

The turn's counters exist only while a turn is in progress: `turn` sets them and
`turn-end` returns them to 0.

### The turn

The turn in progress, or none. There is none before the first turn and **between
turns**: from a `turn-end` to the next `turn`. Things happen between turns (Donate,
Mountain Pass, a player choosing which extra turn to take, turns skipped or lost, the end
condition being met), and none of them is part of a turn.

| Field | |
| --- | --- |
| `player` | whose turn it is |
| `number` | which of that player's turns, from 1, every kind counted |
| `kind` | `regular`; `extra` (given by a card; it doesn't count for the tiebreaker); `final` (one of the round played after the game has ended: Fleet) |
| `extra` | for an extra turn, the card that gave it |
| `phase` | `start`, `action`, `buy`, `night` or `cleanup` |
| `limits` | what this turn forbids beyond the rules of every turn: `noCardBuys` (Mission's turn: no buying cards; Events and Projects may still be bought) and `handPlays` (Voyage's: at most that many plays from the hand). Absent: nothing |

A turn is in `start` from its `turn` event to its first `phase` event. There is no phase
after Clean-up: `turn-end` ends the turn.

### Effects

An **effect** is anything that outlives the play that made it: a Duration's later part,
a "this turn" or "until your next turn" effect, a landscape's, Boon's or State's lasting
part. Every lasting thing the engine keeps is an effect, as it shows them to players,
including markers of a once-per-turn use spent (Alms, Borrow, Save, Pilgrimage bought this
turn; Fortune's doubling): they last until the end of the turn and are the table's record
that the use is spent. `effects` lists them by `id`, which is the order they began.

| Field | |
| --- | --- |
| `id` | names it from its `effect` event to its `effect-end` |
| `card` | the card, landscape, Boon or State it is of, by name |
| `source` | the card it came from, when a card made it: the card played (a Way's effect is the Way's, its source the card played), the Estate playing an inherited card |
| `owner` | a seat |
| `until` | when it ends, as its players are told: `end-of-turn`; `start-of-turn` of a seat; `extra-turn` (when the extra turn it keeps its card in play for starts or doesn't happen); `removed` (when something it waits for happens) |
| `ending` | its card has left play: it still works this turn and ends with it |
| `keeps` | a bag of its owner's play area: the cards it keeps in play past Clean-up |
| `holds` | a bag of its owner's set-aside zone: the cards it holds set aside |
| `faceUp` | a bag: of `holds`, those lying face up |
| `tokens` | how many tokens lie on its card (Garrison) |

Two effects can keep the same card: Throne Room played on Wharf makes two Wharf effects,
each keeping Throne Room and Wharf ([an example](#throne-room-on-wharf)), and the cards
stay in play while either is pending. So the `keeps` of different effects may overlap: a
reader must not add them up to count the cards kept in play. A card that no
effect keeps or holds is not marked: when a copy an effect keeps leaves play, that
effect changes (`effect-change` with fewer `keeps`, or `ending`); when a copy of the same
name that no effect keeps leaves, no effect changes.

`faceUp` is needed beside the zone's own `faceUp`: when cards of one name lie both ways in
a set-aside zone and an effect holds one of them, the zone alone doesn't say whose is the
face-up one.

```json
{"id":12,"card":"Quartermaster","source":"Quartermaster","owner":0,"until":"removed","keeps":["Quartermaster"],"holds":["Copper","Silver"],"faceUp":["Copper","Silver"]}
```

A card set aside that no effect holds belongs to the play in progress that set it aside
(Library) or, in an `aside/<card>` zone, to the card that set it aside for the game.

### Extra turns waiting

`extraTurns` lists the extra turns waiting, in the order the engine keeps them (after the
others, unless queued at the front: Island Folk). Each has:

| Field | |
| --- | --- |
| `id` | names it from its `extra-turn` event until it is taken, skipped, lost or removed |
| `player` | whose |
| `card` | the card that gave it |
| `limit` | `third-in-a-row`: it is lost if it would be that player's third turn in a row, decided when it is up next; `none`: it always happens (Seize the Day) |
| `effect` | the effect keeping its card in play for it (Outpost, Voyage), if any |

Two can wait for one player from the same card, each with its own effect; which one is
lost decides which card is released. After each turn, extra turns are taken in turn order
from the player of the most recent regular turn, and a player with extra turns from
different cards chooses which first. The stream records the outcome (`turn`,
`turn-skipped`); a reader needs no part of this rule.

### The game ending

- `ending` is set when the end condition is met: `reason` (`provinces`, `colonies`,
  `piles` or `turn-limit`) and `finalRound`, the seats still to take a turn of the round
  after the game's end (Fleet), in order. Each turn of that round, taken or skipped,
  removes its seat from the front.
- `ended` is set when the game is over: `reason` (as above, or `resigned`) and `result`,
  per seat: `seat`, `vp`, `turns` (the turns that count for the tiebreaker: regular turns,
  taken or skipped; extra turns and the final round's don't), `rank` (from 1; a seat that resigned ranks below every seat that
  didn't, then more VP, then fewer turns; ties share a rank) and `resigned`.

### Piles

`piles` gives every pile's properties by its zone, `aside/<card>` zones included. A pile
is listed from the moment the game has it.

| Field | |
| --- | --- |
| `card` | the card or randomizer it is named after. Its types are the pile's types, whatever it holds now |
| `supply` | it is in the Supply |
| `hidden` | it lies face down: not even its top card is public (the Black Market deck) |
| `removed` | it is out of the game (Divine Wind): no card's pile any more, though its cards and Traits are still its own |
| `roles` | what setup made it for, each `{card, role}`: `bane` (Young Witch's), `extra-pile` (Ferryman's), `chosen-pile` (Obelisk's), `set-aside` (Riverboat's and Way of the Mouse's card), `deck` (the Black Market deck: contents public, order not) |
| `traits` | the Traits on it |
| `recipe` | what it was made of in setup, never what it holds now: `kind` (`stacked`: groups one on another, top first; `rotating`: groups whose top cards go to the bottom; `shuffled`: a pool shuffled together), `cards` (`{card, count}` groups), and `sample` (how many of a shuffled pool it took, when only some) |

```json
"pile/Will-o'-Wisp": {"card": "Will-o'-Wisp", "recipe": {"kind": "stacked", "cards": [{"card": "Will-o'-Wisp", "count": 12}]}}
```

### Landscapes, the Prophecy and holdings

- `landscapes`: every landscape (Event, Landmark, Project, Way, Ally, Trait, Prophecy) and
  Artifact in the game, sorted by name in code-point order.
- `prophecy`: the game's Prophecy. It is in effect while the `sun` counter is 0.
- `holdings`: who holds each Project (has a cube on it), Artifact and State, by name, as
  a sorted list of seats. A name nobody holds is left out. Kept Boons are in
  `<seat>/boons`, not here.

### Tokens

`tokens` lists each player's tokens that are **out**, each `{player, token, at}`, ordered
by player, then by token in the order of this table:

| `token` | | `at` when listed | Not listed |
| --- | --- | --- | --- |
| `plus-card`, `plus-action`, `plus-buy`, `plus-coin`, `minus-cost`, `trashing`, `estate` | Adventures tokens | a pile's zone; or `player`, on no pile (the Estate token on Inheritance's card, a token whose pile left the game) | not placed yet |
| `minus-card` | the −1 Card token | `player`: on their deck | they don't have it |
| `minus-coin` | the −$1 token | `player`: in front of them | they don't have it |
| `journey` | the Journey token | `face-down` | face up |

### Notes

`notes`: public state a card or landscape keeps that has no other place on the table,
each with `source` (the card or landscape) and as applicable `player`, `pile` (a pile's
zone), `card` and `count`. Examples: the card each player set aside with Inheritance
(`{"source": "Inheritance", "player": 1, "card": "Village"}`), Invest's Exiled cards.
What has a place elsewhere is not a note: Druid's Boons are in `boons/druid`, a Bane is a
pile's role, Fleet's final round is `ending`.

### Derived values

What the rules make of the table rather than things on it. A reader with a rules engine
would compute them; they are in the table so a reader without one has them.

- `costs`: what each card in the game costs now, by name: `coins`, `potions`, `debt`.
  Every name some card in the game has is listed. Events and Projects are not: they never
  change.
- `types`: a card's types, by name, while they are not its printed types (Charlatan's
  Curses, Capitalism's Actions, Enlightenment's Treasures).

VP is not given: a running score says too much about cards a viewer can't see
(Masquerade).

## Reading a stream

A stream is a **header**, then events in order.

The header:

| Field | |
| --- | --- |
| `schema` | `dominion/events@1` |
| `viewer` | whose eyes the stream is written for: `full` (every face, every shuffle's order); later `public` or a seat |
| `game` | the game's id where it has one (Arena's `g12`); optional |

Each event has:

| Field | |
| --- | --- |
| `seq` | its position, from 0, with none missing: the fold refuses any other |
| `by` | optional: the event it happened inside ([Causes](#causes)) |
| `type` | what kind of event it is; its other fields depend on it |

The first event is `setup`, which gives the whole table before anything happens; it
comes only first. Each
later event changes the table as its section below says, or changes nothing (most
occurrences). Applying them in order is **the fold**.

### Three kinds of events

- **Occurrences**: something the rules have a name for happens: a turn begins, a phase
  begins, the turn ends, a card is played, something is bought, an ability resolves, a
  Boon or Hex is received, a card is gained, trashed or discarded, a deck is shuffled.
  They say *why*. Other events happen inside them.
- **Changes**: the table changes: cards move, a counter changes, an effect begins. They
  say *what*.
- **Inputs**: what the rules don't decide: a seat is asked something (`ask`), the seat
  answers (`answer`), chance decides something no `shuffle` shows (`chance`). They say
  *what decided* the game. They change nothing on the table, and nothing happens inside
  them ([Questions, answers and chance](#questions-answers-and-chance)).

A `play`, `gain`, `trash`, `discard` and `shuffle` are both occurrences and changes: they
move cards, and other events happen inside them. A `shuffle` also records a chance
outcome: its `cards`.

### Causes

Every event but `setup` may carry `by`: the `seq` of the **occurrence it happened
inside**. It is always earlier than the event, and an occurrence.

Only these are causes, with what happens inside each:

| Occurrence | What happens inside it |
| --- | --- |
| `turn` | its phases and its `turn-end`; the abilities that resolve at its start; effects that end as it starts (`effect-end`, `expired`); costs that change with it (`derived`) |
| `phase` | the moves its player makes (plays, buys, Coffers, Villagers, paying Debt); abilities at its start; Clean-up's discards and draw, and the −1 Card token that draw uses up |
| `turn-end` | what ends with the turn: effects ending (`expired`, `left-play`), extra turns removed with them, Boons kept until Clean-up discarded, costs changing back |
| `receive` | what a Boon or Hex received does: its +$, its moves, the effect it makes |
| `play` | the Action it costs, the card's bonuses and instructions, its Way, the Reactions to it, the plays it makes (Throne Room's of the card it chose) |
| `buy` | its price (the Buy, $, Potions, Debt, `bought`), overpaying, on-buy abilities, the gain of the card bought, what a bought Event or Project does (its cube's `holding`, a token it moves, the effect or extra turn it makes) |
| `resolve` | what the ability does, `unaffected` included |
| `gain`, `trash`, `discard` | the abilities that answer it ("when you gain / trash / discard") and what the rules attach to it (the Trade Route token moving with a gain) |
| `shuffle` | the cards put at the bottom of the deck as it is shuffled; "when you shuffle" abilities |

`by` is the innermost occurrence still in progress, not the previous event: a draw three
events after a play can name it. So `by` makes a tree of what happened inside what, and a
reader that indents a log by `by` gets the right indentation. Every event from a `turn`
to its `turn-end`, and what ends with it, leads back to that `turn` by following `by`;
`by` never leaves the turn in progress.

**Events with no `by`.** Between turns nothing is inside a turn: `turn`, `turn-skipped`, a
`choose` of which extra turn to take, `game-ending`, `game-end`, the `effect-end`
(`extra-turn`) of the effect an extra turn kept its card in play for as that turn is
taken, skipped or lost, and the counters a skipped turn changes have no `by`. An ability
that resolves between turns is a `resolve` with no `by`, and what it does names it.
Before the first turn the opening shuffles and draws have no `by`; what an ability at
the start of the game does (Inherited) names its `resolve`.

**Inputs are never causes.** An `ask`, `answer` or `chance` has as `by` the occurrence in
progress when it came, like any event: the `play` or `resolve` whose card asks, the
`phase` for a move, the `play` whose removal of the last Sun drew Divine Wind's Kingdom;
none between turns. But they are no occurrences, so no event names one in `by`: what
follows an answer happens inside the occurrence that asked.

**The other state** is read as counters are, so a change to it names the occurrence it
happened in: an `effect` names the `play`, `resolve`, `buy` or `receive` that made it; an
`effect-change` or `effect-end` (`resolved`) what changed or ended it; a `token` moved by
an Event names the `buy`, one moved by an ability the `resolve`; a `holding` names the
`buy` of a Project, the `play`, `gain` or `resolve` that took an Artifact, the `receive`
of the Hex that gave a State; a `take` names what turned the Boon or Hex over (the `play`
or `resolve` receiving it), the Boon's `discard` its `receive`; `pile`, `landscape`,
`notes` and `derived` name whatever was in progress. An `extra-turn` names the `play`,
`resolve` or `buy` that queued it.

**Costs inside their occurrence.** The Action a card played from the Action phase costs
is a `counter` (`actions`, −1) right after the `play`, by it; a card played by another
card costs none. A `buy`'s price is its own `counter` events, by the `buy`, before
anything else the buy causes. They are never netted with what follows: Village's −1 and
+2 Actions are two `counter` events.

**A phase's cause.** A phase the turn moves on to has `by` = the `turn`; a phase an effect
returns the turn to (Villa, Cavalry) has `by` = that effect's `resolve`. `turn-end` has
`by` = the `turn`, not its Clean-up.

**Two pointers for a lasting effect's ability.** A Duration's later part answers one
thing and belongs to another. Its `resolve`'s `by` is the moment it answers (the `turn`),
which keeps `by` a tree turn by turn. Its `origin` is the occurrence that made the
effect it belongs to (the Duration's `play`, possibly turns ago). An extra turn's `turn`
has no `by`; it names the `extra-turn` that entitled it in `extraTurn`, and that event's
`by` is what queued it.

### One event per occurrence

A move event is exactly one occurrence, or cards moved together within one. Cards moving
the same way one after the other are one event only if they have the same cause and no
occurrence among them is over before the next card moves:

- Two gains are two `gain` events, even of one card from one pile by one play: each is
  its own occurrence, over (its "when you gain" abilities resolved) before the next
  begins. A `gain` is always one card.
- Cards trashed or discarded together by one effect (Chapel's, a hand discarded to
  Militia) are one `trash` or `discard`: they are all moved before any of their abilities
  resolve. Each card is still its own occurrence; an ability answering one says which by
  `about` and `index`. Only a `resolve` happens directly inside such an event.
- Moves that are no occurrence (a draw, a top-deck, a reveal, a set-aside, a look) are one
  event when adjacent with the same cause: cards drawn by one draw are one `draw`, and so
  are two draws of one play with nothing between them.
- Moves with different causes are different events even when adjacent: Clean-up's discard
  from play and an ability's discard.

Moves of the same kind with different `player`, `from`, `to`, `at`, `face` or `fromFace`
are different events.

### When a stream is not one game's

The fold **refuses** an event that can't apply to the table it has: the stream is then not
one game's. A refused event changes nothing: the table is as it was before it. The
refusals are given with each event; together they are:

- A `seq` other than the one after the last event's (0 for the first).
- A first event that is no `setup`, or a `setup` after the first.
- Any event after `game-end`.
- `by` or `origin` not earlier than the event, or naming an event that is no occurrence.
- A move that names a card that isn't where it says ([Taking and placing](#taking-and-placing)),
  into a zone that doesn't exist, under more cards than there are, at a position in a bag,
  with a `pos` list of the wrong length, or a `shuffle` into a bag.
- A `play` with `from` and no `to`, or `to` and no `from`.
- A `rename` of a card not where it says.
- A `counter` whose `value` isn't its old value plus `delta`, or on a pile not in `piles`.
- A `phase` with no turn in progress; a `turn-end` of a seat whose turn is not in progress.
- A `turn` or `turn-skipped` while a turn is in progress (no `turn-end` since the last
  `turn`); of kind `extra` naming no extra turn, or one that isn't waiting or is another
  seat's; naming an extra turn when it is of another kind; a `final` one for a seat that
  is not first in `finalRound`.
- An `effect` whose `id` has begun already; an `effect-change` or `effect-end` of an
  effect not on the table.
- An `extra-turn` whose `id` is waiting already; an `extra-turn-removed` of one not
  waiting.
- A `token` placed on a pile not in `piles`.
- A `holding` from a seat that doesn't hold the card, to a seat that already holds it, or
  with neither.

An `ask`, `answer` or `chance` is refused only by the first four: in the wrong place.
The fold doesn't hold an `answer` to its `ask` (right after it, from the seat asked,
indices among its options) nor a `chance` record to anything: [replay](#replay) does.

To refuse an event out of place, a fold keeps where it is in its stream: the `seq` the
next event must have, and which events so far were occurrences. That is no part of the
table: two tables are equal whatever it says, and `setup`'s table never carries it.

The fold checks that a stream can be one game's, not that it is the game the rules
would make: that `by` is the innermost occurrence in progress, that a card moved is the
one the rules move, that the table's derived values are right. `dominion-engine`'s tests
hold its streams to those.

## Events

| Group | Types |
| --- | --- |
| [Beginnings and ends](#beginnings-and-ends) | `setup`, `turn`, `phase`, `turn-end`, `turn-skipped`, `game-ending`, `game-end` |
| [Occurrences](#occurrences) | `play`, `buy`, `resolve`, `receive`, `name`, `way`, `unaffected`, `call`, `choose` |
| [Moves](#moves) | `draw`, `discard`, `gain`, `trash`, `topdeck`, `bottomdeck`, `insert`, `reveal`, `look`, `set-aside`, `exile`, `put`, `return`, `exchange`, `pass`, `rotate`, `take`, `shuffle` |
| [Cards entering and changing](#cards-entering-and-changing) | `add`, `rename` |
| [The table's other changes](#the-tables-other-changes) | `counter`, `effect`, `effect-change`, `effect-end`, `extra-turn`, `extra-turn-removed`, `token`, `holding`, `pile`, `landscape`, `notes`, `derived` |
| [Questions, answers and chance](#questions-answers-and-chance) | `ask`, `answer`, `chance` |

`player` in an event is a seat. A `card` given as a plain name in an occurrence (`buy`,
`resolve`, `receive`, ...) names a card, landscape, Boon or State; it is never `?`.

### Beginnings and ends

#### `setup`

The first event: the game before anything happens.

| Field | |
| --- | --- |
| `rules` | `implementation` and `version`: what decided this game (`dominion-engine`, `0.1.0`) |
| `seats` | the players' names, in turn order |
| `kingdom` | the Kingdom cards, by name |
| `landscapes` | the landscapes in the game, by name: those given (`config.landscapes`) and an Ally or Prophecy setup added at random; absent when none (the table's `landscapes` also has the Artifacts) |
| `table` | the whole table |
| `config` | what the game was set up from besides `seats` and `kingdom` (below). Absent from a stream recorded before it was written: such a stream can be folded, not replayed |
| `chance` | every chance outcome setup drew that no `shuffle` shows, in the order drawn, each a [`chance` record](#chance); absent when none |

**Fold:** the table becomes `table`. Refused unless it is the stream's first event.
`config` and `chance` change nothing.

The setup table has every pile with its cards, properties and costs, the Boons' and
Hexes' zones, and each player's starting cards in their deck, listed by name before they
are shuffled. The opening shuffle and draw of each player follow as events, with no `by`.

`config`:

| Field | |
| --- | --- |
| `landscapes` | the landscapes given. Setup may add more (an Ally or Prophecy at random: a `chance` record); `setup.landscapes` is all of them |
| `colonies` | Platinum and Colony are in the game, as setup decided (given, or from a random Kingdom card) |
| `shelters` | Shelters replace the starting Estates, as setup decided |
| `turnLimit` | the game ends once this many turns have been taken in all; absent: no limit |
| `choices` | choices setup makes that were given rather than drawn, by the card making them: `{"Young Witch": ["Moat"]}`. A given choice may be a card no random choice would make (a card removed in a second edition) |
| `seed` | the engine's seed. It reproduces the chance outcomes only in the build that drew them; replay needs it nowhere |

Colonies and Shelters decided at random and a Kingdom dealt from randomizers are not
`chance` records: `colonies`, `shelters`, `kingdom` and `config.landscapes` are what was
decided.

The setup of [`inherited.events.jsonl`](examples/events/inherited.events.jsonl), its table
trimmed: setup decided on Shelters (it drew a Dark Ages card), shuffled the Ruins pile,
and chose at random Grotto's as the pile the Trait Inherited goes on:

```json
{"seq":0,"type":"setup","rules":{"implementation":"dominion-engine","version":"0.1.0"},"seats":["Ann","Bo"],"kingdom":["Hermit","Rats","Marauder","Fortress","Procession","Quartermaster","Grotto","Village","Smithy","Market"],"landscapes":["Inherited"],"table":{…},"config":{"landscapes":["Inherited"],"colonies":false,"shelters":true,"turnLimit":20,"seed":1},"chance":[{"site":"pile","card":"Ruins","cards":["Ruined Village","Survivors","Ruined Market","Ruined Library","Survivors","Ruined Village","Ruined Village","Ruined Village","Survivors","Ruined Market"]},{"site":"choice","card":"Inherited","cards":["Grotto"]}]}
```

#### `turn`

A turn begins. `player`, `number`, `kind`, and as applicable:

| Field | |
| --- | --- |
| `extra` | for an extra turn, the card that gave it |
| `extraTurn` | for an extra turn, the `id` of the extra turn waiting it is |
| `limits` | what the turn forbids, when anything |

**Fold:** refused while a turn is in progress. If `extraTurn` is given, that extra turn
leaves `extraTurns` (refused if it isn't waiting or is another seat's; `extraTurn` is
given exactly when `kind` is `extra`). A `final` turn removes `player` from the front of
`ending.finalRound` (refused unless it is there). Then the turn in progress is `player`,
`number`, `kind`, `extra`, `limits`, in phase `start`, and the turn's counters are set:
`actions` 1, `buys` 1, `coins` 0, `potions` 0, `next-hand` 5, `bought` 0, `hand-plays` 0.

A `turn` has no `by`.

#### `phase`

`phase`: `action`, `buy`, `night` or `cleanup`. Every phase is written as it begins, in
order, also when nothing happens in it (the Night phase of a game without Night cards). A
phase can come again: a turn that returns to its Action phase (Villa, Cavalry) has a
second `action` and a second `buy`. The `start` phase is the `turn` event itself and is
not written.

**Fold:** the turn's phase becomes `phase`. Refused with no turn in progress.

#### `turn-end`

`player`: their turn is over.

**Fold:** refused unless `player`'s turn is in progress. The table has no turn, and the
turn's counters are 0.

What ends "at the end of the turn" ends after it, inside it (`effect-end` with `expired`),
as do effects whose card left play (`left-play`) and the extra turns removed with them.
Abilities "at the end of this turn" (Squirrel, Island Folk, Coastal Haven) resolve before
it, in Clean-up.

#### `turn-skipped`

A turn a player would have taken doesn't happen. `player`, `kind`, and as applicable
`extra` and `extraTurn` (as for `turn`), and `lost` when an extra turn is lost as a third
turn in a row.

**Fold:** as `turn` for a turn in progress, `extraTurn` and a `final` turn; the turn in
progress and its counters don't change.

A turn skipped by Lich lowers its player's `skip-turns` before this event, and a regular
one raises `turns-skipped`; those `counter` events have no `by`. A skipped turn has no
phases and no `turn-end`.

#### `game-ending`

The end condition is met. `reason`, and `finalRound` when the round after the game's end
is to be played (Fleet).

**Fold:** `ending` becomes `{reason, finalRound}`.

Written between turns, after the turn that met it. A `turn-limit` end never has a final
round. Extra turns still go before the turns of the final round.

#### `game-end`

The game is over. `reason` and `result` ([The game ending](#the-game-ending)).

**Fold:** `ended` becomes `{reason, result}`. It is the last event: the fold refuses any
after it.

After a `game-ending` it comes once `finalRound` is empty and no extra turn comes first.
A resignation is `game-end` alone, with reason `resigned`, wherever the game waits: right
after an `ask` that gets no answer. The turn in progress, its effects and the extra turns
waiting stay on the table as they were. Extra turns still waiting when the game ends
normally are never taken; they stay too.

The end of [`outpost-fleet.events.jsonl`](examples/events/outpost-fleet.events.jsonl):
Bo's turn takes the last Province, and Ann, who has Fleet, takes one turn more.

```jsonl
{"seq":2193,"by":2141,"type":"turn-end","player":1}
{"seq":2194,"type":"game-ending","reason":"provinces","finalRound":[0]}
{"seq":2195,"type":"turn","player":0,"number":27,"kind":"final"}
{"seq":2196,"by":2195,"type":"resolve","player":0,"card":"Haven","when":"start-turn","origin":2091}
…
{"seq":2236,"by":2195,"type":"turn-end","player":0}
{"seq":2237,"type":"game-end","reason":"provinces","result":[{"seat":0,"vp":9,"turns":26,"rank":2},{"seat":1,"vp":42,"turns":26,"rank":1}]}
```

### Occurrences

These change nothing on the table, except a `play` that moves its card. Other events
happen inside them ([Causes](#causes)).

#### `play`

A card is played: its instructions are followed. `player`, `card`, and when it goes into
play as it is played, `from` and `to` (and `pos` for an ordered `from`, `fromFace` for a
zone with faces, as for a move). Without `from` and `to` it moves nowhere: a card played
again (Throne Room's second play), or played where it lies (Necromancer plays a card that
stays in the trash).

**Fold:** with `from` and `to`, the card moves as a one-card `put` would. Refused with one
of `from`, `to` and not the other.

A card played twice is two `play` events: Throne Room's plays of the card it chose each
have `by` = Throne Room's `play`, and what each does names its own play. A card played
by another card costs no Action. Reckless's "follow its instructions twice" is one play,
by the rules: one `play` whose instructions run twice.

##### Throne Room on Wharf

From [`throne-room-wharf.events.jsonl`](examples/events/throne-room-wharf.events.jsonl):

```jsonl
{"seq":870,"by":867,"type":"play","player":1,"card":"Throne Room","from":"1/hand","to":"1/play"}
{"seq":871,"by":870,"type":"counter","counter":"actions","delta":-1,"value":0}
{"seq":872,"by":870,"type":"ask","seat":1,"prompt":"Throne Room: choose up to 1 card to play","kind":"cards","purpose":"play","source":"Throne Room","min":0,"max":1,"options":[…]}
{"seq":873,"by":870,"type":"answer","seat":1,"indices":[0]}
{"seq":874,"by":870,"type":"play","player":1,"card":"Wharf","from":"1/hand","to":"1/play"}
{"seq":875,"by":874,"type":"counter","counter":"buys","delta":1,"value":2}
{"seq":876,"by":874,"type":"draw","player":1,"cards":["Copper","Militia"],"from":"1/deck","to":"1/hand"}
{"seq":877,"by":874,"type":"effect","id":2,"card":"Wharf","source":"Wharf","owner":1,"until":{"start-of-turn":1},"keeps":["Throne Room","Wharf"]}
{"seq":878,"by":870,"type":"play","player":1,"card":"Wharf"}
{"seq":879,"by":878,"type":"counter","counter":"buys","delta":1,"value":3}
{"seq":880,"by":878,"type":"draw","player":1,"cards":["Estate","Copper"],"from":"1/deck","to":"1/hand"}
{"seq":881,"by":878,"type":"effect","id":3,"card":"Wharf","source":"Wharf","owner":1,"until":{"start-of-turn":1},"keeps":["Throne Room","Wharf"]}
…
{"seq":947,"type":"turn","player":1,"number":14,"kind":"regular"}
{"seq":948,"by":947,"type":"resolve","player":1,"card":"Wharf","when":"start-turn","origin":874}
{"seq":949,"by":948,"type":"effect-end","id":2,"why":"resolved"}
{"seq":950,"by":948,"type":"counter","counter":"buys","delta":1,"value":2}
{"seq":951,"by":948,"type":"draw","player":1,"cards":["Estate","Copper"],"from":"1/deck","to":"1/hand"}
{"seq":952,"by":947,"type":"resolve","player":1,"card":"Wharf","when":"start-turn","origin":878}
{"seq":953,"by":952,"type":"effect-end","id":3,"why":"resolved"}
{"seq":954,"by":952,"type":"counter","counter":"buys","delta":1,"value":3}
{"seq":955,"by":952,"type":"draw","player":1,"cards":["Copper","Silver"],"from":"1/deck","to":"1/hand"}
{"seq":956,"by":947,"type":"phase","phase":"action"}
```

The second play of Wharf (878) moves nothing. Each play makes its own effect, which keeps
both cards in play through Clean-up. At the next turn the two abilities have the same
`by` (the `turn`) and different `origin`s: the two plays.

#### `buy`

`player`, `card`: a card, Event or Project is bought: paid for, before it is gained or
does anything. `card` is a name: what is bought is a card of that name, not one copy
(an on-buy ability may gain the copy that was on top).

Inside it: the price (`buys` −1, `coins`, `potions`, `debt`, `bought`), overpaying,
on-buy abilities, then the `gain` of the card, or what the Event or Project does:

```jsonl
{"seq":82,"by":67,"type":"buy","player":0,"card":"Pageant"}
{"seq":83,"by":82,"type":"counter","counter":"buys","delta":-1,"value":0}
{"seq":84,"by":82,"type":"counter","counter":"coins","delta":-3,"value":0}
{"seq":85,"by":82,"type":"counter","counter":"bought","delta":1,"value":1}
{"seq":86,"by":82,"type":"holding","card":"Pageant","to":0}
```

#### `resolve`

An ability of `card` begins to resolve for `player`, answering the moment `when`. Every
triggered ability that resolves has one, whether or not it then does anything, including
bookkeeping ones nothing can interact with (Goons' +1 VP).

| Field | |
| --- | --- |
| `player`, `card` | whose ability, and the card (or landscape, State, ...) it is of |
| `when` | the moment it answers (below) |
| `about` | the card the moment is about: the card gained, about to be gained, trashed, discarded, bought, or that left a Supply pile |
| `index` | when `by` is cards trashed or discarded together: which of its `cards` this answers, from 0 |
| `target` | for `attack`: the player the Attack is played against |
| `origin` | the `seq` of the occurrence that made the lasting effect the ability belongs to: the `play` of a Duration, the `resolve`, `buy` or `receive` that made a "this turn" effect. Absent for an ability of a card that isn't a lasting effect (a card being gained, a Reaction in hand) |

`when`, and what `by` is for each:

| `when` | | `by` |
| --- | --- | --- |
| `game-start` | before the first turn | none |
| `start-turn` | | the `turn` |
| `start-buy-phase`, `start-night`, `start-cleanup` | | the `phase` |
| `end-buy-phase` | as the Buy phase ends, before the next phase | the Buy `phase`, or the `resolve` returning to the Action phase (Villa) |
| `discard-from-play` | before cards are discarded from play | the Clean-up `phase`; outside Clean-up, what discards the cards (Highwayman) |
| `end-turn` | after Clean-up's draw | the Clean-up `phase` |
| `play` | a card is played, before its instructions | the `play` |
| `after-play` | its instructions have been followed | the `play` |
| `attack` | an Attack is played against `target` | the Attack's `play` |
| `buy` | a card, Event or Project is bought | the `buy` |
| `would-gain` | a card is about to be gained: it may not be (a replacement can cancel it) | what is gaining it (a `play`, `buy`, `resolve`) |
| `gain`, `trash`, `discard` | | the `gain`, `trash` or `discard` holding `about` |
| `leave-supply` | a card left a Supply pile other than by being gained or trashed (Exiled, set aside) | what took it out |
| `would-shuffle` | a discard pile is about to be shuffled | what needs the shuffle (a `play`'s draw, Clean-up's) |
| `shuffle` | | the `shuffle` |

A moment that comes before the thing it answers names in `by` the occurrence in
progress, and `when` says which moment of it.

`about` is a card's name. A `gain` is one card, so a `resolve` answering one has no
`index`; one answering cards trashed or discarded together has `index` when that event
moved more than one card. A `target`'s `resolve` has the attacked player as `player` when
it is their Reaction; an ability another player resolves in the same window has its own
`player` and the same `target`.

A Moat against Militia, from [`moat-chapel.events.jsonl`](examples/events/moat-chapel.events.jsonl):

```jsonl
{"seq":876,"by":873,"type":"play","player":0,"card":"Militia","from":"0/hand","to":"0/play"}
{"seq":877,"by":876,"type":"counter","counter":"actions","delta":-1,"value":0}
{"seq":878,"by":876,"type":"ask","seat":1,"prompt":"Ann attacks you with Militia: you may use this ability","kind":"choose","purpose":"trigger","min":1,"max":1,"options":[…]}
{"seq":879,"by":876,"type":"answer","seat":1,"indices":[0]}
{"seq":880,"by":876,"type":"resolve","player":1,"card":"Moat","when":"attack","target":1}
{"seq":881,"by":880,"type":"unaffected","player":1,"attack":"Militia","card":"Moat"}
{"seq":882,"by":876,"type":"counter","counter":"coins","delta":2,"value":2}
```

Chapel trashing four cards, one of them Fortress, from the same game:

```jsonl
{"seq":1076,"by":1065,"type":"play","player":0,"card":"Chapel","from":"0/hand","to":"0/play"}
{"seq":1077,"by":1076,"type":"counter","counter":"actions","delta":-1,"value":0}
{"seq":1078,"by":1076,"type":"ask","seat":0,"prompt":"Chapel: choose up to 4 cards to trash","kind":"cards","purpose":"trash","source":"Chapel","min":0,"max":4,"options":[…]}
{"seq":1079,"by":1076,"type":"answer","seat":0,"indices":[2,3,1,4]}
{"seq":1080,"by":1076,"type":"trash","player":0,"cards":["Militia","Copper","Fortress","Silver"],"from":"0/hand","to":"trash"}
{"seq":1081,"by":1080,"type":"resolve","player":0,"card":"Fortress","when":"trash","about":"Fortress","index":2}
{"seq":1082,"by":1081,"type":"put","player":0,"cards":["Fortress"],"from":"trash","to":"0/hand","pos":[1]}
```

The four cards went onto the trash one after the other, so Silver lies on Fortress: it
leaves from under one card (`pos` 1).

An effect's own ability that removes the effect gives `effect-end` (`resolved`) right
after its `resolve`, before what it does: Haven's ability ends Haven's effect, then puts
the card into the hand ([Moves](#set-aside-cards-and-faces)).

#### `receive`

`player`, `card`: `player` receives a Boon or Hex (its instructions are followed), takes
a State or Artifact, or the Prophecy comes into effect for them. One Hex received by each
other player is one `take` and one `receive` per player.

Everything a Boon or Hex received does is inside its `receive`. A `receive` of a State or
Artifact taken, or of the Prophecy, holds nothing: the `holding` that goes with it names
the occurrence in progress. A Boon or Hex that its card discards itself (a Hex received
by each other player is discarded once all have) has that `discard` named by the card's
`play`. Druid's Boons are received where they lie: a `receive` with no move.

Bard's Boon and Skulk's Hex, from [`boons-hexes.events.jsonl`](examples/events/boons-hexes.events.jsonl):

```jsonl
{"seq":243,"by":240,"type":"play","player":1,"card":"Bard","from":"1/hand","to":"1/play"}
{"seq":244,"by":243,"type":"counter","counter":"actions","delta":-1,"value":0}
{"seq":245,"by":243,"type":"counter","counter":"coins","delta":2,"value":2}
{"seq":246,"by":243,"type":"take","player":1,"cards":["The Sky's Gift"],"from":"boons/deck","to":"1/boons"}
{"seq":247,"by":243,"type":"receive","player":1,"card":"The Sky's Gift"}
{"seq":248,"by":247,"type":"ask","seat":1,"prompt":"The Sky's Gift: discard 3 cards to gain a Gold?","kind":"choose","purpose":"discard","source":"The Sky's Gift","min":1,"max":1,"options":[…]}
{"seq":249,"by":247,"type":"answer","seat":1,"indices":[1]}
{"seq":250,"by":247,"type":"discard","player":1,"cards":["The Sky's Gift"],"from":"1/boons","to":"boons/discard"}
…
{"seq":406,"by":403,"type":"play","player":1,"card":"Skulk","from":"1/hand","to":"1/play"}
{"seq":407,"by":406,"type":"counter","counter":"actions","delta":-1,"value":0}
{"seq":408,"by":406,"type":"counter","counter":"buys","delta":1,"value":2}
{"seq":409,"by":406,"type":"take","player":1,"cards":["Haunting"],"from":"hexes/deck","to":"1/hexes"}
{"seq":410,"by":406,"type":"receive","player":0,"card":"Haunting"}
{"seq":411,"by":410,"type":"ask","seat":0,"prompt":"Haunting: choose a card to put onto your deck","kind":"cards","purpose":"top-deck","source":"Haunting","min":1,"max":1,"options":[…]}
{"seq":412,"by":410,"type":"answer","seat":0,"indices":[4]}
{"seq":413,"by":410,"type":"topdeck","player":0,"cards":["Copper"],"from":"0/hand","to":"0/deck"}
{"seq":414,"by":406,"type":"discard","player":1,"cards":["Haunting"],"from":"1/hexes","to":"hexes/discard"}
```

#### `name`, `way`, `unaffected`, `call`, `choose`

| Type | Fields | |
| --- | --- | --- |
| `name` | `player`, `card` | `player` names a card |
| `way` | `player`, `card`, `way` | `player` plays `card` using the Way `way` instead of following its instructions |
| `unaffected` | `player`, `attack`, `card` | the Attack `attack` doesn't affect `player`, because of `card` |
| `call` | `player`, `card` | `player` calls `card` from their Tavern mat |
| `choose` | `player`, `source`, `choices` | what `player` chose, said to everyone: a card's modes, a Boon, an extra turn to take. `source` is the card that asked (absent when none did); `choices` are the labels of the options chosen, in the engine's words |

None changes the table.

```json
{"seq":755,"by":752,"type":"choose","player":1,"source":"Quartermaster","choices":["Gain a card costing up to $4, setting it aside on this"]}
```

### Moves

Cards change zone. The type is the word the rules use, because the rules care which it
was: a card put into a hand is not gained, a deck put into its discard pile is not
discarded.

| Type | |
| --- | --- |
| `draw` | deck to hand |
| `discard` | to a discard pile (a seat's, or the Boons' or Hexes'), as a discard |
| `gain` | from a pile (or the trash, ...) to a player, as a gain: to their discard pile, or wherever the rules say (their hand, their deck, set aside: Blockade, Reap) |
| `trash` | to the trash |
| `topdeck` | onto a deck |
| `bottomdeck` | under a deck |
| `insert` | into a deck, under some of its cards |
| `reveal` | off the deck into `looking`, face up |
| `look` | off the deck into `looking`, face down |
| `set-aside` | to a set-aside zone (a seat's `aside`, or `boons/druid`) |
| `exile` | to the Exile mat |
| `return` | to its pile |
| `exchange` | one of an exchange's two moves: a card to its pile, another from a pile (Travellers, Changeling, Trader) |
| `rotate` | from the top of a pile to its bottom |
| `take` | a Boon or Hex off its deck, or out of its discard pile, to the player taking or receiving it |
| `pass` | to another player |
| `put` | any other placement: into a hand, onto a mat, a deck into its discard pile |
| `shuffle` | see below |

`pass` is Masquerade's: each card passed is a `pass` of its own, from the passer's hand
to the hand of the next player passing. It is the only move from one player's zone to
another's. A card taken from another player is not passed: it is trashed, then gained
(Thief, Noble Brigand); an Artifact or a State changes hands as a `holding`.

Fields:

| Field | |
| --- | --- |
| `player` | whose action it is: the owner of `from`, else the owner of `to`. Between zones nobody owns, the player of the occurrence the move happens inside (`by`; of a `phase`, the turn's player): who rotates a pile, trashes a card from the Supply (Lurker), puts Black Market's cards back. Absent when nobody acts: the Boons' or Hexes' discard pile shuffled into their deck |
| `cards` | the cards, in the order they move |
| `from`, `to` | zones |
| `at` | where they arrive in an ordered `to`: `top` (absent), `bottom`, or under *n* cards |
| `pos` | for an ordered `from`: how many cards lay over each card as it left. Absent: each came off the top |
| `face` | into a seat's `aside` or `looking`: `up` or `down` |
| `fromFace` | out of a seat's `aside` or `looking`: `up` when the cards lay face up there. Absent: face down |

#### Taking and placing

**Fold:** the cards leave `from` and arrive in `to` **one after the other**, in the order
listed. For each card:

1. **Take it from `from`.**
   - Ordered: the card under `pos` cards (`pos` absent: the top one). The card lying there
     must have the name the move gives, or be `?`. `pos` counts the cards still there,
     after the earlier cards of the move have left. Of a run of cards of one name, `pos`
     is the topmost: taking any of them leaves the same zone, so the stream says the same
     thing whichever copy the rules moved.
   - Bag: one card of that name, or a `?` if the bag has none of that name. With
     `fromFace` `up`, one of the face-up cards of that name, which stops being face up;
     otherwise one that lies face down, so there must be more cards of that name than
     face-up ones.
2. **Mark it**, if `face` is `up` and `to` is a zone with faces: it joins `to`'s face-up
   cards.
3. **Place it in `to`.**
   - Ordered: at `at`: on top (`top`), at the bottom (`bottom`), or under *n* cards (*n*
     at most the zone's size). So of cards put on top, the last listed ends up on top; of
     cards put at the bottom, the last listed ends up lowest.
   - Bag: in its sorted place. `at` must be `top`.

A move within one zone (`from` equal to `to`) takes each card out and puts it back at
`at`.

**Refused:** `to` doesn't exist (a pile or `aside/<card>` zone not on the table); `from`
doesn't exist or doesn't have the card as above; a face that isn't there; `pos` with a
different number of entries from `cards`; `pos` for a bag; `at` other than `top` in a
bag, or under more cards than there are.

Empty zones that always exist leave `zones` and empty face-up bags leave `faceUp` after
each move.

#### `shuffle`

A `shuffle`'s `cards` are the **result**, top first. They leave `from` one after the
other as for any move, then arrive in `to` **together**, in the order listed, at `at`: a
discard pile shuffled under the cards left in a deck is
`"from":"0/discard","to":"0/deck","at":"bottom"`; a deck shuffled where it lies has `from`
equal to `to` and arrives on top. `to` must be ordered. A shuffle takes every card of
`from`.

Its `pos` takes each card as the **topmost card of its name** still in `from`, wherever
the others of that name lie. Which copy of a name went where is no outcome of a shuffle,
and the stream doesn't number copies, so `pos` depends only on the names in `from` and
the result: in [An example](#an-example), Ann's unshuffled deck is seven Coppers over three
Estates, and her first Estate leaves from under the seven Coppers (`pos` 7).

A shuffle's order is a chance outcome, and its `cards` are the record of it
([Chance](#chance)). Cards that go to the bottom of a deck as it is shuffled (Shadow
cards) and "when you shuffle" placements (Stash, Star Chart, Fated) are moves inside the
`shuffle`, after it.

The Boons' and Hexes' discard piles are shuffled into their empty decks the same way:

```json
{"seq":1561,"by":1558,"type":"shuffle","cards":["The Mountain's Gift","The Earth's Gift","The Moon's Gift","The Sky's Gift","The Sun's Gift","The Field's Gift","The Forest's Gift","The Wind's Gift","The River's Gift"],"from":"boons/discard","to":"boons/deck","pos":[3,3,2,5,2,0,0,1,0]}
```

#### `take`

A Boon or Hex turned over: off its deck, or out of its discard pile, to `<seat>/boons` or
`<seat>/hexes`. The rest of a Boon's or Hex's life uses the other moves: `discard` to its
discard pile once received (at Clean-up when kept), `set-aside` to `boons/druid`,
`shuffle`, `add` when Boons or Hexes join the game. Pixie's "discard the top Boon" is a
`take` then a `discard`.

#### Set-aside cards and faces

A move into a seat's `aside` or `looking` says `face`. `reveal` is always `up` and `look`
`down`; `set-aside` and `gain` say which. A move out says `fromFace` when the card lay
face up. An effect that holds a card set aside lists it in `holds`, and the face-up ones
in its `faceUp`.

Haven, from [`throne-room-wharf.events.jsonl`](examples/events/throne-room-wharf.events.jsonl):

```jsonl
{"seq":1194,"by":1188,"type":"set-aside","player":1,"cards":["Province"],"from":"1/hand","to":"1/aside","face":"down"}
{"seq":1195,"by":1188,"type":"effect","id":4,"card":"Haven","source":"Haven","owner":1,"until":{"start-of-turn":1},"keeps":["Haven"],"holds":["Province"]}
…
{"seq":1258,"type":"turn","player":1,"number":18,"kind":"regular"}
{"seq":1259,"by":1258,"type":"resolve","player":1,"card":"Haven","when":"start-turn","origin":1188}
{"seq":1260,"by":1259,"type":"effect-end","id":4,"why":"resolved"}
{"seq":1261,"by":1259,"type":"put","player":1,"cards":["Province"],"from":"1/aside","to":"1/hand"}
```

Quartermaster gains a card set aside face up, and later puts it into the hand, from
[`outpost-fleet.events.jsonl`](examples/events/outpost-fleet.events.jsonl):

```jsonl
{"seq":752,"by":746,"type":"resolve","player":1,"card":"Quartermaster","when":"start-turn","origin":679}
{"seq":753,"by":752,"type":"ask","seat":1,"prompt":"Quartermaster: choose an option","kind":"choose","purpose":"mode","source":"Quartermaster","min":1,"max":1,"options":[…]}
{"seq":754,"by":752,"type":"answer","seat":1,"indices":[0]}
{"seq":755,"by":752,"type":"choose","player":1,"source":"Quartermaster","choices":["Gain a card costing up to $4, setting it aside on this"]}
{"seq":756,"by":752,"type":"ask","seat":1,"prompt":"Quartermaster: choose a pile to gain from","kind":"pile","purpose":"gain","source":"Quartermaster","min":1,"max":1,"options":[…]}
{"seq":757,"by":752,"type":"answer","seat":1,"indices":[1]}
{"seq":758,"by":752,"type":"gain","player":1,"cards":["Silver"],"from":"pile/Silver","to":"1/aside","face":"up"}
{"seq":759,"by":752,"type":"effect-change","id":3,"card":"Quartermaster","source":"Quartermaster","owner":1,"until":"removed","keeps":["Quartermaster"],"holds":["Silver"],"faceUp":["Silver"]}
…
{"seq":847,"by":846,"type":"resolve","player":1,"card":"Quartermaster","when":"start-turn","origin":679}
{"seq":848,"by":847,"type":"ask","seat":1,"prompt":"Quartermaster: choose an option","kind":"choose","purpose":"mode","source":"Quartermaster","min":1,"max":1,"options":[…]}
{"seq":849,"by":847,"type":"answer","seat":1,"indices":[1]}
{"seq":850,"by":847,"type":"choose","player":1,"source":"Quartermaster","choices":["Put a card from this into your hand"]}
{"seq":851,"by":847,"type":"put","player":1,"cards":["Silver"],"from":"1/aside","to":"1/hand","fromFace":"up"}
{"seq":852,"by":847,"type":"effect-change","id":3,"card":"Quartermaster","source":"Quartermaster","owner":1,"until":"removed","keeps":["Quartermaster"]}
```

### Cards entering and changing

#### `add`

`cards`, `to`: cards come into the game in `to`: Boons and Hexes joining, a pile's cards
joining during play (Divine Wind), cards made in play.

**Fold:** `to` is created if it isn't on the table. Each card in turn goes on top of an
ordered `to` (so the last listed ends on top) or into a bag at its sorted place, face
down in a zone with faces.

A pile joining during play is declared by a `pile` event first; its cards follow as
`add`. A card is priced once it is in the game: the `derived` giving a name its first cost
comes after the `add` (or `rename`) that brings in the first card of that name. A `pile`
event comes before anything said of its pile: its counters and tokens.

#### `rename`

`card` in `zone` (under `pos` cards in an ordered zone) is now a card called `name`.

**Fold:** in an ordered zone, the card under `pos` cards (absent: the top one) must be
`card`; it becomes `name`. In a bag, one card named `card` becomes `name`: in a zone with
faces, a face-down one when there is one, otherwise a face-up one, which stays face up.
Refused when `card` isn't there.

The engine writes it only for Inherited, at setup: the starting card the Inherited card
replaces becomes the default one again, in the deck before it is shuffled. From
[`inherited.events.jsonl`](examples/events/inherited.events.jsonl):

```jsonl
{"seq":5,"type":"resolve","player":0,"card":"Inherited","when":"game-start"}
{"seq":6,"by":5,"type":"topdeck","player":0,"cards":["Copper","Overgrown Estate","Copper","Copper","Necropolis"],"from":"0/hand","to":"0/deck"}
{"seq":7,"by":5,"type":"ask","seat":0,"prompt":"Inherited: which starting card does your Grotto replace?","kind":"choose","purpose":"other","source":"Inherited","min":1,"max":1,"options":[…]}
{"seq":8,"by":5,"type":"answer","seat":0,"indices":[3]}
{"seq":9,"by":5,"type":"rename","card":"Necropolis","name":"Hovel","zone":"0/deck"}
{"seq":10,"by":5,"type":"derived","costs":{"Hovel":{"coins":1}}}
{"seq":11,"by":5,"type":"shuffle","player":0,"cards":["Grotto","Copper","Copper","Copper","Copper","Copper","Copper","Copper","Hovel","Overgrown Estate"],"from":"0/deck","to":"0/deck","pos":[8,1,1,2,2,2,2,2,0,0]}
```

The rename comes first, then the `derived` event pricing the new name. When a rename
leaves no card of the old name in the game, that `derived` event gives the old name a
`null` cost.

### The table's other changes

#### `counter`

`counter`, `delta`, `value`: the counter changed by `delta` and is now `value`.

**Fold:** refused unless the counter's old value plus `delta` is `value`, and for a pile's
counter unless the pile is in `piles`. The counter is now `value` (left out of `counters`
when 0).

A change sits between the same two card moves it happened between.

#### `effect`

All of an effect's fields ([Effects](#effects)): it begins.

**Fold:** it joins `effects`, in `id` order. Refused if an effect with that `id` is on the
table.

#### `effect-change`

All of an effect's fields: the effect with that `id` is now this. Written whenever a
field changes as the table shows it: Archive's or Crypt's `holds` shrink, Quartermaster's
or Cargo Ship's grow, Bridge Troll's and Taskmaster's `until` turns, Garrison's `tokens`
count, a Duration whose card leaves play becomes `ending`. A change only in which copies
it keeps or holds is not written.

**Fold:** the effect with that `id` is replaced. Refused if there is none.

#### `effect-end`

`id`, `why`: the effect ends.

| `why` | |
| --- | --- |
| `resolved` | an ability removed it: as a rule its own, resolving (a Duration's at the start of the turn) |
| `expired` | its `until` came: the end of the turn, or its player's turn starting |
| `left-play` | its card had left play: it ended with the turn |
| `extra-turn` | the extra turn it kept its card in play for began, was skipped or was lost |

**Fold:** the effect leaves `effects`. Refused if there is none with that `id`. The cards
it kept or held don't move: what moves them is a move event of its own.

#### `extra-turn`

`id`, `player`, `card`, `limit`, `effect` when an effect keeps its card in play for it,
and `front` when it goes before the others: an extra turn waits.

**Fold:** it joins `extraTurns`, at the front with `front`, otherwise at the end. Refused
if one with that `id` is waiting.

It is taken by the `turn` naming it, skipped or lost by the `turn-skipped` naming it, or
removed by `extra-turn-removed`.

#### `extra-turn-removed`

`id`: the extra turn won't happen, because the effect it came with ended (Voyage or
Outpost left play before its turn). Its effect's `effect-end` (`left-play`) comes first.

**Fold:** it leaves `extraTurns`. Refused if it isn't waiting.

Outpost, from [`outpost-fleet.events.jsonl`](examples/events/outpost-fleet.events.jsonl).
Bo has a Haven holding a Copper and plays Outpost:

```jsonl
{"seq":1038,"by":1031,"type":"effect","id":7,"card":"Haven","source":"Haven","owner":1,"until":{"start-of-turn":1},"keeps":["Haven"],"holds":["Copper"]}
{"seq":1039,"by":1028,"type":"ask","seat":1,"prompt":"Action phase: choose a move","kind":"turn","purpose":"turn","phase":"action","min":1,"max":1,"options":[…]}
{"seq":1040,"by":1028,"type":"answer","seat":1,"indices":[0]}
{"seq":1041,"by":1028,"type":"play","player":1,"card":"Outpost","from":"1/hand","to":"1/play"}
{"seq":1042,"by":1041,"type":"counter","counter":"actions","delta":-1,"value":0}
{"seq":1043,"by":1041,"type":"effect","id":8,"card":"Outpost","source":"Outpost","owner":1,"until":"end-of-turn"}
{"seq":1044,"by":1041,"type":"effect","id":9,"card":"Outpost","source":"Outpost","owner":1,"until":"extra-turn","keeps":["Outpost"]}
{"seq":1045,"by":1041,"type":"counter","counter":"next-hand","delta":-2,"value":3}
{"seq":1046,"by":1041,"type":"extra-turn","id":1,"player":1,"card":"Outpost","limit":"third-in-a-row","effect":9}
{"seq":1047,"by":1023,"type":"phase","phase":"buy"}
{"seq":1048,"by":1047,"type":"ask","seat":1,"prompt":"Buy phase: choose a move","kind":"turn","purpose":"turn","phase":"buy","min":1,"max":1,"options":[…]}
{"seq":1049,"by":1047,"type":"answer","seat":1,"indices":[3]}
{"seq":1050,"by":1023,"type":"phase","phase":"night"}
{"seq":1051,"by":1023,"type":"phase","phase":"cleanup"}
{"seq":1052,"by":1051,"type":"discard","player":1,"cards":["Curse","Gold","Smithy"],"from":"1/hand","to":"1/discard"}
{"seq":1053,"by":1051,"type":"draw","player":1,"cards":["Copper","Copper","Copper"],"from":"1/deck","to":"1/hand"}
{"seq":1054,"by":1023,"type":"turn-end","player":1}
{"seq":1055,"by":1054,"type":"effect-end","id":8,"why":"expired"}
{"seq":1056,"type":"effect-end","id":9,"why":"extra-turn"}
{"seq":1057,"type":"turn","player":1,"number":15,"extra":"Outpost","kind":"extra","extraTurn":1}
{"seq":1058,"by":1057,"type":"ask","seat":1,"prompt":"Start of your turn: choose which of your abilities resolves next (the others stay pending)","kind":"choose","purpose":"trigger","min":1,"max":1,"options":[…]}
{"seq":1059,"by":1057,"type":"answer","seat":1,"indices":[0]}
{"seq":1060,"by":1057,"type":"resolve","player":1,"card":"Haven","when":"start-turn","origin":1031}
{"seq":1061,"by":1060,"type":"effect-end","id":7,"why":"resolved"}
{"seq":1062,"by":1060,"type":"put","player":1,"cards":["Copper"],"from":"1/aside","to":"1/hand"}
…
{"seq":1094,"by":1093,"type":"discard","player":1,"cards":["Haven","Outpost","Copper","Copper","Copper","Copper"],"from":"1/play","to":"1/discard"}
```

Clean-up draws 3 (`next-hand`). The Outpost, kept in play by effect 9 until its extra turn
began, is discarded in that turn's Clean-up.

#### `token`

`player`, `token`, and `at`: the token is now `at`. Without `at`, the table no longer
lists it (a token not had any more, the Journey token turned face up).

**Fold:** the entry for (`player`, `token`) leaves `tokens`; with `at`, it is listed again
at its place in order. Refused if `at` is a pile not in `piles`.

```json
{"seq":1725,"by":1722,"type":"token","player":1,"token":"journey","at":"face-down"}
```

#### `holding`

`card`, and `from` and `to` (either may be absent): a Project cube, Artifact or State
changes hands. `from` no longer holds `card`; `to` does. A Project bought is `to` only; a
State returned is `from` only; an Artifact taken from another player has both. Misery
turning Miserable over is two: Miserable `from` the player, then Twice Miserable `to`
them.

**Fold:** `from` leaves `card`'s holders and `to` joins them (kept sorted; a card with no
holders leaves `holdings`). Refused if `from` doesn't hold it, `to` already does, or
neither is given.

```jsonl
{"seq":1733,"by":1732,"type":"holding","card":"Envious","to":0}
…
{"seq":1786,"by":1784,"type":"holding","card":"Envious","from":0}
```

#### `pile`

`pile` (a pile's zone) and the pile's properties ([Piles](#piles)): they are now these.

**Fold:** `piles[pile]` is replaced; if `pile` has no zone yet, it is created, empty. Its
cards follow as `add`.

Divine Wind's removal of a pile is a `pile` event with `removed`, before the tokens
leaving it and its counters going to 0. A pile given a role after it joined (a Young
Witch joining during play, then its Bane chosen) gets a second `pile` event.

#### `landscape`

`card`, and `prophecy` when it is the game's Prophecy: a landscape or Artifact joins the
game (an Ally for a Liaison, an Artifact for its card, a Prophecy for an Omen, during
play when Divine Wind brings them).

**Fold:** `card` joins `landscapes` (once, in name order); with `prophecy`, `prophecy`
becomes `card`.

#### `notes`

`notes`: the table's notes are now these.

**Fold:** `notes` is replaced.

#### `derived`

`costs` and `types`, each by card name: values the rules derive changed. One event carries
everything that changed together.

- Each name in `costs` costs that now; `null`: no card of that name is in the game any
  more.
- Each name in `types` has those types now; `null`: its printed types again.

**Fold:** each name is set in, or with `null` removed from, the table's `costs` or
`types`.

Costs change whenever a rule says so: a Bridge played, a Canal owner's turn beginning or
ending, Ferry's token placed. Bridge played, from
[`boons-hexes.events.jsonl`](examples/events/boons-hexes.events.jsonl):

```json
{"seq":208,"by":203,"type":"derived","costs":{"Bard":{"coins":3},"Blessed Village":{"coins":3},"Bridge":{"coins":3},"Druid":{"coins":1},"Duchy":{"coins":4},"Estate":{"coins":1},"Flag Bearer":{"coins":3},"Gold":{"coins":5},"Market":{"coins":4},"Province":{"coins":7},"Ranger":{"coins":3},"Silver":{"coins":2},"Skulk":{"coins":3},"Smithy":{"coins":3},"Village":{"coins":2}}}
```

### Questions, answers and chance

The inputs: what the rules leave to the players and to chance. None changes the table,
and none is a cause.

#### `ask`

A seat is asked something, and the game waits on its answer. The fields are
`dominion/agent-view@2`'s decision ([Decisions](README.md#decisions)) as that seat is
shown it, without its `id` and `groups`, with `seat` for `player`:

| Field | |
| --- | --- |
| `seat` | who is asked |
| `prompt` | the question, players called by their names |
| `kind` | `turn`, `cards`, `pile`, `choose`, `name` or `number` |
| `purpose` | what it is for, in agent-view@2's words: `turn`, `discard`, `trash`, `gain`, `top-deck`, `play`, `trigger`, `mode` (a Way question's too), ... |
| `source` | the card asking, if one is |
| `phase` | for `turn`: the phase |
| `ordered` | the cards chosen are ordered: the first listed ends on top |
| `nameAny` | any card may be named: the answer is a name |
| `min`, `max` | how many options to choose |
| `options` | agent-view@2's options: `index` (from 0), `group` (0: a question has one group, whose bounds are `min` and `max`), `action`, `label`, and `card`, `zone`, `cost`, `value`, `player` as they apply |

**Fold:** nothing changes.

Only real questions are written. A decision the engine answers itself, because only one
answer matters (a phase whose only move is to end it, two cards to discard to Militia
from a hand of three Coppers), is not: it is answered the same way every time. An `ask`
is the last event written before the game waits, so a stream of a game in progress ends
with one.

Options are listed in the engine's order. Two options with the same label can be
different things to the rules, and their place in the list tells them apart: the engine
lists the cards of a zone in the zone's order (two Throne Rooms in play, one kept by a
Duration), and the cards a "when you shuffle" choice looks through by name, then from the
top down (Star Chart). What a label shows is what the seat sees: a card it doesn't see is
`a card`.

The `prompt` is the question, not the tool used to answer it: Arena's hint about answering
a Way question in advance is not in it. A `name` question's `options` are the cards of the
piles the seat can see; any card may be named.

#### `answer`

`seat`, and `indices` (into the `ask`'s `options`, in the order chosen; for an `ordered`
question, top first) or `name` (for a `nameAny` question): what the seat answered.

**Fold:** nothing changes.

An `answer` is always the event right after its `ask`, with the same `seat` and `by`. An
`ask` with no `answer` after it is the stream's last event (the game is waiting) or is
followed by `game-end` with reason `resigned`. A named card is said to everyone too, by the
`name` event that follows the answer.

Chapel, from [`moat-chapel.events.jsonl`](examples/events/moat-chapel.events.jsonl):

```jsonl
{"seq":1076,"by":1065,"type":"play","player":0,"card":"Chapel","from":"0/hand","to":"0/play"}
{"seq":1077,"by":1076,"type":"counter","counter":"actions","delta":-1,"value":0}
{"seq":1078,"by":1076,"type":"ask","seat":0,"prompt":"Chapel: choose up to 4 cards to trash","kind":"cards","purpose":"trash","source":"Chapel","min":0,"max":4,"options":[{"index":0,"group":0,"action":"select","label":"Estate","card":"Estate","zone":"hand"},{"index":1,"group":0,"action":"select","label":"Fortress","card":"Fortress","zone":"hand"},{"index":2,"group":0,"action":"select","label":"Militia","card":"Militia","zone":"hand"},{"index":3,"group":0,"action":"select","label":"Copper","card":"Copper","zone":"hand"},{"index":4,"group":0,"action":"select","label":"Silver","card":"Silver","zone":"hand"}]}
{"seq":1079,"by":1076,"type":"answer","seat":0,"indices":[2,3,1,4]}
{"seq":1080,"by":1076,"type":"trash","player":0,"cards":["Militia","Copper","Fortress","Silver"],"from":"0/hand","to":"trash"}
```

Ann chose Militia, a Copper, Fortress and Silver, in that order, and the `trash` lists them
in that order.

**What they are not.** No event names an `ask` or `answer` in `by` ([Causes](#causes)),
and nothing else refers to them: the `trash` above is by Chapel's `play`. A question is
always the last event written before the game waits and its answer the first written
after, so no move was ever merged across one ([One event per
occurrence](#one-event-per-occurrence)). So dropping every `ask` and `answer` from a
stream leaves the other events as they were, but for their numbers.

**Conveniences** a host offers are written as the plain answers they stand for, as they
are given: Arena's Autoplay Treasures is one `ask` and `answer` per Treasure played; a
Way question answered in advance (with the answer that plays the card) is that question's
`ask`, when it comes, and its `answer`, after any other seat's questions that come first.

#### `chance`

A chance outcome no `shuffle` shows: what was drawn, by name. Copies of a name are
interchangeable, so the names are the whole outcome. The same record is an event during
play, and an entry of `setup`'s `chance` for what setup drew.

| Field | |
| --- | --- |
| `site` | what it decides (below) |
| `card` | for `pile`, the pile's card; for `choice`, the card choosing |
| `cards` | the outcome, in order |

Every chance outcome is recorded once, at its site:

| Chance | Recorded as |
| --- | --- |
| A player's deck shuffled: the opening deal, a discard pile into the deck, a whole deck (Inherited's, Inn, Famine) | the `shuffle` event: its `cards`, top first |
| The Boons' or Hexes' discard pile shuffled into their deck | the `shuffle` event |
| The Boons' or Hexes' deck as it is made | `chance` `boons` or `hexes`: the deck, top first |
| A shuffled pile as setup makes it (Knights, Ruins, Loot, ...): its order, and which of the pool it took | `chance` `pile`, `card` the pile's card: the pile, top first |
| A choice setup makes at random: Young Witch's Bane, Ferryman's pile, Way of the Mouse's and Riverboat's card, Approaching Army's, Obelisk's pile, each Trait's pile, Druid's Boons, the Black Market deck | `chance` `choice`, `card` the card choosing: what it chose, in its order (the Black Market deck top first) |
| The Ally, the Prophecy, when none was given | `chance` `ally` or `prophecy` |
| Divine Wind's new Kingdom | `chance` `kingdom`: the Kingdom piles, in the order they are set up. What their setup then draws follows as more `chance` events |

As an event: **Fold:** nothing changes; the `pile`, `add`, `landscape` and move events that
follow change the table. Today only Divine Wind draws chance during play that no shuffle
shows: its new Kingdom and what that Kingdom's setup draws. From
[`divine-wind.events.jsonl`](examples/events/divine-wind.events.jsonl), where Bo's
Mountain Shrine removes the last Sun:

```jsonl
{"seq":411,"by":408,"type":"play","player":1,"card":"Mountain Shrine","from":"1/hand","to":"1/play"}
{"seq":412,"by":411,"type":"counter","counter":"actions","delta":-1,"value":0}
{"seq":413,"by":411,"type":"counter","counter":"sun","delta":-1,"value":0}
{"seq":414,"by":411,"type":"receive","player":1,"card":"Divine Wind"}
{"seq":415,"by":411,"type":"pile","pile":"pile/Young Witch","card":"Young Witch","removed":true,"recipe":{"kind":"stacked","cards":[{"card":"Young Witch","count":10}]}}
…
{"seq":425,"by":411,"type":"pile","pile":"pile/Aristocrat","card":"Aristocrat","removed":true,"roles":[{"card":"Young Witch","role":"bane"}],"recipe":{"kind":"stacked","cards":[{"card":"Aristocrat","count":10}]}}
{"seq":426,"by":411,"type":"chance","site":"kingdom","cards":["Dismantle","Jack of All Trades","Urchin","Druid","Archive","Settlers","Pilgrim","Raider","Shop","Conspirator"]}
{"seq":427,"by":411,"type":"pile","pile":"pile/Dismantle","card":"Dismantle","supply":true,"recipe":{"kind":"stacked","cards":[{"card":"Dismantle","count":10}]}}
{"seq":428,"by":411,"type":"add","cards":["Dismantle"],"to":"pile/Dismantle"}
{"seq":429,"by":411,"type":"derived","costs":{"Dismantle":{"coins":4}}}
…
{"seq":560,"by":411,"type":"chance","site":"boons","cards":["The Sun's Gift","The Sky's Gift","The Earth's Gift","The Forest's Gift","The Wind's Gift","The Field's Gift","The River's Gift","The Sea's Gift","The Mountain's Gift","The Moon's Gift","The Flame's Gift","The Swamp's Gift"]}
{"seq":561,"by":411,"type":"add","cards":["The Swamp's Gift","The Flame's Gift","The Moon's Gift","The Mountain's Gift","The Sea's Gift","The River's Gift","The Field's Gift","The Wind's Gift","The Forest's Gift","The Earth's Gift","The Sky's Gift","The Sun's Gift"],"to":"boons/deck"}
{"seq":562,"by":411,"type":"chance","site":"choice","card":"Druid","cards":["The Sun's Gift","The Moon's Gift","The Sky's Gift"]}
{"seq":563,"by":411,"type":"set-aside","player":1,"cards":["The Sun's Gift","The Moon's Gift","The Sky's Gift"],"from":"boons/deck","to":"boons/druid","pos":[0,8,0]}
```

The Boons' deck is made with Druid in the new Kingdom, then Druid's three Boons are
chosen from it. The `chance` of the Boons' deck lists it top first; the `add` puts the
last listed on top.

The Boons' deck and a shuffled pile made in setup are in the setup table too; their
`chance` record says they were drawn, and keeps the outcomes in one place.

## Replay

A game is determined by its rules, its setup, what the players chose and how chance fell,
and a full stream holds all four. `dominion-agent`'s `replay::replay` plays a game again
from its stream alone, with the engine the stream names, and either gets the same stream,
event for event, or says the first event that differs.

### What a replayable stream holds

| Cause | Where |
| --- | --- |
| The rules | `setup.rules`: `implementation` and `version` |
| How the game was set up | `setup.seats` (the player count), `setup.kingdom`, `setup.config` |
| What setup drew by chance | `setup.chance`, and the opening `shuffle` events |
| What chance drew in play | each `shuffle` event's `cards`; each `chance` event |
| What the players chose | each `answer`, to the `ask` before it |
| A resignation | `game-end` with reason `resigned`, where it happened |

Nothing else: not the seed, not the host's history of answers, not a snapshot. A stream
without `setup.config` (recorded before it was written) can't be replayed, nor can a
stream with a face-down card in a `shuffle` (only a `full` stream holds every outcome).

### Which outcome answers which draw

An outcome is matched to a draw by what it decides, its **site**: a seat's deck, the
Boons' or Hexes' discard pile shuffled, the Boons' or Hexes' deck made, a pile by its
card, a choice by the card choosing, the Ally, the Prophecy, Divine Wind's Kingdom. A
`shuffle` into a seat's deck is that seat's; into `boons/deck` or `hexes/deck` the Boons'
or Hexes' reshuffle. Each site's outcomes are taken in stream order. Within a site the
stream's order is the order of the draws, because an outcome is written as it is drawn
(a `chance`) or by the event that shows the draw (a `shuffle`, written before anything is
drawn again for that deck). Across sites the order doesn't matter: so setup's draws, all
made before event 0, are read from `setup.chance` and the `shuffle` events after `setup`,
and a shuffle's event may come after the draw it shows.

### Playing a stream again

Replay:

1. sets the game up from `setup`'s `seats`, `kingdom` and `config`;
2. gives the engine, in place of its generator, every chance outcome in the stream, each
   site's in order;
3. records a new stream as the game goes and compares each event with the stream's;
4. where the game waits on a question, gives it the stream's `answer` (or, where the
   stream has `game-end` with reason `resigned`, resigns that seat).

The engine takes each outcome it is given if it fits what it is drawing, and **refuses**
one that doesn't: not the same cards as the deck being shuffled, a pick that isn't among
those it picks from, the wrong number. It draws from its generator only after a refusal,
when the replay has already failed.

### What replay promises

- **The same stream, event for event**, equal as values (so in either encoding), when the
  stream is one this engine at this version recorded. Replay then returns the game at the
  end of the stream, over or waiting on the question the stream ends with, and the
  recorder that wrote it, to go on recording.
- **Otherwise the first event that differs**: its `seq`, the stream's event there (or
  none: the stream ended), what the game did there instead (or nothing), and why:
  - the setup the engine writes differs from the stream's, `rules` included: event 0;
  - an outcome refused, or a site with no outcome left: at the event the outcome was read
    from, or at an earlier event that already differs;
  - an answer that isn't one of the question's options: at the `answer`;
  - the stream has something other than an answer where the game waits, or goes on
    after the game is over: at that event;
  - otherwise the game goes differently: at the first event that differs.

  An outcome that fits but is not what happened (two cards of a shuffle swapped) is
  taken, and the game goes on with it until the stream stops being that game's: at the
  latest the first event that no longer folds, sooner where an answer picks a card by its
  place. A different valid answer is found at the first event after it that differs. A
  stream cut right after an `ask` is a game in progress; cut anywhere else, it differs at
  the cut.
- **Nothing from outside the stream**: no seed, no configuration, no snapshot.

### What replay compares

Exact streams written by the same recorder. Everything the recorder decides (which moves
merge into one event, where counters fall between moves, a shuffle's `pos`, the order in
which cards moved together out of a bag are listed, a question's prompt, labels and order
of options) is decided the same way both times, so the comparison can be exact. Another
producer's stream of the same game would differ in those decisions without the game
differing: it would merge moves differently, word its prompts differently, list the cards
of a hand discarded together in another order. Replaying it would need a comparison of
what the events mean ([Not specified yet](#comparing-streams-from-different-producers)).

## Encodings

The format is the model above. An encoding writes its types as bytes; the same stream in
two encodings is the same stream. Two are defined: JSON (written as JSON Lines), the
reference, and CBOR. Any self-describing format can carry the model (MessagePack would);
one that isn't (bincode, postcard) can't, because an event is a tagged map with optional
fields.

### The JSON form

| Model | JSON |
| --- | --- |
| Field names | `camelCase` (`fromFace`, `extraTurn`, `finalRound`) |
| Enumerated values (event types, phases, `when`, `why`, turn kinds, limits, roles, recipe kinds, tokens, faces, chance sites; an `ask`'s `kind`, `purpose`, `phase` and options' `action`) | `kebab-case` strings (`set-aside`, `start-turn`, `third-in-a-row`, `plus-card`, `top-deck`, `end-phase`) |
| An event | one object: `seq`, `by` when present, `type`, then its own fields at the same level. A `pile` event's properties are fields of the event too: `{"type":"pile","pile":"pile/Footpad","card":"Footpad","supply":true,…}` |
| A card | a string: its name, or `"?"` |
| A zone | a string: `<seat>/deck`, `<seat>/native-village`, `pile/<card>`, `pile/<card> (2)`, `aside/<card>`, `trash`, `boons/deck`, `boons/discard`, `boons/druid`, `hexes/deck`, `hexes/discard` |
| A counter key | a string, as in [Counters](#counters): `coins`, `0/coffers`, `pile/Village/embargo`, `landscape/Arena/vp` |
| A token's place | a string: a pile's zone, `player` or `face-down` |
| An ordered zone's cards | an array, top first |
| A bag | an array, sorted: `"?"` first, then names in code-point order |
| `at` | absent for `top`; `"bottom"`; `{"under": n}` |
| `until` | `"end-of-turn"`, `{"start-of-turn": n}`, `"extra-turn"`, `"removed"` |
| `viewer` | `"full"`, `"public"`, `{"seat": n}` |
| A cost | `{"coins": n}`, with `potions` and `debt` when not 0 |
| Maps (`zones`, `faceUp`, `counters`, `piles`, `holdings`, `costs`, `types`) | objects keyed by the text form of their keys. Key order carries no meaning |
| Absence | an optional field that is absent, a `false` flag, an empty list and a note's `count` of 0 are left out. A reader takes a missing field as absent, `false`, empty or 0 |
| An `ask`'s options | objects as in agent-view@2: `{"index": 0, "group": 0, "action": "select", "label": "Estate", "card": "Estate", "zone": "hand"}` |
| `config.choices` | an object keyed by the card choosing, each a list of names |
| A chance record | `{"site": "pile", "card": "Ruins", "cards": [...]}`, in `setup`'s `chance` list or as an event's fields |
| `null` | only in `derived`: a cost or types that are gone |
| Integers | JSON numbers. `seq`, `by`, `origin` and `seed` are unsigned 64-bit; ids, `turnLimit`, `min`, `max` and `indices` unsigned 32-bit; seats 0 to 255; counters signed 64-bit |

Fields always written even at their default: a turn's `kind` (read as `regular` when
missing), a cost's `coins`, an event's `seq` and `type`, `config`'s `colonies` and
`shelters`, an `ask`'s `min`, `max` and `options`, an option's `index`, `group`, `action`
and `label`, a chance record's `cards`. The reference reader ignores
fields it doesn't know and refuses a `type` it doesn't know.

A table in JSON is an object with `zones`, then each other part under its name
(`counters`, `turn`, `ended`, `effects`, `faceUp`, `extraTurns`, `ending`, `piles`,
`landscapes`, `prophecy`, `holdings`, `tokens`, `notes`, `costs`, `types`), each left
out while empty. `setup`'s `table` is one. A table the reference reader has folded and
writes out also carries `progress`, its fold's place in the stream ([When a stream is not
one game's](#when-a-stream-is-not-one-games)): no part of the table, never in `setup`, and
ignored when read there. The turn in progress is `{player, number,
extra, phase, kind, limits}`.

### JSON Lines

A stream in JSON is JSON Lines: one JSON object per line, each line ended by `\n`; the
header, then the events.

### CBOR

A stream in CBOR is a CBOR sequence (RFC 8742): one CBOR data item per record, back to
back, the header first. Each item is the same map the JSON has, with the same text keys
and the same text forms of cards, zones and counter keys; integers are CBOR integers.
[`moat-chapel.events.cbor`](examples/events/moat-chapel.events.cbor) is the same stream as
[`moat-chapel.events.jsonl`](examples/events/moat-chapel.events.jsonl).

## Recorded streams

A recorded stream is a sequence of **records**: the header, then every event in order,
`seq` 0, 1, 2, ... with none missing. A reader never guesses: the file's name says the
encoding, and the first record says the schema and the viewer.

| Encoding | File name ends | Media type |
| --- | --- | --- |
| JSON Lines | `.events.jsonl` | `application/jsonl` |
| CBOR | `.events.cbor` | `application/cbor-seq` |

A third encoding is a new file-name ending and media type, nothing else.

A file is only ever appended to, so a write that never finished leaves at most one record
cut short at its end: a last line with no `\n`, or a CBOR item that runs out. A reader
ignores it. A whole record that doesn't parse, or an event whose `seq` isn't the next,
means the file is not a stream. Recorded files are `full` streams; the reference reader
accepts no other viewer.

### What Arena keeps

Every game `dominion serve` saves (not `--ephemeral`) is recorded from its first event,
to `<state_dir>/<game id>.events.jsonl` (or `.events.cbor`), beside the game's snapshot
`<game id>.json`. The setting `events_encoding` (`jsonl`, the default, or `cbor`; the flag
`--events-encoding`) chooses the encoding of games that start; a game's stream stays in
the encoding it began in. Events are appended as the game is played, after every answer.
When the game is retired (finished and kept past `keep_finished_days`, idle past
`keep_idle_days`, or `dominion games retire`) the stream moves to `<state_dir>/expired/`
with the snapshot and is kept.

`GET /api/games/{id}/recording` serves a game's stream as recorded, in its encoding. The
full stream shows every hidden card and every shuffle's order, the future of a game in
progress, so it is served only once the game is over (409 before), to the game's seats
or, for a watchable game, to anyone (403 otherwise).

Games saved before streams were recorded have none, and streams recorded before
`setup.config`, questions and chance were written fold but can't be replayed. Solo games
(`dominion solo`) and dominion.games games are not recorded.

Arena resumes and undoes a game from its snapshot, not from the stream ([Not specified
yet](#loading-and-undoing-a-game-from-its-stream)).

### After a crash

The snapshot and the stream are separate files. Whenever the server stops, **the
stream's first *n* events are the snapshot's**, where *n* is the number of events the
snapshot says were written. Loading cuts the stream back to those *n* (dropping a record
cut short, and anything a later snapshot that was never saved had added), and the events
the snapshot carries as not yet written follow at the next write. So once the server
goes on, the file is exactly the stream of the game as it was restored, and a reader of a
stream mid-write may see a last record cut short, never a wrong one.

A stream that lacks events its snapshot says were written (a file deleted or damaged
from outside) can't be mended: the server reports it at startup, leaves the file as it
is, and hosts the game without recording more of it.

### After an undo

The stream holds no undo: undo is the host's, not the game's. A game taken back is
replayed from its rules and seed with its remaining answers, which records the same
events as before up to that point, so the stream of the game as it now stands is a prefix
of the old one, ending with the question whose answer was the first taken back. Arena
replaces the file with it, atomically, and appends from there: at every moment the file
is the stream of the game as it stands. What was taken back never happened, and a reader
of the file can't tell that it did.

## Not specified yet

### The seat and public versions

Only `full` exists. A stream for one seat, or for the public, says less, and what it must
not say goes beyond faces. These are known; the versions are not designed in detail:

- **Their own numbering.** Whether a seat is asked at all depends on hidden cards (Library
  asks only about an Action; Black Cat reacts only if held). A shared event number tells
  everyone something happened, so a viewer's stream numbers its own events.
- **More than faces is hidden.** Where a card left a discard pile its owner searched
  (Harbinger); the order of revealed cards put back privately (Rabble, Mandarin); scores
  after each leg of a Masquerade pass; a face-down Boon's or Hex's `pos` in its deck; the
  order of a `shuffle` (only its count shows).
- **A zone per holding.** The full stream joins a set-aside card to its effect by name,
  face and effect id. A viewer who doesn't see a face can't, so face-down set-aside cards
  need a zone per holding (`<seat>/aside/<n>`, named when the holding begins), and an
  effect's `holds` must name that zone. A holding outlives effects (Cage's Duration ends
  when it is trashed and an end-of-turn effect takes over the same cards; a Duration
  whose card left play keeps its cards set aside with no effect), so a later effect must
  be able to name the same zone.
- **Backs that show.** Stash and Shadow cards are known by their backs, the exception to
  "face down means unknown".
- **How a bag mixes `?` and names**, and whether `pos` may be shown.
- **Setup's hidden orders.** The setup table gives the Boons' and Hexes' decks and the
  shuffled piles (Knights, Ruins) in their order; a masked setup can't.
- **Questions are the asked seat's alone.** What a seat is asked, and that it is asked at
  all, is in that seat's stream only, with its answer; the public's has neither. Since no
  event names a question as its cause, dropping them changes no other event.
- **Chance that shows nothing.** `config.seed` is in no masked stream; `chance` records of
  hidden things (a shuffled pile's order below its top, the Boons' and Hexes' decks, the
  Black Market deck) are hidden; a `shuffle` shows its count, not its cards. So only the
  full stream replays.
- **Which `resolve`s to drop.** A `resolve` for every ability is right for the full stream;
  a seat's or the public stream will have to drop some (an ability that exists because of
  a hidden card) and say which causes it can't show. The plain-name `card` fields of
  occurrences can't be `?` today.
- **Deduction stays out.** What a seat can work out is for a knowledge model reading the
  stream, not for the stream.

The test that will hold them to account: two games that differ only in cards a viewer
never sees give that viewer identical streams. No JSON Schema is written until these
versions settle the shapes.

### Loading and undoing a game from its stream

The stream holds every cause of the game, so a host could load a game by replaying its
stream and undo by replaying a stream cut right after the `ask` of the answer taken back.
Arena does neither yet: it resumes and undoes from its snapshot, which keeps the engine's
game and the host's history of answers. What the stream still lacks for it:

- **A Way question answered in advance that is waiting.** An answer may answer the Way
  questions of the card it plays in advance, and they can come after other seats'
  questions (Reactions to an Attack). While one waits, it is the one piece of state that
  changes the game and is in no event. It belongs in the host's snapshot, or in a host
  record beside the stream.
- **Command boundaries.** One command of a seat can be several answers: an Autoplay
  Treasures run, an answer with the Way questions it answered in advance. Undo takes back
  a command, but the stream doesn't say where one began. A field on `answer` marking those
  a host gave on a seat's behalf, or a host record of where each command began, would let
  undo find "my last answer" from the stream alone.

The host's own state stays out of the stream either way: decision ids, each seat's log
cursor, who asked to undo.

### Rules changes and games in progress

A stream replays only with the engine that recorded it, and `rules.version` doesn't
change with every rules fix. A fix that changes what a game does makes a game in progress
recorded before it fail to replay at the first event it changes. No policy is set: keep
the snapshot until such a game ends, accept the difference, or end the game.

### Comparing streams from different producers

Replay compares exact streams from one recorder ([What replay
compares](#what-replay-compares)). Holding another producer's stream to the same game
(dominion.games', or another engine's) needs a comparison by meaning: the table folded at
every question equal, the questions asking the same, the answers equal. It is not built.

### Out of scope

Undo, clocks, chat and who is connected belong to whatever hosts a game, not to the game.

### Known gaps

- **Who an effect affects.** The players an Attack-Duration reached (Corsair, Blockade,
  Swamp Hag, Haunted Woods, Gatekeeper, Frigate) are public, but effects don't carry
  them. Likewise a card an effect is about (Contraband's and War Chest's named cards) and
  a card an effect marks where it lies (Necromancer).
- **What a Boon in `<seat>/boons` is waiting for**: that Blessed Village's Boon will be
  received at the start of the next turn, or that Fool's remaining Boons are still to be
  received.
- **Types of one copy.** `types` is by name. Inheritance gives one player's Estates
  another card's abilities, not new types by name, so it doesn't appear in `types`;
  Inheritance's set-aside card is a note.
- **VP**, by decision ([Derived values](#derived-values)).
- **Causes the stream doesn't give exactly.** The bonus of a replaced or blocked play
  (Enchantress's +1 Card +1 Action) names the `play`, not the `resolve` that replaced it.
  Spending Coffers and Villagers and paying off Debt have no occurrence of their own:
  their counters are by the phase. A pay-otherwise ability resolves before its `buy`, so
  what it does is by the phase. The `hand-plays` counter changes before the `play` it
  counts is written, so it names the phase.
- **What a consequence of cards trashed or discarded together is about**, other than a
  `resolve`'s (`about`, `index`). None is written today; a rule that attached something to
  the trash or discard itself would need a field.
- **Open causes in a snapshot.** A reader joining mid-game would need the occurrences
  still in progress; nothing carries them.
- **Charm** keeps its spent effect until the end of the turn.
- **Questions with several groups.** An `ask` has no `groups`: every question this engine
  asks has one group, whose bounds are `min` and `max`. A producer whose questions have
  several would need them.

## Example streams

Every example in this document is quoted from these, written by `dominion-engine` 0.1.0.
Each is a two-player game whose seats, Ann and Bo, take scripted answers; its
`setup.config` gives the seed and turn limit it was played with. The JSON Lines files were
read back, folded and replayed to themselves, and the CBOR file read back to the same
events.

| File | Kingdom | Shows |
| --- | --- | --- |
| [`moat-chapel.events.jsonl`](examples/events/moat-chapel.events.jsonl), [`.cbor`](examples/events/moat-chapel.events.cbor) | Throne Room, Wharf, Moat, Militia, Chapel, Fortress, Haven, Village, Smithy, Market | a complete opening; questions and answers; Moat against Militia; Fortress trashed with other cards; the same stream in CBOR |
| [`throne-room-wharf.events.jsonl`](examples/events/throne-room-wharf.events.jsonl) | the same | Throne Room on Wharf and the next turn; Haven |
| [`outpost-fleet.events.jsonl`](examples/events/outpost-fleet.events.jsonl) | Outpost, Haven, Quartermaster, Grotto, Library, Village, Smithy, Market, Laboratory, Festival; Fleet | an extra turn; cards set aside face up; the end with a final round |
| [`boons-hexes.events.jsonl`](examples/events/boons-hexes.events.jsonl) | Bard, Blessed Village, Skulk, Druid, Bridge, Ranger, Flag Bearer, Village, Smithy, Market; Pageant | Boons and Hexes; a Project, an Artifact and a State held; the Journey token; costs changing |
| [`inherited.events.jsonl`](examples/events/inherited.events.jsonl) | Hermit, Rats, Marauder, Fortress, Procession, Quartermaster, Grotto, Village, Smithy, Market; Inherited | an ability at the start of the game; `rename`; `setup.config` and `setup.chance` |
| [`divine-wind.events.jsonl`](examples/events/divine-wind.events.jsonl) | Young Witch, Rustic Village, Poet, Tea House, Kitsune, Mountain Shrine, River Shrine, Village, Smithy, Market; Divine Wind | a Bane chosen at random; `chance` events in play: Divine Wind's new Kingdom, the Boons' deck and Druid's Boons it brings |
