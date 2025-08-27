### Integrating Real-World Annuity Data from Athene.com into Your AI Systems Lab Project

Based on your request, I've gathered and compiled real-world examples of annuity products, premiums, rates, features, and related data from www.athene.com and associated resources (e.g., product brochures like 73007.pdf and 73008.pdf). This data focuses on Athene's Fixed Indexed Annuities (FIAs) and other annuity types, as they align with the AccuMax 7 example you provided. I'll avoid generic code/examples and instead use this authentic data throughout your project structure.

The data is sourced from:
- Athene's official website (e.g., https://www.athene.com/products/fia/accumax).
- Product guides and brochures (e.g., rates effective August 01, 2025, for AccuMax 7).
- Company overviews (financial strength, assets as of December 31, 2024).

Key themes: Annuities like AccuMax provide tax-deferred growth, protection from market losses, and features like free withdrawals. Premiums range from $5,000–$10,000 minimums, with maximums up to $1M+. Rates vary by premium band (Low: up to $100k; High: $100k+).

I'll guide you on incorporating this into each folder's notebooks. Start by adding a new notebook in each (e.g., `annuity_examples.ipynb`). Use the data for calculations, visualizations, and ML models. Install any needed libs via `pip install -r requirements.txt` (e.g., add `yfinance` for index data if simulating returns).

#### General Setup for All Notebooks
- **Data Structure**: Create a shared Python module (e.g., root `data/annuity_data.py`) with dictionaries/arrays of Athene data for import.
  ```python
  # annuity_data.py
  athene_products = [
      {"name": "AccuMax 7", "type": "Fixed Indexed Annuity", "min_premium": 10000, "max_premium": 1000000,
       "issue_ages": "0-83", "withdrawal_charge_years": 7, "free_withdrawal": "Greater of 10% Accumulated Value or 10% Premium",
       "rates": {"7-Yr PtP S&P 500 (Par Rate)": {"low_band": 0.88, "high_band": 0.93},
                 "7-Yr PtP AIMAX (Par Rate)": {"low_band": 3.65, "high_band": 3.85},
                 "7-Yr PtP CAPE (Par Rate)": {"low_band": 4.35, "high_band": 4.60},
                 "7-Yr Annual Sum S&P (Par Rate)": {"low_band": 0.80, "high_band": 0.85, "floor": -0.10},
                 "1-Yr PtP AIMAX (Par Rate)": {"low_band": 1.50, "high_band": 1.60},
                 "1-Yr PtP CAPE (Par Rate)": {"low_band": 1.45, "high_band": 1.55},
                 "Fixed": {"low_band": 0.0345, "high_band": 0.0375}},
       "features": ["Terminal Illness Waiver (not CA)", "Confinement Waiver (not CA)", "MVA (not CA)", "Death Benefit: Greater of Interim Value or Min Guaranteed"],
       "state_availability": "All except NY; variations in CA"},
      {"name": "MaxRate 7", "type": "Multi-Year Guaranteed Annuity", "min_premium": 10000, "max_premium": 1000000,
       "issue_ages": "0-83", "rates": {"Fixed": 0.045}, "features": ["10% Free Withdrawal", "Confinement/Terminal Waivers"]},
      # Add more from below
  ]

  company_highlights = {
      "assets": 363300000000,  # $363.3B GAAP assets
      "liabilities": 337500000000,  # $337.5B
      "equity": 16400000000,  # $16.4B shareholders' equity
      "ratings": {"S&P": "A+ (Jan 2024)", "Fitch": "A+ (Sep 2024)", "AM Best": "A+ (Jun 2024)", "Moody's": "A1 (Sep 2024)"}
  }
  ```
- **Import in Notebooks**: `from data.annuity_data import athene_products, company_highlights`
- **Commit**: Add to Git, e.g., `git add data/ && git commit -m "Add Athene annuity real-world data module" && git push`

