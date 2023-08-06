# -*- coding: utf-8 -*-
"""
Created on Thu May 24 14:08:40 2018
Updated on Tue Jan 17 01:17:00 2023 

@author: LXavier

X4XL provides easier implementation of Read/Write from to to excel format

"""

""" This file will test the 'Read' and 'write' capabilities within PYthon
    For this, some previously scraped data will be used, in the form of CSV files.
    They will be loaded into DataFrames, exported to Excel files and then reimported
    to new DataFrame objects for testing. Finally some function will be defined to
    wrap these processes """
    


#import pandas_datareader as pdr
#import datetime
import pandas as pd
#import numpy as np




# Define our lovely I/O functions

def loadExcelSheet(file, sheet, parsef):
    """ 
    'parsef' is a function to perform additional treatment on the DataFrame
    
    """
    # Load Spreadsheet
    xl = pd.ExcelFile(file)
    # Load a sheet into a DataFrame object
    print(xl.sheet_names)
    df=xl.parse(sheet)
    # use the custom function to perform additional treatment
    df=parsef(df)
    return df




def saveExcelSheet(df, file, sheet):
    #Specify a writer variable
    if type(df) is list:
        writer = pd.ExcelWriter(file, engine= 'xlsxwriter')
        for x in range(len(df)):
            # write the Dataframe to the file
            df[x].to_excel(writer,sheet[x])
            # save the result
            print("Data saved to Excel file " + file + " in sheet " + sheet[x])        
            
        writer.save()
    else:

        writer = pd.ExcelWriter(file, engine= 'xlsxwriter')
        # write the Dataframe to the file
        df.to_excel(writer,sheet)
        # save the result
        writer.save()
        print("Data saved to Excel file " + file + " in sheet " + sheet)





# This function specifically handles dataframes previously scraped with proper routines

def doNothing(df):
    return df
    
    
    
    
    
    
