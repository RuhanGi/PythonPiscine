import matplotlib.pyplot as plt
from load_csv import load


def parse(value: str) -> float:
    """
    Parses data of type 24k, 12M, 36B
    Returns in Millions
    """
    try:
        value = value.strip()
        if value.endswith('k') or value.endswith('K'):
            return float(value[:-1]) / 1_000
        elif value.endswith('m') or value.endswith('M'):
            return float(value[:-1])
        elif value.endswith('b') or value.endswith('B'):
            return float(value[:-1]) * 1_000
        else:
            return float(value)
    except ValueError:
        return float('nan')


def plotCountry(df, country: str, colorc: str, labelc=None):
    """
    Plots specific country
    """
    if labelc is None:
        labelc = country
    info = df.loc[country]
    info = info.apply(parse)
    info.dropna(inplace=True)
    plt.plot(info.index, info.values, color=colorc, label=labelc)


def graph():
    """
    Loads the file population_total.csv,
    Displays the country information vs another.
    """
    try:
        df = load("population_total.csv")
        df.columns = df.columns.astype(int)

        plotCountry(df, "United Arab Emirates", 'red', labelc='UAE')
        plotCountry(df, "Saudi Arabia", 'green', labelc='KSA')

        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.xlim(1800, 2050)
        plt.ylabel("Population (millions)")
        plt.legend()

        plt.grid(axis='y')
        plt.gcf().canvas.mpl_connect(
            'key_press_event',
            lambda event: plt.close() if event.key == 'escape' else None
        )
        plt.show()
    except Exception as e:
        print("Error: " + str(e))


if __name__ == "__main__":
    graph()
