import json
import requests
from models import FakeNewsModel
from natural_language_processing import tokenizer, stop_words, stemmer

app = Flask(__name__)

@app.route('/fake_news_detection', methods=['GET'])
def fake_news_detection():
    # Get the JSON payload from the request
    payload = request.get_json()

    # Tokenize the news article
    tokens = tokenizer(payload['text'])

    # Remove stop words
    tokens = [token for token in tokens if token not in stop_words]

    # Stem the remaining words
    tokens = [stemmer(token) for token in tokens]

    # Create a input vector for the model
    input_vector = [token for token in tokens]

    # Load the trained model
    model = FakeNewsModel()

    # Make a prediction using the input vector
    prediction = model.predict(input_vector)

    # Return the prediction as a JSON response
    return json.dumps({'fake_news_likelihood': prediction}), 200

if __name__ == '__main__':
    app.run(debug=True)
