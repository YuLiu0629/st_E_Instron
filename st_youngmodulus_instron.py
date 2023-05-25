import pandas as pd
import scipy
from scipy.signal import find_peaks
import streamlit as st
from sklearn.linear_model import LinearRegression


st.title("Young's modulus by Instron")

# import data file
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, skiprows = 5)

decimal_place = st.slider('How many decimal places do you want the result to be?', 0, 5, value=3, step=1)

# merge first two rows as headers
df = df.iloc[1:].set_axis(df.columns + ' ' + df.iloc[0], axis=1)

# extract strain and stress data, convert types of columns to float
df = df[['Compressive strain (mm/mm)', 'Compressive stress (MPa)']]
df['Compressive strain (mm/mm)'] = df['Compressive strain (mm/mm)'].astype(float)
df['Compressive stress (MPa)'] = df['Compressive stress (MPa)'].astype(float)


# find the breaking point which is the first peak in the plot, two conditions: a minimal prominence of 0.1 and width of at least 80 samples.

peaks, properties = find_peaks(df['Compressive stress (MPa)'], prominence=0.1, width=80)

st.line_chart(data=df, x = 'Compressive strain (mm/mm)',y = 'Compressive stress (MPa)')
st.markdown('The sample was broken at :red[{} mm], and the stress is :blue[{} MPa].'.format(df.iloc[peaks[0]][0], df.iloc[peaks[0]][1]))

# extract first 2%-10% for calculating Young's modulus
df_nobreak = df.iloc[0: peaks[0]]

max_strain = df_nobreak['Compressive strain (mm/mm)'].max()

df_YM = df_nobreak[(df_nobreak['Compressive strain (mm/mm)'] >= 0.02 * max_strain) & (df_nobreak['Compressive strain (mm/mm)'] <= 0.1 * max_strain) ]

# fitting data, find Young's modulus as the slope of linear fitting
from sklearn.linear_model import LinearRegression

X = df_YM['Compressive strain (mm/mm)'].values.reshape(-1, 1)  # values converts it into a numpy array
Y = df_YM['Compressive stress (MPa)'].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
linear_regressor = LinearRegression()  # create object for the class
linear_regressor.fit(X, Y)  # perform linear regression

st.markdown(f"Young's modulus: **{round(linear_regressor.coef_[0,0],decimal_place)} MPa**")
