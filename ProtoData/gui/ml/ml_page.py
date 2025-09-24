import taipy.gui.builder as tgb
from gui.css import page_style
import pandas as pd
from utils.ml_models import run_model
from gui.main_page_folder.main_page import (df,available_columns,target_variable,feature_variables,selected_algorithm,algorithms,model_results,ml_error_message,confusion_matrix_fig,regression_plot_fig)
from gui.css import page_style



with tgb.Page() as ml_page:
    ml_page.set_style(page_style)
    with tgb.part(class_name='container card'):
        tgb.text(value="# 🤖 Machine Learning Workbench", mode="md", class_name='ml_title')
        
        # Show ML controls only if data is loaded
        with tgb.part(render="{len(df) > 0}"):
            tgb.text("## 1. Select Model and Variables", mode="md", class_name="ml_text")
            with tgb.layout("1 1"):
                tgb.selector(value="{selected_algorithm}", lov="{algorithms}", dropdown=True, label="Select Algorithm")
                tgb.selector(value="{target_variable}", lov="{available_columns}", dropdown=True, label="Select Target Variable (y)")
            
            tgb.selector(value="{feature_variables}", lov="{available_columns}", multiple=True, label="Select Feature Variables (X)")
            
            tgb.button("Train and Evaluate Model", on_action=run_model, class_name="plain")
            
            # Display results
            with tgb.part(render="{len(ml_error_message) > 0}"):
                tgb.text(value=" {ml_error_message}", mode="md", class_name="error_message")

            with tgb.part(render="{len(model_results) > 0}"):
                tgb.text("### 2. Model Performance", mode="md")
                tgb.text("{model_results}", mode="md")

            with tgb.part(render="{confusion_matrix_fig is not None}"):
                tgb.text("### 3. Confusion Matrix", mode="md")
                tgb.chart(figure="{confusion_matrix_fig}")
            
            with tgb.part(render="{regression_plot_fig is not None}"):
                tgb.text("### 3. Regression Visualization", mode="md")
                tgb.chart(figure="{regression_plot_fig}")

        # Show a message if no data is loaded
        with tgb.part(render="{len(df) == 0}"):
            tgb.text("*Please upload a data file on the 'Data Exploration' page first to enable this section.*", mode="md", class_name="info_section")