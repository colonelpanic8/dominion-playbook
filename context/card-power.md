# Card Power Levels

There are community ratings of every kingdom card and landscape. Look up
the board's cards with

    python3 data/card-ratings.py Remake "King's Court"

It matches exact names, ignoring case, and suggests close names for a miss.
Naming half of a split pile also shows the whole pile's rating.

- Kingdom cards: the median is about 0, the top 10% is above 3.3 and the
  bottom 10% below −3. The extremes are about +6.9 and −7.8. Landscapes
  are on their own scale.
- Treat cards within about one point of each other as tied.
- Ratings come mostly from 2-player play. Attacks and junkers gain value
  with more players.

## Reading them

A rating is a card's average strength over every kingdom: a good prior and
a poor verdict. On one board a card's value can swing by more than the
whole scale. Gardens rates −1.7 and is the whole plan on some boards. Work
out what a card does on the board first, then look it up.

The useful part is the gap between the rating and your view. Treat each
large gap as a question about combinations:

- **A high-rated card you're passing on**: what usually makes it strong
  (its trashing, its +Buy, its attack), and what on this board makes that
  matter less, or does it better? If you can't name it, look again.
- **A low-rated card you want**: what on this board lifts it? Name the
  card or landscape it works with. If nothing does, the rating is probably
  right.
- **Cards a few points apart**: the ratings don't separate them. What each
  does with the rest of the board decides.
- **A card the board has changed**: a Trait on its pile, a Way, a cost
  reducer, or a partner that supplies the one thing it lacks can make it a
  different card. Rate what it does on this board.

A rating alone is never the reason to take or skip a card.
