import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set the style for seaborn
sns.set(style='darkgrid')

# Load the data from the CSV file
file_path = 'dashboard/main_data.csv'  # Update with your file path
df = pd.read_csv(file_path)

# Streamlit app layout
st.set_page_config(page_title="Olist Store Dashboard", layout="wide")  # Wider layout
st.title('Olist Store Dashboard :sparkles:')
st.markdown("Welcome to the Olist Store data dashboard! Here, you can explore the monthly orders and customer distribution by state.")

# Sidebar for additional information
st.sidebar.header("Dashboard Controls")
st.sidebar.info("Navigate the marketplace landscape! Use this dashboard to uncover powerful insights and optimize your business strategies.")
st.sidebar.image("dashboard/logo.png", width=200)  # Company logo

# Monthly Orders Plot
st.subheader("📅 Number of Orders per Month")

# Extracting monthly orders data from the DataFrame
monthly_orders_df = df.groupby('month').size().reset_index(name='total_orders')

plt.figure(figsize=(10, 5))
plt.plot(monthly_orders_df["month"], monthly_orders_df["total_orders"], marker='o', linewidth=2, color="#72BCD4", label="Total Orders")
plt.title("Monthly Orders", loc="center", fontsize=20)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(True)
plt.legend()
st.pyplot(plt)  # Display the plot in the Streamlit app

# Create a DataFrame for customers by state
bystate_df = df['customer_state'].value_counts().reset_index()
bystate_df.columns = ['customer_state', 'customer_count']

# Customer by State Plot 
st.subheader("🌍 Number of Customers by State")
plt.figure(figsize=(10, 5))
colors_ = ["#72BCD4"] + ["#D3D3D3"] * (len(bystate_df) - 1)
sns.barplot(
    x="customer_count",
    y="customer_state",
    data=bystate_df.sort_values(by="customer_count", ascending=False),
    palette=colors_,
    hue=None,
    legend=False
)
plt.title("Number of Customers by States", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='y', labelsize=12)
st.pyplot(plt)  # Display the plot in the Streamlit app

# Footer
st.markdown("---")
st.markdown("### Contact Information")
st.markdown("If you have any questions, please contact us at support@olist.com.")
