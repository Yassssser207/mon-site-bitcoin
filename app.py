
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Mon Site Bitcoin", layout="wide")

def local_css(css):
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

local_css("""
body {
    margin: 0;
    padding: 0;
    background-image: url('images/background.png');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    font-family: 'Helvetica Neue', sans-serif;
}
#MainMenu, footer {visibility: hidden;}
.navbar {
    position: fixed;
    top: 0;
    width: 100%;
    padding: 1rem 2rem;
    background-color: rgba(0,0,0,0.5);
    z-index: 100;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.nav-links a {
    margin: 0 1rem;
    color: white;
    font-weight: bold;
    cursor: pointer;
    text-decoration: none;
}
.nav-links a:hover {
    color: gold;
    text-shadow: 0px 0px 10px gold;
}
.window {
    background-color: white;
    border-radius: 10px;
    padding: 20px;
    width: 400px;
    box-shadow: 0px 0px 30px rgba(0,0,0,0.5);
    position: absolute;
    top: 120px;
    right: 50px;
    z-index: 200;
}
.window h3 {
    margin-top: 0;
}
"""
)

# Navbar
st.markdown(f"""
<div class="navbar">
    <img src="https://raw.githubusercontent.com/tonutilisateur/mon-site-bitcoin/main/images/logo.png" width="60">
    <div class="nav-links">
        <a href="#accueil">Accueil</a>
        <a onclick="window.location.href='#botcoin'">Botcoin</a>
        <a href="#">À propos</a>
        <a href="#">Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br><br><br>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: white;'>Bienvenue sur notre site</h1>", unsafe_allow_html=True)
st.image("images/background.png", use_column_width=True)

botcoin_clicked = st.button("Ouvrir Botcoin")
if botcoin_clicked:
    st.markdown("""
    <div class="window">
        <h3>Botcoin 🤖</h3>
        <p>Botcoin est une intelligence artificielle intégrée au site pour aider les utilisateurs à trader plus efficacement.</p>
        <p>Elle analyse le marché, propose des prédictions, et vous accompagne dans vos décisions financières.</p>
    </div>
    """, unsafe_allow_html=True)
