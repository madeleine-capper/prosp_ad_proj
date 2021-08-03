import numpy as np
import pandas as pd
from prepare import prepare_logs
from bands import run_bands

def placeholder():
    print('I dont do anything lol this is where you would call your analysis script.')

def main():
    response = input('''
    
    Hello and welcome to the beaconing detection program.
    If you would like to proceed, please ensure that there is a file named access.log that
    you would like to analyze.  Would you like to proceed? (y/n)
    ''').lower()
    while response not in ['y','n','yes','no']:
        response = input('please respond with a y or n to proceed or exit.\n').lower()
    if response not in ['n','no']:
        cleaned_logs = prepare_logs('access.log')
        run_bands(cleaned_logs)
        return main()
    else:
        print('Goodbye!')
        exit()

if __name__ == '__main__':
    main()