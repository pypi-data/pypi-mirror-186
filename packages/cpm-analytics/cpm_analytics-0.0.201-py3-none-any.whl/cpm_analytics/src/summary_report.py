#######################################################################
### summary report
#######################################################################
import os

def show_summary_report(relevant_cols_pairs, df_summary):
    print(f"\n* There are {len(relevant_cols_pairs)} pairs of columns with relevant Corr, PPS, and MIC \n")
    print(relevant_cols_pairs)

    print(f"\n\n* Top 10 MIC scores\n")
    print((df_summary
          .query("AnalysisType == 'MIC'")
          .sort_values(by=['Score'],ascending=False)
          .head(10)
          .reset_index(drop=True) 
          ) )


def save_report(df, file_path):
  if file_path == None:
      file_path = "Report Summary.csv"
  else:
    if not os.path.isdir(file_path): os.makedirs(file_path)
    file_path = f"{file_path}/Report Summary.csv"
  
  df.to_csv(file_path, index=False)


def show_full_report(show_full_report_flag, df_summary):
    if show_full_report_flag:
      print(f"\n\n\n* Scores for each Column Pair per Analysis Type\n")
      print(df_summary.to_string()) 
