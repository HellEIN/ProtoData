import taipy.gui.builder as tgb
from gui.css import page_style
import pandas as pd


from gui.main_page_folder.main_page import selected_file, df, file_name, error_message, file_info, dtypes_df, numeric_describe, categorical_describe
from utils.pre_processing_file import read_file 

with tgb.Page() as ml_model_page:
    ml_model_page.set_style(page_style)
    with tgb.part(class_name="container card"):
        tgb.text("# 🤖 ML Model", mode="md", class_name="website_title")
        tgb.text("*This section is under development.*", mode="md", class_name="website_name")