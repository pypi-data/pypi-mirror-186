#!/usr/bin/env python3

# Import libraries 
import pandas as pd 
import os 
import argparse
import pyfiglet
from tabulate import tabulate
import glob
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import time

# Print the title 
os.system('cls' if os.name == 'nt' else 'clear')
title = pyfiglet.figlet_format('PydTfinder', font='small')
print('\n')
print(title+'\n')
print('\n')
print('------------------------------------------------')
print('If you have any questions, please send your questions to my email.')
print('\nOr, please suggest errors and areas that need updating.')
print('\n 📨 woo_go@yahoo.com')
print('\n')
print('\nVisit https://github.com/wjgoarxiv/pydtfinder for more information.')
print('------------------------------------------------')

# Argparse for the user input 
parser = argparse.ArgumentParser()
parser.add_argument('-it', '--input_type', type=str, default='manual', help='The type of P, T input. The options are: manual, csv (default = manual)')
parser.add_argument('-dt', '--delta_t', type=float, default=5, help='The temperature difference between the two curves (default = 5) [unit: K]')
parser.add_argument('-g', '--degree', type=int, default=5, help='The degree of the regression (default = 5); the higher the degree, the more accurate the regression')
parser.add_argument('-n', '--num_point', type=int, default=10, help='The number of points that will be expressed in your plot (default = 10)')
parser.add_argument('-o', '--output', type=str, default='png', help='The file type of the output file. The options are: png, pdf, svg, and eps (default = png)')
parser.add_argument('-d', '--directory', type=str, default='./', help='The directory location of the csv file (default = ./')
parser.add_argument('-l', '--legend', type=str, default='Your Phase EQ input', help='The legend title of your Phase EQ input data (default = Your Phase EQ input)')
parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0.0')

# Read the arguments
args = parser.parse_args()
input_type = args.input_type
delta_t = args.delta_t
degree = args.degree
num_point = args.num_point
output_type = args.output
input_dirloc = args.directory
userlegend = args.legend

# Show options selected by the user
print('\n')
print('------------------------------------------------')
print('INFO The options that you selected are as follows:')
print('INFO The input type is', input_type)
print('INFO The temperature difference is', delta_t, '[unit: K]')
print('INFO The degree of the regression is', degree)
print('INFO The number of points that will be expressed in your plot is', num_point)
print('INFO The output type is', output_type)
print('INFO The directory location of the csv file is', input_dirloc)
print('INFO The legend title of your Phase EQ input data is', "'"+userlegend+"'")
print('\n')
print('INFO If these options are not correct, please adjust them.')
print('------------------------------------------------')
print('\n')
time.sleep(0.8)

