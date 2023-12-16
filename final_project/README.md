#  The Phoenix League

## How the League Works

The Phoenix League is a local football (or soccer) league in the city of 
Phoenix. The way that this league works is that each team faces each other 
and score points based on goals. Teams can loose points based on losses and 
red cards. Here is how the points system work:
* +4 for every win
* -4 for every loss
* -1 for every red card

The top four teams are then selected to compete in a four-way tournament. These teams are selected after sorting their standings. They are sorted by:
1. points earned
2. number of wins (higher is better)
3. number of losses (lower is better)
4. number of red cards (lower is better) 
5. team aptitude

The winner of the tournament is the winner of the league's season. 

## How Players and Teams Work

Each team comprises of 10 players. Each player contains the following
attributes with a value from 0 to 1:
* `Speed (spd)` - How quick the player is
* `Offense (off)` - How well they are good in playing offensively
* `Defending (dfn)` - How well they are at defending against other teams
* `Handling (hnd)` - How well the player is good at controlling the ball
* `Attitude (att)` - Probability of attaining a red card

A player's total aptitude `apt` is calculated based on the following equation:

$\textrm{apt} = \max\left(\frac{\left(\textrm{spd} + \min{\left(\left(\frac{1}{2}\log(\textrm{dfn})+2\right), 1\right)} + \min{\left(\left(\frac{2}{3}\log(\textrm{off})+\frac{3}{2}\right), 1\right)} + \frac{50^{\textrm{hnd}}}{50} - \left(1.5\cdot\textrm{att}\right)\right)}{4}, 0\right)$

To get a team's average aptitude `taa`, we average all of the player's individual 
aptitude. When teams play against each other, the one with the higher aptitude 
wins. To determine the number of red cards each team makes, we summate on each 
player and use their `att` as a probability to see if they received a red card.

### Training
Players can improve before a match by training. When undergoing training, they
can improve their lowest attribute (excluding `att`) by `0.02`. In return, they're
`att` goes up by `0.005`. 

### Therapy
Players can go to therapy to decrease their `att` by `0.2` by going to therapy.
However, only one player can go to therapy before a match and they cannot go to
training. The player selected to go to therapy is done by selecting the individual
with the highest `att`. If there are similar `att` scored players, then the person
at the very top is selected after sorting by `att`. 

## Project Completion
Your goal for this final project is to implement code based on the following 
docstring descriptions. Parts of the league have been laid out, but you will
need to complete the rest. There is no exact result to compare to as values
are randomized. To determine if you have implemented the correct steps, you 
will need to compare your output to some provided results. You can also contact
Benjamin Herrera at b10@asu.edu or on Discord @bherrera to get approval
or your work. 