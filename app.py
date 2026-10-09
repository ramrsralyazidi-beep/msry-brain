from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route("/")
def home():
    return "<h1>MSRY YEMEN AI - 100% WORKING</h1><h2 style='color:green'>Robot Online</h2><p>msryamene.infy.click - 776894022</p><a href='https://wa.me/967776894022' style='background:gold;padding:15px'>WhatsApp</a>"
@app.route("/health")
def health():
    return jsonify({"status":"100%","phone":"776894022"})
@app.route("/chat")
def chat():
    msg = request.args.get('msg','')
    return jsonify({"reply": f"اهلا بك في MSRY 👑 وصلتني رسالتك: {msg} - تواصل واتساب 776894022 https://wa.me/967776894022"})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
