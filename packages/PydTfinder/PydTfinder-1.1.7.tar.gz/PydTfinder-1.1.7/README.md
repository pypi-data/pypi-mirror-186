# **PydTfinder**
> ::A tool to find the phase equilibrium temperature at a given pressure with a given ΔT value::

<a href="https://www.buymeacoffee.com/woojingo" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-red.png" alt="Buy Me A Coffee" style="height: 40px !important;width: 120px !important;" ></a>

**PydTfinder** is a cutting-edge and user-friendly tool that makes it easy to pinpoint the precise temperature and pressure points where the phase equilibrium shifting occurs in your system. If you're working with <u>Hydrate-Liquid-Vapor (HLV) equilibrium</u> systems, PydTfinder is the perfect tool to help you find the exact equilibrium point of interest you need. By utilizing a temperature difference input and a highly accurate polynomial regression algorithm, PydTfinder is able to <u>identify the precise points of phase transition with pinpoint accuracy</u>. This powerful tool also offers a wide range of customization options, including `manual input`, `csv file input`, `output type`, `degree of regression`, `number of points` displayed in the plot, and `directory location` of the csv file, allowing you to tailor the tool to your specific needs. For researchers, engineers, and scientists working in the field of thermodynamics, phase equilibrium, and phase transition, PydTfinder is an essential tool that will save you time and increase your productivity.

## **Features**
- Plot the phase equilibrium data and the regression line
- Also plot the parallel line according to the temperature difference (ΔT value)
- Input options include `manual` input or input from a `csv` file
- Allows for adjusting the degree of the regression (the higher the degree, the more accurate the regression) and the number of points displayed in the plot
- Output options include `png`, `pdf`, `svg`, and `eps` file types

## **Dependencies**
- `pandas`
- `argparse`
- `pyfiglet`
- `tabulate`
- `matplotlib`
- `numpy`
- `sklearn`

## **Installation**
```
pip install pydtfinder
```
or
```
pip3 install pydtfinder
```

## **Uninstallation**
```
pip uninstall pydtfinder
```
or
```
pip3 uninstall pydtfinder
```

## **Usage**
The tool can be run using the command line 

```
pydtfinder -h
```

### **Optional arguments**
| Argument | Short form | Default | Description |
| --- | --- | --- | --- |
| `--input_type` | `-it` | manual | The type of P, T input. The options are: `manual`, `csv`|
| `--delta_t` | `-dt` | 5 | The temperature difference between the two curves in K |
| `--degree` | `-g` | 5 | The degree of the regression; the higher the degree, the more accurate the regression |
| `--num_point` | `-n` | 10 | The number of points that will be expressed in the plot |
| `--output` | `-o` | png | The file type of the output file. The options are: `png`, `pdf`, `svg`, and `eps` |
| `--directory` | `-d` | "./" | The directory location of the csv file |
| `--legend` | `-l` | "Your Phase EQ input" | The legend title of your Phase EQ input data |
| `--version` | `-v` | | Show the version of the tool |

## **Examples**
### **(1) Manual input**
PydTfinder can handle the manual input data from user. 

**Input**
```
pydtfinder -it manual -dt 6.2 -g 3 -n 4 -o png -l "Hydrogen Sulfide (Bond and Russel (1949))"
INFO Please enter the TEMPERATURE values (K) separated by comma: 283.2, 291.2, 299.7, 302.7
INFO Please enter the PRESSURE values (MPa) separated by comma: 0.310, 0.710, 1.496, 2.241
```

PydTfinder exhibited the below messages and plot.

**Output**
```
INFO The input temperature values are:  [283.2, 291.2, 299.7, 302.7] [unit: K]
INFO The input pressure values are:  [0.31, 0.71, 1.5, 2.24] [unit: MPa]
INFO Your desired temperature at 0.31 MPa is 277.00 K (T = 283.20 K - ΔT = 6.20 K)
INFO Your desired temperature at 0.95 MPa is 288.50 K (T = 294.70 K - ΔT = 6.20 K)
INFO Your desired temperature at 1.60 MPa is 294.07 K (T = 300.27 K - ΔT = 6.20 K)
INFO Your desired temperature at 2.24 MPa is 296.50 K (T = 302.70 K - ΔT = 6.20 K)


INFO The figure is saved as "DeltaT=6.2K.png"
```

**Plot (Manual input)**

<img src="./run_examples/manual/DeltaT=6.2K.png" height="60%" width="60%">

### **(2) CSV input**
PydTfinder can also handle the `.csv` file data from user. 

**Input**
```
pydtfinder -it csv -dt 6.0 -g 4 -n 8 -o pdf -d ./ -l "Adisasmito CO2 (1991)"
```

PydTfinder exhibited the below messages and plot.

**Output**
```
+---------------+-----------------------------+
|   File number | File name                   |
|---------------+-----------------------------|
|             0 | ./Adisasmito CO2 (1991).csv |
+---------------+-----------------------------+
INFO These are the files that are in the folder. Please type the file number that you want to use: 0
INFO The file name that would be utilized is ./Adisasmito CO2 (1991).csv
INFO The input temperature values are:  [274.3, 275.5, 276.8, 277.6, 279.1, 280.6, 281.5, 282.1, 282.9] [unit: K]
INFO The input pressure values are:  [1.42, 1.63, 1.9, 2.11, 2.55, 3.12, 3.51, 3.81, 4.37] [unit: MPa]
INFO Your desired temperature at 1.42 MPa is 268.30 K (T = 274.30 K - ΔT = 6.00 K)
INFO Your desired temperature at 1.84 MPa is 270.53 K (T = 276.53 K - ΔT = 6.00 K)
INFO Your desired temperature at 2.26 MPa is 272.17 K (T = 278.17 K - ΔT = 6.00 K)
INFO Your desired temperature at 2.68 MPa is 273.47 K (T = 279.47 K - ΔT = 6.00 K)
INFO Your desired temperature at 3.11 MPa is 274.57 K (T = 280.57 K - ΔT = 6.00 K)
INFO Your desired temperature at 3.53 MPa is 275.53 K (T = 281.53 K - ΔT = 6.00 K)
INFO Your desired temperature at 3.95 MPa is 276.34 K (T = 282.34 K - ΔT = 6.00 K)
INFO Your desired temperature at 4.37 MPa is 276.90 K (T = 282.90 K - ΔT = 6.00 K)


INFO The figure is saved as "DeltaT=6.0K.pdf"
```
**Plot (CSV input)**

<img src="./run_examples/csv/DeltaT=6.0K.png" height="60%" width="60%">

## **Contact**
If you have any questions or suggestions, please visit the GitHub repository at https://github.com/wjgoarxiv/pydtfinder for more information.

## **License**
This project is licensed under the MIT License. See the LICENSE file for details.

## **Pull requests**
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.