import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import pandas as pd
import argparse

description = """
"""

parser = argparse.ArgumentParser( description = 'Produce scatterplots with continuous x-axis and y-axis; plots are stratified with the categorical column data if asked to- if not, default continuous plots are printed depending on the columns used for x-axis and y-axis.' )
    
parser.add_argument(
    "data_file",
    help = "Path to the input data file (TSV format)",
)
parser.add_argument(
    "-x", "--xaxis",
    type = int,
    default = 1,
    required = True,
    help = "1-based index for continuoous x-axis. '-x' is called in terminal while 'xaxis' is used in conjunction with the argparse syntax. This is a required command variable; if -x is not called, the plot won't be generated. This is a continuous axis composed only with integers; therefore, if the objects are not integers, it would print an error.",
)
parser.add_argument(
    "-y", "--yaxis",
    type = int,
    default = 1,
    required = True,
    help = "1-based index for continuous y-axis. '-y' is called in terminal while 'yaxis' is used in conjunction with the argparse syntax. This is a required command variable; if -y is not called, the plot won't be generated. This is a continuous axis composed only with integers; therefore, if the objects are not integers, it would print an error.",
)
parser.add_argument(
    "-z", "--stratify",
    type = int,
    default = False, 
    help = "1-based index for categorical iris variable to stratify scatterplots. '-z' is called in terminal while 'stratify' is used in conjunction with the argparse syntax. -z is an optional command variable that is not required.",
)

args = parser.parse_args()

fh = open(args.data_file)
df = pd.read_csv(fh, sep='\t') # This function is used to read the input data file as a pandas dataframe.

def x_column(path, index = 1):
    x = df.iloc[:, [index-1]]
    return x
    
def y_column(path, index = 1):
    y = df.iloc[:, [index -1]]
    return y

def z_column(path, index = 1):
    z = df.iloc[:, [index -1]]
    return z
# 1-based index of the column containing continuous x-values, y-values, and categorical series values.

x = x_column(args.data_file, args.xaxis)
y = y_column(args.data_file, args.yaxis)
z = z_column(args.data_file, args.stratify)
# variables x, y, and z are used to plot the plots in the terminal through a command-line interface.

headers = df.dtypes.index # Get header names so that they can be used to label the axes and to stratify the plots using the z-axis header.

if args.stratify: # if the z-argument is used in the terminal, this function is run.
    labeling = list(df[headers[args.stratify-1]].unique())
    # args.stratify is subtracted by 1 here because it is an integer that is based on 0-based python index.
    # This line is used to list unique categories in the specified column

    color = colors.Normalize(vmin = 0, vmax = len(labeling))
    # The default linear normalization in matplotlib
    
    for i in range(len(labeling)):
        data = df[headers[args.stratify-1]] == labeling[i]
        plt.scatter(x[data],y[data],data = data, s = 25 , label = labeling[i])
    # Label the x and y axes data points by the categorical data column with a specified size
    
    plt.title('Stratified Scatterplot by the Categorical Column')
    plt.xlabel(headers[args.xaxis])
    plt.ylabel(headers[args.yaxis])
    plt.legend()
    plt.savefig("scatter.png")
    plt.show()
    
else: # if the z-argument is not used in the terminal, a default continuous plot is generated.
    plt.scatter(x,y)
    plt.title('Continuous Scatterplot of the Input Data')
    plt.xlabel(headers[args.xaxis])
    plt.ylabel(headers[args.yaxis])
    plt.savefig("scatter.png")
    plt.show()