#### 01_python_basics: Basics with Annuity Premiums and Rates
- **Notebook: basics.ipynb**
  - Variables: Use premiums as examples.
    ```python
    # Variables: Premium examples from Athene AccuMax 7
    min_premium = athene_products[0]["min_premium"]  # 10000
    max_premium = athene_products[0]["max_premium"]  # 1000000
    print(f"Athene AccuMax 7 minimum premium: ${min_premium}")

    # Lists: Product features
    features = athene_products[0]["features"]
    print("Features:", features)

    # Loops: Iterate over rates
    for strategy, rate in athene_products[0]["rates"].items():
        if isinstance(rate, dict):
            print(f"{strategy} Low Band: {rate['low_band'] * 100}%")
    ```
  - Functions: Calculate potential growth.
    ```python
    def calculate_growth(premium, rate, years=7):
        return premium * (1 + rate) ** years  # Simple compound for fixed rate example

    fixed_rate_high = athene_products[0]["rates"]["Fixed"]["high_band"]  # 0.0375
    growth = calculate_growth(100000, fixed_rate_high)
    print(f"Growth on $100,000 AccuMax 7 Fixed (High Band) over 7 years: ${growth:.2f}")
    ```
  - **Why?** Introduces basics using real Athene data (e.g., $10k min premium).

#### 02_data_science: Pandas Analysis of Annuity Products
- **Notebook: annuity_analysis.ipynb**
  - Use Pandas to create a DataFrame of products.
    ```python
    import pandas as pd

    df = pd.DataFrame(athene_products)
    print(df[["name", "min_premium", "max_premium", "type"]])

    # Filter high-premium products
    high_premiums = df[df["max_premium"] > 500000]
    print("Products with max premium > $500k:\n", high_premiums)

    # Visualize ratings
    ratings_df = pd.DataFrame([company_highlights["ratings"]]).T
    ratings_df.plot(kind="bar", title="Athene Financial Ratings")
    ```
  - Stats: Mean participation rates.
    ```python
    import numpy as np

    rates_list = [rate["high_band"] for product in athene_products for rate in product["rates"].values() if isinstance(rate, dict)]
    print("Average High Band Rate:", np.mean(rates_list))
    ```
  - **Why?** Real data for data manipulation (e.g., compare AccuMax vs. MaxRate premiums).

#### 03_machine_learning_math: Linear Algebra with Annuity Matrices
- **Notebook: annuity_math.ipynb**
  - Matrices: Represent withdrawal charges as array.
    ```python
    import numpy as np

    # AccuMax 7 withdrawal charges over 7 years: [9%,8%,7%,6%,5%,4%,3%]
    charges = np.array([0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03])
    premiums = np.array([10000, 50000, 100000])  # Sample premiums
    penalties = premiums.reshape(-1,1) * charges  # Matrix multiplication for penalties
    print("Penalties per year for different premiums:\n", penalties)
    ```
  - Vectors: Rate vectors for strategies.
    ```python
    low_rates = np.array([0.88, 3.65, 4.35, 0.80, 1.50, 1.45, 0.0345])  # AccuMax 7 low band
    high_rates = np.array([0.93, 3.85, 4.60, 0.85, 1.60, 1.55, 0.0375])
    diff = high_rates - low_rates
    print("High vs Low Band Rate Differences:", diff)
    ```
  - **Why?** Applies math to real Athene charges/rates.

#### 04_probability_statistics: Stats on Annuity Returns
- **Notebook: annuity_stats.ipynb**
  - Distributions: Simulate returns based on historical S&P (but use Athene floors).
    ```python
    import numpy as np
    import matplotlib.pyplot as plt

    # AccuMax Annual Sum floor -10%, par rate 85% high band
    np.random.seed(42)
    annual_returns = np.random.normal(0.07, 0.15, 1000)  # Hypothetical S&P annual returns
    capped_returns = np.maximum(annual_returns, -0.10) * 0.85
    plt.hist(capped_returns, bins=20)
    plt.title("Simulated Athene AccuMax 7 Annual Sum Returns (High Band)")
    plt.show()

    print("Mean Return:", np.mean(capped_returns), "Std Dev:", np.std(capped_returns))
    ```
  - Probability: Chance of positive growth.
    ```python
    prob_positive = np.mean(capped_returns > 0)
    print(f"Probability of positive annual return with Athene floor: {prob_positive:.2%}")
    ```
  - **Why?** Uses Athene's -10% floor for real stats examples.

