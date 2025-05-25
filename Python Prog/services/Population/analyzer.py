
#Класс анализирует численность населения и находит, в каком регионе наблюдается максимальное и минимальное снижение населения за весь период

class PopulationAnalyzer:
    def __init__(self, df):
        self.df = df

    # Метод рассчитывает разницу между начальным и конечным значением населения по каждому региону, сортирует их и возвращает
    def min_max_decline(self):
        decline = {}
        for region in self.df['Region'].unique():
            values = self.df[self.df['Region'] == region].sort_values('Year')
            decline[region] = values['Population'].iloc[-1] - values['Population'].iloc[0]
        sorted_regions = sorted(decline.items(), key=lambda x: x[1])
        return sorted_regions[0], sorted_regions[-1]
