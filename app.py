from flask import Flask, render_template, request, redirect, url_for
from db import Database

app = Flask(__name__)
db = Database()

db.init_db()

users = db.get_users()
if len(users) == 0:
    db.create_user("Polat", "polat@example.com")

@app.route("/")
def home():
    current_user = db.get_users()[0]
    subs = db.get_subscriptions()
    total_subs = len(subs)
    total_cost = sum(sub['price'] for sub in subs)
    return render_template("dashboard.html", user=current_user, subs=subs, total_subs=total_subs, total_cost=total_cost)

@app.route("/add", methods=["GET", "POST"])
def add_subscription():
    if request.method == "POST":
        name = request.form.get("name")
        plan_type = request.form.get("plan_type")
        price = float(request.form.get("price"))
        start_date = request.form.get("start_date")
        
        user_id = db.get_users()[0]['id']
        db.create_subscription(user_id, name, plan_type, price, start_date)
        return redirect(url_for("home"))
        
    return render_template("add_subscription.html")

# --- YENİ EKLENEN DÜZENLEME (UPDATE) ROTASI ---
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_subscription(id):
    if request.method == "POST":
        # Form güncellenip Kaydet'e basıldığında burası çalışır
        name = request.form.get("name")
        plan_type = request.form.get("plan_type")
        price = float(request.form.get("price"))
        start_date = request.form.get("start_date")
        
        # Veritabanını güncelliyoruz
        db.update_subscription(id, name, plan_type, price, start_date)
        return redirect(url_for("home"))
    
    # Kullanıcı sadece Düzenle butonuna bastığında sayfayı eski verilerle gösterir
    sub = db.get_subscription(id)
    return render_template("edit_subscription.html", sub=sub)

@app.route("/delete/<int:id>")
def delete_subscription(id):
    db.delete_subscription(id)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True, port=5000)