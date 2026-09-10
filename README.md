# FitFlow UI Analysis

Statistical comparison of four FitFlow interface designs to determine which one minimizes user friction and optimizes the time it takes to find and start a workout.

## Overview

This project evaluates four alternative UI designs for the FitFlow fitness app using **One-Way ANOVA** and **Tukey's HSD** post-hoc testing. The goal is to identify the interface that allows users to locate and begin a workout the fastest.

### Designs Tested

| Design | Interface Type       | Mean Completion Time |
|--------|----------------------|----------------------|
| **A**  | Traditional Dropdown | 45.0 seconds         |
| **B**  | Visual Grid          | **31.8 seconds**     |
| **C**  | Search Bar           | 37.8 seconds         |
| **D**  | Personalized Feed    | 34.8 seconds         |

**Key Finding:** The **Visual Grid (Design B)** is significantly faster than all other designs (p < 0.001 for all pairwise comparisons). Interface design explains **92.6%** of the variation in task completion times (η² = 0.926).

## Methodology

- **Data**: 10 simulated user completion times (seconds) per design
- **Primary Test**: One-Way ANOVA
  - F-statistic ≈ 150.05
  - p-value ≈ 2.11 × 10⁻²⁰
- **Post-hoc**: Tukey’s Honestly Significant Difference (HSD)
- **Effect Size**: Eta-squared (η²)

All pairwise differences are statistically significant at α = 0.05.

## Repository Structure
```
FitFlow-UI-Analysis/
├── ANOVA.ipynb          # Full interactive analysis notebook
├── anova_testing.py     # Standalone Python script
├── requirements.txt     # Dependencies
├── LICENSE              # MIT License
└── README.md
```
## Setup

```bash
pip install -r requirements.txt
```
## Dependencies

- `numpy`
- `scipy`
- `seaborn`
- `matplotlib`
- `statsmodels`

## Usage

### Run the standalone script

```bash
python anova_testing.py
```
This will:

1. Generate a boxplot of completion times  
2. Print the ANOVA results  
3. Display Tukey HSD pairwise comparisons  
4. Calculate and report the effect size (η²)

### Explore the notebook

Open `ANOVA.ipynb` in Jupyter for a step-by-step walkthrough of the analysis, including visualizations and interpretation.

## Results Summary

- **Fastest design**: Visual Grid (B) — mean 31.8s  
- **Slowest design**: Traditional Dropdown (A) — mean 45.0s  
- **All differences significant**: Every design pair differs significantly (Tukey HSD)  
- **Large practical effect**: η² = 0.926 indicates interface design is the dominant factor in task time

## License

This project is licensed under the [MIT License](LICENSE).
