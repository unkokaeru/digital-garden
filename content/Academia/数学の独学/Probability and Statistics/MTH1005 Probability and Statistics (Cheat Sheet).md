## MTH1005 Probability and Statistics (Cheat Sheet)

> MTH1005 Probability and Statistics Cheat Sheet by William Fayers :)

### Basic Probability Concepts

- **Multiplicative Rule of Probability**:
	- **Independent Events**: $P(A \cap B) = P(A) \times P(B)$.
	- **Dependent Events**: $P(A \cap B) = P(A) \times P(B|A)$.
- **Conditional Probability**: $P(B|A) = \frac{P(A \cap B)}{P(A)}$.
- **Total Probability Law**: $P(B) = \sum_{i=1}^n P(B|A_i) \times P(A_i)$.
- **Bayes' Formula**: $P(A|B) = \frac{P(B|A) \times P(A)}{P(B)}$.

Useful empty **Venn diagram** for probability visualisation (to understand questions & their solutions):
![[venn diagram.png]]

### Random Variables

- **Discrete Random Variables**: Ensure probabilities of all outcomes sum to 1.
- **Probability Mass Functions (PMF)**: $P(X = x)$.
- **Cumulative Distribution Functions (CDF)**: $F(x) = P(X \leq x)$.
- **Continuous Random Variables**: Probabilities over intervals, not points.
- **Probability Density Functions (PDF)**: $P(a \leq X \leq b) = \int_a^b f(x) \, dx$.
- **CDF for Continuous Variables**: $F(x) = \int_{-\infty}^x f(t) \, dt$.

### Statistical Measures

- **Expectation and Variance**:
	- **Expectation Value**: $E(X) = \sum x_i P(X = x_i)$ or $E(X) = \int x f(x) \, dx$.
	- **Variance**: $\text{Var}(X) = E[(X - \mu)^2]$ or $\text{Var}(X)=E(X^{2})-E(X)^{2}$.
	- **Mappings**: $E(aX+b)=aE(X)+b$, $\text{Var}(aX+b)=a^{2}\text{Var}(X)$.
- **Joint Random Variables**:
	- **Joint PMF**: $P(X = x, Y = y)$.
	- **Joint PDF**: $f_{X,Y}(x, y)$.
	- **Marginal Distributions**: Derived from joint distribution by integrating out other variables.
- **Covariance and Correlations**:
	- **Covariance**: $\text{Cov}(X, Y) = E[(X - E(X))(Y - E(Y))]$.
	- **Correlation**: $\rho_{X,Y} = \frac{\text{Cov}(X, Y)}{\sqrt{\text{Var}(X) \text{Var}(Y)}}$.

### Data Analysis

- **Median and Quantiles**:
	- **Median**: Middle value of sorted data.
	- **Quantiles (Quartiles and Percentiles)**: Divide data into intervals with equal probabilities.
- **Interquartile Distance (IQR)**: $\text{IQR} = Q3 - Q1$.
- **Inequalities**:
	- **Markov's and Chebyshev's Inequalities**:
		- Markov: $P(X \geq a) \leq \frac{E(X)}{a}$.
		- Chebyshev: $P(|X - \mu| \geq k\sigma) \leq \frac{1}{k^2}$.

### Common Distributions

#### 1. **Uniform Distribution**

- **Expectation (Mean)**: $E(X) = \frac{a+b}{2}$
- **Variance**: $\text{Var}(X) = \frac{(b-a)^{2}}{12}$
- **Probability Mass Function (PMF)**: 
  $$P(X = x) = \frac{1}{b - a + 1} \quad \text{for} \quad x=a, a+1, \ldots, b$$
  Every outcome within the range from $a$ to $b$ is equally likely.

#### 2. **Geometric Distribution**

- **Expectation (Mean)**: $E(X) = \frac{1}{p}$
- **Variance**: $\text{Var}(X) = \frac{1-p}{p^{2}}$
- **Probability Mass Function (PMF)**: 
  $$P(X = k) = (1-p)^{k-1} p \quad \text{for} \quad k = 1, 2, 3, \ldots$$
  Represents the probability of getting the first success on the $k$-th trial.

#### 3. **Exponential Distribution**

- **Expectation (Mean)**: $E(X) = \frac{1}{\lambda}$
- **Variance**: $\text{Var}(X) = \frac{1}{\lambda^{2}}$
- **Probability Density Function (PDF)**: 
  $$f(x) = \lambda e^{-\lambda x} \quad \text{for} \quad x \geq 0$$
  Describes the time between events in a Poisson point process.

#### 4. **Normal Distribution**

- **Expectation (Mean)**: $E(X) = \mu$
- **Variance**: $\text{Var}(X) = \sigma^{2}$
- **Probability Density Function (PDF)**: 
  $$f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$$
  Common for continuous data clustering around a mean.

#### 5. **Poisson Distribution**

- **Expectation (Mean)**: $E(X) = \lambda$
- **Variance**: $\text{Var}(X) = \lambda$
- **Probability Mass Function (PMF)**: 
  $$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!} \quad \text{for} \quad k = 0, 1, 2, \ldots$$
  Suitable for modelling the frequency of events within a fixed interval.

#### 6. **Binomial Distribution**

- **Expectation (Mean)**: $E(X) = np$
- **Variance**: $\text{Var}(X) = np(1-p)$
- **Probability Mass Function (PMF)**: 
  $$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k} \quad \text{for} \quad k = 0, 1, 2, \ldots, n$$
  Describes the number of successes in a series of independent Bernoulli trials.

### Decision Guide for Distributions

1. **Outcomes type**:
   - **Discrete**: Focuses on distinct, separate outcomes. Go to Step 2.
   - **Continuous**: Concerns measurable quantities that can vary. Go to Step 4.
2. **Trial Independence**:
   - **Independent with two outcomes**: Each outcome doesn't affect the others, with success/failure options. Go to Step 3.
   - **Not independent or different outcomes**: Outcomes affect each other or there are multiple types of outcomes. Go to Step 5.
3. **Number of trials and interest in successes**:
   - **Known trials and interest in successes**: *Binomial Distribution*, used when the number of trials and the desire to determine the number of specific outcomes (like successes) is known.
   - **Interest in number of trials for first success**: *Geometric Distribution*, applies when focusing on the count of trials needed to achieve a first success.
4. **Time or space between events**:
   - **Events over time/space**: *Exponential Distribution*, ideal for modelling time between continuous, independent events.
   - **Data clustering around mean**: *Normal Distribution*, effective when large data sets naturally cluster around a central value.
5. **Probability equality across range**:
   - **Equal across range**: Uniform Distribution, where each outcome in a range is equally likely.
   - **Not equal across range**: Poisson Distribution, suited for counting the occurrences of events over a fixed interval, where events happen with a known but uneven rate.

![[sudoku-mth1005.png]]
*Generated by github.com/unkokaeru/*.
