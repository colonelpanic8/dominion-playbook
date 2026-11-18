# Worked example: a Recruiter / Wayfarer engine with no +Buy

One kingdom carried from analysis to a plan that won, with what a first
analysis missed. It is here to show the kind of analysis and plan this
skill asks for. Its conclusions belong to this board: don't carry Remodel
as +Buy, the target deck or any of its numbers to another kingdom unless
that kingdom gives the same reasons.

**Kingdom:** Tide Pools, Recruiter, Page, Scrying Pool, Bishop, Wayfarer,
Remodel, Develop, Bazaar, Destrier; Way of the Chameleon. No +Buy anywhere,
no Colonies, no Shelters.

**How it was tested:** about 25 two-player games between agents playing
written plans, plus an expert's games against them. Money lost to the
engine 1–3, and its one win came from a broken engine plan. The expert won
37–18 and 42–12. Written as the plan below (in slightly rougher wording),
the engine won all 4 games it played against the best earlier plans.

## What a first analysis got wrong

Two independent analyses called the board a payload problem: with no +Buy,
how does an engine score faster than one Province a turn? Both leaned
toward money or a small engine, at 55–65% confidence, and both backed this
with simplified simulations that ran too pessimistic. The engine won
easily. What they missed:

- **The constraint was the resource loop, not payload.** The deck works
  while Wayfarer's Silvers keep up with what Recruiter and Remodel eat.
  Step 3's "Resource loop" question finds this; reasoning card by card
  doesn't.
- **A gainer whose fodder is renewable is a stacking +Buy.** Both treated
  Remodel as one copy of a trimming tool. With Wayfarer making a Silver a
  play, each extra Remodel is another $5 part a turn, and late another
  Province. The expert built three.
- **Gains that set other cards' costs.** Wayfarer costs whatever was last
  gained, so a Remodel gain sets its price for the Buy. That only shows up
  when you play concrete hands.
