import pandas
import matplotlib.pyplot as plt


def load_file():
    data = pandas.read_csv('/Users/giuseppetumminello/Desktop/Artificial Inteligence/FirstLabAI/csv/miasta.csv')
    return data


def add_record(data, new_data):
    append_data = pandas.DataFrame(new_data)
    return data.append(append_data, ignore_index=True)


def main():
    data = load_file()
    print(data)
    new_data = {'Rok': [2010], 'Gdansk': [460], 'Poznan': [555], 'Szczecin': 405}
    data2 = add_record(data, new_data)
    print(data2)
    data2.plot(x='Rok', y='Gdansk', kind='line', title='Ludnosc w mistach Polski', marker='o', color='red',
               xlabel='Lata', ylabel='Liczba')
    data2.plot(x='Rok', kind='line', title='Ludnosc w mistach Polski', marker='o', xlabel='Lata', ylabel='Liczba')
    plt.show()


if __name__ == "__main__":
    main()
