# 📊 Student Performance Analyzer

A comprehensive Python-based data analysis tool that examines various factors influencing student academic performance. This project provides detailed insights into how study habits, attendance, parental involvement, and other variables correlate with exam scores.

## 🎯 Project Overview

This analyzer processes student performance data to identify key patterns and relationships between different educational factors and academic outcomes. It generates statistical summaries and visualizations to help educators, administrators, and researchers understand what drives student success.

## ✨ Features

- **Statistical Analysis**: Calculate mean, minimum, and maximum exam scores across the dataset
- **Data Visualization**: Generate multiple charts to visualize performance patterns
- **Factor Analysis**: Examine the impact of:
  - Study hours on exam performance
  - Attendance rates on academic outcomes
  - Parental involvement levels
  - School type (Public vs Private)
  - Student motivation levels
- **Individual Performance Tracking**: Identify top and bottom performers with detailed profiles

## 📋 Prerequisites

Before running this project, ensure you have the following installed:

```bash
Python 3.7+
pandas
matplotlib
```

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/student-performance-analyzer.git
cd student-performance-analyzer
```

2. Install required dependencies:
```bash
pip install pandas matplotlib
```

3. Ensure your dataset file `student_performance.csv` is in the project directory.

## 📁 Dataset Requirements

The CSV file should contain the following columns:

| Column | Description | Type |
|--------|-------------|------|
| `Exam_Score` | Student's exam score (0-100) | Integer/Float |
| `Hours_Studied` | Hours spent studying | Integer/Float |
| `Attendance` | Attendance percentage (0-100) | Integer/Float |
| `Parental_Involvement` | Level of parental involvement | Categorical |
| `School_Type` | Type of school (Public/Private) | Categorical |
| `Motivation_Level` | Student's motivation level | Categorical |

### Sample Data Format:
```csv
Student_ID,Exam_Score,Hours_Studied,Attendance,Parental_Involvement,School_Type,Motivation_Level
1,85,5,90,High,Private,High
2,72,3,75,Medium,Public,Medium
```

## 💻 Usage

Run the analyzer with:

```bash
python student_analyzer.py
```

The script will:
1. Load and display dataset information
2. Calculate statistical summaries
3. Generate six visualization plots
4. Display profiles of best and worst performing students

## 📊 Visualizations Generated

The analyzer creates the following charts:

1. **Exam Score Distribution Histogram** - Shows the spread of exam scores across the student population
2. **Study Hours vs Exam Score** - Line plot showing correlation between study time and performance
3. **Attendance vs Exam Score** - Bar chart comparing performance across attendance levels
4. **Parental Involvement Impact** - Bar chart showing effect of parental support
5. **School Type Comparison** - Performance comparison between Public and Private schools
6. **Motivation Level Impact** - How student motivation correlates with exam scores

## 📈 Sample Output

```
===== EXAM SCORE SUMMARY =====
Average Score: 78.45
Minimum Score: 52
Maximum Score: 98

===== BEST STUDENT =====
Student_ID: 145
Exam_Score: 98
Hours_Studied: 8
Attendance: 95
...
```

## 🔍 Key Insights

This tool helps answer questions such as:
- What is the average performance across all students?
- How do study hours correlate with exam scores?
- Does attendance significantly impact academic performance?
- What role does parental involvement play in student success?
- Are there performance differences between school types?
- How does student motivation affect outcomes?

## 🛠️ Customization

You can modify the analysis by:
- Adjusting histogram bins in the score distribution plot
- Changing attendance level categories
- Adding additional factors for analysis
- Customizing chart colors and styles


## 👤 Author

Your Name
- GitHub: [@yourusername](https://github.com/Deepakkumar188)
- LinkedIn: [Your LinkedIn](https://www.linkedin.com/in/deepak-kumar-a6037a327)

## 🙏 Acknowledgments

- Thanks to the educational data science community
- Inspired by real-world educational analytics needs
- Built with Python, pandas, and matplotlib

---
**Note**: This tool is designed for educational and research purposes. Ensure you have appropriate permissions before analyzing student data and comply with all relevant data privacy regulations (FERPA, GDPR, etc.).

## 🔄 Version History

- **v1.0.0** (2024-01-09)
  - Initial release
  - Core analysis features
  - Six visualization types
  - Statistical summaries

---

⭐ If you find this project helpful, please consider giving it a star on GitHub!
