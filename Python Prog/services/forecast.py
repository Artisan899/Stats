import pandas as pd


class ForecastService:
    def forecast(self, df, period, window_size=5):
        df_result = df.copy()
        result_rows = []

        for region in df['Region'].unique():
            region_data = df[df['Region'] == region].sort_values('Year')
            values = region_data['Population'].tolist()

            # Прогнозируем на заданный период
            for _ in range(period):
                if len(values) >= window_size:
                    # Вычисляем скользящую среднюю по последним `window_size` значениям
                    next_val = sum(values[-window_size:]) / window_size
                else:
                    # Для первых лет (когда данных мало) используем только последние значения, чтобы не создавать резких изменений
                    next_val = values[-1]

                    # Если полученный прогноз значительно отклоняется от текущих данных, применяем корректировку
                if len(values) > 1 and abs(next_val - values[-1]) > (values[-1] * 0.05):  # 5% допустимая погрешность
                    next_val = values[-1] * 0.95  # Прогноз не должен резко изменяться

                new_year = region_data['Year'].max() + 1
                result_rows.append({'Year': new_year, 'Region': region, 'Population': next_val})
                values.append(next_val)

                # Обновляем DataFrame
                region_data = pd.concat(
                    [region_data, pd.DataFrame([{'Year': new_year, 'Region': region, 'Population': next_val}])],
                    ignore_index=True)

        # Объединяем оригинальные данные с результатами прогноза
        df_forecast = pd.concat([df, pd.DataFrame(result_rows)], ignore_index=True)
        return df_forecast
