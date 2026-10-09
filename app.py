from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "<h1>MSRY YEMEN AI - 100% WORKING</h1><p>Chatbot LIVE for msryamene.infy.click</p>"

@app.route("/health")
def health():
    return jsonify({"status": "100%", "store": "msryamene.infy.click", "phone": "MSRY Yemen"})

@app.route("/chat")
def chat():
    msg = request.args.get('msg', '')
    if not msg:
        reply = "أهلا بك في متجر مسرى اليمن! كيف أقدر أساعدك اليوم؟"
    else:
        reply = f"أهلا بك! استفسارك: {msg} - راسلنا واتساب لإكمال طلبك من مسرى اليمن"
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
