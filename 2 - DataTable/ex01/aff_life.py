import matplotlib.pyplot as plt
from load_csv import load


def graph():
    """
    Loads the file life_expectancy_years.csv
    Displays the country information of your campus.
    """
    try:
        df = load("life_expectancy_years.csv")
        df.columns = df.columns.astype(int)
        info = df.loc["United Arab Emirates"]

        plt.plot(info.index, info.values)
        plt.title("UAE Life Expectancy Projections")
        plt.xlabel("Year")
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
