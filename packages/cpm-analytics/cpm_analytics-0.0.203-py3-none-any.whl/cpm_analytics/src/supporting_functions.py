#######################################################################
### supporting functions to the class
#######################################################################
import numpy as np

def data_validation(self, dataframe):
    if len(dataframe.columns) == 1: 
      raise ValueError(f'The dataframe should have more than 1 column. \nCurrent dataset column: {dataframe.columns.to_list()}')

    if dataframe.isna().sum().sum() > 0:
      raise ValueError("Your dataset has missing values, you should handle first.")

    for var in self.target_vars:
      if var not in dataframe.columns.to_list() and var != None:
        raise ValueError(f"{var} is not found at dataframe columns: {dataframe.columns.to_list()}")

    datetime_cols = dataframe.select_dtypes(include=[np.datetime64, 'datetime' or 'datetime64']).columns.to_list()
    if datetime_cols:
      print(f"* Note: The dataframe has a datetime variable: {datetime_cols}, which will be removed to compute the scores.\n\n")
      dataframe.drop(datetime_cols, axis=1,inplace=True)    
    
    return dataframe

def check_flags(self):
  if self.flag_compute_score == None:
    raise ValueError(f'The method .compute_score() should be run first')

  if self.flag_summary_report == None:
    raise ValueError(f'The method .summary_report() should be run first')

  if self.flag_plot_relationship == None:
    raise ValueError(f'The method .plot_relationships() should be run first')
  