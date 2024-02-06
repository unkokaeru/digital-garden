# Maple Logbook

## Personal Details

- **Name:** William Fayers
- **Course:** MTH1006 - Computer Algebra and Technical Computing
- **Academic Year:** 2023-2024
- **Institution:** University of Lincoln, School of Mathematics and Physics

## Declaration

I confirm that this logbook is all my own work and that all references and quotations from both primary and secondary sources have been fully identified and properly acknowledged - William Fayers

## Table of Contents

- Declaration
- Week by Week
	- Week One, 29th January 2024 to 4th February 2024
		- In-Class Work
			- Tutorials
		- Extra Work
	- Week Two, 5th February 2024 to 11th February 2024
		- In-Class Work
			- Tutorials
			- Calculator
			- Calculus
		- Extra Work
- References

## Week by Week

I was unsure how to layout this logbook, due to the nature of Maple's "documents". However, at least for now whilst I learn what sort of problems we'll be solving, I've decided on just linking the Maple Document files. I tried transcribing, as well as exporting them as various file types, but none of them procured visually appealing results.

**Note**: Review the layout in the future, perhaps re-exporting or developing a Python program to make it a bit nicer.

### Week One, 29th January 2024 to 4th February 2024

Overall, this week pretty standard and simple! All we did were the basic Maple tutorials built into the program - they were simple, but definitely useful. The program is fairly unique compared to other tools I use regularly. To begin with, it was difficult just to understand what to do, but I eventually figured it out and then it was all very simple.

Since I didn't feel very tested this week, and I know that it's unlikely I'll stay engaged with something that isn't very engaging, at the first opportunity I had I went to the library and loaned a Maple book [1]! Hopefully it'll be a useful supplement for my learning, and extend the difficulty of the problems each week.

#### In-Class Work

##### Tutorials

We began by demonstrating how simple arithmetic is calculated in Maple, then extended that to simple calculus, graphing, finding coefficients, then finally solving equations - even differential ones.

Whilst completing these first exercises, it felt a lot like my experience with WolframAlpha (and similar tools). Initially, the maths felt clunky, with the GUI being very necessary and slowing down my progress since I couldn't simply type everything.

![[Exercise 1.1.1.mw]]

Next, we expressed the usefulness of Maple versus similar tools like the aforementioned WolframAlpha: combining text with maths! I found this was very useful, and honestly wish I had the ability in my normal maths notetaking (maybe I'll try it out for a week, but it's unlikely).

More than this, we demonstrated the ability to solve equations more, and assigning expressions to mathematical functions and procedures - the latter of which being similar to the programming construct of "functions".

![[Exercise 1.1.2.mw]]

#### Extra Work

After loaning the Maple book[1] from the library, I immediately went home and began working through the questions. I spent about an hour going through the first chunk of the questions, finding a few interesting things in them.

First, each calculation ended in either **;** (if the calculation was to be displayed as a block) or **:** (if the calculation was to be displayed inline). I assume this is from the worksheet form of Maple (rather than the document form), but I've adopted the same convention, since I think it helps to differentiate from the inline answers better.

Secondly, I've learned a few ways to type everything more, rather than just using the GUI, which has been very useful in engaging with Maple. I also learned how to plot multiple equations on a single graph, and in multiple dimensions. I even learned about the different packages you can use, like *plots* and *plottools*.

Finally, I not only learned some more commands to evaluate, simplify, and convert expressions in different ways, but also a very important takeaway: how Maple calculates expressions. From this, I understand how verbose you have to be with Maple, explicitly using commands to state certain traits so that it has expected behaviour. I quite like this, though, as it allows for much more personalised output.

At this point I stopped, since I didn't want to go into content for next week, instead waiting for our session on Monday to clarify what future lectures will hold.

![[Extra Exercises (pages 1-34).mw]]

### Week Two, 5th February 2024 to 11th February 2024

This week was similarly simple to last week, but I could really tell how my extra work helped me remember how certain commands work and the nuances of Maple. Overall, a good week!

#### In-Class Work

##### Tutorials

We begun this week with some more tutorials, which coincidently coincide with the work I did last extra last week. First, we went over some common commands, as well as some packages to use more commands.

![[Exercise 2.1.1.mw]]

Next up, we learned about plotting in 2D and higher dimensions, as well as plotting multiple graphs on a single graph. After a lot of simple work, the final exercise was quite tricky - to make an interactive graph with variables, like so (using the `Explore` command):

```Maple
Explore(plot(sin(a*x + b) + c, x = -10 .. 10), parameters = [a = -10 .. 10, b = -10 .. 10, c = -10 .. 10])
```

![[Exercise 2.1.2.mw]]

##### Calculator

Next felt like a bit of a test of the knowledge we learned during the tutorial questions - some simple calculations that I completed pretty quickly.

![[Exercise 2.2.x.mw]]

##### Calculus

Last, some calculus! This was again quite simple, apart from one set of questions: checking which integrals can be solved by Maple analytically and which are solvable numerically. I wasn't sure what this meant, so I tried to simply evaluate each expression - this worked for all but two questions which returned `Error, unable to match delimiters`. Perhaps I'll understand more during the extra work later in the week and come back to fix this.

![[Exercise 2.3.x.mw]]

#### Extra Work

No extra work yet, maybe later in the week - look at procedures, further calculus, and interactive plotting.

## References

[1] Martha and J. P. Braselton, Maple By Example. Elsevier, 2005.
‌