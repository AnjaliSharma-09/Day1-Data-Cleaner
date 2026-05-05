#Student Score Analyzer 
def calculate_average(data):
    return sum(marks) / len(marks)
def find_min_max(data):
    return min(data), max(data)
def count_above_average(data, avg):
    return len([x for x in data if x > avg])
def grade_distribution(data):
    grades = {"A": 0, "B": 0, "C": 0, "Fail": 0}
    for score in data:
        if score >= 90:
            grades["A"] += 1
        elif score >= 75:
            grades["B"] += 1
        elif score >= 50:
            grades["C"] += 1
        else:
            grades["Fail"] += 1
    return grades
# Median Function
def calculate_median(data):
    sorted_data = sorted(data)
    n = len(data)
    if n % 2 == 0:
        return (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
    else:
        return sorted_data[n//2]
def performance_summary(data):
    avg = calculate_average(data)
    return{
        "Excellent": len([x for x in marks if x >= 90]),
        "Good": len([x for x in marks if 75 <= x < 90]),
        "Average": len([x for x in marks if 50 <= x < 75]),
        "Poor": len([x for x in marks if x < 50])
    }
# Execution
marks = [78, 85, 90, 67, 85, 92, 78]
avg = calculate_average(marks)
low, high = find_min_max(marks)
above_avg_count = count_above_average(marks, avg)
grades = grade_distribution(marks)
median = calculate_median(marks)
summary = performance_summary(avg)
#Output
print(" STUDENT SCORE ANALYZER")
print("-" * 35)
print(f"Marks: {marks}")
print(f"Average Score: {avg:.2f}")
print(f"Highest Score: {high}")
print(f"Lowest Score: {low}")
print(f"Students Above Average: {above_avg_count}")
print("\n Grade Distribution:")
for grade, count in grades.items():
    print(f"{grade}: {count}")
print(f"Median Score: {median}")
print("\n Performance Summary:")
print(summary)
