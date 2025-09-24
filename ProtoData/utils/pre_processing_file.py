import pandas as pd
import numpy as np  


def read_file(state):
    """Callback function to read the uploaded data file."""
    if state.selected_file:
        state.file_name = state.selected_file
        state.error_message = ""  # Clear previous errors
        file = state.selected_file
        
        try:
            if file.endswith('.csv'):
                new_df = pd.read_csv(file, )
            elif file.endswith('.xlsx'):
                # i want it to read all sheets and concatenate them
                new_df = pd.concat(pd.read_excel(file, sheet_name=None), ignore_index=True)
            elif file.endswith('.feather'):
                new_df = pd.read_feather(file)
            elif file.endswith('.parquet', ):
                new_df = pd.read_parquet(file,)
            else:
                state.error_message = "Unsupported file format"
                return
            
            # Update data exploration state
            state.df = new_df.copy()
            dtypes_info = pd.DataFrame({
                'Column': new_df.columns, 'Data Type': new_df.dtypes.astype(str),
                'Non-Null Count': new_df.count(), 'Null Count': new_df.isnull().sum()
            }).reset_index(drop=True)
            state.dtypes_df = dtypes_info.copy()
            
            numeric_cols = new_df.select_dtypes(include=np.number).columns
            if not numeric_cols.empty:
                numeric_stats = new_df[numeric_cols].describe().round(3).T.reset_index().rename(columns={'index': 'Column'})
                state.numeric_describe = numeric_stats.copy()
            else:
                state.numeric_describe = pd.DataFrame()

            categorical_cols = new_df.select_dtypes(include=['object', 'category']).columns
            if not categorical_cols.empty:
                cat_stats = [{
                    'Column': col, 'Count': new_df[col].count(), 'Unique': new_df[col].nunique(),
                    'Top Value': new_df[col].mode().iloc[0] if not new_df[col].mode().empty else 'N/A',
                    'Top Frequency': new_df[col].value_counts().iloc[0] if len(new_df[col].value_counts()) > 0 else 0,
                    'Missing': new_df[col].isnull().sum()
                } for col in categorical_cols]
                state.categorical_describe = pd.DataFrame(cat_stats)
            else:
                state.categorical_describe = pd.DataFrame()
                
            rows, cols = state.df.shape
            state.file_info = f"**Data Summary:** {rows:,} rows × {cols} columns"
            
            # Update and reset ML state for the new dataset
            state.available_columns = new_df.columns.tolist()
            
            # Reset ML plots and results when new data is loaded
            state.confusion_matrix_fig = None
            state.regression_plot_fig = None
            state.model_results = ""
            state.ml_error_message = ""
            state.target_variable = ""
            state.feature_variables = []

        except Exception as e:
            state.error_message = f"Error reading file: {str(e)}"



def reset_all_data(state):
    """Resets all dataframes and file info."""
    state.df = pd.DataFrame()
    state.file_info = ""
    state.file_name = ""
    state.dtypes_df = pd.DataFrame()
    state.numeric_describe = pd.DataFrame()
    state.categorical_describe = pd.DataFrame()
    state.available_columns = []
    
    # Also reset ML state when all data is reset
    state.confusion_matrix_fig = None
    state.regression_plot_fig = None
    state.model_results = ""
    state.ml_error_message = ""
    state.target_variable = ""
    state.feature_variables = []