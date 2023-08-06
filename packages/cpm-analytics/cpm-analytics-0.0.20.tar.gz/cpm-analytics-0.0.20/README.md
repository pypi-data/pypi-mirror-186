# Readme




The package analyzes the data by calculating Correlation levels, Power Predictive Score 
and Maximal Information Coefficient. That gives insights on how variables relate to each other, 
and is useful in the Exploratory Data Analysis workflow.


Logic
- It calculates correlation (Spearman and Person) using with all columns pairs, 
  then filters correlation levels based on pre-defined threshold.
  As a result, only relevant column pairs for Corrlaion remain.
- It calculates PPS using all columns pairs, 
  then filter PPS levels based on pre-defined threshold.
  As a result, only relevant column pairs for PPS remain.
- The list of relevant pairs for both Correlation and PPS are merged, and used as
  reference to compute MIC. 
  Computing MIC is expensive, and depending on your resources (time, processing etc),
  it would worth to compute MIC only in the most promising columns pairs. However, the 
  most complete analysis is made considerin all possible columns pairs combinations, 
  although that is more expensive


Outputs
- it reports the variables pairs with most interesting relationships
- as well as a scatter plot for each pair
