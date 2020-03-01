#!/usr/bin/env python3


''' imports '''
import pandas as pd
import matplotlib as plt
import numpy as np

class ASP:

    def read_csvdata():

        file_data = 'Worksheet in D  Lesson 2019 Applied Sriptong Using Python Python Elective (IT49450) - Project_14Mar19.csv'

        df = pd.read_csv(file_data, delimiter='\t', header=None, names = ['Brunei Darussalam', 'Indonesia', 'Malaysia'])
        df = df.isnull()
        print(df.head(3))
        print('1978 - 1987')

    read_csvdata()