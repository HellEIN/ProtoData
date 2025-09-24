import taipy.gui.builder as tgb
from gui.css import page_style
import pandas as pd

from gui.variable_state.variables import *
from utils.pre_processing_file import read_file


with tgb.Page() as main_page:
    main_page.set_style(page_style)
    with tgb.part(class_name="container card"):
        tgb.text("# 📊 ProtoData", mode="md", class_name="website_title")
        tgb.text("*Upload and explore your data files*", mode="md", class_name="website_name")
        tgb.text("*Note: Supported formats are csv, xlsx (concatenate all sheets), feather, parquet",mode="md",class_name="website_note",)
        tgb.text("*Advice :* For large files, consider converting them to **Parquet** or **Feather** for faster loading and smaller size.",mode="md",class_name="advice_note")
        with tgb.part(class_name="file_selector_container"):
            tgb.file_selector('{selected_file}', label="Select a data file", extensions=["csv", "xlsx", "feather", "parquet"],class_name="file_selector", on_action=read_file,)
            with tgb.part(render="{len(selected_file) > 0}"):
                tgb.text("**Selected File:** {selected_file if selected_file else 'No file selected'}", mode="md")
                tgb.text("**{file_info}**", mode="md", class_name="info_row_col")
            with tgb.part(render="{len(df) == 0}", class_name="data_preview_container"):
                tgb.text("**{error_message}**", mode="md", class_name="error_row_col")
        with tgb.part(render="{len(df) > 0}", class_name="data_preview_container"):
            tgb.text(value="---", mode="md", class_name="spacer")
            tgb.text(value="## Data Preview", mode="md", class_name="website_name")
            tgb.table('{df}', class_name="data_table", page_size=10, rebuild=True)
            tgb.text(value="---", mode="md", class_name="spacer")
            
            with tgb.part(render="{len(dtypes_df) > 0}"):
                tgb.text(value="## Column Information", mode="md", class_name="website_name")
                tgb.table('{dtypes_df}', class_name="data_table", page_size=50, rebuild=True)
                tgb.text(value="---", mode="md", class_name="spacer")
            with tgb.part(render="{len(numeric_describe) > 0}"):
                tgb.text(value="## Numeric Columns Statistics", mode="md", class_name="website_name")
                tgb.table('{numeric_describe}', class_name="data_table", page_size=50, rebuild=True)
                tgb.text(value="---", mode="md", class_name="spacer")
            with tgb.part(render="{len(categorical_describe) > 0}"):
                tgb.text(value="## Categorical Columns Statistics", mode="md", class_name="website_name")
                tgb.table('{categorical_describe}', class_name="data_table", page_size=50, rebuild=True)
                tgb.text(value="---", mode="md", class_name="spacer")

