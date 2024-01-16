import streamlit as st
import pickle
import pandas as pd

st.title("Movie Recommendation System")

movies = pickle.load(open('movies.pkl', 'rb'))
movies = movies.reset_index()
movies_list = movies['title'].values
titles = movies[['title', 'poster_path']]
indices = pd.Series(movies.index, index=movies['title'])

cosine_similarity = pickle.load(open('cosine_similarity.pkl', 'rb'))

selected_option = st.selectbox('Choose a Movie', movies_list)

def fetch_poster(poster_path):
    base_url = 'https://image.tmdb.org/t/p/w500/'
    return base_url + poster_path

def recommend_movies(movie):
    i = movies[movies['title'] == movie].index[0]
    similarity_scores = list(enumerate(cosine_similarity[i]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similarity_scores = similarity_scores[1:6]
    rec_movies = [i[0] for i in similarity_scores]
    return titles.iloc[rec_movies]['title'].values, titles.iloc[rec_movies]['poster_path'].values

if st.button('Recommend Movies :clapper:', type='primary'):
    recommendations, posters = recommend_movies(selected_option)
    st.write('Showing Recommendations based on : ', selected_option)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommendations[0])
        st.image(fetch_poster(posters[0]))
    with col2:
        st.text(recommendations[1])
        st.image(fetch_poster(posters[1]))
    with col3:
        st.text(recommendations[2])
        st.image(fetch_poster(posters[2]))
    with col4:
        st.text(recommendations[3])
        st.image(fetch_poster(posters[3]))
    with col5:
        st.text(recommendations[4])
        st.image(fetch_poster(posters[4]))
    