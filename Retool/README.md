
# Product Review Sentiment Analysis Dashboard

## Overview
This dashboard provides an at-a-glance view of product reviews, sentiment analysis, and key metrics to help teams monitor and analyze customer feedback over time.

## Features

- **Filters**:  
  - Filter reviews by date range, product, sentiment, and rating.

- **Key Metrics**:  
  - **Total Reviews:** The total number of reviews analyzed.
  - **Average Rating:** Displays the average rating across all reviews (on a 1–5 scale).
  - **Positive Reviews:** Percentage of reviews classified as positive.
  - **Negative Reviews:** Percentage of reviews classified as negative.

- **Reviews with Sentiment Analysis Table**:  
  Displays a data table with the following columns:
  - Review ID
  - Product
  - Review Text
  - Rating
  - Date
  - Sentiment (Positive/Neutral/Negative)
  - Confidence Score (in %)

- **Actions**:  
  - Refresh sentiment analysis.
  - Download filtered review data.

- **Analytics Visualizations**:
  - **Sentiment Distribution**: Bar/graph breakdown of positive, neutral, and negative sentiment over time.
  - **Average Rating Over Time**: Tracks average review rating across dates.

## Example Data Schema
| Review ID | Product                | Review Text                                                        | Rating | Date       | Sentiment | Confidence |
|-----------|------------------------|--------------------------------------------------------------------|--------|------------|-----------|------------|
| 1         | Wireless Headphones Pro| Amazing sound quality! The noise cancellation is incredible...     | 5      | 2024-01-15 | Positive  | 95%        |

## Usage Instructions

1. **Apply Filters:**  
   Select date range, product, sentiment, and rating filters as needed.

2. **Review Key Metrics & Analytics:**  
   Review the high-level summary and trend graphs for actionable insights.

3. **Analyze Individual Reviews:**  
   Use the table to drill down into each review, see the assigned sentiment, and the model's confidence.

4. **Download Reports:**  
   After applying filters, download the review data for offline analysis or reporting.

5. **Refresh Analysis:**  
   Use the 'Refresh' button to re-run sentiment analysis on the latest dataset.
