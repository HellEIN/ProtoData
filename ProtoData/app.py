from taipy.gui import Gui
from gui.main_page_folder.main_page import main_page
# from gui.navigation import root_page
from gui.ml.ml_page import ml_model_page

from taipy.gui import Gui, Icon, navigate
import taipy.gui.builder as tgb



def menu_option_selected(state, action, info):
    page = info["args"][0]
    navigate(state, to=page)

with tgb.Page() as root_page:
    tgb.menu(
        label="Menu",
        lov=[
            ("main_page", Icon("images/map.png", "EDA")),
            ("ML_Models", Icon("images/person.png", "Machine Learning Models")),
        ],
        on_action=menu_option_selected,
    )



pages = {"/": root_page,
        "main_page": main_page,
        "ML_Models": ml_model_page
        }

if __name__ == "__main__":
    Gui(pages=pages).run(watermark=False, dark_mode=False, title="ProtoData", port=5000, use_reloader=True)
