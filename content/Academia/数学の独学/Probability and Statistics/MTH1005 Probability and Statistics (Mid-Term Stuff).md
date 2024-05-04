### Outline of Possible Topics

[[MTH1005 Probability and Statistics (Cheat Sheet)]]

#### 1. **Multiplicative Rule of Probability**

**Description**:  
The multiplicative rule of probability is used to find the probability that two events, A and B, both occur. It depends on whether the events are independent or dependent.

**Methods**:
- **Independent Events**: Events A and B are independent if the occurrence of A does not affect the occurrence of B, and vice versa.
  - **Formula**: $P(A \cap B) = P(A) \times P(B)$
- **Dependent Events**: Events are dependent if the occurrence of one affects the probability of occurrence of the other.
  - **Formula**: $P(A \cap B) = P(A) \times P(B|A)$
  
Where $P(B|A)$ is the probability of B given that A has occurred.

#### 2. **Conditional Probability**

**Description**:  
Conditional probability measures the probability of an event occurring given that another event has already occurred. This concept is fundamental in understanding the dependence between events.

**Methods**:
- **Formula**: $P(B|A) = \frac{P(A \cap B)}{P(A)}$
- Here, $P(A)$ must be greater than 0.

This formula states that the probability of B given A is the probability of both A and B occurring divided by the probability of A.

#### 3. **Total Probability Law**

**Description**:  
The law of total probability allows calculating the probability of an event based on a partition of the sample space into several distinct scenarios or outcomes, integrating all different ways in which the event can occur.

**Methods**:
- **Formula**: $P(B) = \sum_{i=1}^n P(B|A_i) \times P(A_i)$
- Here, $\{A_i\}$ are mutually exclusive events that cover the entire sample space.

This is useful for breaking down complex problems into simpler, conditional parts.

#### 4. **Bayes' Formula**

**Description**:  
Bayes' formula is a way of reversing conditional probabilities. It allows you to update the probability estimate of an event based on new evidence.

**Methods**:
- **Formula**: $P(A|B) = \frac{P(B|A) \times P(A)}{P(B)}$
- Remember, $P(B)$ can be calculated using the total probability law if not given directly.

This formula is particularly useful in scenarios where the direct computation of $P(A|B)$ is complicated or when new information is received after the initial probability assessment.

#### 5. **Tree Diagrams**

**Description**:  
Tree diagrams are visual representations used to calculate the probabilities of various outcomes, based on sequences of events. They are particularly useful for organising and visualising the conditional and joint probabilities involved in multi-step processes.

**Methods**:
- Draw branches for each possible outcome of an event, starting from a single point.
- Label each branch with the probability of the corresponding outcome.
- To find the probability of an event occurring in a sequence, multiply the probabilities along the path of branches leading to the desired outcome.

Tree diagrams are especially helpful in illustrating the applications of conditional and total probability laws.

#### 6. **Discrete Random Variables**

**Description**:  
A discrete random variable has a countable number of possible values. Each value of this random variable is associated with a certain probability.

**Methods**:
- List the possible outcomes and their associated probabilities.
- Ensure that the probabilities sum up to 1.

**Examples**:
- Rolling a die (where outcomes are 1 through 6).
- Number of heads when flipping coins.

#### 7. **Probability Mass Functions (PMF)
**
**Description**:  
A Probability Mass Function for a discrete random variable gives the probability that the random variable is exactly equal to some value.

**Methods**:
- **Formula**: $P(X = x)$
- The function $f(x) = P(X = x)$ is defined such that $f(x) \geq 0$ for all $x$ and the sum of $f(x)$ over all possible values of $x$ equals 1.

**Applications**:
- Used to model the probabilities of outcomes for discrete variables.

#### 8. **Cumulative Distribution Functions (CDF)**

**Description**:  
The Cumulative Distribution Function for a discrete random variable $X$ gives the probability that $X$ will take a value less than or equal to $x$.

**Methods**:
- **Formula**: $F(x) = P(X \leq x)$
- $F(x)$ is non-decreasing and right-continuous with $F(-\infty) = 0$ and $F(\infty) = 1$.

**Applications**:
- Useful for determining the probability that the random variable falls within a specified range.

#### 9. **Continuous Random Variables**

**Description**:  
A continuous random variable can take an infinite number of possible values. For continuous random variables, probabilities are calculated over intervals rather than specific points.

