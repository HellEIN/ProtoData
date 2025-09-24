# 📊 ProtoData: Data Analysis & Machine Learning Dashboard

A comprehensive web-based data analysis and machine learning application built with Taipy. This application provides an intuitive interface for data exploration, preprocessing, and machine learning model training with interactive visualizations.

## ✨ Features

### 🔍 Data Exploration
- **Multi-format Support**: Load CSV, Excel (with multi-sheet support), Feather, and Parquet files
- **Comprehensive Data Summary**: Automatic generation of data type information, null counts, and basic statistics
- **Statistical Analysis**: 
  - Numeric columns: Descriptive statistics (mean, std, min, max, quartiles)
  - Categorical columns: Unique values, top frequencies, missing data analysis

### 🤖 Machine Learning Workbench
- **Supported Algorithms**:
  - Linear Regression with regression line visualization
  - Logistic Regression with confusion matrix
- **Interactive Visualizations**:
  - Scatter plots with regression lines for single-feature models
  - Actual vs Predicted plots for multi-feature models
  - Confusion matrices for classification problems
- **Model Performance Metrics**:
  - R-squared and MSE for regression
  - Accuracy scores for classification
- **Smart Data Handling**: Automatic preprocessing with missing value removal and categorical encoding

### 🎨 User Interface
- **Responsive Design**: Clean, modern interface with custom CSS styling
- **Multi-page Navigation**: Organized sections for different functionalities
- **Real-time Updates**: Dynamic content rendering based on data availability
- **Error Handling**: User-friendly error messages and validation

## 🚀 Quick Start

### Prerequisites
```bash
pip install taipy pandas numpy scikit-learn plotly
```

### Installation & Running
1. Clone the repository:
```bash
git clone https://github.com/HellEIN/ProtoData.git
cd ProtoData
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and navigate to the displayed URL (typically `http://localhost:5000`)

## 📁 Project Structure

```
├── app.py                      # Main application entry point
├── gui/
│   ├── css.py                  # Custom styling and CSS classes
│   ├── main_page_folder/
│   │   └── main_page.py       # Data exploration page and main variables
│   ├── ml/
│   │   └── ml_page.py         # Machine learning interface
│   ├── personal_page/
│   │   └── personal_pg.py     # Personal/about page
│   └── variable_state/
│       └── variables.py       # Global state variables
├── utils/
│   ├── ml_models.py           # Machine learning model implementations
│   └── pre_processing_file.py # Data loading and preprocessing functions
└── image/                     # Application icons and images
```

## 🔧 Core Components

### Data Loading (`utils/pre_processing_file.py`)
- **`read_file(state)`**: Handles multiple file formats with comprehensive error handling
- **`reset_all_data(state)`**: Cleans application state for new data sessions
- **Smart Excel Processing**: Automatically concatenates multiple sheets

### Machine Learning (`utils/ml_models.py`)
- **`run_model(state)`**: Unified model training and evaluation pipeline
- **Automatic Data Preprocessing**: Handles categorical variables and missing data
- **Visualization Generation**: Creates appropriate plots based on model type

### User Interface (`gui/`)
- **Modular Design**: Separate pages for different functionalities
- **State Management**: Centralized variable management across components
- **Responsive Layout**: Adapts to different screen sizes and data states

## 📊 Supported Data Formats

| Format | Extension | Special Features |
|--------|-----------|------------------|
| CSV | `.csv` | Standard comma-separated values |
| Excel | `.xlsx` | Multi-sheet concatenation |
| Feather | `.feather` | High-performance columnar format |
| Parquet | `.parquet` | Compressed columnar storage |

## 🤖 Machine Learning Capabilities

### Linear Regression
- **Single Feature**: Scatter plot with fitted regression line
- **Multiple Features**: Actual vs Predicted visualization
- **Metrics**: R-squared, Mean Squared Error
- **Requirements**: Numeric target variable

### Logistic Regression
- **Classification**: Binary and multi-class support
- **Visualization**: Interactive confusion matrix
- **Metrics**: Accuracy score
- **Preprocessing**: Automatic label encoding

## 🎯 Usage Tips

1. **Data Upload**: Start by uploading your dataset on the main data exploration page
2. **Data Review**: Examine the generated statistics and data quality metrics
3. **ML Training**: Navigate to the ML page, select your target and feature variables
4. **Model Selection**: Choose between Linear or Logistic Regression based on your problem type
5. **Results Analysis**: Review performance metrics and visualizations

## 🛠️ Customization

### Adding New Algorithms
1. Implement the algorithm in `utils/ml_models.py`
2. Add the algorithm name to the algorithms list
3. Update the conditional logic in `run_model()`
4. Add appropriate visualization code

### Styling Modifications
- Edit `gui/css.py` to customize the application appearance
- Modify class names and styling rules as needed

### New File Formats
- Extend `read_file()` function in `utils/pre_processing_file.py`
- Add appropriate pandas reading functions for new formats

## 🐛 Troubleshooting

### Common Issues
- **Import Errors**: Ensure all required packages are installed
- **File Loading**: Check file format and encoding
- **ML Errors**: Verify data types match algorithm requirements
- **Visualization**: Ensure data has sufficient samples for meaningful plots

### Performance Considerations
- Large datasets (>200MB) may experience slower loading times
- Complex models with many features may require additional processing time
- Browser memory limitations may affect very large visualizations

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## 📞 Support

For questions or support, please open an issue in the project repository.
