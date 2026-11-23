# Dominion Strategy Basics

Principles that strong players broadly agree on. Unless noted, they assume
2-player games, which is how most competitive play happens.

Everything here is a rule of thumb, including every number. Dominion has
almost no strategy rules that hold on every board, because the kingdom
shapes each game: how fast decks are, when to green and which cards are
strong all move with it. Start from these defaults, and when a card on
the board gives a reason to depart from one, follow the board and name
the reason.

## Deck composition

Dominion is a game about what is in your deck. You never choose your hand:
each turn you draw five cards from a deck you built. So the decisions that
last are what goes into the deck and what comes out of it. Every gain,
trash and Victory card changes the deck's composition, and the composition
decides what every later hand can be.

- **A card is good if a deck with it produces better turns than a deck
  without it.** No card is good in isolation. A Gold lifts a deck of Coppers
  and Estates, and can stop a turn in a deck that draws itself. Judge every
  gain, Treasure and Victory cards included, by what it does to the hands
  you will draw.
- **Every card dilutes the others.** Adding a card makes each other card
  turn up less often. Junk (Coppers, Estates, Curses, Ruins) is pure
  dilution. Victory cards are junk you choose to take, which is why
  greening has a cost.
- **Proportions matter more than counts.** One copy of a key card is in a
  given 5-card hand one turn in three in a 15-card deck, and one turn in
  six in a 30-card deck.
- **Tempo compounds.** Games between strong players mostly end between
  turns 11 and 15, later with Colonies, and the fastest decks end them by
  turn 8 or 9 (see "How fast decks are"). A card gained early is drawn many
  more times than one gained late, so early gains should improve the deck
  and late gains mostly need to be points.

## Payload and deck control

Every card in a deck does one of two jobs: it is worth playing, or it helps
you play the cards that are. This split, from Adam Horton's
[Payload and Deck Control](https://adamhorton.com/flog/dominion-payload-and-control/),
is the main tool for judging what a card does for a deck.

- **Payload** is what a turn produces once you have played your cards: $
  to spend, Buys to spend it with, cards gained, VP tokens, and harm to the
  opponent. In a plain money deck the payload is its Treasure (see
  "Payload").
- **Deck control** lets you play your other cards: draw, villages,
  thinning, sifting and top-of-deck control (see "Deck control"). Junking
  the opponent attacks *their* deck control.
- **Dead cards** do neither: Victory cards and Curses once they're in your
  deck, or a trasher you no longer need.
- **Hybrids** (e.g. Grand Market, Torturer) do both. They're usually very
  strong, and the right move is often to add them as fast as possible.

The two limit each other. Payload is worth only as many plays as deck
control gets it per turn, and deck control is worth only the payload it
reaches. Name the job of each card before you add it, and ask which of the
two the deck is short of.

## Reliability

Because every hand is drawn at random, a deck has a spread of possible
turns, not one turn. How often it produces the turn you need matters as
much as how big that turn is.

- **Prices are thresholds.** $9 buys what $8 does, and $7 buys what $6
  does. $ above a price is mostly wasted and $ below it loses the gain, so
  a deck that hits $8 on 70% of turns beats one that alternates between $11
  and $4.
- **A plan is worth its typical turn, not its best one.** A deck built to
  draw itself is only as good as how often it does. A stalled turn of
  villages and draw is often worse than a money turn, because those cards
  produce nothing on their own. A plan that completes on half its turns
  usually loses to plain money (see "The Big Money baseline").
- **What makes a deck reliable**: thinning, so draw finds draw; one or two
  cards of spare draw beyond exactly enough; an Action for every terminal
  the turn plays; non-terminal draw, which can't collide; Actions and cards
  that arrive at the start of the turn (Durations); top of deck control
  that puts the key card in hand; and enough copies of any card the turn
  can't do without.
- **What makes it unreliable**: a single copy of a key card; terminal
  draw with too few Actions; junk, which dilutes draw; handsize attacks,
  which cut the hand a turn starts from; and draw that leaves the
  reshuffle to chance late in the turn.
- **Money's strength is reliability.** It never stalls, it only
  fluctuates, which is why it is the baseline. A plan that beats money on
  its good turns but not on average loses to it.
- **A built engine is more reliable than money.** Money never stalls,
  but it hits $8 only about half its turns. A deck that draws itself
  plays the same cards every turn. Unreliability is a risk while the
  engine is building, and the fix is spare draw and Actions, not a
  money plan.
- **Reliability decides when to stop building.** Add a spare village or
  draw card before more payload whenever the deck still stalls, and
  especially when ahead (see "Risk and luck").

## Deck control

Deck control is how much of your deck you can play in a turn, and how much
say you have in which cards. Without it, a turn is a random five cards and
the deck produces its average hand. With enough of it, a deck draws itself
every turn and produces the sum of all its cards, so each payload card adds
directly, which is why such decks keep growing. Junk, greening and the
opponent's attacks erode deck control, so it has to be maintained.

### Terminal slots and collision

A *terminal* is an Action that gives no +Action. A turn starts with one
Action, so without villages each turn has one **terminal slot**: room to
play one terminal.

- **Collision**: draw two terminals together without a village and one of
  them is dead. Two terminal openers land in the same hand on turn 3 or 4
  about 30% of the time.
- **Over-terminaled**: a deck holding more terminals than its turns have
  slots. Size the budget by the cards a turn sees, not by deck size: a
  turn that sees h of N cards finds about T×h/N of its T terminals, and
  only one fits. With 5-card hands and no village, that is roughly one
  terminal per 8–10 cards. Draw tightens it: a turn that sees 8 cards has
  room for about one per 13–16, and a deck that draws itself has room for
  one terminal in all, however big it is. Past the budget, a new terminal
  collides often enough that Treasure or a non-terminal is usually the
  better gain, whether bought or gained.
- **Slots are a budget.** Every terminal you add competes for the same
  slots, so a terminal is worth only what it adds over the best other use
  of the slot. A $2 terminal can cost you a turn's play of your draw card
  or your attack.
- **Villages add slots, and non-terminals use none.** Treasures and
  *cantrips* (cards that give at least +1 Card and +1 Action, so they
  replace themselves) never collide. A cantrip's bonus (+$1, +Buy,
  trashing, an attack) is close to free: it costs a gain and a place in
  the deck, but no slot and no space in the hand. Its +1 Card is worth
  nothing once you draw your whole deck.

