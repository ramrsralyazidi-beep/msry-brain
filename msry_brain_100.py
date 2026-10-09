from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html dir='rtl' style='background:#0A1931;color:#D4AF37;text-align:center;padding:30px'>
    <h1>👑 MSRY YEMEN AI - BRAIN 100%</h1>
    <h2 style='color:lime'>● الروبوت شغال 100%</h2>
    <p>متجرك: msryamene.infy.click</p>
    <p>واتساب: 776894022</p>
    <p><a style='background:#D4AF37;color:#0A1931;padding:10px 20px;border-radius:20px;text-decoration:none' href='/brain'>دخول العقل</a></p>
    </html>
    """

@app.route("/brain")
def brain():
    return {"brain":"100%","facebook":"جاهز","insta":"جاهز","whatsapp":"776894022","tiktok":"جاهز"}

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
