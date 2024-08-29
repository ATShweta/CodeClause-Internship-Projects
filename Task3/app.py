import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Function to load and preprocess the data
def load_data(uploaded_file):
    data = pd.read_csv(uploaded_file)
    return data
    

# Function to perform clustering
def perform_clustering(data, n_clusters):
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(scaled_data)
    data['Cluster'] = kmeans.labels_
    return data

# Streamlit App
st.title('Customer Segmentation Tool')

# Upload CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    data = load_data(uploaded_file)
    st.write("Data preview:")
    st.write(data.head())

    # Select number of clusters
    n_clusters = st.slider('Select the number of clusters', 2, 10)

    if st.button('Cluster'):
        clustered_data = perform_clustering(data, n_clusters)
        st.write("Clustered Data:")
        st.write(clustered_data)

else:
    st.write("Please upload a CSV file to proceed.")
