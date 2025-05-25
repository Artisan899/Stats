


class MarriageAnalyzer:
    @staticmethod
    def calculate_stats(df):
        df_sorted = df.sort_values('year')

        # Вычисление наиболее частых возрастов
        max_men_marry_age = df_sorted.loc[df_sorted['men_marry_count'].idxmax(), 'age']
        max_men_divorce_age = df_sorted.loc[df_sorted['men_divorce_count'].idxmax(), 'age']
        max_women_marry_age = df_sorted.loc[df_sorted['women_marry_count'].idxmax(), 'age']
        max_women_divorce_age = df_sorted.loc[df_sorted['women_divorce_count'].idxmax(), 'age']

        result = {
            'max_men_marry_age': max_men_marry_age,
            'max_men_divorce_age': max_men_divorce_age,
            'max_women_marry_age': max_women_marry_age,
            'max_women_divorce_age': max_women_divorce_age,
        }
        return result