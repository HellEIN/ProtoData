# 📊 ProtoData - Advanced Data Analysis Platform

A comprehensive, modular data analysis platform built with Taipy that provides seamless data exploration, visualization, and machine learning capabilities with a professional, organized architecture.

## 🏗️ Project Structure

```
protodatatest/
│
├── app.py                          # Main application entry point
│
├── .vscode/                        # VS Code configuration
│   └── settings.json
│
├── core/                          # Core business logic (reserved for future expansion)
│
├── gui/                           # User interface components
│   │
│   ├── css.py                     # Global CSS styling and themes
│   │
│   ├── main_page_folder/          # Data exploration module
│   │   ├── main_page.py           # Main data exploration page
│   │   └── main_page_variable_state.py  # State management for data page
│   │
│   ├── ml/                        # Machine learning module
│   │   ├── ml_page.py             # ML algorithms and model training page
│   │   └── ml_page_variable_state.py    # State management for ML page
│   │
│   └── personal_page/             # Personal information/about page
│       └── personal_pg.py         # About/contact information page
│
├── image/                         # Static assets and icons
│   ├── favicon files              # Website favicons
│   ├── eda_1.png                  # Data exploration icon
│   ├── ml128.png                  # Machine learning icon
│   ├── information.png            # Info/about icon
│   └── about.txt                  # Image attribution info
│
└── utils/                         # Utility functions and helpers
    ├── ml_models.py               # Machine learning model implementations
    └── pre_processing_file.py     # Data preprocessing utilities
```

## 🚀 Features

### 📈 Data Exploration & Analysis
- **Multi-format Data Support**: CSV, Excel, JSON, Parquet, and more
- **Statistical Summaries**: Comprehensive descriptive statistics
- **Data Quality Assessment**: Missing values, data types, and distribution analysis
- **Real-time Data Profiling**: Automatic data quality reports


### 🤖 Machine Learning Suite
- **Algorithm Variety**: 
  - **Regression**: Linear, Polynomial, Ridge, Lasso
  - **Classification**: Logistic Regression, SVM, Random Forest, Gradient Boosting
  - **Clustering**: K-Means, DBSCAN, Hierarchical
  - **Dimensionality Reduction**: PCA, t-SNE
- **Model Evaluation**: Comprehensive metrics and validation
- **Hyperparameter Tuning**: Grid search and random search optimization
- **Feature Engineering**: Automatic feature selection and transformation
- **Model Comparison**: Side-by-side performance analysis

### 🎨 Professional UI/UX
- **Modern Design**: Clean, intuitive interface with professional styling
- **Responsive Layout**: Works seamlessly on desktop, tablet, and mobile
- **Interactive Navigation**: Smooth page transitions and intuitive menu system

## 🛠️ Installation & Setup

### Prerequisites
- **Python 3.8+** (Python 3.9+ recommended)
- **pip** package manager
- **Git** (for cloning the repository)

### Quick Start

1. **Clone the Repository**
   ```bash
   git clone <your-repository-url>
   cd protodatatest
   ```

2. **Create Virtual Environment** (Recommended)
   ```bash
   python -m venv protodata_env
   
   # Windows
   protodata_env\Scripts\activate
   
   # macOS/Linux
   source protodata_env/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install taipy pandas numpy scikit-learn plotly seaborn matplotlib openpyxl
   ```

4. **Run the Application**
   ```bash
   python app.py
   ```

5. **Access the Application**
   - Open your web browser
   - Navigate to `http://localhost:5000`
   - Start exploring your data!

## 📋 Dependencies

### Core Framework
- **taipy** `>=3.0.0` - Web application framework
- **pandas** `>=1.5.0` - Data manipulation and analysis
- **numpy** `>=1.21.0` - Numerical computing

### Machine Learning
- **scikit-learn** `>=1.1.0` - Machine learning algorithms
- **scipy** `>=1.9.0` - Scientific computing

### Visualization
- **plotly** `>=5.0.0` - Interactive visualizations
- **matplotlib** `>=3.5.0` - Static plotting
- **seaborn** `>=0.11.0` - Statistical data visualization

### Data I/O
- **openpyxl** `>=3.0.0` - Excel file support
- **pyarrow** `>=8.0.0` - Parquet file support

## 🎯 Usage Guide

### 1. Data Upload & Exploration
```python
# Navigate to the main page
# Upload your data file (CSV, Excel, etc.)
# Explore automatic data profiling and statistics
```

### 2. Creating Visualizations
```python
# Go to the visualization section
# Select your variables and chart type
# Customize appearance and export results
```

### 3. Machine Learning Workflow
```python
# Access the ML page
# Choose your algorithm and parameters
# Train models and evaluate performance
# Compare different approaches
```

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the root directory:
```env
TAIPY_PORT=5000
TAIPY_DEBUG=False
DATA_UPLOAD_MAX_SIZE=100MB
ML_MODEL_CACHE=True
```

### Custom Styling
Modify `gui/css.py` to customize the application appearance:
```python
# Add your custom CSS rules
# Define color schemes and themes
# Customize component styling
```



## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production Deployment
```bash
# Using Gunicorn (recommended)
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# Using Docker
docker build -t protodata .
docker run -p 5000:5000 protodata
```


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Taipy Team** - For the excellent web framework
- **Pandas Community** - For the powerful data manipulation library
- **Scikit-learn Contributors** - For the comprehensive ML toolkit
- **Plotly Team** - For the interactive visualization capabilities
- **Open Source Community** - For inspiration and continuous improvement

---

*Transform your data into insights with ProtoData - where analysis meets intuition.*
