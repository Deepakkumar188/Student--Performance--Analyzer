# ==========================================
#      Student Performance Analyzer 
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
#  Load Dataset
# -------------------------------
df = pd.read_csv("student analyser.csv")

# -------------------------------
#  Dataset Overview
# -------------------------------
print("\n===== DATASET INFO =====")
print(df.info())

print("\n===== FIRST 5 RECORDS =====")
print(df.head())

# -------------------------------
#  Exam Score Summary
# -------------------------------
avg_score = df["Exam_Score"].mean()
min_score = df["Exam_Score"].min()
max_score = df["Exam_Score"].max()

print("\n===== EXAM SCORE SUMMARY =====")
print("Average Score:", round(avg_score, 2))
print("Minimum Score:", min_score)
print("Maximum Score:", max_score)

# -------------------------------
#  IMPROVED Exam Score Distribution (Histogram)
# -------------------------------
plt.figure(figsize=(8, 5))

plt.hist(
    df["Exam_Score"],
    bins=[50,55,60,65,70,75,80,85,90,95,100],
    edgecolor="black"
)

# Reference lines
plt.axvline(avg_score, linestyle="--", label=f"Average = {avg_score:.1f}")
plt.axvline(min_score, linestyle=":", label=f"Min = {min_score}")
plt.axvline(max_score, linestyle=":", label=f"Max = {max_score}")

plt.xlabel("Exam Score Range")
plt.ylabel("Number of Students")
plt.title("Distribution of Exam Scores")
plt.legend()
plt.grid(axis="y", alpha=0.5)
plt.show()

# -------------------------------
#  Study Hours vs Exam Score
# -------------------------------
study_hours_avg = df.groupby("Hours_Studied")["Exam_Score"].mean()

plt.figure(figsize=(8, 5))
plt.plot(study_hours_avg.index, study_hours_avg.values, marker='o')
plt.xlabel("Hours Studied")
plt.ylabel("Average Exam Score")
plt.title("Impact of Study Hours on Exam Score")
plt.grid(True)
plt.show()

# -------------------------------
#  Attendance Impact
# -------------------------------
attendance_bins = pd.cut(
    df["Attendance"],
    bins=[0,60,75,90,100],
    labels=["Low","Moderate","Good","Excellent"]
)

attendance_avg = df.groupby(attendance_bins)["Exam_Score"].mean()

plt.figure(figsize=(8, 5))
plt.bar(attendance_avg.index, attendance_avg.values)
plt.xlabel("Attendance Level")
plt.ylabel("Average Exam Score")
plt.title("Attendance vs Exam Score")
plt.show()

# -------------------------------
#  Parental Involvement Impact
# -------------------------------
parent_avg = df.groupby("Parental_Involvement")["Exam_Score"].mean()

plt.figure(figsize=(8, 5))
plt.bar(parent_avg.index, parent_avg.values)
plt.xlabel("Parental Involvement")
plt.ylabel("Average Exam Score")
plt.title("Effect of Parental Involvement on Exam Score")
plt.show()

# -------------------------------
#  School Type Comparison
# -------------------------------
school_avg = df.groupby("School_Type")["Exam_Score"].mean()

plt.figure(figsize=(8, 5))
plt.bar(school_avg.index, school_avg.values)
plt.xlabel("School Type")
plt.ylabel("Average Exam Score")
plt.title("Public vs Private School Performance")
plt.show()

# -------------------------------
#  Motivation Level Impact
# -------------------------------
motivation_avg = df.groupby("Motivation_Level")["Exam_Score"].mean()

plt.figure(figsize=(8, 5))
plt.bar(motivation_avg.index, motivation_avg.values)
plt.xlabel("Motivation Level")
plt.ylabel("Average Exam Score")
plt.title("Motivation Level vs Exam Score")
plt.show()

# -------------------------------
#  Best & Worst Student
# -------------------------------
best_student = df.loc[df["Exam_Score"].idxmax()]
worst_student = df.loc[df["Exam_Score"].idxmin()]

print("\n===== BEST STUDENT =====")
print(best_student)

print("\n===== WORST STUDENT =====")
print(worst_student)
