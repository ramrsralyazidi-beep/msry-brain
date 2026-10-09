from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return """
    <html dir='rtl' style='background:#0A1931;color:white;text-align:center;padding:50px;font-family:tahoma'>
    <h1>👑 MSRY YEMEN AI - 100% الدماغ</h1>
    <h2 style='color:lime'>● الروبوت شغال 100</h2>
    <p>المتجر: msryamene.infy.click</p>
    <p>واتساب: 776894022</p>
    <p><a style='background:#D4AF37;color:#000;padding:15px 30px;text-decoration:none;border-radius:10px;font-weight:bold' href='https://wa.me/967776894022'>تواصل واتساب</a></p>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({"status":"100%","facebook":"جاهز","insta":"جاهز","whatsapp":"776894022"})

@app.route("/chat")
def chat():
    msg = request.args.get('msg','').lower()
    if 'شعار' in msg or 'logo' in msg:
        r = "أبشر بالشعار الفخم 👑\n🔹 برونز 1500 ريال\n🔸 فضي 3000\n👑 ذهبي 5000\nارسل اسم مشروعك + واتسابك؟\nhttps://wa.me/967776894022"
    elif 'سلام' in msg or 'مرحبا' in msg or 'هلا' in msg:
        r = "أهلا وسهلا في MSRY YEMEN 👑\nأنا العقل الذكي حق المتجر\nأصمم لك شعارات وهويات ومتاجر تبيع لحالها\nايش تبغى اليوم؟"
    else:
        r = f"تم 👑 وصلتني: {msg}\nتواصل مباشر واتساب: https://wa.me/967776894022 - 776894022"
    return jsonify({"reply": r})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
