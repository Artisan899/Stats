import pandas as pd

#Класс отвечает за прогнозирование численности населения с помощью скользящей средней.

class ForecastService:

    #Метод на основе исходных данных прогнозирует численность на заданное количество лет, возвращает обьединенный DataFrame

    def forecast(self, df, period, window_size=5):
        df_result = df.copy()
        result_rows = []

        for region in df['Region'].unique():
            region_data = df[df['Region'] == region].sort_values('Year')
            values = region_data['Population'].tolist()

            # Прогнозируем на заданный период
            for _ in range(period):
                if len(values) >= window_size:
                    # Вычисляем скользящую среднюю
                    next_val = sum(values[-window_size:]) / window_size
                else:
                    # Для первых лет (когда данных мало)
                    next_val = values[-1]

                new_year = region_data['Year'].max() + 1
                result_rows.append({'Year': new_year, 'Region': region, 'Population': next_val})
                values.append(next_val)

                region_data = pd.concat(
                    [region_data, pd.DataFrame([{'Year': new_year, 'Region': region, 'Population': next_val}])],
                    ignore_index=True)

        # Объединяем
        df_forecast = pd.concat([df, pd.DataFrame(result_rows)], ignore_index=True)
        return df_forecast