**Methods**:
- **Probability**: $P(a \leq X \leq b)$ is the area under the curve of the variable’s probability density function between $a$ and $b$.

#### 10. **Probability Density Functions (PDF)**

**Description**:  
A Probability Density Function for a continuous random variable is a function that describes the relative likelihood for this random variable to take on a given value. The probability for the variable to fall within a particular range is given by the integral of this function over that range.

**Methods**:
- **Formula**: $f(x)$, where $\int_{-\infty}^\infty f(x) \, dx = 1$.
- $P(a \leq X \leq b) = \int_a^b f(x) \, dx$.

#### 11. **Cumulative Distribution Functions for Continuous Random Variables**

**Description**:  
Similar to the discrete case, the CDF for a continuous random variable $X$ gives the probability that $X$ will take a value less than or equal to $x$.

**Methods**:
- **Formula**: $F(x) = \int_{-\infty}^x f(t) \, dt$
- This function is continuous and non-decreasing, where $F(-\infty) = 0$ and $F(\infty) = 1$.

#### 12. **Expectation Values and Variance**

**Description**:  
Expectation values (expected values or means) and variance are measures of central tendency and variability, respectively, for random variables.

**Methods**:
- **Expectation Value (Mean)**: The expected value of a discrete random variable $X$ is calculated as $E(X) = \sum_{i} x_i P(X = x_i)$, where $x_i$ are the values that $X$ can take, and $P(X = x_i)$ is the probability mass function. For a continuous variable, $E(X) = \int_{-\infty}^\infty x f(x) \, dx$.
- **Variance**: The variance measures the spread of the random variable around its mean and is defined as $\text{Var}(X) = E[(X - \mu)^2] = E(X^2) - [E(X)]^2$.

**Applications**:
- Provides a fundamental measure for the average and the dispersion of a random variable.

#### 13. **Joint Random Variables**

**Description**:  
Joint random variables deal with the probability distribution that involves two or more random variables. It is used to describe scenarios where the outcome depends on the interplay between multiple variables.

**Methods**:
- **Joint Probability Mass Function** for discrete variables: $P(X = x, Y = y)$.
- **Joint Probability Density Function** for continuous variables: $f_{X,Y}(x, y)$, where the probability that $X$ and $Y$ fall into particular ranges is given by the double integral over those ranges.
- **Marginal Distributions**: These are derived from the joint distribution by summing or integrating out the other variables.

#### 14. **Covariance and Correlations**

**Description**:  
Covariance and correlation are statistical measures that describe how two random variables are related or change together. Covariance indicates the direction of the linear relationship between variables, whereas correlation measures both the strength and direction of the linear relationship.

**Methods**:
- **Covariance**: Defined as $\text{Cov}(X, Y) = E[(X - E(X))(Y - E(Y))]$.
- **Correlation**: Defined as $\rho_{X,Y} = \frac{\text{Cov}(X, Y)}{\sqrt{\text{Var}(X) \text{Var}(Y)}}$, which normalizes the covariance by the standard deviations of $X$ and $Y$, thus providing a dimensionless measure ranging from -1 to 1.

**Applications**:
- These metrics are crucial in fields like finance, economics, and any other domain where understanding the relationships between different factors is essential.

#### 15. **Median**

**Description**:  
The median is the value that divides a dataset into two equal parts. It is the middle value when the data points are arranged in ascending order, or the average of the two middle numbers if the dataset has an even number of observations.

**Methods**:
- Arrange the data in non-decreasing order.
- If the number of observations (n) is odd, the median is the middle data point: $\text{Median} = x_{(n+1)/2}$.
- If n is even, the median is the average of the two middle data points: $\text{Median} = \frac{x_{(n/2)} + x_{(n/2)+1}}{2}$.

**Applications**:
- Median is a robust measure of central tendency, particularly useful in skewed distributions as it is less affected by outliers and extreme values than the mean.

#### 16. **Quantiles (Quartiles and Percentiles)**

**Description**:  
Quantiles are points in your data that divide the data into intervals with equal probabilities. Quartiles and percentiles are specific types of quantiles.

**Methods**:
- **Quartiles**: Divide the data into four equal parts. 
  - Q1 (first quartile) is the 25th percentile.
  - Q2 (second quartile) is the 50th percentile, also the median.
  - Q3 (third quartile) is the 75th percentile.
