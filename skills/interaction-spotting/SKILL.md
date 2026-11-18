---
name: interaction-spotting
description: Find how the cards and landscapes on a Dominion board work together, including tricks no card's text announces. Use when asked what combos, synergies or interactions a kingdom has, or before analysing a kingdom when the board looks unusual.
---

# Interaction spotting

Find what the cards on this board do together that none of them does
alone. The interactions that decide games are rarely the ones a card
advertises. They come from reading a card closely enough to see what it
quietly takes for granted, and then noticing that something else on the
board changes that.

No checklist finds these. Treat any list of known patterns as a reminder of
what interactions look like, never as the set to search. The method is to
think concretely: picture each card being played in a real turn of a deck
built on this board, and ask what goes wrong, what is left over, and what
almost works. Spend your effort there, not on formatting.

Work from the exact card text you were given, never from memory. Read
`context/rules.md` when an interaction turns on timing, phases, triggers or
where cards go.

## 1. Read every card to the bottom

Every Kingdom card, landscape, and every card the setup adds (Heirlooms,
non-Supply piles, the cards in split or mixed piles, Boons and Hexes that
can appear). Include Copper, Curse and the starting Estates: they are cards
on this board too.

For each, think through, briefly in writing:

- **What it does, in order**: each step of the text as it resolves, its
  types, the text below the line, and what happens when it is gained,
  discarded, trashed or set aside. Order matters: what has already happened
  when each step runs?
- **What it costs beyond its price**: the Action it uses, cards it takes out
  of your hand, money it throws away, a turn it delays, junk it brings,
  something it must give up. Most of these costs are written nowhere. They
  follow from the rules and from where the card sits in a turn.
- **What it leaves behind**: cards it moves, gains, discards, sets aside or
  reveals, tokens, a changed cost, a state, an empty pile, information.
- **When it would be great**: the situation in which this card is at its
  best, as concretely as you can put it ("with nothing left in hand", "if it
  could be played again this turn", "if that discard happened outside
  Clean-up").
- **Which rule it leans on or bends**: when Treasures can be played, where
  gains go, what happens in Clean-up, how many cards a hand has, which
  cards count as Actions, what "in play" means.

## 2. Make each card great, and take its costs away

For each card, take its best situation and its hidden costs and search the
whole rest of the board for something that creates that situation or
removes that cost. Then the other way round: for each thing a card leaves
behind, ask who on this board wants it.

Think in turns, not pairs of texts:

- Walk through a concrete turn with both cards in it, and the turns before
  and after. Many tricks span turns: setting up the next hand, Durations,
  Clean-up, when the shuffle happens.
- Change the order. What if one card resolves before the other, a cheap
  card is gained first, or a Treasure is played early?
- Change the count. What if there are two copies, or one is played twice,
  or the pile is empty?
- Change whose card it is. What does the opponent's attack, gain or
  discard give you?
- Ask what a strong player would want to do with this card that its text
  seems to forbid, and whether anything here permits it.

Go beyond pairs where a third card closes a loop. Don't stop at the first
partner you find for a card.

## 3. Test every candidate

- **Does it work?** Step through it against the exact text and the rules.
  Quote the words that make it work, and check the qualifiers: "from your
  hand", "other than during Clean-up", "when you gain" against "when you
  buy", "this turn", "if you have".
- **If it fails, try to rescue it.** A failure names exactly what is
  missing: a card in hand, an Action, the right timing. Search the board
  for whatever supplies that, and remember that each play of a card, a
  replay included, may be made differently. Only a candidate nothing here
  rescues goes under Rejected, with the reason and what you tried.
- **How often?** What does a deck need to set it up (copies, ratio, other
  pieces) and how soon could it? An interaction that needs two cards in the
  same hand happens far less often than one that needs each card once in
  the deck.
- **What is it worth?** In cards, Actions, $, Buys, gains or VP per turn,
  against what the cards do without each other. Show the worked turn.

## 4. Look again

You have missed something. For every card that has no partner yet, go
through the others one at a time and spend a moment on the turn where both
are played. Then look at the landscapes against every card. Anything new
goes through step 3.

## Output

Rank interactions by how much they could change how the board is played.

```markdown
**Interactions:**
1. <Cards>: <how it works, in turn order> · <worked turn or rate> ·
   <what it needs: copies, setup, timing> · <decides the board / shapes the
   plan / minor>
**Costs removed:** <a card whose hidden cost something here takes away, and
how>, or "none found"
**Rejected:** <candidates that don't work or don't matter, and why>
**Unpaired:** <cards with no interaction found>
**Unsure:** <rules readings you weren't sure of>
```
