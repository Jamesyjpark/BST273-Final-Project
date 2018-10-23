1.	List your name and email address.

Yeongjun Park
ypark1@hsph.harvard.edu
https://github.com/Jamesyjpark/BST273-Final-Project


2.	Summarize your experience working on the final project. For example, you might approximate how many hours you spent on it and how those hours were distributed. If you found some aspects considerably harder than others, list those here. If there are known problems with your final project script, list those here.

ANSWER:

I spent about 16 hours on the final project. I was able to produce the scatterplots using the data frame pretty quickly (in 3 hours); however, the implementation of the argparse module took a lot longer (about 9 hours). I spent the last 4 hours verifying and reproducing my script in terminal to traceback my errors by using another text file provided. 


3.	In a few sentences, describe what your final project script does.

ANSWER:

My final project produces scatterplots based on columns of data from TSV-format input files. In my script, these files are converted to pandas data frame. The argparse module is used to implement a command-line interface with four argparse arguments. The first argument indicates the path to the input file; other three arguments are used to facilitate 1-based index of the columns containing x-values, y-values, and categorical values to produce various plots. The column containing categorical series values is used to stratify the scatterplot; if this column is not called from terminal, a default scatterplot is produced that only contains x and y values. This is accomplished using an if-else function where the stratified plot is asked to be generated when the categorical column is used. If the categorical column is not used, the else function prints the default plot. Lastly, plots are labeled, titled, and saved in your working directory using the plt functions from the matplotlib module.  

4.	List any modules (outside of the Python standard library) that are required to execute your final project script. You may answer “N/A” if no such modules are required.

ANSWER:

matplotlib
- matplotlib.pyplot
- matplotlib.colors
pandas
argparse

5.	Describe your sample INPUT FILE(S). If you are completing a custom final project that does not require an input file, explain that clearly here.

ANSWER:

For a default project, we are provided a text file named iris_renamed.tsv. This is a TSV formatted text file that contains five different columns. The first four columns ('sepal_width', 'sepal_length', 'petal_width', 'petal_length') contain continuous integer data points that can be plotted as x or y values. The last column, 'label', contains three categorical variables (Iris-setosa, Iris-versicolor, Iris-virginica). This column is used to stratify the scatterplots by each unique category. The top row contains the names of fields from the data frame, and the input file is assumed to behave like a well-formed data frame. 


6.	Provide the command used to produce your sample OUTPUT FILE with flags and arguments specified (e.g. “$ python script_name.py arguments”).

ANSWER:

python scatter.py iris.renamed.tsv -x 1 -y 2 -z 5


7.	Describe your sample OUTPUT FILE(S). If you are completing a custom final project that does not produce an output file, capture the STDOUT of the command specified above and include it here (e.g. “$ command > sample_stdout.txt”).

ANSWER:

8.	What was your favorite part of learning to program in BST 273 (i.e. something we should definitely NOT change in future incarnations of the course)?

ANSWER:

My favorite part of this class is going over every essential component of python programming. I am familiar with R as I have used it for work for a few years so it was nice to see how python, as an object-oriented program, operates differently from R. This class was a clear reminder why the industry prefers Python over R even in statistical and graphical analyses. My favorite part was the use of loops in python. In R, I feel like loops are never used because they are extremely slow. Although these two languages are syntactically different, I found it helpful to understand and learn to construct loops to facilitate various operations. 

9.	What was your LEAST favorite part of learning to program in BST 273 (i.e. something we should look into changing for future incarnations of the course)?

ANSWER:

My least favorite part was using the argparse module. I do see the benefits of using this library, but I found it difficult to construct theoretical understanding of this module. I wish we had learned more functional programming using different python libraries like numpy and pandas. I am in a biostatistics program so I naturally wished that this class had been more data-science oriented. Nonetheless, I am still grateful to walk away with what I learned in this class.