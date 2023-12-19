---
title: Tutoring Profit Margin
---
##### Seeking a sensible profit margin
There are two factors in a profit margin - revenue and cost.
$$\frac{\text{revenue}-\text{cost}}{\text{revenue}}\times100=\text{profit margin (\%)}$$
So, if we find a sensible profit margin and calculate the cost for a session, then it's easy to find the last variable in the equation: revenue, or the amount to charge per session.

First, if we calculate the cost, then we can plot the profit margin equation to find a reasonable percentage, as well as research to find common small business profit margins.
###### Cost
To run an online tutoring business, costs can be broken down into three areas:
 - [[Advertising]] (to get clients)
	 - How are clients going to know they need your services unless you tell them?
 - [[Education]] (to keep clients)
	 - A strong education means that you have the knowledge to teach your clients, so they keep paying you for your time.
 - [[Delivery]] (to exponentiate clients)
	 - Good delivery means that clients talk to other potential clients, doing your advertising for you.

These costs total to about £20.10 per session - one hour of preparation, one hour of delivery, and one hour of summarisation.

Cost may be affected in the future by differing education, advertisement costs, delivery costs, as well as the addition of summarisation costs if I use resources from the [[Untitled Project]].
###### Graphing potential profit margins
First, let's input some numbers into our profit margin equation:
$$\frac{\text{revenue}-\text{cost}}{\text{revenue}}\times100=\text{profit margin (\%)}$$
Revenue is still an unknown, so let's give that the designation $x$.
Cost is now known, so we can replace that with the value $20.1$.
Profit margin is also unknown, so let's give that the designation $y$.
$$\frac{x-20.1}{x}\times100=y$$
However, our model is slightly flawed, as all of this assumes only one session occurs - and that the session is paid. In reality, usually clients begin with a trial session (at a heavy discount, often reaching 100%) and then go onto many more sessions.

The number of sessions they go onto differs depending on the category of client - which we haven't even touched on yet. These categories are as follows:
 - Failing student (**FS**) - failed an exam (once or multiple times). These students often cram a lot of tutoring into a short timespan before their resit, so opt for "on demand" pricing.
 - Worrying student (**WS**) - hasn't failed an exam yet, but is on track to. These students are often funded by their parents, so opt for "bulk" pricing.
 - Perfectionist student (**PS**) - hasn't failed an exam and probably won't. These students are rare, usually occurring at lower levels (e.g. 11+ exams). Usually they opt for "on demand" pricing, if they ever stop questioning the idea of online tutoring.
	 - Note that the trial session previously mentioned has a 100% success rate (over 30+ trials) at getting a client over this hurdle.

As a PS is rather rare, I'll consider them negligible. However, we do need to split our equation into the other two categories: FS and WS. The former on average purchase ten sessions after an initial trial, and the latter on average purchase sixteen sessions after an initial trial (although there is one case of purchasing thirty-two, and another of purchasing ten).

Mathematically, we can model this as the following:
 - FS: $n = 10, f = 1, p = x_{FS}$, where $n$ is the number of sessions, $f$ is the number of trial sessions, and $p$ is the price of each session (which is related to the revenue, $x$).
 - WS: $n = 16, f = 1, p = x_{WS}$, where $n$ is the number of sessions, $f$ is the number of trial sessions, and $p$ is the price of each session (which is related to the revenue, $x$).

Using these new variables, we can further define revenue ($x=np$) and cost (no longer the constant 20.1 as discussed, now $20.1n$), as both now depend on how many sessions are delivered, as well as how many were trials and the price of the paid sessions.

For the sake of modelling, we'll treat trial sessions as free for the client (as they often are).
$$\text{General Case: }\frac{np-20.1(n+f)}{np}=y$$
$$\text{FS Case (simplified): }\frac{p-22.11}{p}=y$$
$$\text{WS Case (simplified): }\frac{p-21.35625}{p}=y$$
Plotting these in [Desmos](https://www.desmos.com/calculator) gives the following results, where FS is red and WS is blue (note that this is normalised, such that $p\mapsto 1000p$):
![[desmos-graph.png]]

Examining the graph, both the WS and FS cases are very similar in terms of profit margin trend, so it seems to simplify our search to just needing one percentage. However, how do we find this from the graph?

First, we don't want a profit margin which requires reduced returns - displayed on the graph where the gradient is less than 1. Mathematically, we can find this turning point using calculus. For the sake of completion I've done this generally.
$$f(x)=\frac{p-k}{p}$$
$$\implies f^\prime(x)=\frac{k}{p^2}$$
We want where $f^\prime(x)>1$, so: $k>p^2$, or $-\sqrt{k}<p<\sqrt{k}$. Since we're only dealing on the positive side of our equation, however, we'll only use the principal inequality $0<p<\sqrt{k}$. However, we also don't want a negative profit margin, so we'll ensure that p begins at the x-intersection. However, this is at k. **So the perfect profit margin is... undefined.**

Clearly there's a mistake somewhere. Actually, it's quite obvious - all of the gradients shown in the graph are less than 1, so we don't want anything in the graph. But what number do we want to aim for if not a gradient greater than 1? Perhaps 0.5?

Doing the same calculations as before, substituting 1 for 0.5, we result with the following inequality:
$$p<\sqrt{2k}$$
In the case of FS, $k=22.11, y=89.49\%$. In the case of WS, $k=21.35625, y=89.67\%$. So, our perfect profit margin is approximately $90\%$. From now I'll also treat $k$ as $22$, as it roughly fits our approximations and is a lot easier to use.

**It was also at this point that I realised my huge overarching mistake.** My initial mapping to "normalise" the data, accidentally warped my equation massively, as I only mapped the x values to match the y, without realising what I did.
#### The correction
After a lot of work, I came to this inequality:
$$1000k<kx^2$$
This simplifies roughly to our golden profit margin: 31.62% - irrelevant of $k$.