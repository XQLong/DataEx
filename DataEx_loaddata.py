import matplotlib.pyplot as plt
import pandas
from pandas.plotting import scatter_matrix

def main():
    url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
    names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
    # Load CSV using Pandas from URL
    data = pandas.read_csv(url, names=names)
    # Statistical Summary
    print(data.shape)
    print(data.get('preg'))
    print(data.head())
    print(data.describe())
    # Scatter Plot Matrix
    scatter_matrix(data)
    plt.show()

if __name__ == '__main__':
    main()
