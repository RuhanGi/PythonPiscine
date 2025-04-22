import matplotlib.pyplot as plt
from load_csv import load


def graph():
    """
    Loads the files and displays the projection of life expectancy
    in relation to the GDP of the year 1900 for each country
    """
    try:
        df_gdp = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        )
        df_exp = load("life_expectancy_years.csv")

        plt.scatter(df_gdp.loc[:, "1900"].values, df_exp.loc[:, "1900"].values)
        plt.xscale("log")

        plt.title("Life Expectancy vs. GDP (1900)")
        plt.xlabel("Gross Domestic Product")
        plt.ylabel("Life Expectancy")

        plt.gcf().canvas.mpl_connect(
            'key_press_event',
            lambda event: plt.close() if event.key == 'escape' else None
        )
        plt.show()
    except Exception as e:
        print("Error: " + str(e))


if __name__ == "__main__":
    graph()
