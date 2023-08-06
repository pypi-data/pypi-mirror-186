import pandas as pd
from .src.compute_score import correlation_analysis, pps_analysis, mic_analysis, get_relevant_pairs
from .src.encode_categorical_variables import pipeline_encode_categorical_variables
from .src.supporting_functions import data_validation, check_flags
from .src.summary_report import show_summary_report, save_report, show_full_report
from .src.plot_variables_relationship import plot_relationship
from .src.plot_heatmap import process_data_for_heatmap, plot_heatmap

class CorrPpsMicAnalytics:

  def __init__(self, corr_threshold=0.0, pps_threshold=0.0, target_vars=None):
    self.corr_threshold = corr_threshold
    self.pps_threshold = pps_threshold
    self.mic_threshold = 0
    if not isinstance(target_vars, list): 
      target_vars = [target_vars]
    self.target_vars = target_vars
    # flags to check if previous methods were run
    # self.flag_compute_score = None
    # self.flag_summary_report = None
    # self.flag_plot_relationship = None


  def compute_score(self, dataframe):
    # self.flag_compute_score = 1
    df_validated = data_validation(self, dataframe.copy())
    self.df, df_numerical = pipeline_encode_categorical_variables(df_validated)

    self.df_corr = correlation_analysis(df_numerical, self.corr_threshold)
    self.df_pps = pps_analysis(df_numerical, self.pps_threshold)
    self.df_mic = mic_analysis(self.df_corr, self.df_pps, df_numerical, self.target_vars)

    
  def summary_report(self, show_full_report_flag=False, file_path=None):
    # self.flag_summary_report = 1
    # check_flags(self)

    self.df_summary = (pd.concat([self.df_mic, self.df_pps, self.df_corr], axis=0).reset_index(drop=True))
    self.df_summary = self.df_summary.sort_values(by=['AnalysisType','Score'],ascending=False)
    self.relevant_cols_pairs = get_relevant_pairs(self.df_corr, self.df_pps, self.target_vars)

    show_summary_report(self.relevant_cols_pairs, self.df_summary)    
    save_report(self.df_summary, file_path)
    show_full_report(show_full_report_flag, self.df_summary)


  def plot_relationships(self):
    # self.flag_plot_relationship = 1
    # check_flags(self)
    plot_relationship(self.df, self.relevant_cols_pairs, self.df_summary)
    

  def plot_heatmaps(self, figsize=(15, 12)):
    # check_flags(self)

    for analysis_type in self.df_summary['AnalysisType'].unique():
      (self.df_summary
       .pipe(process_data_for_heatmap, analysis_type) 
       .pipe(plot_heatmap, analysis_type, self, figsize)
       )
