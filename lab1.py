from matplotlib import pyplot as plt
import pandas as pd


def get_input():
    qty = int(input("input number columns to plot: "))
    args = []

    for i in range(qty):
        correct_input = False
        name = input('column: ')
        while not correct_input:
            if name in DF.columns:
                correct_input = True
                args.append(name)
            else:
                name = input('again: ')

    print(args)
    return args


def display(df, args):
    for column in args:
        if df[column].dtype == object:
            plt.pie(df[column].value_counts(), labels=df[column].value_counts().to_frame().index)
            plt.show()
        else:
            df.reset_index().plot(x='Date', y=column)
            plt.show()
    return


def to_format(df, name, replace, replace_with, var_type):
    return df[name].str.replace(replace, replace_with).astype(var_type)


def format_time(df):
    df['Time'] = pd.to_datetime(df['Time']).dt.strftime('%H:%M:%S')
    df['day/month'] = df['day/month'] + '.2020'
    df['Date'] = pd.to_datetime(df['day/month'] + ' ' + df['Time'])
    del df['day/month'], df['Time']
    return df


def parser(df):
    df = format_time(df)
    df.set_index('Date', inplace=True)
    df['Humidity'] = to_format(df, 'Humidity', '%', '', int)
    df['Wind Gust'] = to_format(df, 'Wind Gust', ' mph', '', int)
    df['Wind Speed'] = to_format(df, 'Wind Speed', ' mph', '', int)
    df['Pressure'] = to_format(df, 'Pressure', ',', '.', float)
    return df


DF = pd.read_csv('/Users/ry/Downloads/DATABASE.csv', sep=';')
DF = parser(DF)
Args = get_input()

display(DF, Args)
