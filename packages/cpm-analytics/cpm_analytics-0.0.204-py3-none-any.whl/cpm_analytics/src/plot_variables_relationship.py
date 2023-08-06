import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

#######################################################################
### plot relationship
#######################################################################
def plot_relationship(df, relevant_cols_pairs,df_summary, alpha_scatter=0.7):
  
  for index, row in relevant_cols_pairs.iterrows():
    print(f"========  {index + 1}: {row['Column1']} and {row['Column2']}  ========\n")
    print(f"* {show_scores(row,df_summary)}\n") # df_summary gets score (corr, pps, mic) for each column pair

    # decide plot type for each columns' combination
    x, y = row['Column1'] , row['Column2']
    var_type_x , var_type_y = df[x].dtype, df[y].dtype
    if var_type_x not in [object,"category"] and var_type_y not in [object,'category'] :
      plot_type = "scatterplot"
    elif var_type_x in [object, "category"] and var_type_y in [object, "category"] :
      plot_type = "barplot"
    else:
      plot_type = "boxplot"

    # plot accoriding to columns' type
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18,6))
    if plot_type == "scatterplot":
      sns.scatterplot(data=df, x=x, y=y, alpha=alpha_scatter, ax=axes[0])
      sns.scatterplot(data=df, x=y, y=x, alpha=alpha_scatter, ax=axes[1])
    
    elif plot_type == 'boxplot':
      # assume x is categorical, and y is numerical
      # if it's not, swap them
      if var_type_x not in [object,"category"]:
        x , y = y , x
      sns.boxplot(data=df, x=x, y=y, ax=axes[0])
      sns.histplot(data=df, x=y, hue=x, kde=True, ax=axes[1])
    
    elif plot_type == 'barplot':
      df.groupby([x,y]).size().unstack().plot(kind='bar', stacked=True, ax=axes[0]).legend(loc='best')
      df.groupby([y,x]).size().unstack().plot(kind='bar', stacked=True,ax=axes[1]).legend(loc='best')

    # set title and x/y label for both plots
    axes[0].set_title(f"{y}  x  {x}", fontsize=14, y=1.05)
    axes[0].set_xlabel(x)
    axes[0].set_ylabel(y)
    axes[1].set_title(f"{x}  x  {y}", fontsize=14, y=1.05)
    axes[1].set_xlabel(y)
    if plot_type == 'boxplot': axes[1].set_ylabel("Count")
    else: axes[1].set_ylabel(x)

    plt.show()
    print("\n\n")


def show_scores(row,df_summary):
  subset = df_summary.query(f"(Column1 == '{row['Column1']}' and Column2 == '{row['Column2']}') or (Column2 == '{row['Column1']}' and Column1 == '{row['Column2']}') ")
  statement = ""
  for analysis_type in subset['AnalysisType'].unique():
    if analysis_type != "PPS": score = subset.query(f"AnalysisType == '{analysis_type}'")['Score'].round(3).values[0]
    else: score = subset.query(f"AnalysisType == '{analysis_type}'")['Score'].round(3).values
    statement = statement + analysis_type + " " + str(score) + "  "

  return statement