- **Rules instead of ideas.** The first plans were buy lists and trash
  orders. Agents followed their gaps literally (Copper Remodeled into
  Copper, Recruiter fed Coppers for no Villagers, a Recruiter turned down
  to keep $5 for a buy that wasn't needed). Stating the plan as ideas, and
  allowing reasoned deviation, turned losing plans into winning ones.

## The analysis

**Board:** An engine board with no +Buy. Wayfarer and Recruiter draw,
Recruiter's Villagers play them, and Remodel is the way past one gain a
turn. Open question at first glance: how a one-Buy deck scores.

**Engine:** Wayfarer and Recruiter for draw, Villagers from Recruiter (and
Bazaar) for Actions, Recruiter for thinning, 2–3 Remodels as the extra
gains. Draws its deck by turns 7–9. Once built, 2–4 gains a turn, so two
Provinces a turn at the finish.

**Key interactions:**
- Wayfarer + Recruiter: each Wayfarer play gains a Silver; each Recruiter
  play draws 2 and trashes a Silver for 3 Villagers, which play 3 more
  Wayfarers. At about two Wayfarers per Recruiter, the loop feeds
  itself.
- Wayfarer + Remodel: a Remodel turns a Wayfarer Silver into a $5 part
  (Recruiter, Bazaar, Remodel). With the Buy, that is two parts a turn on
  a board with no +Buy, and each extra Remodel adds one more.
- Remodel → Wayfarer's price: Copper → Page makes Wayfarer cost $2, Estate
  → Silver makes it $3, so a $2–3 hand buys a $6 draw card from turn 3.
- Hero (from Page) + Remodel: Gold → Province, after which a spare
  Wayfarer costs $8 and a second Remodel turns it into another Province.

**Other cards:** Bazaar: Actions without eating a Silver, close to a
second-choice Recruiter. Destrier: non-terminal draw, cheap late in a
turn of gains, but a Wayfarer is usually better. Page: a $2 cantrip and
Remodel target; climbed to Hero, a source of Gold for Province Remodels.
Bishop: late VP without the Buy, only in a long game. Tide Pools: early
draw, later Recruiter food (4 Villagers). Develop, Scrying Pool: none.

**Plans considered:**
- Engine as above: Provinces from turns 9–11, then 1–2 a turn ·
  needs a Recruiter by turn 5 and Wayfarers in step with Recruiters ·
  weakness: a slow first Recruiter · the pick.
- Money with Page and Recruiter for thinning: $8 about every other turn
  from turn 8 · simple and reliable · one gain a turn with no way past it
  · would be the pick only if the engine couldn't draw its deck by
  turn 10.

**Recommendation:** the engine. At one Province a turn from turns 9–11 it
already keeps pace with money, and Remodel lifts its ceiling to two a turn.

**Open:** 4/3: Remodel / Silver · 5/2: Recruiter / Page.

**Least sure of:** how much to build against another engine. Building two
turns longer cost a game against a lean engine.

## The plan

Written for a player who carries the ideas, not a list of rules:

```
PLAN: An engine built around Recruiter and Wayfarer, using Remodel to gain the extra
parts that a board with no +Buy otherwise couldn't. The ideas below matter more than the
numbers: when your deck clearly needs something else, do that and say why.

HOW IT WORKS. Wayfarer and Recruiter are your draw. Wayfarer draws 3 cards and gains
you a Silver, and those Silvers fuel the rest of the deck. Recruiter draws 2 cards and
trashes one: a Silver gives 3 Villagers, which let you play more Wayfarers. Remodel
turns a Silver into a $5 part (a Recruiter, a Bazaar, a cheap Wayfarer, another Remodel)
and, late in the game, into a Duchy. With no +Buy on the board, each Silver from
Wayfarer that a Remodel then turns into a part is effectively an extra gain of most of
the parts the engine needs, so two or three Remodels plus your Buy gain 2-4 cards a
turn.

Before each play and each gain, ask what your deck is most short of right now: draw
(Wayfarer, Recruiter, Bazaar, Destrier), Actions (Recruiter food, Bazaar), gains
(another Remodel), fodder for Remodel (Silvers), or points. Then get that.

CARD DETAILS THAT MATTER.
- Wayfarer costs whatever the last other card you gained this turn cost: $2 after a
  Page, $3 after a Silver, $5 after a Recruiter or Bazaar, $8 after a Province, and $6
  if you haven't gained anything yet.
- Destrier costs $1 less for each card you've gained this turn.
- Recruiter gives Villagers equal to the cost of the card it trashes: 3 for a Silver, 4
  for a Remodel, 6 for a Gold, 2 for an Estate or Page, and none for a Copper.

OPENING. On $4/$3, open Remodel and Silver; on $5/$2, Recruiter and Page.

GET A RECRUITER EARLY. This is crucial: Recruiter draws, removes junk outright (Remodel
only swaps it for another card) and gives the Villagers that let you play several
Wayfarers a turn, and no other card here does all three. Spend your first $5 on
Recruiter, and if you still have none, Remodeling your opening Silver into one is worth
more than anything else that turn could buy.

GET A WAYFARER EARLY WITH REMODEL. Remodel a Copper (or an Estate) into a Page: Wayfarer
now costs $2, so your Buy can take one with the two Coppers left in hand. With $3 left,
Remodel an Estate into a Silver instead, which makes Wayfarer cost $3. This gets you a
$6 card on a $2-3 hand.

BUILDING (until the deck draws itself, usually by turns 7-9).
- Keep pricing Wayfarer with Remodel whenever it would otherwise cost more than you
  have.
- Build Recruiters and Wayfarers in step, about one Recruiter for every two Wayfarers.
  Wayfarers bring the Silvers Recruiters eat and help find them; Recruiters' Villagers
  play the Wayfarers. Too few Recruiters and Wayfarers sit dead in hand for want of
  Actions; too many and Recruiters run short of food and eat Coppers for nothing or
  cards you need. Bazaars supply Actions too, so with several you need fewer Recruiters.
- Remodel a Silver into whatever part the deck lacks: a Recruiter, a Bazaar, a cheap
  Wayfarer or another Remodel. Your Buy can then take a second part, so one turn can add
  two $5 cards.
- Take Wayfarer's Silver when you'll use it as fodder or money this turn or next, and
  decline it when it would only dilute your deck.
- Never Remodel a Copper into a Copper.

TARGET DECK: roughly 3 Recruiters, 5-6 Wayfarers, 2-3 Remodels, 2-4 Bazaars and a few
Silvers, perhaps a Destrier, with almost no Coppers or Estates.

BAZAAR OR RECRUITER. As a source of Actions the two are close. Recruiter draws more,
thins your deck and pays Villagers, but each play eats a card, which is a Silver once
the junk is gone. Bazaar's +2 Actions cost nothing, which leaves your Silvers free for
Remodel; its +$1 rarely matters. Lean toward Recruiter while there is still junk to
trash, and toward Bazaar once Remodel is short of Silvers.

FEEDING RECRUITER. Decide what each Recruiter should trash before you play it. If that
card isn't in your hand yet, play your draw first and hold the Recruiter until it is.
Early on, trash Estates, then Coppers whenever you have enough Villagers for the turn.
Once you're drawing your whole deck, the targets are mostly the Silvers your Wayfarers
keep making, but stay flexible: a Copper you don't need, or a card whose job is done (a
spare Page or Remodel), can be worth its Villagers. Never trash a Wayfarer.

PLAY ORDER. Play non-terminal draw first (Bazaar, Destrier), then Wayfarers, then each
Recruiter once its target is in hand, and Remodels last, once you've seen everything the
turn holds. Spend Villagers on what the turn needs, but bank a few when you can.
Villagers carry over, so banked ones mean next turn's Wayfarers can't be drawn dead and
can dig for a Recruiter when your hand lacks one.

WAY OF THE CHAMELEON. Take +$ instead of cards when the money reaches your price, or when
drawing would reshuffle your deck while your best cards are in play.

PAGE is a side option: one on a $5/$2 opening, or one gained by Remodel to price a
Wayfarer. Mostly it climbs to Hero, whose Gold gives Remodel a Province target for a
double-Province turn. It is worth more against another engine than against money.

SCORING. Once your deck draws itself, buy a Province with each $8. Late in the game,
spend Remodels on points too: a Gold into a Province, a Silver into a Duchy, and, once
you've gained a Province this turn, a spare Wayfarer (which now costs $8) into another
Province. With 3 Remodels the finish takes 2 Provinces a turn. Each turn, check whether
your Remodels plus your Buy can end the game with you ahead, and never leave exactly one
Province for your opponent to win with.

BISHOP is optional late payload. It scores without using your Buy: 4 VP for trashing a
Gold, 2 for a spare Remodel or Silver. Gain it with Remodel from a spare Page, or buy it
with a spare $4. It only pays off if the game runs long enough to play it several times,
so against an opponent who is pushing the pace, skip it and take Provinces and Duchies.

DON'T buy Develop, Scrying Pool or Potion.
```

This is longer than a game plan you keep for yourself (`play-game` asks for
about ten lines), because it was written for another player to follow. What
carries over is its shape: the loop first, the question to ask before every
gain, the tricks the cards allow, a target deck given as a direction, and
judgment calls framed as trade-offs rather than rules.
