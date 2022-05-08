import pandas
import os


def create_data_frame():
    data = {'total_bill': [16.99, 10.34, 21.01, 23.68, 24.59],
            'tip': [1.01, 1.66, 3.50, 3.33, 3.61],
            'sex': ['Female', 'Male', 'Male', 'Male', 'Female']
            }
    return pandas.DataFrame(data)


def export_data_frame():
    try:
        data_frame = create_data_frame()
        data_frame.to_csv('/Users/giuseppetumminello/Desktop/Artificial Inteligence/FirstLabAI/csv/tips.csv',
                          index=False)
        if os.path.exists('/Users/giuseppetumminello/Desktop/Artificial Inteligence/FirstLabAI/csv/tips.csv'):
            print("Data Exported in csv")
    except Exception:
        print("Exception occurred")


def mean(column_name):
    return create_data_frame()[column_name].mean()


def max_value(column_name):
    return create_data_frame()[column_name].max()


def main():
    create_data_frame()
    export_data_frame()
    print('The mean of the columns total_bill is: ', mean('total_bill'))
    print('The max number of column tip is: ', max_value('tip'))


if __name__ == "__main__":
    main()
