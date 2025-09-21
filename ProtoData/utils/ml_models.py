import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (r2_score, mean_squared_error, accuracy_score, confusion_matrix)
from sklearn.preprocessing import LabelEncoder
from gui.variable_state.variables import *



def run_model(state):
    """Callback function to train and evaluate the selected ML model."""


    # 1. Input Validation
    if not state.target_variable or not state.feature_variables:
        state.ml_error_message = "Please select a target variable and at least one feature."
        return
    if state.target_variable in state.feature_variables:
        state.ml_error_message = "Target variable cannot also be a feature variable."
        return

    # 2. Data Preparation
    try:
        df_ml = state.df.copy()
        cols_to_check = [state.target_variable] + state.feature_variables
        df_ml.dropna(subset=cols_to_check, inplace=True)
        
        if len(df_ml) < 10: # Ensure enough data to split
            state.ml_error_message = "Not enough data to train a model after removing rows with missing values."
            return

        X = pd.get_dummies(df_ml[state.feature_variables], drop_first=True)
        y = df_ml[state.target_variable]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    except Exception as e:
        state.ml_error_message = f"Data preparation error: {e}"
        return

    # 3. Model Training & Evaluation
    algo = state.selected_algorithm
    if algo == "Linear Regression":
        if not pd.api.types.is_numeric_dtype(y):
            state.ml_error_message = "Linear Regression requires a numeric target variable."
            return
        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        r2 = r2_score(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        state.model_results = f"**R-squared:** `{r2:.4f}`\n\n**Mean Squared Error:** `{mse:.4f}`"

    elif algo in ["Logistic Regression", "K-Nearest Neighbors"]:
        le = LabelEncoder()
        y_train_encoded = le.fit_transform(y_train)
        y_test_encoded = le.transform(y_test)
        class_names = le.classes_

        model = LogisticRegression(max_iter=1000) if algo == "Logistic Regression" else KNeighborsClassifier()
        model.fit(X_train, y_train_encoded)
        y_pred_encoded = model.predict(X_test)
        
        accuracy = accuracy_score(y_test_encoded, y_pred_encoded)
        state.model_results = f"**Accuracy:** `{accuracy:.4f}`"
        
        # Generate confusion matrix plot
        cm = confusion_matrix(y_test_encoded, y_pred_encoded)
        fig = px.imshow(cm, text_auto=True, labels=dict(x="Predicted", y="Actual"),
                        x=class_names, y=class_names, color_continuous_scale='Blues')
        fig.update_layout(title_text='Confusion Matrix', title_x=0.5)
        state.confusion_matrix_fig = fig


