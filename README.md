This repository includes code for the sample dataset generator and the analytic model for repeated measure ANOVA. <br>

<figure>
  <img src="RMANOVA.png" alt="Box plot comparing rational and emotional treatments across three time steps">
  <figcaption>Figure 1: Repeated measure analysis of variance (ANOVA) showing the distribution of scores across three time steps for participants receiving rational (green) vs. emotional (orange) advertisements. While T1 and T2 show no significant difference (n.s.), T3 exhibits a highly significant difference (***), indicating a strong long-term effect in favor of the rational treatment over the emotional. The datapoints are based on the 7-point Likert scale.</figcaption>
</figure><br>

<br>
[1] Dataset
The dataset generator is designed to simulate a longitudinal study that captures the long-term effects of interventions by measuring replies across three time steps. Unlike a typical pre-post design in pre-post, which is based on two time steps, the modeling with three time steps provides a more robust depiction of how participant responses change in the long-term. In this context, the answers are designed in a 7-point Likert scale that assesses the participants' willingness to take a vaccine; 1 indicates Strongly Disagree, 2 Disagree, 3 Slightly Disagree, 4 Neutral, 5 Slightly Agree, 6 Agree, and 7 indicates Strongly Agree. To achieve a realistic case, the code generates data for 5,000 participants with a 90% completion rate at the final time step. The synthetic dataset is created based on the expected mean and standard deviation derived from a normal distribution. Time step 1 is before the treatment, time step 2 is right after the treatment, and time step 3 is a week after the treatment.


<br>
[2] Demographic Table
This section describes the general information of the demographics, including age, gender, and income. Each subgroups are fairly represented in the dataset.

#### Age Group Distribution:

| Age Group | Count | Percentage (%) |
|-----------|-------|----------------|
| 18-24     | 832   | 16.64          |
| 25-34     | 804   | 16.08          |
| 35-44     | 784   | 15.68          |
| 45-54     | 836   | 16.72          |
| 55-64     | 870   | 17.40          |
| 65+       | 874   | 17.48          |

#### Gender Distribution:

| Gender    | Count | Percentage (%) |
|-----------|-------|----------------|
| Female    | 2458  | 49.16          |
| Male      | 2542  | 50.84          |

#### Income Distribution:

| Income    | Count | Percentage (%) |
|-----------|-------|----------------|
| High      | 1609  | 32.18          |
| Low       | 1753  | 35.06          |
| Medium    | 1638  | 32.76          |


<br>
[3] Repeated Measure ANOVA
The Fig 1. shows the overall change in willingness to take the vaccine by the two types of treatment, rational and emotional, across three time steps. The repeated measure ANOVA component is geared towards uncovering treatment effects over time. This method inherently assumes that the data follow the properties of normality and sphericity:
<br>
1. Normal distribution: Since the dataset uses the "np.random.normal" function, the assumption of the Gaussian distribution of ANOVA is satisfied.
<br>
2. Sphericity: the same variance across timesteps is observed despite the standard deviation of the time step 1 is greater.
<br>
The statistical significance between two groups at each time step is measured using the paired t-test.


In this analysis, scores from the three time points are compared across different treatment groups to assess whether there are statistically significant changes attributable to the intervention over the long-term period. The code not only conducts the necessary statistical tests but also visualizes the results by plotting the data and annotating significance levels with clear markers. This dual approach of numerical and visual analysis ensures that any observed effects are both statistically sound and intuitively understandable, thereby providing comprehensive insights into the dynamics of the intervention.


Interpretation - 
