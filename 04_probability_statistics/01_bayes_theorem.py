import matplotlib.pyplot as plt

# Bayes' Theorem function
def bayes_theorem(prior, sensitivity, specificity):
    evidence = (sensitivity * prior) + ((1 - specificity) * (1 - prior))
    posterior = (sensitivity * prior) / evidence
    return posterior

# Disease example
prior = 0.01
sensitivity = 0.95
specificity = 0.90
posterior = bayes_theorem(prior, sensitivity, specificity)
print("Probability of Disease Given Positive Test: ", round(posterior * 100, 1), "%")

# Candy jar example
prior_candy = 0.2    # 20% chance jar is red
sensitivity_candy = 0.9  # 90% chance of red if red
specificity_candy = 0.1  # 10% chance of red if not red
posterior_candy = bayes_theorem(prior_candy, sensitivity_candy, specificity_candy)
print("Probability Jar is Red After Seeing Red Candy: ", round(posterior_candy * 100, 1), "%")

# Plot how prior affects posterior
priors = [0.01, 0.1, 0.2, 0.5]
posteriors = [bayes_theorem(p, sensitivity, specificity) for p in priors]
plt.plot(priors, posteriors, '-o')
plt.title("How Starting Guess Changes Disease Chance")
plt.xlabel("Prior Probability")
plt.ylabel("Posterior Probability")
plt.grid(True)
plt.show()