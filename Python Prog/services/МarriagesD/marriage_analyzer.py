import pandas as pd

class MarriageDivorceAnalyzer:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def most_common_ages(self):
        result = {}

        for gender in ['Male', 'Female']:
            data = self.df[self.df['Gender'] == gender]

            marriage_age = data.groupby('Age')['Marriages'].sum().idxmax()
            divorce_age = data.groupby('Age')['Divorces'].sum().idxmax()

            result[gender] = {
                'marriage_age': marriage_age,
                'divorce_age': divorce_age
            }

        return result
