# Bar Simulation
Simple agent-based toy simulation based on the book [The Wisdom of Crowds]([https://en.wikipedia.org/wiki/The_Wisdom_of_Crowds).

## Short Summary

Simulate a bar, which has space for 100 persons (`n`), but a capacity of 60 (`c`) persons to still have an enjoyable evening. If a person decides to go and there bar is at capacity or higher (>= 60), the bar will be too crowded and is unenjoyable.
The people inside the bar would have been better off staying at home and vice-a-versa.

Keep in mind a person is not allowed to go scope out the bar and then make a decision. They all must make a decision at the same time, and once a decision is made, it cannot be changed.

The participants have knowledge of past attendance to a certain time period (`d`) in the past. They are to employ a strategy (`s`) to decided whether to go or stay home.

Simulation This program is being written to simulate the attendance of the bar with the method discussed above. People will be randomly given a set of strategies to use and evaluate. They will select the best strategy of the ones they have been randomly assigned. They will employ that strategy and then re-evaluate each given strategy for the potential of a new best. The attendance numbers (`a`) are then calculated and stored and the process is to be run again.


### Arthur Strategy
Assume the 100 agents (`n`) can individually form several predictors or hypotheses, in the form of functions that map the past `d`  weeks' attendance figures into next week's. For example, recent attendance (`a`) might be:  
..., 44, 78, 56, 15, 23, 67, 84, 34, 45, 76, 40, 56, 22, 35.  
Particular hypotheses or predictors might be: predict next week's number to be  
- the same as last week's [35]
- a mirror image around 50 of last week's [65]
- a (rounded) average of the last four weeks [49]
- the trend in last 8 weeks, bounded by 0,100 [29]
- the same as 2 weeks ago (2-period cycle detector) [22]
- the same as 5  weeks ago (5-period cycle detector) [76]
- etc.

### Bell and Sethares Strategy
Bell and Sethares's bargoers all follow the same strategy: if their recent experiences at the bar has been good, they go again. If their recent experiences has been bad, they don't.
Bell and Sethares's bargoers are therefore much less sophisticated than Arthur's. They didn't worry much about what the
other bargoers might be thinking, and they don't not know—as
Arthur's bargoers do—how many people were at El Farol on the
nights when they didn't show up. All they really know is whether
they'd recently enjoyed themselves at El Farol or not. If they'd had
a good time, they want to go back. If they'd had a bad time, they
don't.

Let $`f_i`$ be frequency (period) with which the i-th agent wishes to attend and $`p_i`$ the phase (note that $`p_i < f_i`$). Let $`\mu_i`$ be a stepsize parameter that defines how much the i-th agent changes $`f_i`$ in response to new information. The evolution of an agent `i` at time iteration `k` is then defined as:
```math
c_i(k + 1) = \begin{cases}
   c_i(k) &\text{if } p_i(k) > 1 \\
   \max(1, f_i(k) + \mu_i(k) \text{Dsgn}(n(k) - n)) &\text{if } p_i(k) \le 1
\end{cases}
```
where \texttt{Dsgn(x)} represents the signum function with dead zone that is positive when $`x > 0`$, negative when $`x - d \le 0`$, and zero otherwise.

The initial conditions $`f_i(0)`$ and $`p_i(0)`$ are chosen randomly. Each agents phase term $`p_i`$ counts down until it drops below one. Meanwhile, the counter $`f_i`$ remain unchanged. Once $`p_i`$ reaches one, the agent attends the bar. At this point, $`f_i`$ is increased by $`\mu_i`$ if bar attendance exceeds `c` (the bar is crowded), and remains unchaned if attendance falls in the dead zone just below the cutoff point `c`. The phase $`p_i`$ is then reset to the current (updated) value of $`f_i`$.

## Detailed Descriptions

<details>
<summary>Simulation Description ("The Wisdom of Crowds")</summary>
<br>
Consider, to begin with, this problem. There's a local bar that you
like. Actually, it's a bar that lots of people like. The problem with
the bar is that when it's crowded, no one has a good time. You're
planning on going to the bar Friday night. But you don't want to go
if it's going to be too crowded. What do you do?
To answer the question, you need to assume, if only for the
sake of argument, that everyone feels the way you do. In other
words, the bar is fun when it's not crowded, but miserable when it
is. As a result, if everyone thinks the bar will be crowded on Friday
night, then few people will go. The bar, therefore, will be empty,
and anyone who goes will have a good time. On the other hand, if
everyone thinks the bar won't be crowded, everyone will go. Then
the bar will be packed, and no one will have a good time. (This
problem was captured perfectly, of course, by Yogi Berra, when he
said of Toots Shor's nightclub: "No one goes there anymore. It's too
crowded.") The trick, of course, is striking the right balance, so that
every week enough—but not too many—people go.
There is, of course, an easy solution to this problem: just invent an all-powerful central planner—a kind of iiber-doorman—
who tells people when they can go to the bar. Every week the
central planner would issue his dictate, banning some, allowing
others in, thereby ensuring that the bar was full but never crowded.
Although this solution makes sense in theory, it would be intolerable in practice. Even if central planning of this sort were possible, it would represent too great an interference with freedom of
choice. We want people to be able to go to a bar if they want, even
if it means that they'll have a bad time. Any solution worth talking
about has to respect people's right to choose their own course of action, which means that it has to emerge out of the collective mix of all the potential bargoers' individual choices.  

In the early 1990s, the economist Brian Arthur tried to figure
out whether there really was a satisfying solution to this problem.
He called the problem the "El Farol problem," after a local bar in
Santa Fe that sometimes got too crowded on nights when it featured Irish music. Arthur set up the problem this way: If El Farol
is less than 60 percent full on any night, everyone there will have
fun. If it's more than 60 percent full, no one will have fun. Therefore, people will go only if they think the bar will be less than 60
percent full; otherwise, they stay home.
How does each person decide what to do on any given Friday?
Arthur's suggestion was that since there was no obvious answer, no
solution you could deduce mathematically, different people would
rely on different strategies. Some would just assume that the same
number of people would show up at El Farol this Friday as showed up
last Friday. Some would look at how many people showed up the last
time they'd actually been in the bar. (Arthur assumed that even if you
didn't go yourself, you could find out how many people had been in
the bar.) Some would use an average of the last few weeks. And some
would assume that this week's attendance would be the opposite of
last week's (if it was empty last week, it'll be full this week).
What Arthur did next was run a series of computer experiments designed to simulate attendance at El Farol over the period
of one hundred weeks. (Essentially, he created a group of computer
agents, equipped them with the different strategies, and let them
go to work.) Because the agents followed different strategies,
Arthur found, the number who ended up at the bar fluctuated
sharply from week to week. The fluctuations weren't regular, but
were random, so that there was no obvious pattern. Sometimes the
bar was more than 60 percent full three or four weeks in a row,
while other times it was less than 60 percent full four out of five
weeks. As a result, there was no one strategy that a person could
follow and be sure of making the right decision. Instead, strategies
worked for a while and then had to be tossed away.
The fluctuations in attendance meant that on some Friday
nights El Farol was too crowded for anyone to have fun, while on
other Fridays people stayed home who, had they gone to the bar,
would have had a good time. What was remarkable about the experiment, though, was this: during those one hundred weeks, the bar was—on average—exactly 60 percent full, which is precisely
what the group as a whole wanted it to be. (When the bar is 60 per-
cent full, the maximum number of people possible are having a
good time, and no one is having a bad time.) In other words, even
in a case where people's individual strategies depend on each
other's behavior, the group's collective judgment can be good.

A few years after Arthur first formulated the El Farol problem,
engineers Ann M. Bell and William A. Sethares took a different
approach to solving it. Arthur had assumed that the would-be bargoers
would adopt diverse strategies in trying to anticipate the crowd's behavior. Bell and Sethares's bargoers, though, all followed the same strategy: if their recent experiences at the bar had been good, they
went. If their recent experiences had been bad, they didn't.
Bell and Sethares's bargoers were therefore much less sophisticated than Arthur's. They didn't worry much about what the
other bargoers might be thinking, and they did not know—as
Arthur's bargoers did—how many people were at El Farol on the
nights when they didn't show up. All they really knew was whether
they'd recently enjoyed themselves at El Farol or not. If they'd had
a good time, they wanted to go back. If they'd had a bad time, they
didn't. You might say, in fact, that they weren't worrying about coordinating their behavior with the other bargoers at all. They were just relying on their feelings about El Farol.
Unsophisticated or not, this group of bargoers produced a different solution to the problem than Arthur's bargoers did. After a
certain amount of time had passed—giving each bargoer the experience he needed to decide whether to go back to El Farol—the group's weekly attendance settled in at just below 60 percent of the
bar's capacity, just a little bit worse than that ideal central planner
would have done. In looking only to their own experience, and not
worrying about what everyone else was going to do, the bargoers
came up with a collectively intelligent answer, which suggests that
even when it comes to coordination problems, independent thinking may be valuable.
There was, though, a catch to the experiment. The reason the
group's weekly attendance was so stable was that the group quickly
divided itself into people who were regulars at El Farol and people
who went only rarely. In other words, El Farol started to look a lot
like Cheers. Now, this wasn't a bad solution. In fact, from a utilitarian perspective (assuming everyone derived equal pleasure from going to the bar on any given night), it was a perfectly good one.
More than half the people got to go to El Farol nearly every week,
and they had a good time while they were there (since the bar was
only rarely crowded). And yet it'd be hard to say that it was an ideal
solution, since a sizable chunk of the group rarely went to the bar
and usually had a bad time when they did.
The truth is that it's not really obvious (at least not to me)
which solution—Arthur's or Sethares and Bell's—is better, though
both of them seem surprisingly good. This is the nature of coordination problems: they are very hard to solve, and coming up with any good answer is a triumph. When what people want to do depends on what everyone else wants to do, every decision affects every other decision, and there is no outside reference point that
can stop the self-reflexive spiral. When Francis Galton's fairgoers
made their guesses about the ox's weight, they were trying to evaluate a reality that existed outside the group. When Arthur's computer agents made their guesses about El Farol, though, they were
trying to evaluate a reality that their own decisions would help construct. Given those circumstances, getting even the average attendance right seems miraculous.
</details>  

[The Wisdom of Crowds](http://www.asecib.ase.ro/mps/TheWisdomOfCrowds-JamesSurowiecki.pdf): Chapter 5.2

<details>
<summary>Paper Description B. Arthur</summary>
<br>
### The Bar Problem
Consider now a problem I will construct to illustrate inductive reasoning and how it might be modeled. N people decide independently each week whether to go to a bar that offers entertainment on a certain night. For concreteness, let us set N at 100. Space is limited, and the evening is enjoyable if things are not too crowded-specifically, if fewer than 60 percent of the possible 100 are present. There is no sure way to tell the numbers coming in advance; therefore a person or agent goes (deems it worth going) if  he expects fewer than 60 to show up or stays home if he expects more than 60 to go. Choices are unaffected by previous visits; there is no collusion or prior communication among the agents; and the only information available is the numbers who came in past weeks. (The problem was inspired by the bar El Farol in Santa Fe which offers Irish music on Thursday nights; but the reader may recognize it as applying to noontime lunch-room crowding, and to other commons or coordination problems with limits to desired coordination.) Of interest is the dynamics of the numbers at- tending from week to week. Notice two interesting features of this problem. First, if there were an obvious model that all agents could use to forecast attendance and base their decisions on, then a deductive solution would be possible. But this is not the case here. Given the numbers attending in the recent past, a large number of expectational models might be reason- able and defensible. Thus, not knowing which model other agents might choose, a reference agent cannot choose his in a well-defined way. There is no deductively rational solution-no "correct" expectational model. From the agents' viewpoint, the problem is ill-defined, and they are propelled into a  world of induction. Second, and diabolically, any commonalty of expectations gets broken up: if all believe few will go, all will go. But this would invalidate that belief. Similarly, if all believe most will go, nobody will go, invalidating that belief.3 Expectations will be forced to differ. At this stage, I invite the reader to pause and ponder how attendance might behave dynamically over time. Will it converge, and if so to what? Will it become chaotic? How might predictions be arrived at? A. A Dynamic Model To answer the above questions, I shall construct a model along the lines of the framework sketched above. Assume the 100 agents can individually form several predictors or hypotheses, in the form of functions that map the past d  weeks' attendance figures into next week's. For example, recent attendance might be:  
...,44,78,56,15,23,67,84,34,45,76,40,56,22,35.  
Particular hypotheses or predictors might be: predict next week's number to be  
- the same as last week's [35]
- a mirror image around 50 of last week's [65]
- a (rounded) average of the last four weeks [49]
- the trend in last 8 weeks, bounded by 0,100 [29]
- the same as 2 weeks ago (2-period cycle detector) [22]
- the same as 5  weeks ago (5-period cycle detector) [76]
- etc.

Assume that each agent possesses and keeps track of a individualized set of k such focal predictors. He decides to go or stay according to the currently most accurate predictor in his set. (I will call this his active predictor.) Once decisions are made, each agent learns the new attendance figure and updates the accuracies of his monitored predictors. Notice that in this bar problem, the set of hypotheses currently most credible and acted upon by the agents (the set of active hypotheses) determines the attendance. But the attendance history determines the set of active hypotheses. To use John Holland's term, one can think of these active hypotheses as forming an ecology. Of interest is how this ecology evolves over time. B. Computer Experiments For most sets of hypotheses, analytically this appears to be a difficult question. So in what follows I  will proceed by computer experiments. In the experiments, to generate hypotheses, I  first create an "alphabet soup" of predictors, in the form of several dozen focal predictors replicated many times. I then randomly ladle out k (6 or 12 or 23, say) of these to each of 100 agents. Each agent then possesses k predictors or hypotheses or "ideas" he can draw upon. We need not worry that useless predictors will muddy behavior. If predictors do not "work" they will not be used; if they do work they will come to the fore. Given starting conditions and the fixed set of predictors available to each agent, in this problem the future accuracies of all predictors are predetermined. The dynamics here are deterministic. The results of the experiments are interesting (Fig. 1). Where cycle-detector predictors are present, cycles are quickly "arbitraged" away so there are no persistent cycles. (If several people expect many to go because many went three weeks ago, they will stay home.) More interestingly, mean attendance converges always to 60. In fact the predictors self-organize into an equilibrium pattern or "ecology" in which, of the active predictors (those most accurate and therefore acted upon), on average 40 percent are forecasting above 60, 60 percent below 60. This emergent ecology is almost organic in nature. For, while the population of active predictors splits into this 60/40 average ratio, it keeps changing in membership forever. This is something like a forest whose contours do not change, but whose individual trees do. These results appear throughout the experiments and are robust to changes in types of predictors created and in numbers assigned. How do the predictors self-organize so that 60 emerges as average attendance and forecasts split into a 60/40 ratio? One explanation might be that 60 is a natural "attractor" in this bar problem; in fact, if one views it as a pure game of predicting, a mixed strategy of forecasting above 60 with probability 0.4 and below it with probability 0.6 is a Nash equilibrium. Still, this does not explain how the agents approximate any such outcome, given their realistic, subjective reasoning. To get some understanding of how this happens, suppose that 70 percent of their predictors forecasted above 60 for a longish time. Then on average only 30 people would show up; but this would validate predictors that forecasted close to 30 and invalidate the above-60 predictors, restoring the "ecological" balance among predictions, so to speak. Eventually the 40-60-percent combination would assert itself. (Making this argument mathematically exact appears to be nontrivial.) It is important to be clear that one does not need any 40-60 forecasting balance in the predictors that are set up. Many could have a tendency to predict high, but aggregate behavior calls the equilibrium predicting ratio to the fore. Of course, the result would fail if all predictors could only predict below 60; then all 100 agents would always show up. Predictors need to "cover" the available prediction space to some modest degree. The reader might ponder what would happen if all agents shared the same set of predictors. It might be objected that I  lumbered the agents in these experiments with fixed sets of clunky predictive models. If they could form more open-ended, intelligent predictions, different behavior might emerge. One could certainly test this using a more sophisticated procedure, say, genetic programming (John Koza, 1992). This continually generates new hypotheses, new predictive expressions, that adapt "intelligently" and often become more complicated as time progresses. However, I would be surprised if this changes the above results in any qualitative way. The bar problem introduced here can be generalized in a  number of ways (see E. R. Grannan and G. H. Swindle, 1994). I encourage the reader to experiment.
</details>

[Paper by Brian Arthur](https://sites.santafe.edu/~wbarthur/Papers/El_Farol.pdf): Chapter II.

Paper Description Bell and Sethares  
[Paper by Bell and Sethares](http://fmwww.bc.edu/cef99/papers/Bell.Sethares.pdf)
