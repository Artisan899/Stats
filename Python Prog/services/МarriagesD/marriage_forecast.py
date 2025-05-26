import pandas as pd

class MarriageDivorceForecast:
    def forecast(self, df, period, window_size=3):
        df_result = df.copy()
        result_rows = []

        for gender in df['Gender'].unique():
            for age in df['Age'].unique():
                sub_data = df[(df['Gender'] == gender) & (df['Age'] == age)].sort_values('Year')

                years = sub_data['Year'].tolist()
                marriages = sub_data['Marriages'].tolist()
                divorces = sub_data['Divorces'].tolist()

                for i in range(period):
                    new_year = years[-1] + 1
                    if len(marriages) >= window_size:
                        next_m = sum(marriages[-window_size:]) / window_size
                        next_d = sum(divorces[-window_size:]) / window_size
                    else:
                        next_m = marriages[-1]
                        next_d = divorces[-1]

                    result_rows.append({
                        'Year': new_year,
                        'Gender': gender,
                        'Age': age,
                        'Marriages': round(next_m),
                        'Divorces': round(next_d)
                    })

                    years.append(new_year)
                    marriages.append(next_m)
                    divorces.append(next_d)

        forecast_df = pd.DataFrame(result_rows)
        return pd.concat([df_result, forecast_df], ignore_index=True)
