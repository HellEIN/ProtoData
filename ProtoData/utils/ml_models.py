import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import (r2_score, mean_squared_error, accuracy_score, confusion_matrix)
from sklearn.preprocessing import LabelEncoder
from gui.variable_state.variables import *



def run_model(state):
    """Callback function to train and evaluate the selected ML model."""

    # Reset previous plots
    state.confusion_matrix_fig = None
    state.regression_plot_fig = None

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
        y_pred_train = model.predict(X_train)
        r2 = r2_score(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        state.model_results = f"**R-squared:** `{r2:.4f}`\n\n**Mean Squared Error:** `{mse:.4f}`"
        
        # Create regression plot
        # For visualization purposes, if we have multiple features, we'll plot against the first feature
        # or create a plot of actual vs predicted values
        if len(state.feature_variables) == 1:
            # Single feature - plot scatter with regression line
            feature_name = state.feature_variables[0]
            
            # Combine train and test data for plotting
            X_combined = pd.concat([X_train, X_test])
            y_combined = pd.concat([y_train, y_test])
            y_pred_combined = model.predict(X_combined)
            
            # Create scatter plot
            fig = go.Figure()
            
            # Add scatter points
            fig.add_trace(go.Scatter(
                x=X_combined.iloc[:, 0] if X_combined.shape[1] == 1 else df_ml[feature_name],
                y=y_combined,
                mode='markers',
                name='Data Points',
                marker=dict(color='blue', opacity=0.6)
            ))
            
            # Add regression line
            x_line = X_combined.iloc[:, 0] if X_combined.shape[1] == 1 else df_ml[feature_name]
            sorted_indices = x_line.argsort()
            fig.add_trace(go.Scatter(
                x=x_line.iloc[sorted_indices],
                y=y_pred_combined[sorted_indices],
                mode='lines',
                name='Regression Line',
                line=dict(color='red', width=2)
            ))
            
            fig.update_layout(
                title=f'Linear Regression: {state.target_variable} vs {feature_name}',
                xaxis_title=feature_name,
                yaxis_title=state.target_variable,
                showlegend=True
            )
            
        else:
            # Multiple features - plot actual vs predicted values
            y_combined = pd.concat([y_train, y_test])
            y_pred_combined = pd.concat([pd.Series(y_pred_train), pd.Series(y_pred)])
            
            fig = go.Figure()
            
            # Add scatter points for actual vs predicted
            fig.add_trace(go.Scatter(
                x=y_combined,
                y=y_pred_combined,
                mode='markers',
                name='Predictions',
                marker=dict(color='blue', opacity=0.6)
            ))
            
            # Add perfect prediction line (diagonal)
            min_val = min(y_combined.min(), y_pred_combined.min())
            max_val = max(y_combined.max(), y_pred_combined.max())
            fig.add_trace(go.Scatter(
                x=[min_val, max_val],
                y=[min_val, max_val],
                mode='lines',
                name='Perfect Prediction',
                line=dict(color='red', width=2, dash='dash')
            ))
            
            fig.update_layout(
                title='Linear Regression: Actual vs Predicted Values',
                xaxis_title=f'Actual {state.target_variable}',
                yaxis_title=f'Predicted {state.target_variable}',
                showlegend=True
            )
        
        state.regression_plot_fig = fig

    elif algo == "Logistic Regression":
        le = LabelEncoder()
        y_train_encoded = le.fit_transform(y_train)
        y_test_encoded = le.transform(y_test)
        class_names = le.classes_

        model = LogisticRegression(max_iter=1000)
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