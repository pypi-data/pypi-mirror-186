############################################################
### Heatmaps: Corr, PPS, and MIC
############################################################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

def process_data_for_heatmap(df, analysis_type):
  df_part1 = df.query(f"AnalysisType == '{analysis_type}'").drop("AnalysisType",axis=1)
  df_part2 =  df_part1.copy()
  df_part2['Column1'] , df_part2['Column2'] = df_part1['Column2'] , df_part1['Column1']
  
  if analysis_type != 'PPS':
    df_combined = pd.concat([df_part1,df_part2],axis=0).reset_index(drop=True)
  else: 
    df_combined = df_part1.copy()

  df_pivot = pd.pivot_table(data=df_combined,
                            index=['Column1'],
                            columns=['Column2'],
                            values='Score')
  
  return df_pivot


def plot_heatmap(df, analysis_type, self, figsize):
  print(f"\n\n\n===== Heatmap: {analysis_type} =====")
  if analysis_type in ['Spearman','Pearson']:
    heatmap_lower_triangle_only(df,self.corr_threshold, figsize)
  elif analysis_type in ['PPS']:
    heatmap_remove_diagonal(df, self.pps_threshold, figsize)
  elif analysis_type in ['MIC']:
    heatmap_lower_triangle_only(df, self.mic_threshold, figsize)
  else:
    print(f"** {analysis_type} is not found as analysis type!")


def heatmap_lower_triangle_only(df, threshold, figsize=(20, 12), font_annot=8):
  mask = np.zeros_like(df, dtype=np.bool)
  mask[np.triu_indices_from(mask)] = True
  mask[abs(df) < threshold] = True

  fig, axes = plt.subplots(figsize=figsize)
  sns.heatmap(df, annot=True, xticklabels=True, yticklabels=True,
              mask=mask, cmap='viridis', annot_kws={"size": font_annot}, 
              ax=axes,linewidth=0.5)
  axes.set_yticklabels(df.columns, rotation=0)
  plt.ylim(len(df.columns), 0)
  plt.ylabel('')
  plt.xlabel('')
  plt.show()


def heatmap_remove_diagonal(df, threshold, figsize=(20, 12), font_annot=8):
  mask = np.zeros_like(df, dtype=np.bool)
  mask[abs(df) < threshold] = True

  fig, ax = plt.subplots(figsize=figsize)
  ax = sns.heatmap(df, annot=True, xticklabels=True, yticklabels=True,
                    mask=mask, cmap='viridis', annot_kws={"size": font_annot},
                    linewidth=0.05, linecolor='grey')
  plt.ylim(len(df.columns), 0)
  plt.ylabel('')
  plt.xlabel('')
  plt.show()