### Draw and villages

Further reading: Adam Horton on
[draw](https://adamhorton.com/flog/dominion-draw/) and
[villages](https://adamhorton.com/flog/dominion-villages/).

- **Draw** is anything that increases your hand size. Most of it is
  +Cards on an Action, but Durations, Night cards and Treasures can draw
  too. A cantrip only replaces itself, so it isn't draw.
- **Non-terminal draw** (Laboratory: +2 Cards +1 Action) grows your hand
  and keeps your Action, so any number of copies can be played in a turn.
- **Terminal draw** (Smithy: +3 Cards) grows your hand more per card but
  uses your Action, so playing more than one needs Actions from elsewhere
  (see "Terminal slots and collision").
- **A village** is anything that lets you play more than one terminal in a
  turn. That includes Throne Room and King's Court. Cards that at best
  replace the Action they use, like Conspirator, Ruined Village or Vassal,
  are not villages.
- **A village doesn't have to be an Action card that says +2 Actions.** A
  spare Action can arrive at the start of your next turn from a Duration or
  Night card, or come from Villagers. A Night card costs no Action to play,
  so one that leaves +1 Card and +1 Action for next turn (Ghost Town) nets
  the same as a Village, and it can't be drawn dead after your Actions run
  out. Its Action comes a turn late, so it doesn't rescue the hand it is
  drawn in. Find villages by reading every card's whole text for Actions
  and Villagers, not by its name or type line.
- Many cards draw or act as villages only with support: an action-dense
  deck, a way to line cards up, a pile emptying, Favors, a specific trasher.
  Before relying on one, check that this board provides that support.
- A village that works once per turn (Crossroads), or only under a
  condition, caps how many terminals you can play. Count the Actions a real
  turn gets, not the number of village cards.
- **Setting up the next hand counts too.** Durations that draw at the start
  of the turn, gains that land on top of your deck, and cards that order the
  top of your deck all put chosen cards into your next hand without using
  Actions. If something can put the same key card (the only village, the
  trasher, the payoff) in your hand every turn, a deck that looks
  inconsistent may be reliable.

Even without cards that increase hand size, a chain of cantrips can cycle
through most of a deck once strong thinning has cut it down to a dozen
cards. Check how quickly you can thin and what the cantrips do before
choosing between a thin cantrip deck and money. Villages matter only in
proportion to terminals: non-terminal draw needs none.

### Thinning: addition by subtraction

*Thinning* removes cards from the deck you draw from. It looks like a loss:
a trashing turn often buys nothing, and the deck ends up with fewer cards
and less total money. But a hand is five cards drawn from the deck, so what
matters is the average card, not the total. Removing any card worse than
the average makes every later hand better.

- **Each good card turns up more often.** One key card in a 12-card deck
  is in a given hand 5 times in 12. Trash 3 Estates and 2 Coppers and it
  is in 5 hands in 7.
- **Copper is junk once the deck is better than Copper.** In the starting
  deck the average card is worth $0.70, so trashing Estates alone lifts the
  average hand from $3.50 to $5. Once your average card is worth more than
  $1, every Copper drags hands down too.
- **Every later gain is worth more.** In a 10-card deck a new Gold is drawn
  about every other turn; in a 25-card deck about one turn in five. A thin
  deck gets more plays out of everything it adds, and that compounds.
- **Draw finds draw.** In a thin deck a few draw cards play the whole
  deck, so thinning is what lets a deck reach "draws itself every turn".
- **It's one of the strongest effects in the game, and the default whenever available.** Chapel costs $2 and
  does nothing but trash, and it rates in the top tier — but thinning doesn't
  need to be Chapel-fast to decide a game. Even one-card-per-turn trashing
  (including non-terminal, Duration, or multi-mode cards that offer trashing
  as one option) compounds over a whole game and usually beats skipping
  thinning for extra economy. Don't pass up strong or steady trashing because
  a turn spent trashing looks empty.

In practice:

- **Trashing** (Chapel, Sentry, Steward, …) is the usual way. With fast
  multi-card trashing, on turn 3 or 4 trash your whole hand, even if it's
  only Coppers (except a hand holding your other opener).
- **If you buy a trasher, play it early.** A trasher only pays off when it
  actually removes starting cards in the first few shuffles. Repeatedly
  skipping or discarding your trasher for small short-term bonuses (a couple
  of VP, a modest terminal play) leaves you with a bloated deck while an
  opponent who thins pulls permanently ahead.
- **Thinning stops paying once the deck draws itself.** The average-card
  argument holds while a hand is a sample of the deck. A deck that plays
  every card makes their sum, so removing a card that makes $ lowers
  every later turn by that much: there a Copper is $1 of payload, not
  junk. From then on trash what makes nothing, and anything else only if
  the total left still reaches the price you need (see "Count what the
  deck makes").
- A trasher that goes dead late in the game has usually already paid for
  itself.
- Thinning matters less where the deck wants many cards (card-count VP),
  where junk arrives faster than you can remove it, or where a board rule
  puts trashed cards back into players' decks (which also weakens cards that
  rely on a clean deck or drawing two specific cards together).
- **Thinning without a trasher.** Anything that takes a card out of your
  deck for good thins it: Exile, a mat, or a card that turns one card into
  another (Remodel; Displace Exiles a card and gains one costing up to $2
  more). A swap removes one card per play, which is slow, but each play
  also adds a part: a Copper becomes a $2 piece and an Estate a $3 or $4
  one. Exiled Victory cards still score, so Exiling Estates costs no
  points. Before calling a board "no trashing", check every card for one of
  these.

## Payload

Every deck has payload; in a plain money deck it is the Treasure. Payload
counts *relative* to the opponent, so attacks, denying a key pile, and the
ability to end (or threaten to end) the game on piles while ahead are
payload too. Early in the game, gainers such as Workshop are payload that
builds the deck rather than scoring.

### +Buy turns a big turn into points

You score by gaining Victory cards, and each Buy gains one card. So
without +Buy, gainers or VP tokens, a turn's payload is capped at one
card, whatever $ it makes: $16 buys one Province, the same as $8. A deck
that draws itself every turn then takes one Province a turn at most. That
is still about twice a money deck's rate (see "The Big Money baseline"),
but it has to win back the turns it spent building. A one-Buy engine
taking a Province a turn from turn 10–11 has 4 by turn 14, level with
BM+X, and pulls ahead from there, more so if it plays an attack every
turn or the top card is a Colony. So no +Buy makes the comparison close;
it doesn't settle it.

With +Buy, each extra Buy raises the ceiling by one card: $16 and 2 Buys is
two Provinces, $13 and 2 Buys is a Province and a Duchy. That is what lets
an engine catch up with and pass a money deck that started scoring earlier.
So the number of Buys a built turn can reach often decides whether an
engine is worth building at all. +Buy also speeds the build itself (a
village and a draw card in one turn, or several cheap parts), and it is
what makes a three-pile ending possible.

Other ways past one card per turn: gainers that gain without a Buy, Events
and Projects bought with spare Buys, VP tokens, and Victory cards that
gain or come with other cards. Count them alongside +Buy.

A gainer that trades a card up (Remodel and its relatives) is one more gain
each time it is played, so in a deck that plays most of itself several
copies act like several +Buys. That holds only while it has fodder: ask
what it trashes, and whether the deck makes that card again every turn. A
card that gains a Silver or other cheap card each play supplies it, and
then each extra copy of the gainer turns that byproduct into an engine part
while building and a Duchy or Province at the end. Count the copies the
fodder can feed, not one.

### Payload depends on the deck

Whether a payload card is good depends on whether the deck around it can
play it many times per turn.

- **Flat payload** pays about the same every time it is played: Gold, a
  terminal that gives $2, a cantrip that gives $1. It is as useful in a
  money deck as in an engine, and its value doesn't grow with copies.
- **Stacking payload** pays off only when several copies, or several
  plays, land in one turn: cost reduction, +Buy terminals with a small
  bonus, multipliers, effects that count cards in play. Bridge is the usual
  example. In a money deck it is a weak terminal: $1, a +Buy you rarely
  use, and $1 off a single purchase. In an engine that plays four or five
  Bridges, each one cuts every purchase that turn by $1 and adds a Buy,
  which can take several Provinces at once.

So judge payload cards after deciding how much of the deck this board lets
you play. A card that looks like the board's best payload may be close to
useless in the deck the board actually wants, and the reverse.

- **Before the game**, work out the best payload this kingdom allows, given
  its deck control. Ten Bridges is no payload without villages to play them.
  If the ceiling is about one Province per turn, a complex deck has to win
  by taking it every turn, sooner than money's every other turn: compare
  the worked lines (see "+Buy turns a big turn into points").
- **If deck control is weak** (little draw or trashing), you won't
  reliably play your full payload, so build less.
- **Once your deck is under control**, balance adding payload against still
  drawing most or all of your deck each turn.

### Count what the deck makes

A deck that draws itself has a ceiling: what it makes with every card
played. No turn can beat it, so know the number. Count it when the deck
starts drawing most of itself, and again before a card that makes $
leaves it.

- **Total $** is Treasure, plus $ from Actions, plus tokens you would
  spend. Treasure alone undercounts a deck whose money is on its Actions.
  Count a card that either draws or makes $ once: if the turn needs it to
  reach the rest of the deck, it isn't money. Take off what the turn's own
  plays must trash or discard.
- **Set it against the prices the turns left need**: $8 for a Province,
  $13 and two Buys for a Province and a Duchy, $16 and two Buys for two
  Provinces. Include the turn that decides the game, which often needs
  the last Province.
- **A total that only just reaches the price isn't reliable.** It needs
  every money card in the same turn, so one missed draw or forced trash
  drops it a price step. Keep $1–2 spare, as with spare draw.
- **A total below the price can't be fixed by drawing or thinning.** The
  next gains have to be payload. In a thin deck that is quick: one Gold
  adds $3 to every later turn.
- **Trashing for benefit spends the deck.** The VP, Villagers or gain from
  trashing a card that makes $ is paid once, and the $ is lost on every
  turn left. Dropping from a Province to a Duchy costs 3 VP a turn, so a
  trash that gains 3 VP and causes that drop is behind after two more
  turns. The same holds for trashing a core draw or village card for points:
  cannibalizing deck control before the finish is guaranteed can turn a
  lead into a bricked final turn. Trashing a working piece is right on the
  last turn or two, when the remaining deck still clears the price reliably
  afterwards, or when the same turn replaces the card. Check too that the
  rest of the game will use what the trash pays for.

### Gold, Treasure gainers and Coffers

- **Gold in an engine** is a card that doesn't draw, so it can stop your
  turn. Add it late, once draw can absorb it, and prefer gaining it free
  over buying it.
- **Treasure gainers**: time them for when the deck can draw the gained
  Treasure that turn. In money decks they free your buys for other things.
- **Coffers**: spend them early, because early gains compound. In the
  midgame keep one or two to hit key prices. Late, hoard them to guarantee
  $8 or to threaten a turn with several Provinces (with +Buy). A second
  source of Coffers adds less than the first.

## The Big Money baseline

"Big Money" means buying only Treasures and Victory cards. It's the
benchmark every plan should be measured against: a floor to beat, not a
likely pick. With the full modern card pool, most boards have an engine or
another plan that beats it, and strong players rarely end up playing money.

- Buy Province at $8, Gold at $6–7 and Silver at $3–5. Start buying Duchies
  at $5–7 once 4–5 Provinces are left, and Estates at $2–4 near the very end.
- With Colonies, buy Colony at $11 and Platinum at $9–10, and take Gold
  rather than a Province at $8 until the Colonies start running low.
- **Big Money + X** adds one or two copies of a strong terminal, such as
  Smithy, a good attack or a strong draw card. It is a solid default when
  the kingdom offers nothing better. A good BM+X deck takes 4 Provinces by
  roughly turn 14–17.
- **Choosing X when the opponent also plays money**: count what each X
  takes from their turns as well as what it adds to yours. A money deck
  has no draw to recover lost cards, so a hand-size attack turns many of
  its Province hands into Gold hands and its Gold hands into Silver hands.
  That is often worth more than a second draw card.
  Plan enough copies to play the attack on most turns, within your
  terminal slots (see "Terminal slots and collision"), rather than one copy
  that is played about one turn in three.
  Hypothesis, from a rough simulation of one board without villages
  against a money bot: Militia with Smithy beat Smithy-BM, and two Militias
  beat both by a wide margin. The size of the gap is unconfirmed.
- **Big Money doesn't choke.** Optimized plain Big Money keeps taking about
  one Province every other turn for as long as the game lasts. On its own
  it empties all 8 Provinces in roughly 21–23 turns
  ([ragingduckd, "The Myth of Big Money Choking"](http://forum.dominionstrategy.com/index.php?topic=9512.0)).
  Don't assume a money opponent stalls once they green. Use these numbers as
  the race clock any slower plan has to beat.
- Any plan that can't beat a competent BM+X in this kingdom is a mistake.

## Archetypes

Each archetype is a different answer to how much deck control the board
supports and what payload it rewards. Engines are usually the strongest,
so look for one first.

- **Engine**: enough deck control (draw, thinning, and Actions for its
  terminals) to play most of the deck, plus payload that scales past one
  card per turn. Aim to draw most of your deck each turn and gain several
  cards, often more than one Province, per turn. Engines start slower but
  usually win (see "Engines" below).
- **Money / BM+X**: few Actions, lots of Treasure, greens early. The right
  plan only on the minority of boards that lack draw, or where a junker
  or rush punishes slow decks and nothing answers it.
- **Good-stuff deck**: no real draw, but a few good non-drawing
  terminals (still one slot a turn without villages, so keep to the
  budget in "Terminal slots and collision"), cantrips and Silver-like
  cards. Buy whatever helps your next
  turn most, add Silver and better Treasure, and skip terminal draw.
  Junking that the board's draw and trashing can't answer pushes toward
  this deck. A lone village earns its place only
  once you have several terminals worth playing together
  ([Wandering Winder](http://wanderingwindergames.blogspot.com/2015/07/dominion-good-stuff-deck.html)).
  It is the answer to a board without real draw, not a rival to an engine
  on a board that has one. There, the strong non-drawing cards are the
  engine's payload, bought once the deck can draw them.
- **Thin cantrip deck**: halfway to an engine. Nothing increases hand
  size, but thinning cuts the deck to a small one that is mostly cantrips,
  so a turn plays nearly all of it: every cantrip, plus the five cards
  left in hand. It needs strong thinning, started early and removing most
  of the starting cards, and cantrips that carry payload ($, +Buy, an
  attack). With weak or slow thinning the cantrips only cycle a deck of
  Coppers, and money or a good-stuff deck is better.
- **Slog**: heavy junking (Curses, Ruins) or no good draw make big turns
  impossible. Gain many cards, value cheap or alternative VP, and expect a
  long game.
- **Rush**: race to empty three piles, e.g. Workshop/Gardens or a cheap
  pile plus +Buy. Strong only when the kingdom enables it and the opponent
  can't punish it.
- **Combos**: a plan built around a specific interaction (see "Interactions
  to look for"). Always look for them, but check that they beat the plain
  options. Against one, count how many copies of the key card it needs and
  contest that pile; if you can't deny it, work out when it finishes and
  whether a faster plan or a three-pile ending gets there first.

## How fast decks are

Reference points for a race, from commentated top-level games and designers'
solo playtests. They assume a strong player and no interference. They are
typical values, not limits: the kingdom moves them, so work out what this
board's cards do to each plan rather than reading the number off.

- **Money**: BM+X has 4 Provinces around turn 14–17 and doesn't speed up
  (see "The Big Money baseline").
- **Engines**: a well-built engine has its first big turn (two or more
  Provinces, or the same in other VP) around turn 8–11, and wins or ends the
  game by turn 11–14. No trashing, pieces at $5 or a junker each cost it a
  turn or two. They rarely cost it the race.
- **Combos and one-huge-turn decks**: the fast ones finish in 8–10 turns,
  and a few have their one turn as early as turn 7.
- **Whole games** between strong players mostly end between turns 11 and
  15.

No turn is too late in itself. A plan is too slow only when another plan
on the same board, or the opponent's deck, ends the game or takes the
points first.

An estimate of an unfamiliar deck runs late, often by five turns or more:
it counts one gain per turn, leaves out the helpers and stops at the first
stall. For money it is about right, because money is simple. So "the engine
arrives around turn 15" is weak evidence against the engine. Check it
against these numbers before trusting it. A simulation runs late the same
way: it plays only what its policy knows, so a policy that gains one card a
turn can't see a deck that gains three.

### Colony games

The numbers above are for games that end on Provinces. With Colony and
Platinum in the Supply, games run longer, often by several turns:

- The top card costs $11 and is worth 10 VP to a Province's 6. A deck
  capped at $8–10 falls behind one that reaches $11 most turns, so every
  plan needs more economy before greening pays.
- Money gains least from the extra turns. BM+X reaches $11 only with
  several Platinums, while a deck that draws itself with +Buy takes two or
  more Colonies a turn. Building that pays off late (draw, +Buy, payload,
  VP that adds no card) has more turns to repay itself, so it gets the
  benefit of the doubt unless something can end the game first.
- The game still ends when the Provinces run out or three piles do. It
  runs long only while nobody who can end it wants to. Ask who is ahead on
  the projected split (see "Who's ahead") and whether they can empty the
  Provinces or three piles. If they can, use that ending as the clock, not
  the Colony pile.

## Engines

Engines are usually the strongest decks a board allows, and most boards
allow one. A deck that plays most of itself each turn gets the full value
of every card in it, keeps growing as it adds payload, and can take
several Provinces a turn where a money deck takes one. So start every board
by looking for the engine, and settle for another archetype only when the
board can't support one or a faster plan beats it.

**The engine gets the benefit of the doubt.** When the board has draw that
can reach most of the deck and the Actions to play it (a village with
terminal draw, or non-terminal draw), the engine is the plan. Choosing
anything else needs a compelling reason, shown with a worked line for
both plans. Compelling reasons are few:

- A rival plan ends the game, or takes a lead the engine can't recover,
  before the engine's first big turn, judged against the speeds in "How
  fast decks are".
- A junker or attack the engine has no answer to: nothing trashes the
  junk, and the draw can't outgrow it.
- No way past one card per turn, on a Province board with no attack worth
  playing every turn, and the worked lines show money keeping pace (see
  "+Buy turns a big turn into points").

Not reasons on their own: parts at $5 or more, no trashing, a conditional
village, a slower start, "money is simpler", strong non-drawing cards
elsewhere on the board, or a guessed turn count for the engine. Each costs
the engine a turn or two at most, and the build should work round it.

What an engine needs follows from payload and deck control, not from a
fixed list of cards:

- **Draw that reaches most of the deck** (see "Draw and villages").
- **An Action for every terminal the built turn plays, and no more.**
  Villages exist to give terminals slots. Payload that gives +Actions
  (Festival) supplies its own. A deck whose draw and payload are all
  non-terminal needs no village at all: Laboratories for draw, Treasure for
  money and a non-terminal +Buy (a cantrip, a Treasure or an Event) are an
  engine.
- **Payload that scales past one card per turn**: +Buy from any source,
  gainers, VP tokens or a repeatable attack.
- **Thinning** of any kind (see "Thinning: addition by subtraction"), or
  draw strong enough to beat the junk. Strong engines can overcome Curses.

Any of these can come from a card that doesn't look like it, so read the
whole board for each before deciding one is missing. None of them has a
price limit: some engines are built entirely from $5 cards.

### Judging one

Engines are harder to estimate than money, and that is the usual way they
get underrated. Write the build out turn by turn: the opening, when the
deck first draws itself, how often it does after that, and what a built
turn produces. Compare that with the reference speeds in "How fast decks
are" and with the board's other plans. An engine that looks slow or awkward (expensive parts, a
conditional village, no village at all) is not evidence either way.

Things that weaken an engine, to weigh rather than to rule it out:

- The only "draw" is cantrips. With strong thinning that can still be a
  thin cantrip deck; without it a good-stuff deck is usually better (see
  Archetypes).
- Draw with nothing to pay its Actions, or villages with nothing to draw.
- No +Buy, gaining or alternative payload, so a built turn still takes
  one Province.
- The opponent can three-pile or rush before the engine comes online.
- A key piece sits in one pile the opponent also wants.

### How to build one

- Open with trashing and economy, so you can afford the parts.
- **Build fast.** Gaining one card per turn is too slow. +Buy and
  Workshop-style gainers roughly double the build rate, and Remodel-style
  gainers turn Estates into engine parts. Prefer a $5 engine piece over
  Gold.
- Count terminals and Actions together: each terminal you add needs an
  Action on the turns it is drawn. Get draw before payload, unless the
  payload is a strong attack.
- **Actions and cards at the start of the turn are worth the most**,
  because that's when turns stall. Duration villages and duration draw
  (Fishing Village, Wharf) give them before you draw anything. Spread them
  across turns rather than bunching them.
- Aim for one or two cards of spare draw beyond exactly enough. That makes
  the deck consistent, which matters most against attacks and when you're
  ahead. Spare draw can be spent by gaining a card mid-turn and drawing it.
- Stop adding Treasure once the deck draws itself, unless Treasure is the
  payload, and add payload once it draws itself reliably.
- Don't overbuild past the payload ceiling. But when unsure whether to
  green, one more building turn usually costs less than it seems.
- **Contested piles**: when both players want the board's only source of a
  bottleneck (the sole village, primary draw, or main VP scaler), start
  contesting it early — waiting until the rest of your deck is built hands
  the split away. Conversely, don't chase a single pile split past what
  your deck's ratios can support: winning a split of terminal draw or extra
  villages while starving on Actions, draw, or scaling payload stalls your
  deck and concedes the board's other scarce piles.

### Building for one huge turn

Some decks save resources for a single game-winning turn: cards on mats
(Native Village), Reserve cards, banked Coffers, Villagers or Favors.

- Saving up means you don't use those resources while building, so playing
  your payload every turn usually builds faster.
- It's worth it mainly with an explosive finisher such as cost reduction
  (Bridge, Highway, Bridge Troll) stacked many times.
- Attacks of every kind hurt a saving deck badly. Check the opponent's
  attacks before committing.
- Start the big turn only when you can see it through, since a turn that
  fizzles partway can lose on the spot. If it can't end the game, make sure
  the opponent's best reply can't win.

## Interactions to look for

Many boards are decided by how two cards (or a card and a landscape) work
together. Nearly every interaction is one card supplying something another
card wants: a gain, a discard, a trash, a card on top of the deck, a type, a
card in play.

Look for them before the game, and again during it whenever a new card
appears: a Black Market reveal, a Loot, a card the opponent starts buying.

**This list is not complete.** It shows the kinds of things cards care
about, so that you recognise the same shape in cards that aren't named
here. Expect a board to have interactions that fit none of these. When a
card on the board cares about something, find what on the board supplies
it, whether or not the pair appears below.

### Something happens to a card

- **Benefits from trashing**: trashers paired with cards that reward being
  trashed or trashing. Fortress returns to hand when trashed. Market Square
  gains a Gold when one of your cards is trashed. Procession + Fortress
  plays Fortress twice and gains a card costing $1 more.
- **Gainers + on-gain effects**: Workshop-style gainers feeding "when you
  gain this" cards, e.g. Border Village also gains a cheaper card.
- **Discard for benefit + discarders**: Tunnel gains a Gold when discarded
  outside Clean-up, so it pairs with Warehouse or Vault, or an opponent's
  Militia. Discards from the top of the deck count too.
- **Cards that play themselves**: a card that plays itself when gained or
  discarded (Trail) uses no Action. A terminal gainer that gains one gets
  its Action back, and any discard effect becomes a way to play it.
- **Byproducts as fuel**: a card's side gain that looks like dilution (a
  Silver, a Ruins, a Curse you gain yourself) can be exactly what another
  card wants to trash, trade up or count. Then the first card feeds the
  second every turn, and the pair works as a loop: write it with what each
  turn produces and consumes (`kingdom-analysis`, "Resource loop"). Check
  every gain a card makes for a card here that wants it.
- **VP per gain or per play + cheap repeats**: VP tokens earned each time
  you gain or play something (Collection, Groundskeeper, Monument) pair with
  +Buy, cheap piles, cards that gain two at once, and anything that replays
  the scoring card.

### Where cards are

- **Top-of-deck control + a key card**: a gain that lands on your deck
  (Artificer, Tiara), a card put back from your hand (Courtyard), or the top
  of the deck put in order (Cartographer) decides part of your next hand.
  Use it to draw this turn's gains next turn, or to have the key card every
  turn.
- **Using a card twice**: anything that returns a played card to your deck
  or hand, or plays a card from somewhere other than your hand, can make
  one card work twice. Scheme puts an Action back on your deck, Herbalist
  does it for a Treasure, and Royal Carriage replays an Action. Check
  whether something else on the board can draw or play the returned card
  again in the same turn.
- **Where a gained card lands**: some cards are gained to your hand or onto
  your deck. A Night card gained to hand (Ghost Town, Guardian) works the
  turn you buy it, because Night comes after the Buy phase.
- **Draw-to-X + cards that shrink your hand**: Library draws up to 7, so it
  loves Festival and other villages that don't draw.
- **Hand contents**: cards that reward a particular hand (Menagerie wants
  no duplicates, Shanty Town wants no Actions) pair with trashing,
  discarding and Villagers.
- **Cards in play**: cards that check or count what is in play (Peddler's
  cost, Berserker's "an Action in play") pair with cheap cantrips and with
  Durations still out from last turn.

### What a card is

- **Cost**: trash-for-benefit cards (Salvager, Apprentice) want cards whose
  cost is high compared with what you paid: a Gold gained for free, Border
  Village, Peddler at its full $8 in the Action phase.
- **Cost reduction + gainers or +Buy**: lower costs let "gain a card
  costing up to $4" reach better cards and stretch each $, e.g. Highway or
  Bridge with Ironworks, King's Court + Bridge.
- **Types**: cards that count or check types want multi-type cards or a
  deck dense in one type. Courtier pays out per type, Ironworks gives both
  bonuses for an Action–Victory card, Vineyard counts Actions, and
  Crossroads draws per Victory card.
- **Names**: cards that reward differently named cards (Fairgrounds) want
  cheap variety, mixed piles and +Buy.
- **Multipliers on the right target**: Throne Room, King's Court and
  Procession on strong terminals, Durations and one-shots. Tiara and Crown
  do the same for Treasures that do something when played. Watch the risk
  of drawing a multiplier with nothing to multiply.

### Resources and piles

- **Tokens standing in for a missing piece**: Villagers let terminal draw
  work on a board with no village. Coffers smooth out awkward prices.
- **Piles**: cards that improve as piles empty (City, Animal Fair) pair
  with piles that drain fast: Curses under a junker, cheap piles, cards
  that gain copies of themselves. Cards that take from or return to the
  Supply (Lurker, Experiment) change who can end the game.
- **Alternative VP + enablers**: Gardens + Workshop (a rush), Duke +
  Duchy, and cards that make a cheap pile score.

### Landscapes and the opponent

- **Landscapes changing what cards do**: Way of the Mouse borrows a
  set-aside card. A Way can turn junk Actions such as Ruins into something
  useful. Events can supply +Buy where the Kingdom has none. A Trait such as
  Cheap can land on a key pile.
- **The opponent's turn**: some Reactions act when the opponent does
  something you can predict, such as gaining a Province (Fool's Gold) or any
  Victory card (Black Cat). They change what greening costs the opponent.
- **Counters**: cards that blunt the opponent's attack or plan. Library
  refills after a handsize attack, trashing removes Curses, and on-gain
  Reactions can swap a Curse for a Silver. Check the other direction too:
  your discard attack triggers the opponent's when-discarded cards, and
  cards you make them gain can help them.

An interaction is only worth building around if the result beats the plain
options, starting with Big Money + X.

## Openings

Sources: Adam Horton's
[Discipline in the Opening](https://adamhorton.com/flog/dominion-discipline-in-the-opening/)
and general community consensus.

Your two opening buys are a sixth of a 12-card deck, and each is drawn on
turn 3 or 4 five times in six. No later gain shapes as many hands.

- With the standard starting deck, turns 1–2 give $7 between them, split
  4/3 or 5/2 (5/2 is about 1 in 6). Heirlooms and Shelters change the
  starting deck, and some Heirlooms change the money: Cursed Gold makes the
  total $9. Work the splits out from the actual deck.
- **What the opening is for**, in order: trashing or a junking attack
  first, then gainers. Draw and payload rarely drive the opening. Buying
  Silver to reach $5 for a key $5 trasher or junker counts as working
  toward that goal. Opening a plain village is almost never right.
- **A gainer can reach the key price for you.** A card that trades up
  (Remodel turns a $3 Silver into a $5 card) gets the key $5 piece on a hand
  that can't buy it, and frees the Buy for something else. Gainer + Silver
  is then a strong 4/3: the Silver is both money and fodder.
- **A turn 1 buy that acts before the shuffle changes turn 2.** A card
  gained to your hand or onto your deck, a when-gain effect, or a Night
  card played the turn it is bought makes the turn 2 hand something other
  than the leftover five cards. Work that hand out before choosing, and
  the hands after it. Example: on a $3 turn 1, Ghost Town is gained to
  hand and played that Night. Turn 2 is then the known $4 hand plus one
  card from the reshuffled turn 1 hand (3 Coppers, 2 Estates), so it has
  $5 three times in five, a turn or two before a Silver opening can reach
  it. The cost is turn 3, which draws the other four of those cards plus
  one.
- **The turn 3–4 test**: if an opening buy won't do something useful on
  turn 3 or 4, look hard for something better. Durations and Reserves often
  miss the second shuffle. Know which price you need on turns 3–4 and avoid
  openings unlikely to hit it.
- **Turn order**: going first, an attack like Militia drawn on turn 3 can
  deny the opponent's first $5. Going second, it's much weaker, because you
  must draw it on turn 3 exactly.
- With 5/2, a strong $5 (Witch, Laboratory-class draw) plus a $2 trasher
  (Chapel, Lookout) can be much stronger than 4/3. Avoid a 5/2 that leaves
  the $2 slot weak.
- Buying nothing is a real option. A card that doesn't help the plan makes
  the deck worse, so with nothing useful at a price, pass.
- Don't open with two terminals that collide often unless their payoff is
  worth it.

## Attacks and defense

Attacks work on the opponent's deck. Junkers worsen its composition,
handsize attacks cut how much of it they play, and trashing attacks take
cards out of it.

- **Junking** (Curses, Ruins) is the strongest attack class: it costs the
  victim tempo and points.
  - A junker doesn't rule out an engine. On many boards the right plan is
    to buy the junker first and build the engine around it: the engine
    plays it more often and wins the split. Junking makes engines less
    viable when the board's draw and thinning are too weak to keep up with
    the junk arriving.
  - Thinning makes junk hurt less, since it can be trashed, but rarely
    makes a junker worthless: the opponent still spends plays removing
    junk instead of building. A junker can be worth skipping when their
    thinning would remove the junk at little extra cost, or when your deck
    can't spare the plays it takes.
  - Whether the opponent junks changes your plan too. An engine their
    junker would have shut down can become the best plan if they skip it.
  - You can ignore a junker only if your deck will draw itself before more
    than about one junk card per turn arrives.
  - Don't ignore active junking when solid trashing or anti-gain defense is
    available. A slow trasher alone won't outrun heavy junking if you stop
    building, so pair trashing with draw — or, when no efficient answer
    exists, lower your sights (Duchies / alternative VP).
  - **Conditional attacks need real support**: an attack or payoff that only
    fires under a condition (such as discarding multiple Actions, or pairing
    two specific cards in hand) does nothing unless your *actual* deck
    supplies that condition reliably and the board won't disrupt it. If you
    pivot away from its support cards, stop buying it.
  - With a junker in play, the Curse pile will empty. Curses plus Duchies
    make two of the three piles, so a three-pile ending is the money
    player's main weapon against an engine. Curses that players give
    themselves (Cursed Gold, Ritual) drain the pile much more slowly.
  - With a stacking attack like Torturer, don't always take the option that
    keeps your deck clean if it costs you your own attack plays.
- **Play an attack every turn**: if you can only play one attack per turn,
  still buy several copies so you play one every turn. A Duration attack
  stays in play through your next turn, so it takes two copies to attack
  every turn. The first copy of an attack on the opponent's economy is
  high priority, because it can stop them reaching the price of their own
  copy.
- **Hand-size attacks** (Militia, Ninja) hurt money decks and are usually
  weaker against decks that draw after the attack. The exception is
  attacks that punish drawing (Frigate): there, an attacking money deck can
  beat draw-heavy decks.
- **Trashing attacks** (Knights, Swindler): lean on gainers and rely less
  on Treasure.
- Defend with draw that refills your hand, with trashing, and with
  Reactions only when they're actually good. Attacks lengthen the game and
  make three-pile endings likelier.

## Greening and the endgame

Greening trades deck quality for points. A Victory card scores once, but
it is a dead card in every hand it lands in for the rest of the game. Its
real cost is the hands it spoils before the game ends, which depends on
how many shuffles are left and how much each hand needs every card.

- **The fewer VP a card gives, the later it pays.** A Province, a Duchy
  and an Estate are the same dead card for 6, 3 and 1 VP. So Duchies wait
  until the end is in sight, and Estates usually wait for the last turn or
  two.
- **Spare $ and Buys aren't free points.** An Estate taken on an early
  Province turn just because $2 and a Buy are left over is usually a
  mistake. It lands in many later hands, and each is a little less likely
  to hit its price. You can't count that cost exactly, but it always has
  to be weighed. The Estate can be right when the deck has far more
  reliability than it needs, or when the point builds a lead the opponent
  can't match (they have no +Buy, say). Otherwise a useful cheap card, or
  nothing, is usually better. Cheap VP is also fine when the game ends
  within about a shuffle, the point decides a close score, the card count
  is what scores, or the board takes away its cost.
- **Some boards take away the cost.** Ask of each card on the board
  whether it keeps Victory cards out of your hands while they still score,
  or makes them useful when drawn. For example, a way to Exile a card from
  your hand every turn (Sanctuary) makes an Estate close to a free point.
  VP that adds no card at all is the extreme case (below).
- Start buying Victory cards when the remaining turns are few enough that
  the points beat the economy you give up. The faster your deck can still
  improve, the later you green:
  - Gardens rush: immediately.
  - Duke/Duchy slog: once you reliably hit $5.
  - One-buy money decks: once you reliably hit $8.
  - Engines: once they reliably produce enough for two or three Provinces
    per turn ($13–18+).
  - Decks aiming for one huge final turn: only on that turn.
- Engines green late and fast. In engine mirrors, green earlier than you
  would against money. When behind against money, don't panic-green.
- **VP that adds no card to your deck** (VP tokens, and Landmarks or Events
  that pay them) has no greening cost. It can be taken while still building,
  so scoring starts much earlier than the list above suggests, and the
  Province pile stops being the VP ceiling.
- Track the score, the Province count and how close any piles are to empty,
  every turn.
- **Penultimate Province Rule**: don't buy the second-to-last Province if
  that lets your opponent win by buying the last one. A Duchy can be better.
  Exceptions:
  - If your deck has less future potential than theirs, take the Province
    now.
  - If you need both of the last two Provinces anyway, go for them.
  - In a tied game with one Buy each, player two buying the second-to-last
    Province can force a win, since taking the last one only ties and ties
    go to fewer turns.
- **Check the opponent's whole next turn**, not just the Province pile:
  unused extra turns (Seize the Day), stored Coffers, Villagers or Favors,
  cards on mats, how many +Buys and Golds they have left this shuffle,
  scaling or alternative VP they can score across one or two turns
  (multipliers, card-count thresholds, VP-per-gain combos), and any
  negative VP they can inflict on *you* (such as Curses given or Exiled)
  before ending the game.
- **Three-pile endings** are a real threat with +Buy, gainers, and cheap
  piles. Count how many gains each player can make to empty the piles; in
  mirrors, the number of gains often matters more than money.
  - **$0 and cheap piles (especially Curses)** cost little or no $ — only
    Buys, cursers, or gainers. A pile of 4 or 5 is not safe against an
    opponent who already has active +Buys or multi-buy turns.
  - **When behind, don't help empty piles.** Avoid dropping a contested
    pile to 1 (handing away a second empty pile) or buying low-VP cards
    from a shrinking pile while trailing an opponent who wants a three-pile
    finish, unless you can win the three-pile yourself.
- Colony games last longer and change who wants the game to end (see
  "Colony games").

## Who's ahead

The score counts points already taken. The decks decide the points still
to come. Early on almost all the points are still to come, so the score
says little: the player who greened first is often behind. Being ahead
means expecting more points by the time the game ends: the score plus
each deck's share of what's left.

- **Clocks**: when each deck reaches full output (draws its deck, or hits
  $8 with a Buy reliably), and how many points per turn it makes once it
  does. Compare them with "How fast decks are".
- **Projected split**: the Provinces and other VP left, shared out by each
  deck's rate up to the likely end. Add each share to that player's score.
- **The same plan on both sides**: compare directly: copies of the key
  cards, how far the thinning has got, junk taken, turns to the payoff. A
  shuffle's lead here is a real lead.
- **Banked resources**: Coffers, Villagers, cards on mats, Favors and the
  like are output that doesn't show in the deck.
- **Control of the end**: who can empty the piles or take the last
  Provinces when it suits them. A slower deck that controls the ending can
  be ahead.

Say how sure the read is and why. A mirror can support a firm assessment
when one deck has the same capabilities plus better thinning, key pieces
or reliability; sharing a strategy alone doesn't establish a lead. Being
clearly ahead still doesn't guarantee a win. Comparing unlike decks is
often less certain, and an estimate of an unfamiliar deck runs late (see
"How fast decks are"). If the evidence doesn't settle it, say so.

As the game nears its end, use the endgame check above: calculate the
scores after plausible finishing turns and replies. A score lead matters
in relation to what can still be scored and who controls the ending;
even a large lead can be overtaken by an engine's final turn or VP tokens.
Before then, judge position mainly from the decks and their clocks.

## Risk and luck

Judge ahead or behind as in "Who's ahead", not from the score.

- When ahead, cut variance: add a spare village, stop drawing to avoid a
  bad reshuffle, keep spare draw.
- When behind, take higher-variance lines. Late in the game, play for the
  luck you need: if you need both of the last Provinces, go for them.
- Player two starts at a disadvantage and can justify a little more risk.

## Multiplayer (3–6 players)

- Each opponent's attacks hit you, so defenses like Moat get better as the
  player count rises.
- Your own junker adds less, since the Curses split more evenly. One-card
  trashers can't keep up with several junkers.
- Key piles get contested, so value boards with substitutes for them. A thin
  deck adapts more easily than a bloated one.
- There's less time to build and less control over the ending: ask when you
  must green, given what the others are doing.
- Three-pile endings (four with 5–6 players) come sooner than you'd expect.
