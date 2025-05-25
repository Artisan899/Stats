import pandas as pd

class VVP_ForecastService:
    @staticmethod
    def forecast(df, period, window_size=5):
        df_result = df.copy()
        result_rows = []

        # Сортируем данные по годам
        df_sorted = df.sort_values('Year')

        # Прогнозируем на заданный период для ВВП и ВНП
        vvp_values = df_sorted['VVP'].tolist()
        vnp_values = df_sorted['VNP'].tolist()

        for _ in range(period):
            # Прогнозируем ВВП с использованием скользящей средней
            if len(vvp_values) >= window_size:
                next_vvp = sum(vvp_values[-window_size:]) / window_size
            else:
                next_vvp = vvp_values[-1]  # Для первых лет используем последнее значение ВВП

            # Прогнозируем ВНП с использованием скользящей средней
            if len(vnp_values) >= window_size:
                next_vnp = sum(vnp_values[-window_size:]) / window_size
            else:
                next_vnp = vnp_values[-1]  # Для первых лет используем последнее значение ВНП

            # Если разница слишком велика, корректируем прогноз
            if len(vvp_values) > 1 and abs(next_vvp - vvp_values[-1]) > (vvp_values[-1] * 0.05):
                next_vvp = vvp_values[-1] * 0.95  # Корректировка для ВВП

            if len(vnp_values) > 1 and abs(next_vnp - vnp_values[-1]) > (vnp_values[-1] * 0.05):
                next_vnp = vnp_values[-1] * 0.95  # Корректировка для ВНП

            # Новый год для прогноза
            new_year = df_sorted['Year'].max() + 1

            # Добавляем прогноз в результат
            result_rows.append({
                'Year': new_year,
                'VVP': next_vvp,
                'VNP': next_vnp
            })

            # Обновляем значения для следующего прогноза
            vvp_values.append(next_vvp)
            vnp_values.append(next_vnp)

            # Обновляем DataFrame с прогнозом
            df_sorted = pd.concat(
                [df_sorted, pd.DataFrame([{'Year': new_year, 'VVP': next_vvp, 'VNP': next_vnp}])],
                ignore_index=True)

        # Объединяем оригинальные данные с результатами прогноза
        df_forecast = pd.concat([df, pd.DataFrame(result_rows)], ignore_index=True)
        return df_forecast