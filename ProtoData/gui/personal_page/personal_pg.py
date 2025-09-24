import taipy.gui.builder as tgb
from gui.css import page_style
import pandas as pd

# Personal information - customize these with your details
name = "Mohamed Ali Ettanji"
title = "Python Developer"
motivation = """
I love working with data — exploring it, analyzing it, and finding insights that tell a story. Python is my main tool for turning raw information into clear results, whether through data visualization or practical analysis. I’m also building my skills in machine learning, where I enjoy creating models that can make predictions and support better decisions. My goal is to keep learning, experimenting, and sharing what I discover along the way.
"""

# Python skills data
python_skills = pd.DataFrame({
    "Skill Category": [
        "Core Python", 
        "Data Science", 
        "GUI Development", 
        "Databases", 
        "Tools & Libraries"
    ],
    "Technologies": [
        "Python 3.x, OOP, Decorators, Context Managers",
        "Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn",
        "Taipy, Streamlit",
        "PostgreSQL",
        "Git, Jupyter"
    ],
    "Experience Level": [
        "Advanced",
        "Intermediate", 
        "Beginner",
        "Intermediate",
        "Intermediate"
    ]
})

with tgb.Page() as aboutme_page:
    aboutme_page.set_style(page_style)
    
    # Single card containing all content
    with tgb.part(class_name="container card"):
        # Header section
        tgb.text("# About Me", mode="md", class_name="website_title")
        tgb.text(f"## {name}", mode="md", class_name="website_name")
        tgb.text(f"*{title}*", mode="md", class_name="subtitle")
        
        # Introduction/Motivation section
        tgb.text("## My Motivation", mode="md", class_name="section_title")
        tgb.text(motivation, mode="md", class_name="motivation_text")
        
        # Skills section
        tgb.text("## Python Skills & Technologies", mode="md", class_name="section_title")
        tgb.text("Here's an overview of my technical expertise:", mode="md")
        tgb.table("{python_skills}", class_name="skills_table")
        
        # Additional info section
        tgb.text("## Current Focus", mode="md", class_name="section_title")
        tgb.text("""
        - Building interactive web applications with Taipy / Streamlit
        - Enhancing data analysis workflows with Pandas 
        - Exploring machine learning and data visualization
        - Continuous learning and skill development
        """, mode="md")
        
        # Contact section
        tgb.text("## Let's Connect", mode="md", class_name="section_title")
        tgb.text("""
        I'm always interested in collaborating on exciting projects or discussing 
        new opportunities in Python development. Feel free to reach out!

        *GitHub*: https://github.com/HellEIN
        *LinkedIn*: https://www.linkedin.com/in/mohamed-ali-ettanji

        """, mode="md")

# If you want to add custom CSS styles, you can extend your page_style
additional_styles = """
.motivation_text {
    line-height: 1.6;
    margin: 1rem 0;
    font-size: 1.1rem;
}

.section_title {
    color: #2c3e50;
    border-bottom: 2px solid #3498db;
    padding-bottom: 0.5rem;
}

.skills_table {
    margin: 1rem 0;
    width: 100%;
}

.subtitle {
    color: #7f8c8d;
    font-size: 1.2rem;
}
"""