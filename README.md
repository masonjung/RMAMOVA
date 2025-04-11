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
The Fig 1. shows the overall change in willingness to take the vaccine by the two types of treatment: (1) rational and (2) emotional, across three time steps. Two groups before the treatment did not show any meaningful difference. After the treatment, the average score increased meaningfully, and the majority of people are willing to take the vaccine, while the people who were exposed to the emotional advertisement are more likely to the negative replies. This indicates that the advertisement increases the willingness to take the vaccine, and both group shows a similar enough increase. While the initial increase in vaccine willingness may be temporary, a follow-up experiment conducted one week later revealed that those exposed to rational appeals maintained a higher level of willingness, suggesting a more durable long-term effect and supporting the prioritization of rational messaging in public health campaigns.

<br>
The repeated measure ANOVA of this research is designed to meet statistical assumptions that provide the validity of the experiment. This method inherently assumes that the data follow the properties of normality and sphericity: (1) Normal distribution: Since the dataset uses the "np.random.normal" function, the assumption of the Gaussian distribution of ANOVA is satisfied. (2) Sphericity: the same variance across timesteps is observed, despite the standard deviation of the time step 1 is greater. Additionally, the statistical significance between two groups at each time step is measured using the paired t-test.



