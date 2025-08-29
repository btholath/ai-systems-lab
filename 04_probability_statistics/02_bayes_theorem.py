# Bayes' Theorem Step-by-Step
def bayes_theorem_step(prior, sensitivity, specificity):
    # Step 1: Evidence = Chance of positive test (sick * true positive + healthy * false positive)
    evidence = (sensitivity * prior) + ((1 - specificity) * (1 - prior))
    # Step 2: Posterior = (Chance of positive if sick * prior) / evidence
    posterior = (sensitivity * prior) / evidence
    return posterior, evidence

# Disease Problem
prior = 0.01      # 1% chance of disease
sensitivity = 0.95 # 95% chance test is right if sick
specificity = 0.90 # 90% chance test is right if healthy
posterior, evidence = bayes_theorem_step(prior, sensitivity, specificity)
print("Evidence (P(Positive Test)): ", evidence)
print("Probability of Disease Given Positive Test: ", round(posterior * 100, 1), "%")

# Candy Jar Example
prior_candy = 0.2    # 20% chance jar is red
sensitivity_candy = 0.9  # 90% chance of red if red
specificity_candy = 0.1  # 10% chance of red if not red
posterior_candy, evidence_candy = bayes_theorem_step(prior_candy, sensitivity_candy, specificity_candy)
print("Evidence (P(Red Candy)): ", evidence_candy)
print("Probability Jar is Red After Seeing Red: ", round(posterior_candy * 100, 1), "%")