import pandas as pd

def analyze_data(file_path):
    data = pd.read_excel("topic_detect_final_test.xlsx")
    
    # Perform analysis on the data (you can customize this part)
    summary = data.describe()
    
    return summary

if __name__ == "__main__":
    data_file = input("Enter the path to the CSV data file: ")
    analysis_results = analyze_data(data_file)
    print(analysis_results)
