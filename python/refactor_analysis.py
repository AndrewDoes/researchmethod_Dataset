import os
import csv
import time
from radon.complexity import cc_visit
from radon.metrics import mi_visit
from radon.raw import analyze

def analyze_code(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()

    # Start timing
    start_time = time.time()

    # Cyclomatic Complexity
    complexity_results = cc_visit(code)
    avg_complexity = sum([c.complexity for c in complexity_results]) / len(complexity_results) if complexity_results else 0

    # Maintainability Index
    maintainability_index = mi_visit(code, True)

    # Raw Metrics
    raw = analyze(code)

    end_time = time.time()
    analysis_time = round(end_time - start_time, 2)

    return {
        "avg_complexity": round(avg_complexity, 2),
        "mi": round(maintainability_index, 2),
        "loc": raw.loc,
        "lloc": raw.lloc,
        "sloc": raw.sloc,
        "comments": raw.comments,
        "time": analysis_time
    }

def analyze_directory(folder_path, output_csv):
    rows = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".py"):
            full_path = os.path.join(folder_path, filename)
            result = analyze_code(full_path)
            result["filename"] = filename
            rows.append(result)

    # Write to CSV
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["filename", "avg_complexity", "mi", "loc", "lloc", "sloc", "comments", "time"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    print(f"Analysis complete! Results saved to {output_csv}")

if __name__ == "__main__":
    input_folder = "python"      # Change this
    output_csv = "analysis_results.csv"
    analyze_directory(input_folder, output_csv)
