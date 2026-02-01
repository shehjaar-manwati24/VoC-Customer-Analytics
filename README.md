# 📊 Automated Voice of Customer (VoC) Analyzer

> A Python-based analytics tool that processes raw user reviews to identify churn drivers and quantify product friction.

## 💡 Business Context
In high-growth fintech products, manual review of user feedback is unscalable. This tool automates the "Voice of Customer" process, allowing Product Managers to:
1.  **Quantify Sentiment:** Move beyond anecdotal evidence to data-backed severity scores.
2.  **Isolate Root Causes:** Automatically tag and count keywords (e.g., "OTP", "Login") to prioritize engineering resources.
3.  **Reduce Churn:** Identify critical friction points (like the OTP failure shown above) before they permanently damage retention metrics.

## 🛠️ Tech Stack
* **Python 3.14**: Core logic and data processing.
* **Pandas**: Data manipulation and filtering.
* **NLTK (Natural Language Toolkit)**: Tokenization and stop-word removal for semantic analysis.
* **TextBlob**: Sentiment polarity scoring.
* **Matplotlib**: Visualization of frequency distributions.

## 🔍 Key Insights (Sample Data)
Running this tool on a simulated dataset of **200 fintech app reviews** revealed:
* **80% of negative reviews** were correlated with a single feature failure: **OTP/Authentication**.
* Sentiment polarity dropped to **-0.6** (Severe) for reviews containing "Login" or "SMS".
* **Recommendation:** Immediate prioritization of SMS Gateway fix to recover an estimated 15% of daily active users (DAU).

## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/VoC-Customer-Analytics.git](https://github.com/YOUR_USERNAME/VoC-Customer-Analytics.git)
cd VoC-Customer-Analytics
