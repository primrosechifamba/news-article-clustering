import streamlit as st
import pandas as pd
import pickle

def load_all_data():
    df = pd.read_csv('dataall.csv')
    return df

def main():
    st.markdown("PRIMROSE CHIFAMBA R205534Y ")

    st.title("News Article Clustering")

    
    data = load_all_data()

    
    unique_clusters = data['Cluster'].unique()

    selected_cluster = st.sidebar.selectbox("Select a Cluster", unique_clusters)

    st.success(f"Cluster {selected_cluster}")

    cluster_articles = data[data['Cluster'] == selected_cluster]

    for idx, row in cluster_articles.iterrows():
        st.write(f"Title: {row['Title']}")
        st.write(f"Category: {row['Category']}")
        st.write(f"Source: {row['Source']}")
        st.write(f"URL: {row['Link']}")
        st.write(" ")


if __name__ == "__main__":
    main()
