# Selection bias in data
In data science, selection bias occurs when you have data that aren’t properly randomized. If your dataset isn’t properly randomized, it means the sample isn’t representative - it doesn’t truly reflect the analyzed population.
For example, choosing “number of arrests of family or friends” as a feature in the [COMPAS](https://www.uclalawreview.org/injustice-ex-machina-predictive-algorithms-in-criminal-sentencing/) algorithm, knowing that arrests are more common among blacks than whites, could be discussed. Then, sampling the data can lead to bias when some members of a population are systematically more likely to be selected in a sample than others.

## How to evaluate bias?
There are some standard indicators we can use to evaluate bias in data and ML models. They aim at assessing whether the ground truth or the model predictions differ significantly among groups with different values in protected attributes, such as gender, race, religion, etc.

Let’s consider a binary classifier, against a protected attribute $A\in\{0,1\}$. Let’s denote $Y\in\{0,1\}$ the ground truth, and  
$\hat{Y}\in\{0,1\}$ the prediction. Three indicators we can use to quantify bias are:

- Demographic parity (or calibration): it assesses if the proportion of people that are positive in a population is equal to the proportion of people that are positive in each subgroup of the population. $$ \frac{|(Y=1)|}{|(A=0)\cup(A=1)|}=\frac{|(Y=1,A=0)|}{|(A=0)|}=\frac{|(Y=1,A=1)|}{|(A=1)|} $$

- Statistical Parity Difference (SPD): it measures the difference between the probability of positive outcomes across the groups of the protected attribute:
$$SPD = P(\hat{Y}=1|A=0) - P(\hat{Y}=1|A=1)$$

- Equal Opportunity Difference (EOD): it quantifies the discrepancy between the True Positive Rate within the groups:
$$EOD = P(\hat{Y}=1|Y=1,A=0) - P(\hat{Y}=1|Y=1, A=1)$$

For example, if A represents gender, the fact that a person is a man should not increase or decrease the chance of a positive prediction (SPD), or the chance of being well classified (EOD). We can use similar formulas for other classification rates such as false positive rate, false omission rate, etc. Each of those metrics define one specific bias measure. Therefore, debiasing data by minimising SPD or EOD for example does not imply unbiased data, but unbiased (or less biased) data in regards to a certain metric.

## debiasing solutions in causality
- [Debiasing with orthogonalization](https://matheusfacure.github.io/python-causality-handbook/Debiasing-with-Orthogonalization.html)
- [Debiasing with propensity score](https://matheusfacure.github.io/python-causality-handbook/Debiasing-with-Propensity-Score.html)

## Recommendation how to deal with selection bias
- Selection bias will cause high variance in the region of feature space where labels are missing. Simply adding more data, until variance decreases, mitigates selection bias.
- Build a propensity model considering all features (X) and bias column (S), the quality of this model indicate the selection bias effect. You can sabotage the relationship of X and S by removing top features. keep your fingers crossed that those features are not important features for target prediction.