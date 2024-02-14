# Bayes’ Theorem

Bayes' Theorem is a fundamental concept in probability theory and statistics. It offers a mathematical framework for updating our beliefs based on new evidence. This theorem is named after Thomas Bayes, an 18th-century British mathematician and Presbyterian minister, who first provided an equation that allows new evidence to update beliefs in his posthumously published work "An Essay towards solving a Problem in the Doctrine of Chances" (1763).

## Understanding Bayes’ Theorem

At its core, Bayes' Theorem relates the conditional and marginal probabilities of random events. It is expressed mathematically as:

$$ P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)} $$

Where:
- $P(A|B)$ is the probability of event A occurring given that B is true.
- $P(B|A)$ is the probability of event B occurring given that A is true.
- $P(A)$ and $P(B)$ are the probabilities of observing A and B independently of each other.

## The Role of Prior Knowledge

One of the key aspects of Bayes' Theorem is its emphasis on prior knowledge, or the 'prior'. The prior, $P(A)$, represents what is known about the probability of event A before observing new data (B). As new evidence (B) is considered, Bayes' Theorem updates the belief about A, resulting in the posterior probability, $P(A|B)$. This process underscores the dynamic nature of probability assessment, allowing beliefs to be updated as new information becomes available.

## Applications of Bayes’ Theorem

Bayes' Theorem has wide-ranging applications across various fields, including:
- **Machine Learning**: In spam filtering, for instance, it helps in determining the likelihood that an email is spam based on its content.
- **Medical Diagnosis**: Estimating the probability of a disease given a positive test result.
- **Decision Making**: In finance, it can be used for risk assessment and making informed investment decisions.

## Example

Suppose a disease affects 1 in 1,000 people. A test for the disease is 99% accurate: it correctly identifies the disease in 99% of cases (true positive rate) and correctly identifies non-disease in 99% of cases (true negative rate). If a person tests positive, what is the probability they actually have the disease?

Applying Bayes' Theorem:
- Let A be the event of having the disease.
- Let B be the event of testing positive.

Given:
- $P(A) = \frac{1}{1000}$
- $P(B|A) = 0.99$
- $P(B|A^c) = 0.01$ (where $A^c$ denotes not having the disease)
- $P(B) = P(B|A) \cdot P(A) + P(B|A^c) \cdot P(A^c)$

Calculating $P(A|B)$ gives us the updated probability of having the disease given a positive test result.

## Conclusion

Bayes' Theorem provides a powerful tool for understanding the nature of conditional probability, emphasizing how prior knowledge should be integrated with new evidence to make informed decisions. Its application is a testament to the interconnectedness of mathematical theory and practical decision-making across disciplines.

### Test Questions
1. **[Basic]** If the probability of event A is 0.5, and the probability of event B given A is 0.3, what is the probability of A given B if the probability of B is 0.4?
2. **[Basic]** A bag contains 3 red and 7 blue balls. A ball is drawn randomly from the bag and then replaced along with 2 more balls of the same color. If a ball is then drawn again and is found to be red, what is the probability it was drawn from the original set of 3 red balls?
3. **[Basic]** Consider a scenario where 2% of a population has a certain condition, and a test for this condition has a 95% true positive rate and a 5% false positive rate. If a randomly selected individual from the population tests positive, what is the probability they actually have the condition?

These questions are designed to reinforce the concepts discussed in this note and encourage further exploration of Bayes' Theorem and its applications.