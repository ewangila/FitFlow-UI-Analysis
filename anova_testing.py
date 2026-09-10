import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# FitFlow completion times (seconds)
design_A = np.array([45, 42, 47, 44, 46, 43, 48, 45, 44, 46])
design_B = np.array([32, 30, 33, 31, 34, 32, 31, 33, 30, 32])
design_C = np.array([38, 36, 39, 37, 40, 38, 37, 39, 36, 38])
design_D = np.array([35, 33, 36, 34, 37, 35, 34, 36, 33, 35])

# Combine data for plotting
data = [design_A, design_B, design_C, design_D]
labels = ['A (Dropdown)', 'B (Grid)', 'C (Search)', 'D (Feed)']

# Create a boxplot
plt.figure(figsize=(8, 5))
sns.boxplot(data=data)
plt.xticks(ticks=[0, 1, 2, 3], labels=labels)
plt.ylabel('Completion Time (seconds)')
plt.title('FitFlow: Time to Find Workout by Interface Design')
plt.show()

# Perform One-Way ANOVA
f_stat, p_value = stats.f_oneway(design_A, design_B, design_C, design_D)

print(f"F-statistic: {f_stat:.4f}")
print(f"p-value: {p_value:.4e}")

# Combine all data into a single array
all_times = np.concatenate([design_A, design_B, design_C, design_D])

# Create matching group labels for each data point
group_labels = ['Traditional']*10 + ['Grid']*10 + ['Search']*10 + ['Personalized']*10

# Run Tukey's HSD test
tukey_results = pairwise_tukeyhsd(endog=all_times, groups=group_labels, alpha=0.05)

# Display the results
print(tukey_results)

# Calculate effect size (Eta-squared)
def calculate_eta_squared(groups):
    all_data = np.concatenate(groups)
    grand_mean = np.mean(all_data)
    ssb = sum(len(group) * (np.mean(group) - grand_mean)**2 for group in groups)
    sst = sum((x - grand_mean)**2 for x in all_data)
    return ssb / sst

groups = [design_A, design_B, design_C, design_D]
eta_squared = calculate_eta_squared(groups)

print("Effect Size Analysis:")
print(f"Eta-squared: {eta_squared:.3f}")
print(f"Interface design explains {eta_squared*100:.1f}% of variation in start times")