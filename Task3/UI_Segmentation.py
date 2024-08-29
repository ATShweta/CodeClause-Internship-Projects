{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7c038380-8388-4d6b-8ea9-7886933968e8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Overwriting app.py\n"
     ]
    }
   ],
   "source": [
    "%%writefile app.py\n",
    "import streamlit as st\n",
    "import pandas as pd\n",
    "from sklearn.cluster import KMeans\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "\n",
    "# Function to load and preprocess the data\n",
    "def load_data(uploaded_file):\n",
    "    data = pd.read_csv(uploaded_file)\n",
    "    return data\n",
    "    \n",
    "\n",
    "# Function to perform clustering\n",
    "def perform_clustering(data, n_clusters):\n",
    "    scaler = StandardScaler()\n",
    "    scaled_data = scaler.fit_transform(data)\n",
    "    kmeans = KMeans(n_clusters=n_clusters)\n",
    "    kmeans.fit(scaled_data)\n",
    "    data['Cluster'] = kmeans.labels_\n",
    "    return data\n",
    "\n",
    "# Streamlit App\n",
    "st.title('Customer Segmentation Tool')\n",
    "\n",
    "# Upload CSV file\n",
    "uploaded_file = st.file_uploader(\"Choose a CSV file\", type=\"csv\")\n",
    "\n",
    "if uploaded_file is not None:\n",
    "    data = load_data(uploaded_file)\n",
    "    st.write(\"Data preview:\")\n",
    "    st.write(data.head())\n",
    "\n",
    "    # Select number of clusters\n",
    "    n_clusters = st.slider('Select the number of clusters', 2, 10)\n",
    "\n",
    "    if st.button('Cluster'):\n",
    "        clustered_data = perform_clustering(data, n_clusters)\n",
    "        st.write(\"Clustered Data:\")\n",
    "        st.write(clustered_data)\n",
    "\n",
    "else:\n",
    "    st.write(\"Please upload a CSV file to proceed.\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
