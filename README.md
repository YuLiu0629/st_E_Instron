# st_E_Instron
This code creates an online streamlit app for analysing data collected using Instron to get young's modulus of tested materials. 

> [!CAUTION]
> This code is written at colleague's request, the equation for calculation might not be correct, please double check the code before using! I am cerrently checking with the colleague for validation of this method. Modification and references will be added afterwards!

## How to use
1. Install streamlit, information on installing streamlit can be found on https://docs.streamlit.io/get-started/installation
2. Save the .py file and run this code in your terminal using
```
streamlit run st_E_Instron.py
```
The app should now be running on your browser! :beers:

### Alternatively
The app can be easily accessed on http://172.22.94.79:8501

## Format of data
As suggested in the app, the code analyzes .csv data file collected with Instron. 2 columns in the datatable that are used to calculate Young's modulus are 'Compressive strain (mm/mm)', 'Compressive stress (MPa)'. If the data generated with your instrument is different, remember to amend the column titles in the code.
