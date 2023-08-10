# import pandas as pd

# def analyze_data(file_path):
#     data = pd.read_excel("topic_detect_final_test.xlsx")
    
#     # Perform analysis on the data (you can customize this part)
#     summary = data.describe()
    
#     return summary

# if __name__ == "__main__":
#     data_file = input("Enter the path to the CSV data file: ")
#     analysis_results = analyze_data(data_file)
#     print(analysis_results)


import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

def main():
    st.title("Machine Learning Application")
    
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write("Uploaded Data:")
        st.write(data)
        
        X = data.drop('target_column', axis=1)  # Replace 'target_column' with your target column name
        y = data['target_column']
        
        model = LinearRegression()
        model.fit(X, y)
        
        st.write("Model Coefficients:", model.coef_)
        st.write("Model Intercept:", model.intercept_)
        
if _name_ == "_main_":
    main()