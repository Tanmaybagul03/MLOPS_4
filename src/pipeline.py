import pandas as pd

# Step 1: Data Collection
def collect_data():
    df = pd.read_csv("data/data.csv")
    print("1. Data Collection completed.")
    return df


# Step 2: Data Preprocessing
def preprocess_data(df):

    # Handle missing values
    df["Study_Hours"] = df["Study_Hours"].fillna(df["Study_Hours"].mean())

    df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

    # Remove duplicate records
    df = df.drop_duplicates()

    print("2. Data Preprocessing completed.")
    return df


# Step 3: Feature Engineering
def feature_engineering(df):

    def performance_level(marks):
        if marks >= 85:
            return "Excellent"
        elif marks >= 70:
            return "Good"
        elif marks >= 50:
            return "Average"
        else:
            return "Poor"

    df["Performance_Level"] = df["Marks"].apply(performance_level)

    df["Attendance_Category"] = df["Attendance"].apply(
        lambda x: "Good" if x >= 75 else "Low"
    )

    print("3. Feature Engineering completed.")

    return df


# Step 4: Data Validation
def validate_data(df):

    assert df["Student_ID"].notnull().all()
    assert df["Marks"].between(0, 100).all()
    assert df["Attendance"].between(0, 100).all()
    assert df.isnull().sum().sum() == 0

    print("4. Data Validation completed.")


# Step 5: Save Processed Data
def save_data(df):

    df.to_csv("output/students_processed.csv", index=False)

    print("5. Processed data saved successfully.")


# Complete Pipeline
def main():

    print("\n--- Starting Data Pipeline ---")

    df = collect_data()

    df = preprocess_data(df)

    df = feature_engineering(df)

    validate_data(df)

    save_data(df)

    print("\n--- Pipeline Completed Successfully! ---")


# Execute Pipeline
if __name__ == "__main__":
    main()