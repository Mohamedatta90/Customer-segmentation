
import streamlit as st
import pandas as pd 
import joblib

inputs = joblib.load('inputs.pkl')
data = pd.read_csv('data.csv') 

def get_recommended_merchants(customer_id):
    
    customer_info = data[data['CustomerID'] == customer_id]
    
    if not customer_info.empty:
        
        recommended_merchants = customer_info['Recommended Merchants'].values[0]
        return recommended_merchants
    else:
        return None

def main(): 
    st.title("Customer Segmentation App")
    
   
    customer_id = st.sidebar.text_input("Enter Customer ID:")
    
    if st.sidebar.button("Get Recommended Merchants"):
        if customer_id:
            
            try:
                customer_id = int(customer_id)
                recommended_merchants = get_recommended_merchants(customer_id)

                if recommended_merchants is not None:
                    # Create a DataFrame to display the result
                   
                   result = f"CustomerID: {customer_id}\n\nRecommended Merchants\n\n{recommended_merchants} " 


                   st.write(result)
                else:
                    st.write("Customer ID not found. Please check your input.")
            except ValueError:
                st.write("Please enter a valid Customer ID (numeric).")
        else:
            st.write("Please enter a Customer ID to see the recommendations.")

if __name__ == "__main__":
    main()
