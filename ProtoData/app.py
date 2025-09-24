
from gui.main_page_folder.main_page import main_page
# from gui.navigation import root_page
from gui.ml.ml_page import ml_page   

from taipy.gui import Gui, Icon, navigate
import taipy.gui.builder as tgb
from gui.personal_page.personal_pg import aboutme_page



def menu_option_selected(state, action, info):
    page = info["args"][0]
    navigate(state, to=page)

with tgb.Page() as root_page:
    tgb.menu(
        label="Menu",
        lov=[
            ("main_page", Icon("image/eda_1.png", "EDA",)),
            ("ML_Models", Icon("image/ml128.png", "Machine Learning Models")),
            ("about_me", Icon("image/information.png", "About Me")),
        ],
        on_action=menu_option_selected,
    )



pages = {"/": root_page,
        "main_page": main_page,
        "ML_Models": ml_page,
        "about_me": aboutme_page
        }

if __name__ == "__main__":
    Gui(pages=pages).run(watermark=None,
                        dark_mode=False, 
                        title="ProtoData", 
                        port=5000, 
                        use_reloader=True, 
                        favicon="image/favicon.ico")