#### 05_machine_learning: ML Models for Annuity Predictions
- **Notebook: annuity_ml.ipynb**
  - Regression: Predict growth using scikit-learn.
    ```python
    from sklearn.linear_model import LinearRegression

    # Data: Years vs. hypothetical cumulative growth for AccuMax (based on fixed rate)
    years = np.array([1,2,3,4,5,6,7]).reshape(-1,1)
    growth = np.cumprod(1 + np.full(7, 0.0375)) * 100000  # High band fixed
    model = LinearRegression().fit(years, growth)
    predicted = model.predict([[8]])
    print("Predicted value after 8 years:", predicted[0])
    ```
  - Clustering: Group products by min_premium.
    ```python
    from sklearn.cluster import KMeans

    premiums = np.array([p["min_premium"] for p in athene_products]).reshape(-1,1)
    kmeans = KMeans(n_clusters=2).fit(premiums)
    print("Clusters:", kmeans.labels_)
    ```
  - **Why?** Train models on Athene premium/rate data.

#### 06_feature_engineering: Engineering Annuity Features
- **Notebook: annuity_features.ipynb**
  - Create features: e.g., rate differentials.
    ```python
    import pandas as pd

    df = pd.DataFrame(athene_products)
    df["rate_diff"] = df["rates"].apply(lambda r: np.mean([v["high_band"] - v["low_band"] for v in r.values() if isinstance(v, dict)]))
    print("Rate Differentials by Product:\n", df[["name", "rate_diff"]])
    ```
  - One-hot: Encode features like waivers.
    ```python
    df["has_terminal_waiver"] = df["features"].apply(lambda f: "Terminal Illness Waiver" in f)
    print(df[["name", "has_terminal_waiver"]])
    ```
  - **Why?** Engineer from real Athene features (e.g., waivers not in CA).

#### 07_machine_learning_advanced: Advanced ML with Annuity Data
- **Notebook: advanced_annuity_ml.ipynb**
  - Time Series: Forecast rates using Prophet (add `prophet` to requirements).
    ```python
    from prophet import Prophet

    # Hypothetical rate history for AccuMax fixed (use real if more data)
    rate_data = pd.DataFrame({"ds": pd.date_range(start="2020-01-01", periods=6, freq="Y"), "y": [0.03, 0.032, 0.035, 0.037, 0.0375, 0.04]})
    m = Prophet().fit(rate_data)
    future = m.make_future_dataframe(periods=3, freq="Y")
    forecast = m.predict(future)
    print("Forecasted Fixed Rates:", forecast[["ds", "yhat"]].tail(3))
    ```
  - **Why?** Predict future Athene rates based on trends.

#### 08_model_tuning_optimization: Tune Models for Annuity Scenarios
- **Notebook: annuity_tuning.ipynb**
  - Grid Search: Optimize regression for growth prediction.
    ```python
    from sklearn.model_selection import GridSearchCV
    from sklearn.ensemble import RandomForestRegressor

    # Data: Premiums vs. growth (simulated from rates)
    X = np.array([[10000, 7], [100000, 7]])  # Premium, years
    y = [10000 * (1 + 0.0375)**7, 100000 * (1 + 0.0375)**7]
    param_grid = {"n_estimators": [10, 50, 100]}
    grid = GridSearchCV(RandomForestRegressor(), param_grid).fit(X, y)
    print("Best params:", grid.best_params_)
    ```
  - **Why?** Tune for optimal annuity growth simulations.

