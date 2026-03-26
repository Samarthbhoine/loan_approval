def preprocess_input(data):
    import pandas as pd
    import numpy as np

    df = pd.DataFrame([data])

    # Feature Engineering (SAFE)
    df['TotalIncome'] = df['ApplicantIncome'] + df['CoapplicantIncome']

    # Avoid division by zero
    df['LoanAmount'] = df['LoanAmount'].replace(0, 1)
    df['Loan_Amount_Term'] = df['Loan_Amount_Term'].replace(0, 1)

    df['EMI'] = df['LoanAmount'] / df['Loan_Amount_Term']
    df['Income_Loan_Ratio'] = df['TotalIncome'] / df['LoanAmount']

    # Encoding
    mappings = {
        'Gender': {'Male': 1, 'Female': 0},
        'Married': {'Yes': 1, 'No': 0},
        'Education': {'Graduate': 1, 'Not Graduate': 0},
        'Self_Employed': {'Yes': 1, 'No': 0},
        'Property_Area': {'Urban': 2, 'Semiurban': 1, 'Rural': 0}
    }

    for col, mapping in mappings.items():
        df[col] = df[col].map(mapping)

    df['Dependents'] = df['Dependents'].replace('3+', 3).astype(int)

    # 🔥 FINAL SAFETY CHECK (VERY IMPORTANT)
    df.replace([np.inf, -np.inf], 0, inplace=True)
    df.fillna(0, inplace=True)

    return df
