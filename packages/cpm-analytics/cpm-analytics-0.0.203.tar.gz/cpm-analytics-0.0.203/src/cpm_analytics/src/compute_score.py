import numpy as np
import pandas as pd
import ppscore as pps
from minepy import MINE

#######################################################################
### Correlation
#######################################################################
def correlation_analysis(df, corr_threshold):
  print("===== Computing Correlation =====\n")
  df_corr_spearman = calculate_corr(df, corr_threshold, "spearman")
  df_corr_pearson = calculate_corr(df, corr_threshold, "pearson")   
  df_corr = (pd.concat([df_corr_spearman,df_corr_pearson],axis=0)
            .reset_index(drop=True)
            )
  print("* Completed!\n")
  return df_corr


def calculate_corr(df, corr_threshold, corr_type):
  df_corr = (df
             .corr(method=corr_type)
             .stack()
             .reset_index()
             .rename({"level_0":'Column1',"level_1":'Column2',0:'Score'}, axis=1)
             .query("Column1 != Column2") # drop if col1 and col2 are the same
             .assign(AnalysisType = corr_type.capitalize())
             )
  df_corr = df_corr[df_corr['Score'].abs() >= corr_threshold] # filter based on threshold
  df_corr.reset_index(drop=True, inplace=True)

  # remove duplicated pairs (based on Col1 and Col2 levels)
  # https://stackoverflow.com/questions/47051854/remove-duplicates-based-on-the-content-of-two-columns-not-the-order
  # improvement? https://stackoverflow.com/questions/48395350/how-to-remove-duplicates-from-correlation-in-pandas
  mask = ~pd.DataFrame(np.sort(df_corr[['Column1','Column2']], axis=1)).duplicated()
  df_corr = df_corr[mask]

  return df_corr.sort_values(by='Score', key=abs, ascending=False)


#######################################################################
### PPS
#######################################################################
def pps_analysis(df, pps_threshold):
  print("===== Computing PPS =====\n")
  pps_matrix_raw = pps.matrix(df)
  pps_matrix = (pps_matrix_raw
                .filter(['x', 'y', 'ppscore'])
                .pivot(columns='x', index='y', values='ppscore')
                .stack()
                .reset_index()
                .rename({"y":'Column1',"x":'Column2',0:'Score'}, axis=1)
                .query("Column1 != Column2") # drop if col1 and col2 are the same
                .assign(AnalysisType = "PPS")
                )
  
  pps_matrix = pps_matrix[pps_matrix['Score'].abs() >= pps_threshold] # filter based on threshold
  pps_matrix.reset_index(drop=True, inplace=True)
  print("* Completed!\n")
  return pps_matrix.sort_values(by='Score', key=abs, ascending=False).reset_index(drop=True)


#######################################################################
### MIC
#######################################################################
def mic_analysis(df_corr, df_pps, df, target_vars):
  # https://minepy.readthedocs.io/en/latest/
  print("===== Computing MIC =====\n")
  df_relevant_pairs = get_relevant_pairs(df_corr, df_pps, target_vars)
  df_mic = compute_mic(df, df_relevant_pairs)
  print("\n* Completed! \n")
  return df_mic


def get_relevant_pairs(df_corr, df_pps, target_vars):
  df_relevant_pairs = pd.concat([df_pps,df_corr], axis=0).reset_index(drop=True)
  mask = ~pd.DataFrame(np.sort(df_relevant_pairs[['Column1','Column2']], axis=1)).duplicated()
  df_relevant_pairs = df_relevant_pairs[mask].filter(["Column1","Column2"],axis=1).reset_index(drop=True)
  
  # subset only pairs where target_vars is present
  if None in target_vars:
    return df_relevant_pairs
  else:
    return df_relevant_pairs.query(f"Column1 in {target_vars} or Column2 in {target_vars}").reset_index(drop=True)
  

def compute_mic(df, df_relevant_pairs):
  df_mic = pd.DataFrame([])
  for index, row in df_relevant_pairs.iterrows():
    print(f"Computation {index + 1} / {df_relevant_pairs.shape[0]}")
    try:
        feature1,feature2 = row['Column1'], row['Column2']
        mine = MINE(alpha=0.6, c=15, est="mic_approx")
        mine.compute_score(df[feature1],df[feature2])
        mic_data = pd.DataFrame(data={"Column1":[feature1], "Column2":[feature2],
                                      "Score":[mine.mic()], "AnalysisType":"MIC"})
        df_mic = df_mic.append(mic_data)

    except: 
      print(f"MIC computation error :{feature1} and {feature2} on index {index + 1}")
      pass
  
  return df_mic.sort_values(by='Score', key=abs, ascending=False).reset_index(drop=True)