def main():
    ########## Input type handling ##########
    # Separate the cases depending on the -it argument: 
    if input_type == 'manual':
        # Input the Phase EQ points from the user. There are two options for the user; the one is type them manually, the other is upload a `csv` file which contains the Phase EQ points. There should be no headers. 
        ## 1st option (manual)
        print('\nINFO If you have a prepared csv file, please use the `pydtfinder -it csv` command.')
        print('\nINFO For more information, please enter `pydtfinder -h` command.')
        print('\n\n')

        temperature = input('INFO Please enter the TEMPERATURE values (K) separated by comma: ')
        temperature = temperature.split(',')
        temperature = [float(i) for i in temperature]

        pressure = input('INFO Please enter the PRESSURE values (MPa) separated by comma: ')
        pressure = pressure.split(',')
        # pressure values should be written upto the first decimal place. If the input is integer, it will be converted to float.
        if pressure[0].isdigit():
            pressure = [float(i) for i in pressure]
        else:
            pressure = [float(i) for i in pressure]
            pressure = [round(i, 2) for i in pressure]

        print('INFO The input temperature values are: ', temperature, '[unit: K]')
        print('INFO The input pressure values are: ', pressure, '[unit: MPa]')
        
    elif input_type == 'csv':
        ## 2nd option (upload a csv file)
        ### File number and name checking 
        file_list = glob.glob(input_dirloc + '*.csv')
        file_list.sort()
        try:
            if len(file_list) == 0:
                raise Exception
            else:
                pass
        except:
            print("\nINFO There is no csv file in your directory. Please check the directory location.")
            time.sleep(0.2)
            print("INFO The program will stop.")
            time.sleep(1)
            exit()

        ### Label file numbers and show all the files
        file_num = []
        for i in range(len(file_list)):
            file_num.append(i)
        print(tabulate({'File number': file_num, 'File name': file_list}, headers='keys', tablefmt='psql'))

        file_number = int(input('INFO These are the files that are in the folder. Please type the file number that you want to use: '))
        try:
            print("INFO The file name that would be utilized is", file_list[file_number])
        except IndexError:
            print("ERROR Your input number is out of range. Please check the file number again.")
            print("ERROR The program will stop.")
            exit()

        df = pd.read_csv(file_list[file_number], header=None)
        temperature = df[0].tolist()
        pressure = df[1].tolist()
        # Make pressure stored up to the 1st decimal place.
        pressure = [round(i, 2) for i in pressure]

        print('INFO The input temperature values are: ', temperature, '[unit: K]')
        print('INFO The input pressure values are: ', pressure, '[unit: MPa]')

    else: 
        print('ERROR The input type is not correct. Please check the input type.')
        print('ERROR The input type should be either `manual` or `csv`.')
        print('ERROR For more information, please enter `pydtfinder -h` command.')
        exit()
    ########## Input type handling ##########

    ########## Polynomial regression ##########
    # Convert the input data to numpy array
    x = np.array(temperature, dtype='float64') # x for temperature
    y = np.array(pressure, dtype='float64') # y for pressure

    # Reshape the data
    x = x.reshape(-1, 1)
    y = y.reshape(-1, 1)

    # Polynomial regression
    poly = PolynomialFeatures(degree=degree)
    y_poly = poly.fit_transform(y)

    # Create and fit linear regression model
    model = LinearRegression().fit(y_poly, x)

    # Predict x values for y
    x_pred = model.predict(y_poly)

    # Make a plot storing all the data
    min_x = min(x)
    max_x = max(x)
    diff_x = max_x - min_x
    min_y = min(y)
    max_y = max(y)
    diff_y = max_y - min_y

    # Plot 
    # create scatter plot (void circle)
    plt.scatter(x, y, color = 'black', marker = 'o', facecolors = 'none')

    # add regression curve
    plt.plot(x_pred, y, linestyle='dotted', color='black', alpha=0.7)

    # add labels
    plt.xlabel('Temperature (K)')
    plt.ylabel('Pressure (MPa)')
    plt.xlim(min_x - 0.7 * diff_x, max_x + 0.5 * diff_x)
    plt.ylim(min_y - 0.2 * diff_y, max_y + 0.2 * diff_y)
    plt.minorticks_on()
    ########## Polynomial regression ##########

    ########## Delta T calculation ##########
    def find_point(pressure):
        x = model.predict(poly.fit_transform([[pressure]]))
        return x

    # Make another variable for the pressure values
    barpres = y*10 # To put these values into the for loop range.
    barpres_min = min(barpres)
    barpres_max = max(barpres)

    for pressure in np.linspace(barpres_min, barpres_max, num_point):
        pressure = float(pressure)/10
        x = find_point(pressure)

        # Print the temperature at the given pressure in the regressed curve. 
        print('INFO Your desired temperature at {:.2f} MPa is {:.2f} K '.format(pressure, x[0][0]-delta_t) + '(T = {:.2f} K - ΔT = {:.2f} K)'.format(x[0][0], delta_t))

        # Mark that point on the graph (diamond shaped)
        plt.scatter(x, pressure, color='blue', marker='D')

        # The distance should be marked with dotted red line too.
        plt.scatter(x-delta_t, pressure, color='red', marker='D', label='$\Delta$T = -'+str(delta_t)+' K')

        # Write the "delta_t" K point information (temperature, pressure) on that point.
        plt.text(x, pressure, '({:.2f}, {:.2f})'.format(x[0][0], pressure), color='blue', size=12)
        plt.text(x-delta_t, pressure, '({:.2f}, {:.2f})'.format(x[0][0]-delta_t, pressure), color='red', size=12)

        # Add the legend info. 
        plt.legend([str(userlegend), 'Regressed', '$\Delta$T = 0 K', '$\Delta$T = '+str(delta_t)+' K'], loc='upper left')

        # Dot lines
        plt.axvline(x=x-delta_t, color='red', linestyle='dotted', alpha=0.5)
        plt.axhline(y=pressure, color='red', linestyle='dotted', alpha=0.5)
    plt.tight_layout()

    print('\n')
    # Save the figure according to the filetype option
    if output_type == "png":
        plt.savefig('DeltaT='+str(delta_t)+'K.png', dpi=300)
        print('INFO The figure is saved as "DeltaT='+str(delta_t)+'K.png"')
    elif output_type == "pdf":
        plt.savefig('DeltaT='+str(delta_t)+'K.pdf')
        print('INFO The figure is saved as "DeltaT='+str(delta_t)+'K.pdf"')
    elif output_type == "svg":
        plt.savefig('DeltaT='+str(delta_t)+'K.svg')
        print('INFO The figure is saved as "DeltaT='+str(delta_t)+'K.svg"')
    elif output_type == "eps":
        plt.savefig('DeltaT='+str(delta_t)+'K.eps')
        print('INFO The figure is saved as "DeltaT='+str(delta_t)+'K.eps"')
    else:
        print('ERROR The output type is not correct. Please check the output type again.')
        print('ERROR The output type should be either `png`, `pdf`, `svg`, or `eps`.')
        print('ERROR For more information, please enter `pydtfinder -h` command.')
        exit()
    ########## Delta T calculation ##########

if __name__ == "__main__":
    main()
