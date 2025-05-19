
# 🗳️ YouTube Election Sentiment Analysis

This project analyzes public sentiment in YouTube comments on political podcast episodes featuring **Donald Trump** and **Kamala Harris** during their U.S. election campaigns.

It scrapes real-time YouTube comments, processes them using the VADER sentiment analysis model, and exports the data for visualization or further research.

---

## 🎯 Objective

- Scrape comments from YouTube videos featuring U.S. presidential candidates.
- Perform sentiment analysis using VADER (lexicon-based model).
- Identify trends in public opinion based on podcast appearances.

---

## 🧠 Why This Matters

Understanding how people react to political figures on social media platforms like YouTube offers a unique lens into public opinion and election sentiment. This project helps visualize and quantify those reactions in a structured and meaningful way.

---

## 🗂️ Project Structure

```
yt-election-sentiment/
│
├── data/                         # Raw and processed CSVs
│   └── youtube_comments.csv
│
├── scripts/
│   ├── data_scraper.py          # Scrapes YouTube comments via YouTube Data API
│   └── sentiment_analysis.py    # Analyzes comment sentiment using VADER
│
├── requirements.txt             # Python dependencies
├── .gitignore                   # Files to exclude from Git
└── README.md                    # Project overview (this file)
```

---

## 🚀 How to Run This Project

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/yt-election-sentiment.git
cd yt-election-sentiment
```

### 2. Install Dependencies

(Optional but recommended: create a virtual environment)

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

Install the Python libraries:

```bash
pip install -r requirements.txt
```

### 3. Run the Scripts

- To scrape YouTube comments:
  ```bash
  python scripts/data_scraper.py
  ```

- To perform sentiment analysis:
  ```bash
  python scripts/sentiment_analysis.py
  ```

---

## 🧪 Output

The final file `data/youtube_comments_with_sentiment.csv` includes:

- Original comment
- Candidate and podcast details
- Sentiment scores (compound value)
- Sentiment category: `positive`, `negative`, `neutral`
- Random jitter value for visual separation in charts

---


## 🛠️ Tools Used

- Python
- YouTube Data API (via `google-api-python-client`)
- VADER Sentiment Analysis (`nltk`)
- Pandas, NumPy, tqdm

---

## 📎 License

This project is open for educational and research purposes. Feel free to fork and build upon it.

---

## 🙋 Author

**[Your Name]**  
[GitHub Profile](https://github.com/mtayyabqureshi)  
Reach out if you're curious about YouTube sentiment, data scraping, or political data projects!
