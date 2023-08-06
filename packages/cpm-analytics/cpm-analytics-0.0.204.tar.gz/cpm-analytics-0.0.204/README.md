## CPM Analytics


ADD EMOTICONS

`cpm-analytics` goal is to provide insights on major relationships in a tabular dataset. The package analyzes the data by computing the following scores: Correlation levels, Power Predictive Score (PPS) and Maximal Information Coefficient (MIC). 
Next, for each variable's pair, it plots the scatterplot, boxplot or bar plot. 
Finally, it shows a heatmap for each score and each variable pair.
 That gives insights on how variables relate to each other, and is useful in the Exploratory Data Analysis workflow. From there on, you can decide to which additional data visualizations to look after,

By the way, CPM is a short for **C**orrelation, **P**PS and **M**IC.


The overall logic is
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


The outputs
- it reports the variables pairs with most interesting relationships
- as well as a scatter plot for each pair

Please visit the documentation

Example usage

from cpm_analytics import CorrPpsMicAnalytics
analytics = CorrPpsMicAnalytics() #corr_threshold=0.4, pps_threshold=0.2)
analytics.compute_score(df_raw)
analytics.summary_report()
analytics.plot_relationships()
analytics.plot_heatmaps(figsize=(20,5))