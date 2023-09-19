import streamlit as st

# Set the title and header
st.title("Calculator App")
st.header("Perform basic calculations")

# Create input fields for user input
num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")

# Create a selectbox for the operation
operation = st.selectbox("Select an operation:", ["Addition", "Subtraction", "Multiplication", "Division"])

# Perform calculations based on the selected operation
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 == 0:
            result = "Error: Division by zero"
        else:
            result = num1 / num2

    # Display the result
    st.success(f"Result: {result}")
