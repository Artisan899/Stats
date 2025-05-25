import pandas as pd

class MarriageForecast:
    def forecast(self, df, period, window_size=3):
        df_result = df.copy()
        result_rows = []

        for region in df['Region'].unique():
            region_data = df[df['Region'] == region].sort_values('Year')
            values = region_data['Population'].tolist()

            for _ in range(period):
                next_val = sum(values[-window_size:]) / window_size if len(values) >= window_size else values[-1]
                new_year = region_data['Year'].max() + 1
                result_rows.append({'Year': new_year, 'Region': region, 'Population': next_val})
                values.append(next_val)

        df_forecast = pd.concat([df, pd.DataFrame(result_rows)], ignore_index=True)
        return df_forecast