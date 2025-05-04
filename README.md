# BookBridge
**BookBridge** is a Streamlit-powered book recommendation system built as a community project to help students in grades 1 through 8 discover books they’ll actually enjoy. It tackles a common problem: many kids stop reading because they don’t know what to read next—especially when books aren’t recommended to them in a personalized way.

This project makes finding the “next great book” easy, fast, and fun. 

---

## How It Works

BookBridge recommends the top 4 or 5 books (depending on preference-specific factors) from a curated list of ~100 titles using an intuitive questionnaire:

- **Grade Level**: Choose the reader’s current reading range (note that the system favors recommending books slightly above the reading level instead of slightly below, as challenging readers is valuable)
- **Sliders** for:
  - Plot- vs. Character-driven
  - Fast vs. Slow pace
  - Lighthearted vs. Serious tone
  - Picture-rich vs. Text-heavy
  - Fantasy vs. Realistic settings
- **Genre Selector**: Pick from popular genres like adventure, mystery, historical fiction, etc. Genre is NOT the primary factor in recommendations, but rather contributes to similarity in the same way any other variable does.

The system uses weighted similarity matching to score and return the most relevant books. Each recommendation includes:
- Book title and summary
- A similarity graph showing how well the book matches the reader’s input

---

## Why It Matters

Many kids abandon reading not because they dislike books—but because they don’t know where to look. BookBridge solves that with an inviting, intelligent system that recommends stories that truly fit the reader's style and interests.

It is designed/can be used for:
- **School Libraries**
- **Public Libraries**
- **After-school programs**
- **Parents or educators looking for smarter recommendations**
- **Any child, on their own, looking for the next great read**

This tool supports literacy development by making book choice more accessible, more engaging, and more aligned with individual taste.

---

## Try It Live

Try the project yourself **[here](https://bookbridge.streamlit.app)**.

**Important Note**: BookBridge offers a feature to minimize distractions for children who click buttons they see to wander off the page (including a button that links to this GitHub!) If this is a concern, add ?mode=kid to the URL (or click **[here](https://bookbridge.streamlit.app?mode=kid)**.)

---

## Built With

- Python, one of (if not the most) popular coding languages in the world
- Streamlit, a framework for data apps to be built
- Pandas, a Python package for data manipulation
- Numpy, another package for array manipulation
- Scikit-learn, a machine learning library with tools
- Custom weighted similarity engine in Python

---

## About the Author

This project was created by a middle school student as an initiative for their MYP Community Project, with the goal of making personalized reading accessible to all children. 
