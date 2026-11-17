# dominion/events@1

A precise language for what happens in a game of Dominion: a stream of events, each one
unambiguous statement about the table. The same stream is

- how a game is **talked about** (by a program, a log, an agent),
- how a game is **recorded** (the stream in a file is the replay), and
- what a client can be sent to **follow** a game (apply the events as they arrive).

A reader needs no rules engine: **the table after event *n* is the fold of events
`0..=n`**, and this document defines what each event does to the table.

Status: working draft. [Implemented](#status) says what `dominion-engine` writes today.

## The table

What the events describe.

- **Cards** are physical cards. Each sits in exactly one zone.
- **Zones** hold cards:

  | Zone | |
  | --- | --- |
  | `<seat>/deck`, `<seat>/discard` | ordered |
  | `<seat>/hand`, `/play`, `/aside` (set aside), `/looking` (off the deck, being looked at or revealed), `/tavern`, `/island`, `/native-village`, `/exile` | unordered |
  | `pile/<card>` | a pile, by the card or randomizer it is named after. Ordered |
  | `aside/<card>` | cards a card set aside for the game: the Black Market deck, Way of the Mouse's card. Ordered |
  | `trash` | ordered |

  `<seat>` is a player's index in turn order, from 0. An **ordered** zone lists its cards
  top first. An **unordered** zone lists them in the order they arrived. A seat's zones
  and the trash always exist, and are left out of a snapshot while empty; a pile exists
  from the moment the game has it, empty or not.
- **Counters** are integers, zero unless an event says otherwise:

  | Counter | |
  | --- | --- |
  | `actions`, `buys`, `coins`, `potions` | the turn's |
  | `<seat>/coffers`, `/villagers`, `/favors`, `/debt`, `/vp-tokens`, `/pirate-ship` | a player's |
  | `pile/<card>/vp`, `/debt`, `/embargo`, `/trade-route` | tokens on a pile |
  | `trade-route-mat`, `sun` | the game's |

- **The turn**: whose it is, which of theirs it is, the card that gave it if it is an
  extra turn, and its phase.

A **snapshot** is the table as JSON:

```json
{
  "zones": {"0/deck": ["Copper#249", "Estate#257"], "0/hand": ["Copper#254"], "pile/Village": ["Village#31", "Village#30"]},
  "counters": {"actions": 1, "buys": 1, "1/coffers": 2},
  "turn": {"player": 0, "number": 3, "phase": "buy"}
}
```

## Cards and viewers

A stream is written for a **viewer**, named in its header: `full`, `public`, or a seat.
Only `full` is specified so far: every card's face, every shuffle's order.

A card is written `Name#handle` when the viewer sees its face and `?` when not. A
**handle** names one physical card for as long as the viewer keeps seeing its face. In a
`full` stream every face is seen, always, so a card keeps one handle for the whole game.

The `public` and seat versions are the same language with less shown. What they must
not show goes beyond faces (see [Status](#status)), so they number their own events.

## The stream

JSON Lines. The first line is the header:

```json
{"schema": "dominion/events@1", "viewer": "full"}
```

Every other line is an event, in order:

```json
{"seq": 14, "type": "gain", "player": 0, "cards": ["Copper#45"], "from": "pile/Copper", "to": "0/discard"}
```

- `seq` counts from 0 with no gaps.
- `type` says what happened.
- `by` (optional) is the `seq` of the event that caused this one.

## Events

### `setup`

The first event. `rules` (`implementation`, `version`: what decides this game), `seats`
(the players' names, in turn order), `kingdom`, `landscapes`, and `table`: the snapshot
before anything happens. Each player's starting cards are in their deck, not yet
shuffled.

### Moves

Cards change zone. The `type` is the word the rules use, because the rules care which it
was: a card put into a hand is not gained; a deck put into its discard pile is not
discarded.

| Type | |
| --- | --- |
| `draw` | deck to hand |
| `discard` | to a discard pile, as a discard |
| `gain` | from a pile (or the trash) to a player, as a gain |
| `trash` | to the trash |
| `topdeck`, `bottomdeck`, `insert` | onto, under, or into a deck |
| `reveal`, `look` | off the deck into `looking`, for everyone or for the player |
| `set-aside` | to `aside` |
| `exile` | to the Exile mat |
| `return` | to its pile |
| `exchange` | one of an exchange's two moves: a card to its pile, another from a pile |
| `pass` | to another player |
| `rotate` | from the top of a pile to its bottom |
| `put` | any other placement |
| `shuffle` | see below |

Fields:

- `player`: whose action it is.
- `cards`: the cards, in the order they move.
- `from`, `to`: zones.
- `at` (optional): where they arrive in an ordered `to`: `"top"` (the default),
  `"bottom"`, or `{"under": n}` for under *n* cards.
- `pos` (optional): for an ordered `from`, how many cards lay over each card when it
  left. Absent when each came off the top.

The cards leave `from` and arrive in `to` **one after the other**, in the order listed.
So of cards put on top of a deck, the last listed ends up on top; of cards put at the
bottom, the last listed ends up lowest. In an unordered zone a card arrives at the end.
A move within one zone (`from` equal to `to`) takes the card out and puts it back at
`at`.

**`shuffle`** is the exception: its `cards` are the result, top first. They leave `from`
and arrive in `to` **together**, in the order listed, at `at`. A discard pile shuffled
under a deck is `"from": "0/discard", "to": "0/deck", "at": "bottom"`; a deck shuffled
where it is has `from` equal to `to`.

### `play`

`player`, `card`: the card is played, and its instructions are followed. With `from` and
`to` (and `pos` for an ordered `from`) it goes into play as it is played. Without them
it moves nowhere: a card played again by Throne Room, or played where it lies.

### What a player does that moves no card

| Type | Fields | |
| --- | --- | --- |
| `buy` | `player`, `card` | a card or landscape is bought: paid for, before it is gained or does anything. `card` is a name: what is bought is a card of that name |
| `resolve` | `player`, `card` | an ability of `card` begins to resolve for `player` |
| `name` | `player`, `card` | a card is named |
| `way` | `player`, `card`, `way` | the play uses a Way instead of the card's instructions |
| `unaffected` | `player`, `attack`, `card` | `attack` doesn't affect `player`, because of `card` |
| `call` | `player`, `card` | a Reserve card is called from the Tavern mat |
| `choose` | `player`, `source`, `choices` | a choice said to everyone: a card's modes, a number |
| `turn-skipped` | `player`, `extra`, `lost` | a turn that doesn't happen: skipped, or `lost` as a third in a row |

These change nothing on the table.

### `add`

`cards`, `to`: cards come into the game in `to`, each on top of the one before. A pile
that wasn't there now is.

### `rename`

`card`, `name`: the card is now a card called `name`, with the same handle.

### `turn`

`player`, `number` (which of that player's turns it is, from 1), and `extra` (the card
that gave it) for an extra turn. The phase becomes `start`, and the turn's counters
become 1 Action, 1 Buy, $0 and no Potions.

### `phase`

`phase`: `start`, `action`, `buy`, `night`, `cleanup` or `end`. A turn has as many as
the rules give it, in the order they happen: a turn that returns to its Action phase
(Villa, Cavalry) has two Buy phases.

### `counter`

`counter`, `delta`, `value`: the counter changed by `delta` and is now `value`. A stream
whose `value` isn't the counter's old value plus `delta` is not one game's.

### `game-end`

`reason` (`provinces`, `colonies`, `piles`, `turn-limit`, `resigned`) and `result`: per
seat `vp`, `turns`, `rank` (from 1; ties share one) and `resigned`.

## An opening

```jsonl
{"schema":"dominion/events@1","viewer":"full"}
{"seq":0,"type":"setup","rules":{"implementation":"dominion-engine","version":"0.1.0"},"seats":["P1","P2"],"kingdom":["Throne Room","Sentry","Workshop","…"],"table":{"zones":{"0/deck":["Copper#248","Copper#249","…"],"pile/Copper":["Copper#45","…"]}}}
{"seq":1,"type":"shuffle","player":0,"cards":["Estate#256","Copper#254","Copper#248","Copper#251","Estate#255","Copper#249","Estate#257","Copper#252","Copper#250","Copper#253"],"from":"0/deck","to":"0/deck","pos":[8,6,0,2,4,0,3,1,0,0]}
{"seq":2,"type":"draw","player":0,"cards":["Estate#256","Copper#254","Copper#248","Copper#251","Estate#255"],"from":"0/deck","to":"0/hand"}
{"seq":5,"type":"turn","player":0,"number":1}
{"seq":6,"type":"phase","phase":"buy"}
{"seq":7,"type":"play","player":0,"card":"Copper#254","from":"0/hand","to":"0/play"}
{"seq":8,"type":"counter","counter":"coins","delta":1,"value":1}
{"seq":13,"type":"buy","player":0,"card":"Copper"}
{"seq":14,"type":"counter","counter":"buys","delta":-1,"value":0}
{"seq":15,"type":"gain","player":0,"cards":["Copper#45"],"from":"pile/Copper","to":"0/discard"}
{"seq":16,"type":"phase","phase":"cleanup"}
{"seq":17,"type":"discard","player":0,"cards":["Copper#254","Copper#248","Copper#251"],"from":"0/play","to":"0/discard"}
{"seq":18,"type":"discard","player":0,"cards":["Estate#256","Estate#255"],"from":"0/hand","to":"0/discard"}
{"seq":19,"type":"draw","player":0,"cards":["Copper#249","Estate#257","Copper#252","Copper#250","Copper#253"],"from":"0/deck","to":"0/hand"}
{"seq":20,"type":"phase","phase":"end"}
{"seq":21,"type":"turn","player":1,"number":1}
```

## Status

`dominion-engine` writes the **full** stream (`dominion-agent`'s `events::Recorder`), and
`dominion-protocol`'s `events::Table` folds it. Over random games of every set the fold
equals the engine's table at every decision: every zone with its order, every counter
above, the turn's player and phase.

Not written yet, in the order planned:

1. `by`: what caused each event.
2. Boons, Hexes, States and Artifacts being received and returned.
3. The rest of the table: Adventures tokens and the −Card, −Coin and Journey tokens,
   Project cubes, Artifacts, States, Boons and Hexes, Traits; lasting effects with the
   cards they keep in play or hold; extra turns waiting; a card that is another card
   while in play; what the rules derive (costs, VP).
4. The `public` and seat versions. Review found that masking faces is not enough: a
   position in a discard pile its owner searched, the order of cards put back
   privately, and whether a seat was asked at all (Library asks only about an Action)
   each say something about hidden cards. So a viewer's stream has its own numbering,
   says where a card left only when that viewer could see it, and holds face-down cards
   set aside in a zone per holding.
5. Decisions: what a seat was asked and answered. With every shuffle's order these are
   everything that caused the game, so an engine can be driven by a full stream and
   checked against it.

Known imprecision: a phase the turn passes through with nothing happening in it is not
reported. A move between two zones nobody owns is given to the turn's player.

Out of scope: undo, clocks, chat, who is connected. Those belong to whatever hosts a
game, not to the game.
