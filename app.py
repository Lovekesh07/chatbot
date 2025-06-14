from flask import Flask, render_template, request
import nltk
from nltk.tokenize import word_tokenize

app = Flask(__name__)
nltk.download('punkt')

def generate_reply(message):
    message = message.lower()
    words = word_tokenize(message)

    if "order" in words or "track" in words:
        return "You can track your order here: https://www.amazon.in/gp/css/order-history/"
    elif "cancel" in words:
        return "To cancel an order, go to 'Your Orders' > select the item > click 'Cancel Order'."
    elif "return" in words:
        return "To return a product, visit: https://www.amazon.in/returns"
    elif "refund" in words:
        return "Refunds are processed within 3-5 business days after we receive the item."
    elif "support" in words or "help" in words:
        return "You can call Amazon support at 1800-3000-9009."
    elif "hi" in words or "hello" in words:
        return "Hello! What can I do for you today?"
    else:
        return "Sorry, I didn't understand. Try asking about orders, returns, or support."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET"])
def get_bot_response():
    user_input = request.args.get("msg")
    return generate_reply(user_input)

if __name__ == "__main__":
    app.run(debug=True)
