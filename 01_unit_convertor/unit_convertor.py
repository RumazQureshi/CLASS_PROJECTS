import streamlit as st
st.set_page_config(page_icon="®",page_title="Unit Convertor",layout="centered")
st.title("📏Unit Convertor")
st.markdown("**:orange-background[Select choice to change]**")

conversion_units = {
    "Length": ["Metre", "Kilometre", "Centimetre", "Millimetre", "Mile", "Yard", "Foot", "Inch"],
    "Mass": ["Gram","Kilogram","Milligram","Pound", "Ounce", "Ton"],
    "Time": ["Second", "Minute", "Hour", "Day"],
    "Speed": ["Metre per second", "Kilometre per hour", "Miles per hour"],
    "Temperature":["Kelvin","Celsius","Fahrenheit"]
}

conversion_factors = {
    # metre to others
    ("Metre", "Kilometre"): 0.001,
    ("Metre", "Centimetre"): 100,
    ("Metre","Millimetre"):1000,
    ("Metre","Foot"):3.28084,
    ("Metre","Mile"):0.000621371,
    ("Metre","Yard"):1.09361,
    ("Metre","Inch"):39.37008,
    # kilometres to others
    ("Kilometre", "Metre"): 1000,
    ("Kilometre", "Centimetre"): 100000,
    ("Kilometre","Millimetre"):1000000,
    ("Kilometre","Foot"):3280.84,
    ("Kilometre","Mile"):0.621371,
    ("Kilometre","Yard"):1093.61,
    ("Kilometre","Inch"):39370.08,
    # centimetres to others
    ("Centimetre", "Metre"): 0.01,
    ("Centimetre", "Kilometre"): 0.00001,
    ("Centimetre","Millimetre"):1,
    ("Centimetre","Foot"):0.0328084,
    ("Centimetre","Mile"):0.00000621371,
    ("Centimetre","Yard"):0.0109361,
    ("Centimetre","Inch"):0.3937008,
    # millimetres to others
    ("Millimetre", "Metre"): 0.001,
    ("Millimetre", "Kilometre"): 0.000001,
    ("Millimetre","Centimetre"):0.001,
    ("Millimetre","Foot"):0.00328084,
    ("Millimetre","Mile"):0.000000621371,
    ("Millimetre","Yard"):0.00109361,
    ("Millimetre","Inch"):0.03937008,
    # foot to others
    ("Foot", "Metre"): 0.3048,
    ("Foot", "Kilometre"): 0.0003048,
    ("Foot","Centimetre"):30.48,
    ("Foot","Millimetre"):304.8,
    ("Foot","Mile"):0.000189394,
    ("Foot","Yard"):0.333333,
    ("Foot","Inch"):12,
    # mile to others
    ("Mile", "Metre"): 1609.34,
    ("Mile", "Kilometre"): 1.60934,
    ("Mile","Centimetre"):160934,
    ("Mile","Millimetre"):1609340,
    ("Mile","Foot"):5280,
    ("Mile","Yard"):1760,
    ("Mile","Inch"):63360,
    # yard to others
    ("Yard", "Metre"): 0.9144,
    ("Yard", "Kilometre"): 0.0009144,
    ("Yard","Centimetre"):91.44,
    ("Yard","Millimetre"):914.4,
    ("Yard","Foot"):0.333333,
    ("Yard","Inch"):36,
    ("Yard","Mile"):0.000568182,
    # inch to others
    ("Inch", "Metre"): 0.0254,
    ("Inch", "Kilometre"): 0.0000254,
    ("Inch","Centimetre"):2.54,
    ("Inch","Millimetre"):25.4,
    ("Inch","Foot"):0.0833333,
    ("Inch","Yard"):0.0277778,
    ("Inch","Mile"):0.000015783,

    # gram to others
    ("Gram", "Kilogram"): 0.001,
    ("Gram", "Ton"): 0.000001,
    ("Gram", "Pound"): 0.00220462,
    ("Gram", "Ounce"): 0.035274,
    ("Gram", "Milligram"):1000,
    # kilogram to others
    ("Kilogram", "Ton"): 0.00110231,
    ("Kilogram", "Gram"): 1000,
    ("Kilogram", "Pound"): 2.20462,
    ("Kilogram", "Ounce"): 35.274,
    ("Kilogram", "Milligram"):1000000,
    # ton to others
    ("Ton", "Kilogram"): 907.18474,
    ("Ton", "Gram"): 907184.74,
    ("Ton", "Pound"): 2000,
    ("Ton", "Ounce"): 35273.92,
    ("Ton", "Milligram"):907184740,
    # pound to others
    ("Pound", "Kilogram"): 0.45359237,
    ("Pound", "Gram"): 453.59237,
    ("Pound", "Ton"): 0.0005,
    ("Pound", "Ounce"): 16,
    ("Pound", "Milligram"):453592.37,
    # ounce to others
    ("Ounce", "Kilogram"): 0.000028,
    ("Ounce", "Gram"): 28.3495,
    ("Ounce", "Ton"): 0.000028,
    ("Ounce", "Pound"): 0.0625,
    ("Ounce", "Milligram"):28349.5,
    # milligram to others
    ("Milligram", "Kilogram"): 0.000001,
    ("Milligram", "Gram"): 0.001,
    ("Milligram", "Ton"): 0.000000001,
    ("Milligram", "Pound"): 0.00000220462,
    ("Milligram", "Ounce"): 0.000035274,

    # second to others
    ("Second", "Minute"): 1 / 60,
    ("Second", "Hour"): 1 / 3600,
    ("Second", "Day"): 1 / 86400,
    # minutes to others
    ("Minute", "Second"): 60,
    ("Minute", "Hour"): 1 / 60,
    ("Minute", "Day"): 1 / 1440,
    # hour to others
    ("Hour", "Second"): 3600,
    ("Hour", "Minute"): 60,
    ("Hour", "Day"): 1 / 24,
    # day to others
    ("Day", "Second"): 86400,
    ("Day", "Minute"): 1440,
    ("Day", "Hour"): 24,

    # Celsius to others
    ("Celsius", "Fahrenheit"): lambda x: x * 9 / 5 +32,
    ("Celsius", "Kelvin"): lambda x: x + 273.15,
    # Fahrenheit to others
    ("Fahrenheit", "Celsius"): lambda x: (x - 32) *5 / 9,
    ("Fahrenheit", "Kelvin"): lambda x: (x - 32) *5 / 9 + 273.15,
    # Kelvin to others
    ("Kelvin", "Celsius"): lambda x: x - 273.15,
    ("Kelvin", "Fahrenheit"): lambda x: (x - 273.15)* 9 / 5 + 32,
    
    # metre per second to others
    ("Metre per second","Kilometre per hour"):lambda x: x * 3.6,
    ("Metre per second","Miles per hour"):lambda x: x * 2.23694,

    # miles per hour to others
    ("Miles per hour", "Metre per second"):lambda x: x / 2.23694,
    ("Miles per hour", "Kilometre per hour"):lambda x: x * 1.60934,
    # kilometer per hour to others
    ("Kilometre per hour", "Miles per hour"):lambda x: x / 1.60934,
    ("Kilometre per hour", "Metre per second"):lambda x: x /3.6,
}

# Select category
category = st.selectbox("Choose a category", list(conversion_units.keys()), index=None, placeholder="Select a category")

if category:
    st.write("Select units to convert between:")
    
    # Select first unit
    unit1 = st.selectbox("Convert from:", conversion_units[category])

    # Select second unit (removing already selected unit)
    available_units = [u for u in conversion_units[category] if u != unit1]
    unit2 = st.selectbox("Convert to:", available_units)

    # Input value for conversion
    # Input value for conversion
    value = st.number_input(f"Enter value in {unit1}:", min_value=0.0, step=0.1)
    st.button("🔄Convert")
    # Perform conversion
    if (unit1, unit2) in conversion_factors:
        factor = conversion_factors[(unit1, unit2)]
    
        if callable(factor):  # If it's a function, call it
            result = factor(value)
        else:  # Otherwise, just multiply
            result = value * factor
        st.success(f"{value} {unit1} = {result} {unit2}")
    else:
        st.error("Conversion factor not defined for this unit pair.")
st.markdown("---")
st.markdown("👨‍💻 Developed by ***Rumaz Naveed Qureshi***")