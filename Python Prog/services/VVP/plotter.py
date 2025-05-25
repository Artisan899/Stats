import matplotlib.pyplot as plt
import os
import pandas as pd


#та же функция но для ВВП
def plot_gdp_gnp(df, original_years):
    fig, ax = plt.subplots(figsize=(10, 5))

    # Сортируем данные по годам
    df_sorted = df.sort_values('Year')

    # Фактические данные (до последнего года в оригинальном списке)
    actual = df_sorted[df_sorted['Year'].isin(original_years)]

    # Прогнозные данные (после последнего года в оригинальном списке)
    forecast = df_sorted[~df_sorted['Year'].isin(original_years)]

    # График фактических данных для ВВП
    ax.plot(
        actual['Year'], actual['VVP'],
        label="ВВП факт",
        linewidth=2
    )

    # График прогнозных данных для ВВП (если есть прогноз)
    if not forecast.empty:
        joined = pd.concat([actual.tail(1), forecast])
        ax.plot(
            joined['Year'], joined['VVP'],
            label="ВВП прогноз",
            linestyle='--',
            linewidth=2,
            alpha=0.8
        )

    # График фактических данных для ВНП
    ax.plot(
        actual['Year'], actual['VNP'],
        label="ВНП факт",
        linewidth=2
    )

    # График прогнозных данных для ВНП (если есть прогноз)
    if not forecast.empty:
        joined = pd.concat([actual.tail(1), forecast])
        ax.plot(
            joined['Year'], joined['VNP'],
            label="ВНП прогноз",
            linestyle='--',
            linewidth=2,
            alpha=0.8
        )

    ax.set_xlabel('Год')
    ax.set_ylabel('Показатели ВВП и ВНП')
    ax.legend()

    # Сохраняем график в папку static
    static_dir = os.path.join(os.path.dirname(__file__), '..', 'static')
    os.makedirs(static_dir, exist_ok=True)
    chart_path = os.path.join(static_dir, 'gdp_gnp_chart.png')
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()
    return 'gdp_gnp_chart.png'