#%%

import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
from statsmodels.stats.anova import AnovaRM
sys.path.append('.')
from dataset_econ import dataset1, dataset2, dataset3
import seaborn as sns
import pingouin as pg

# ============================
# Dataset check
# ============================

df = pd.concat([dataset1, dataset2, dataset3], axis=1)
df["Completed"].value_counts()

# Only completed instances
df = df[df["Completed"] == "Yes"]
df["Completed"].value_counts()

# Check the distribution <- treatment
rational_scores = df[df["Treatment"] == "Rational"][["T1", "T2", "T3"]]

# Plot histograms for each time point <- just to check
plt.figure(figsize=(12, 8))
for i, time_point in enumerate(["T1", "T2", "T3"], 1):
    plt.subplot(3, 1, i)
    plt.hist(rational_scores[time_point].dropna(), bins=10, alpha=0.7, color='blue', edgecolor='black')
    plt.title(f'Distribution of Scores at {time_point} (Rational Treatment)')
    plt.xlabel('Score')
    plt.ylabel('Frequency')
    plt.grid(True)

plt.tight_layout()
plt.show()

# ============================
# Demograhpic table
# ============================

def create_demographic_tables(df):
    return tuple(pd.DataFrame({
        'Count': df[col].value_counts().sort_index(),
        'Percentage (%)': (df[col].value_counts(normalize=True).sort_index() * 100).round(2)
    }) for col in ['Age_Group', 'Gender', 'Income'])

age_table, gender_table, income_table = create_demographic_tables(dataset1)

print("Age Group Distribution:\n", age_table)
print("\nGender Distribution:\n", gender_table)
print("\nIncome Distribution:\n", income_table)


# ============================
# Repeated measure ANOVA (timestep = 3) 
# ============================


# Melt data for plotting
df_melted = pd.melt(df, id_vars=['Treatment'], value_vars=['T1', 'T2', 'T3'],
                    var_name='Time', value_name='Score')

plt.figure(figsize=(10, 6))
ax = sns.boxplot(x='Time', y='Score', hue='Treatment', data=df_melted, palette='Set2')
plt.title('Repeated measures ANOVA: Treatment effect over three time steps')

# Determine the maximum y-value <- to position the significant bars
y_max = df_melted['Score'].max()

# Define time points and assign treatment groups
time_points = sorted(df_melted['Time'].unique())
treatment_groups = sorted(df_melted['Treatment'].unique())

for i, tp in enumerate(time_points):
    # Data for the current time point
    subset = df_melted[df_melted['Time'] == tp]
    
    # Scores for each treatment group
    group1 = subset[subset['Treatment'] == treatment_groups[0]]['Score']
    group2 = subset[subset['Treatment'] == treatment_groups[1]]['Score']
    
    # Paired t-test
    ttest_result = pg.ttest(group1, group2)
    p_val = ttest_result['p-val'].values[0]
    
    # Significance notation based on the p-value
    if p_val < 0.001:
        significance = '***'
    elif p_val < 0.01:
        significance = '**'
    elif p_val < 0.05:
        significance = '*'
    else:
        significance = 'n.s.'
        
    delta = 0.2
    x1, x2 = i - delta, i + delta
    
    # Draw the significance bar
    y, h, col = y_max + 1 + i * 0.5, 0.2, 'k'
    ax.plot([x1, x1, x2, x2], [y, y + h, y + h, y], lw=1.5, c=col)
    ax.text((x1 + x2) * 0.5, y + h, significance, ha='center', va='bottom', color=col)

ax.set_ylim(0, 10)
plt.xticks(rotation=45)
plt.legend(title='Treatment')
plt.show()


# %%
