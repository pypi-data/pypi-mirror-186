#######################################################################
### supporting functions to the class
#######################################################################

def data_validation(self, df):
    if len(df.columns) == 1: 
      raise ValueError(f'The dataframe should have more than 1 column. \nCurrent dataset column: {df.columns.to_list()}')

    if df.isna().sum().sum() > 0:
      raise ValueError("Your dataset has missing values, you should handle first.")

    for var in self.target_vars:
      if var not in df.columns.to_list() and var != None:
        raise ValueError(f"{var} is not found at dataframe columns: {df.columns.to_list()}")


def check_flags(self):
  if self.flag_compute_score == None:
    raise ValueError(f'The method .compute_score() should be run first')

  if self.flag_summary_report == None:
    raise ValueError(f'The method .summary_report() should be run first')

  if self.flag_plot_relationship == None:
    raise ValueError(f'The method .plot_relationships() should be run first')
  