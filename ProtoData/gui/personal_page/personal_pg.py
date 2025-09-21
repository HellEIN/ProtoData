import taipy.gui.builder as tgb
from gui.css import page_style
import pandas as pd



with tgb.Page() as aboutme_page:
    aboutme_page.set_style(page_style)
    with tgb.part(class_name="container card"):
        tgb.text("# About Me", mode="md", class_name="website_title")
        tgb.text("*This section is under development.*", mode="md", class_name="website_name")