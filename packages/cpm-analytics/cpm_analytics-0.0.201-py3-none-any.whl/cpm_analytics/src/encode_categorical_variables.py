#######################################################################
### pipeline for encoding categorical variables
#######################################################################
from sklearn.pipeline import Pipeline
from feature_engine.encoding import OrdinalEncoder

def pipeline_encode_categorical_variables(df):
  """
  * if df has categorical variables
      df has original data, df_encoded has encoded categories to number
  * otherwise
      df_encoded is df, df is df
  """
  
  cat_cols = df.select_dtypes(exclude=['int64','float64']).columns.to_list()
  if cat_cols:
    pipeline = Pipeline([
        ("OrdinalEncoder", OrdinalEncoder(encoding_method='arbitrary', variables=cat_cols ) )
    ])
    df_encoded = pipeline.fit_transform(df)
  else:
    df_encoded = df.copy()

  return df, df_encoded