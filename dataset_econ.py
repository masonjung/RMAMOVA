#%%

import numpy as np
import pandas as pd

np.random.seed(42)

number_of_participants = 5000

# Dataset 1: Demographic Information
def generate_demographic_dataset(n=number_of_participants):
    age_groups = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
    genders = ['Male', 'Female']
    incomes = ['Low', 'Medium', 'High']

    data = []
    for i in range(n):
        age = np.random.choice(age_groups)
        gender = np.random.choice(genders)
        income = np.random.choice(incomes)
        completed = 'No' if i < n * 0.1 else 'Yes'
        data.append([age, gender, income, completed])

    df = pd.DataFrame(data, columns=['Age_Group', 'Gender', 'Income', 'Completed'])
    return df

# Dataset 2: Treatment Information
def generate_treatment_dataset(n=number_of_participants):
    treatments = ['Rational', 'Emotional']

    data = []
    for i in range(n):
        treatment = np.random.choice(treatments, p=[0.5, 0.5])
        data.append([treatment])

    df = pd.DataFrame(data, columns=['Treatment'])
    return df

def generate_likert_dataset(
    treatments,
    t1_mean=4,
    t1_std=1.2,
    t2_increase=2.1,
    t2_std=0.3,
    rational_decrease=0.2,
    emotional_decrease=1.2,
    t3_std=0.6,
    likert_min=1,
    likert_max=7,
    seed=42
):
    np.random.seed(seed)
    data = []

    for treatment in treatments:
        # t1
        t1 = int(round(np.random.normal(loc=t1_mean, scale=t1_std)))
        t1 = np.clip(t1, likert_min, likert_max)

        # t2
        t2 = int(round(t1 + np.random.normal(loc=t2_increase, scale=t2_std)))
        t2 = np.clip(t2, likert_min, likert_max)

        # t3
        if treatment == 'Rational':
            decrease = np.random.normal(loc=rational_decrease, scale=t3_std)
        else:
            decrease = np.random.normal(loc=emotional_decrease, scale=t3_std)

        t3 = int(round(t2 - decrease))
        t3 = np.clip(t3, likert_min, likert_max)

        data.append([t1, t2, t3])

    return pd.DataFrame(data, columns=["T1", "T2", "T3"])



# Generate datasets
dataset1 = generate_demographic_dataset()
dataset2 = generate_treatment_dataset()
dataset3 = generate_likert_dataset(dataset2['Treatment'])

# download dataset 123 and merged
# dataset1.to_csv("dataset1.csv", index=False)
# dataset2.to_csv("dataset2.csv", index=False)
# dataset3.to_csv("dataset3.csv", index=False)

# datasset_merged = pd.concat([dataset1, dataset2, dataset3], axis=1)
# datasset_merged.to_csv("dataset_merged.csv", index=False)


# %%
