from memory_profiler import profile
import pandas as pd
@profile
def method1(a):
    def inner_method(b):
        tmp = []
        for i in range(b):
            df = pd.read_csv('/Users/sathishkumar/Learnings/practice ML copy/datasets/Admission_Dataset.csv')
            tmp.append(df)
        print(b)
    inner_method(a)
method1(10000)