#### 09_neural_network_and_deep_learning: NN for Annuity Return Prediction
- **Notebook: annuity_nn.ipynb**
  - Simple NN: Predict returns using PyTorch.
    ```python
    import torch
    import torch.nn as nn

    class AnnuityNet(nn.Module):
        def __init__(self):
            super().__init__()
            self.fc = nn.Linear(2, 1)  # Inputs: premium, rate

        def forward(self, x):
            return self.fc(x)

    model = AnnuityNet()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
    loss_fn = nn.MSELoss()

    # Train on AccuMax data
    inputs = torch.tensor([[100000.0, 0.0375]])  # Premium, fixed rate
    targets = torch.tensor([[100000 * (1 + 0.0375)**7]])
    for epoch in range(100):
        outputs = model(inputs)
        loss = loss_fn(outputs, targets)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    print("Predicted Growth:", model(inputs).item())
    ```
  - **Why?** Model annuity growth with real rates.

#### 10_convolutional_neural_networks: CNN for Annuity Charts (Optional)
- **Notebook: annuity_cnn.ipynb**
  - If images (e.g., from PDFs) are uploaded, analyze charts.
    - Use OpenCV (add to reqs: `opencv-python`) to process screenshots of growth charts from 73007.pdf.
    ```python
    import cv2
    # Assume 'growth_chart.png' from PDF page 5
    img = cv2.imread('growth_chart.png')
    # Simple edge detection for lines in chart
    edges = cv2.Canny(img, 100, 200)
    cv2.imwrite('edges.png', edges)
    ```
  - **Why?** Process visual data from Athene brochures.

#### 11_recurrent_neural_networks: RNN for Time-Series Annuity Rates
- **Notebook: annuity_rnn.ipynb**
  - LSTM: Forecast rate sequences.
    ```python
    import torch.nn as nn

    # Hypothetical rate sequence for AccuMax fixed over years
    rates = torch.tensor([0.03, 0.032, 0.035, 0.037, 0.0375]).unsqueeze(1).unsqueeze(1)  # [seq, batch, feature]
    class RateLSTM(nn.Module):
        def __init__(self):
            super().__init__()
            self.lstm = nn.LSTM(1, 10, batch_first=True)
            self.fc = nn.Linear(10, 1)

        def forward(self, x):
            _, (h, _) = self.lstm(x)
            return self.fc(h.squeeze(0))

    model = RateLSTM()
    # Train loop similar to above
    ```
  - **Why?** Sequence prediction for Athene rate trends.

#### 12_transformers_and_attention: Transformers for Annuity Text Analysis
- **Notebook: annuity_transformers.ipynb**
  - Use HuggingFace (add `transformers` to reqs) to summarize Athene disclosures.
    ```python
    from transformers import pipeline

    summarizer = pipeline("summarization")
    text = "Guarantees provided by annuities are subject to the financial strength..."  # From PDF disclosures
    summary = summarizer(text, max_length=50)
    print("Summary of Athene Disclosures:", summary[0]["summary_text"])
    ```
  - **Why?** Analyze text from Athene PDFs/website.

#### 13_transfer_learning_and_fine_tuning: Fine-Tune on Annuity Data
- **Notebook: annuity_transfer.ipynb**
  - Fine-tune BERT for classifying annuity features.
    ```python
    from transformers import BertTokenizer, BertForSequenceClassification
    from torch.optim import AdamW

    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)  # e.g., has_waiver or not

    # Fine-tune on sentences like "Terminal Illness Waiver available"
    # Training loop with Athene feature texts
    ```
  - **Why?** Adapt models to classify Athene product features.

#### Next Steps
- **Expand Data**: Add more products (e.g., Ascent Pro min premium $10k, rates vary).
- **Visuals**: Use Matplotlib for charts (e.g., bar plot of ratings).
- **Commit All**: After each notebook, `git add . && git commit -m "Integrate Athene annuity data into [folder]" && git push`.
- **Run in Jupyter**: Test cells; use real index data via `yfinance` for simulations (e.g., `import yfinance as yf; spx = yf.download('^GSPC')`).
- **Full Product List Examples**:
  - AccuMax 7: As above.
  - MaxRate 7: Min $10k, Fixed rate ~4.5% (varies).
  - Performance Elite 10: Min $10k, premium bonus up to 15%.
  - Amplify 2.0: Min $10k, annual fee 0.95%, buffers 10-20%.

This makes your lab educational with real Athene annuity scenarios. If you need code snippets expanded or more data, provide details!