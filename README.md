# Fake News Detection API

This is a fake news detection API built using Python and various machine learning libraries. It uses natural language processing techniques to analyze news articles and predict the likelihood that they are fake news.

## Installation

To install the fake news detection API, follow these steps:

1. Clone the repository by running `git clone https://github.com/your-username/fake-news-detection.git` in your terminal.
2. Install the required dependencies by running `pip install -r requirements.txt` in the cloned repository.
3. Run the API by running `python fake_news_detection.py` in the cloned repository.

## Usage

To use the fake news detection API, send a GET request to `http://localhost:5000/fake_news_detection` with a JSON payload containing the text of the news article you want to analyze. The API will return a JSON response with the likelihood that the news article is fake news.

### Example Request
curl -X GET
http://localhost:5000/fake_news_detection
-H 'Content-Type: application/json'
-d '{"text": "This is a sample news article"}'
### Example Response
{ "likelihood_of_fake_news": 0.2 }

