import streamlit as st
import pandas as pd
import sklearn
import pickle 
import joblib

st.title('Movie Recommendation System')

with open('movies.pkl' ,'rb') as m:
    movies = pickle.load(m)

similarities = joblib.load('similarities.joblib')

movie_name = movies['title'].values

def recommend(selected_movie):
    movie_index = movies[movies['title'] == selected_movie].index[0]
    recommendations = similarities[movie_index]
    movies_list = sorted(list(enumerate(recommendations)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    
    return recommended_movies


selected_movie = st.selectbox('enter a movie name', movie_name)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)

    st.write('Recommended Movies:')

    for i in recommendations:
        st.write(i)