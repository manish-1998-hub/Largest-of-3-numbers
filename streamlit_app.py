import streamlit as st

def find_largest(num1, num2, num3):
    return max(num1, num2, num3)

def main():
    st.title("Find the Largest of Three Numbers")
  
    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    num3 = st.number_input("Enter the third number:")

    largest_num = find_largest(num1, num2, num3)

    st.write("The largest number is:", largest_num)

if __name__ == "__main__":
    main()

