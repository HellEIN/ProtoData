
import pandas as pd

# Data Exploration State
selected_file = ""
df = pd.DataFrame()
file_name = ""
error_message = ""
file_info = ""
dtypes_df = pd.DataFrame()
numeric_describe = pd.DataFrame()
categorical_describe = pd.DataFrame()


# Machine Learning State
selected_algorithm = "Linear Regression"
algorithms = ["Linear Regression", "Logistic Regression", "K-Nearest Neighbors"]
available_columns = []
target_variable = None
feature_variables = []
model_results = ""
ml_error_message = ""
confusion_matrix_fig = None