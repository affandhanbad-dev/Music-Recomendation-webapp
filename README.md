# Music-Recomendation-webapp

✅ README.md — Spotify Lyrics-Based Song Recommendation System
# 🎵 Spotify Song Recommendation System (Lyrics Based)

This project builds a **content-based song recommendation system** using lyrical similarity.  
Instead of audio features, we use **TF-IDF Vectorization + Cosine Similarity** on the lyrics dataset from **Kaggle** to find songs with similar lyrical content.

---

## 📦 Dataset

We use the **Spotify Million Song Dataset (Lyrics)**

📌 Kaggle Dataset:  
`notshrirang/spotify-million-song-dataset`

After downloading, we load:

| Column | Description |
|--------|-------------|
| artist | Name of artist |
| song | Song title |
| link | Song webpage (removed later) |
| text | Song lyrics |

After preprocessing → sampled **20,000 songs** for training.

---

## 🧹 Data Preprocessing

✔ Removed unwanted characters using Regex  
✔ Text normalized → lowercase  
✔ Tokenized using NLTK  
✔ Stopwords removed  
✔ WordCloud used to visualize frequent words  
✔ Added new feature:


clean_text → processed lyrics


---

## 🧠 Machine Learning Technique

| Step | Method |
|------|--------|
| Feature Extraction | TF-IDF Vectorizer (`max_features=10000`) |
| Similarity Calculation | Cosine Similarity |
| Recommendation | Top-N most similar lyrics by TF-IDF vectors |

---

## 🔍 Recommendation Function

```python
recomended_songs("Human Touch")


✅ Output Example:

One More Time
I Need You Like A Drug
Model Citizen
I Need To Know
Give It A Go

📊 Visualization Example

✅ Generated Word Cloud from all lyrics
🖼️ Useful for observing trending lyrical patterns

📂 Project Structure
│── spotify-million-song-dataset.zip
│── spotify_millsongdata.csv
│── recommendation.ipynb (your notebook)
│── kaggle.json (API credentials)
│── README.md

🛠 Requirements

Install dependencies:

pip install kaggle nltk wordcloud pandas numpy scikit-learn matplotlib


Also download NLTK resources:

nltk.download('punkt')
nltk.download('stopwords')