- **Percentiles**: Indicate the value below which a given percentage of observations in a group of observations falls. For example, the 90th percentile is the value below which 90% of the data points may be found.

**Applications**:
- Quantiles are critical in statistical analyses for assessing the spread and distribution of data, especially in non-parametric statistics.

#### 17. **Interquartile Distance (IQR)**

**Description**:  
The interquartile range (IQR) is a measure of statistical dispersion and is the difference between the third quartile (Q3) and the first quartile (Q1).

**Methods**:
- **Formula**: $\text{IQR} = Q3 - Q1$
- It measures the middle 50% spread of the data, which is useful for identifying outliers.

**Applications**:
- The IQR is used to build box plots and is valuable for comparing the variability of different datasets, as well as identifying potential outliers.

#### 18. **Markov's and Chebyshev's Inequalities**

**Description**:  
These are fundamental inequalities in probability that provide bounds on the probabilities of extreme deviations from the mean.

**Methods**:
- **Markov's Inequality**: Applies to non-negative random variables and is used to bound the probability that a random variable is greater than a certain value.
  - **Formula**: $P(X \geq a) \leq \frac{E(X)}{a}$ for $a > 0$.
- **Chebyshev's Inequality**: Provides a bound for the probability that a random variable deviates from its mean by more than a certain multiple of the standard deviation.
  - **Formula**: $P(|X - \mu| \geq k\sigma) \leq \frac{1}{k^2}$ for any $k > 0$.

**Applications**:
- Both are non-parametric and do not require the distribution to be normal, making them versatile tools in probability theory and statistics to assess the tail behaviour of probability distributions.

#### 19. **Distribution Functions**

##### **Uniform Distribution**

**Description**:  
The uniform distribution is a type of probability distribution in which all outcomes are equally likely. It can be discrete or continuous.

**Methods**:
- **Discrete Uniform Distribution**: Each of the n outcomes has equal probability, $P(X = x_i) = \frac{1}{n}$.
- **Continuous Uniform Distribution**: Defined on an interval [a, b]. The probability density function (PDF) is $f(x) = \frac{1}{b-a}$ for $x$ in [a, b], and 0 otherwise.

**Applications**:
- Used to model scenarios where each outcome is equally likely, such as rolling a fair die or drawing a card from a well-shuffled deck.

##### **Geometric Distribution**

**Description**:  
The geometric distribution models the number of trials until the first success in a sequence of independent Bernoulli trials, where each trial has the same probability of success, $p$.

**Methods**:
- **Probability Mass Function (PMF)**: $P(X = k) = (1-p)^{k-1} p$ for $k = 1, 2, 3, \ldots$

**Applications**:
- Useful in modeling the number of attempts required until success, such as in reliability testing or quality control processes.

##### **Exponential Distribution**

**Description**:  
The exponential distribution is used to model the time between events in a process where events occur continuously and independently at a constant average rate.

**Methods**:
- **Probability Density Function (PDF)**: $f(x) = \lambda e^{-\lambda x}$ for $x \geq 0$, where $\lambda$ is the rate parameter.

**Applications**:
- Commonly used to model waiting times, such as the time until a radioactive particle decays, or the time between customer arrivals in a queue.

##### **Normal Distribution**

**Description**:  
The normal or Gaussian distribution is one of the most important probability distributions in statistics, applicable due to the Central Limit Theorem, which states that the sums of independent random variables tend toward a normal distribution, regardless of the original distribution under certain conditions.

**Methods**:
- **Probability Density Function (PDF)**: $f(x) = \frac{1}{\sqrt{2\pi \sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$, where $\mu$ is the mean and $\sigma^2$ is the variance.

**Applications**:
- The normal distribution is widely used across all fields of science and economics for real-valued random variables whose distributions are not known. It's used in hypothesis testing, confidence intervals, and as a model for measurement errors and natural phenomena.

### Given Resources

- [[Lecture Slides.pdf]],
- [[Worked Solutions.pdf]] (from the practical classes),
- [Revision WebAssign](https://www.webassign.net/web/Student/Assignment-Responses/last?dep=34367122) (first seven questions),
- [Numerical Assignment 3](https://www.webassign.net/web/Student/Assignment-Responses/view_key?dep=34183437&tags=autosave),
- [Numerical Assignment 4](https://www.webassign.net/web/Student/Assignment-Responses/view_key?dep=34341574&tags=autosave).