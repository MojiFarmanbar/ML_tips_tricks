# Handling missing values with law of total conditional probability
## Problem:
- building a classifier that output $$ Pr(Class|feature_{1}, feature_{2}, ..., feature_{m})$$
- At prediction time, some features might be missing for some examples

## Solution: 
1. fill in the missing feature with the most common value
2. fill in the missing feature with the expected value
3. fill in the missing feature with the avg of the neighbourhood
4. Build a machine learning algorithm to predict the missing feature

## Common issues with above solutions:
- Some of them are not applicable for categorical data
- Some are specific to a particular problem
- Most of them are too naive or too expensive too build


# Reductionism

- Suppose the classifier is trained using three features
- Given a classifier that outputs $$Pr(Class| fa,fb,fc)$$
- Build a classifier that output Pr(Class|fa,fc) since feature_b is missing
- Assuming fa, fb, and fc are all independent we can estimate $$Pr(Class|fa=a_{1}, fc=c_{7})$$ as
$$\Sigma_{i}Pr(Class|fa=a_{1}, fb = b_{i}, fc=c_{7})$$



### How it works:
- Law of Total Probability:
$$Pr(A) = \Sigma_{i} Pr(A,B_{i})Pr(B)$$
- Low of Total Conditional Probability:
if B and C are independent then $$Pr(A|C) = \Sigma_{i}Pr(A,B_{i}|C) = \Sigma_{i}Pr(A|B_{i},C)Pr(B_{i})$$

Example:
- Given a classifier outputs $$Pr(Happy|src, dst, purpose)$$ where purpose can be {Work, Vacation} is sometimes missing.
- Assumoe purpose is independent from src and dst
- Estimate $$Pr(Happy|Paris,Tokyo)$$ as
$$Pr(Happy|Paris, Tokyo, work)Pr(work)\newline+Pr(Happy|Paris, Tokyo, Vacation)Pr(Vacation)$$
