

# 🎤 TED Talk Recommender System using Machine Learning

A machine learning-based web app that recommends TED Talks based on the title you input. It uses content-based filtering and natural language processing (NLP) to find similar talks using features like title, tags, and description.

## 🚀 Features

- Input the title of a TED Talk and get top 5 similar talk recommendations.
- Powered by **TF-IDF vectorization** and **cosine similarity**.
- Flask backend API serving recommendations.
- CORS-enabled API for easy integration with frontend (Gradio, React, etc.).

---

## 🧠 How It Works

1. **Data Preprocessing**:
   - The TED dataset is loaded with fields like `title`, `tags`, `description`, etc.
   - Text is cleaned and combined into a single metadata string.

2. **Vectorization**:
   - TF-IDF (Term Frequency–Inverse Document Frequency) is applied to transform metadata into numerical feature vectors.

3. **Similarity Calculation**:
   - Cosine similarity is calculated between all TED talks.
   - For a given talk title, the most similar ones are retrieved based on vector similarity.

4. **Flask API**:
   - A `/recommend` POST endpoint receives a talk title and returns recommended talks in JSON.

---

## 🛠 Project Structure

```
TED-Recommender/
│
├── recommender.py          # Core ML logic: TF-IDF, cosine similarity, get_recommendations()
├── app.py                  # Flask API to handle POST requests and return recommendations
├── ted_data.csv            # Dataset of TED Talks (titles, tags, descriptions, etc.)
├── requirements.txt        # Required Python packages
└── README.md               # Project documentation
```

---

## 🔁 API Usage

**Endpoint:** `/recommend`  
**Method:** `POST`  
**Input:**

```json
{
  "title": "The power of vulnerability"
}
```

**Output:**

```json
[
  "Listening to shame",
  "The skill of self-confidence",
  "What makes a good life?",
  "The puzzle of motivation",
  "How to speak so that people want to listen"
]
```

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/TED-Recommender.git
cd TED-Recommender
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Flask App

```bash
python app.py
```

The app will start at `http://127.0.0.1:5000`

---

## ✅ Requirements

- Python 3.7+
- Flask
- Scikit-learn
- Pandas
- Flask-CORS

---

## 📊 Dataset

This project uses a TED Talk dataset with fields like:
- `title`
- `tags`
- `description`
- `views`
- `speaker`
- `published_date`

Make sure to include a valid `ted_data.csv` with these fields.

---

## 👨‍💻 Author

Developed by PALLETI YONA  
Feel free to contribute or fork the project!
