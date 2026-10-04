from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3
import pytesseract
from PIL import Image
import os
import uuid
from flask import send_from_directory
from flask import send_from_directory
import os
from PIL import Image
import cv2
import re
from google import genai
from flask import jsonify
import pandas as pd
import numpy as np

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


app = Flask(__name__)
app.secret_key = "supersecretkey" # required for sessions 
client = genai.Client(api_key="AIzaSyDzwvmulVfRFd7L1pf1I8vkctFDZrX9vHg")
CATEGORY_KEYWORDS = {
    "Food": [
        "milk", "banana", "rice", "vegetable", "tomato", "potato",
        "bread", "apple", "onion", "peas", "broccoli", "fruit","milk","banana","rice","vegetable","tomato","potato","bread","apple","onion","peas","broccoli","fruit",
        "carrot","cabbage","cauliflower","spinach","beans","capsicum","pumpkin","beetroot","sweetcorn","mushroom",
        "garlic","ginger","lemon","lime","orange","grapes","mango","pineapple","watermelon","papaya","pomegranate",
        "strawberry","blueberry","pear","peach","plum","kiwi","avocado","corn","oats","cornflakes","noodles","pasta",
        "macaroni","egg","chicken","mutton","fish","prawns","crab","paneer","cheese","butter","curd","yogurt",
        "icecream","cake","pastry","biscuit","cookie","chocolate","jam","honey","peanutbutter","ketchup","mayonnaise",
        "soysauce","vinegar","salt","sugar","brownsugar","jaggery","ghee","oil","oliveoil","sunfloweroil","coconutoil",
        "turmeric","chilipowder","pepper","cumin","coriander","garammasala","cardamom","cinnamon","cloves","bayleaf",
        "tea","coffee","greentea","juice","smoothie","burger","pizza","sandwich","shawarma","roll","wrap","hotdog",
        "fries","nuggets","taco","burrito","quesadilla","nachos","pancake","waffle","donut","croissant","bagel",
        "muffin","cupcake","brownie","pudding","custard","kheer","halwa","laddu","jalebi","gulabjamun","rasgulla",
        "rasmalai","barfi","mysorepak","payasam","upma","poha","idli","dosa","vada","sambar","chutney","pongal",
        "paratha","roti","chapati","naan","kulcha","biryani","friedrice","pulao","khichdi","dal","rajma","chole",
        "paneerbuttermasala","palakpaneer","aloo","bhindi","baingan","samosa","pakora","cutlet","kachori","sev",
        "mixture","namkeen","chips","popcorn","trailmix","granola","energybar","proteinbar","almond","cashew",
        "pistachio","walnut","hazelnut","peanut","dates","fig","raisin","apricot","prune","cherry","dragonfruit",
        "passionfruit","lychee","guava","jackfruit","starfruit","tamarind","sapota","custardapple","berries",
        "blackberry","cranberry","mulberry","gooseberry","radish","turnip","zucchini","lettuce","celery","leek",
        "springonion","shallot","artichoke","asparagus","kale","bokchoy","edamame","lentils","chickpeas","soybean",
        "tofu","tempeh","seitan","quinoa","barley","millet","sorghum","buckwheat","semolina","flour","maida",
        "wholewheat","riceflour","cornflour","arrowroot","breadcrumbs","yeast","bakingpowder","bakingsoda",
        "condensedmilk","evaporatedmilk","cream","whippedcream","custardpowder","chocolatesyrup","maplesyrup",
        "caramelsauce","strawberrysyrup","vanilla","cocoa","darkchocolate","whitechocolate","milkchocolate",
        "marshmallow","gelatin","jelly","toffee","lollipop","candies","mint","peppermint","spearmint","herbs",
        "basil","oregano","thyme","rosemary","parsley","dill","sage","chives","tarragon","fennel","mustard",
        "sesame","poppyseed","sunflowerseed","chia","flaxseed","pumpkinseed","lotusseed","makhana","coconut",
        "desiccatedcoconut","coconutmilk","coconutwater","soup","tomatosoup","chickensoup","mushroomsoup",
        "vegetablesoup","noodlesoup","ramen","udon","pho","laksa","curry","gravy","stew","broth","bbq","grill",
        "roast","bake","steam","boil","fry","deepfry","stirfry","saute","pickle","achar","relish","salsa",
        "guacamole","hummus","tahini","falafel","pita","couscous","risotto","lasagna","spaghetti","fettuccine",
        "penne","ravioli","tortellini","gnocchi","meatball","steak","bacon","sausage","ham","salami","pepperoni",
        "salad","coleslaw","potatosalad","pastasalad","fruitsalad","greensalad","dressings","vinaigrette",
        "caesardressing","ranchdressing","thousandisland","lemonade","milkshake","lassi","buttermilk","soda",
        "cola","energydrink","sportsdrink","mineralwater","sparklingwater","icedtea","coldcoffee","mocktail",
        "cocktail","beer","wine","whiskey","vodka","rum","brandy","gin","tequila"
    ],
    "Travel": [
        "bus", "train", "uber", "ola", "taxi", "metro", "fuel", "petrol","travel","flight", "air ticket", "train ticket", "bus ticket", "taxi", "cab", "uber", "ola", "metro ticket", "travel pass",
       "hotel", "hostel", "resort", "guesthouse", "homestay", "lodge", "booking", "travel package", "tour package", "vacation",
"holiday trip", "road trip", "cruise", "travel insurance", "luggage", "suitcase", "travel bag", "backpack", "trolley bag",
"travel pillow", "passport cover", "visa fee", "airport transfer", "airport taxi", "airport lounge", "baggage fee",
"travel adapter", "travel charger", "travel sim", "roaming recharge", "map", "tour guide", "sightseeing", "city tour",
"museum ticket", "monument ticket", "park entry", "theme park ticket", "zoo ticket", "water park ticket",
"trekking", "camping", "hiking gear", "camp tent", "sleeping bag", "travel insurance premium", "car rental",
"bike rental", "fuel for trip", "toll fee", "parking fee", "ferry ticket", "boat ride", "cruise ticket",
"travel snacks", "travel food", "tourist pass", "metro recharge", "local transport", "tour guide fee",
"travel permit", "national park permit", "camera ticket", "photography permit", "travel accessories",
"neck pillow", "eye mask", "ear plugs", "travel bottle", "travel toiletries", "travel organizer",
"packing cubes", "travel wallet", "travel card", "foreign currency", "currency exchange", "international roaming",
"travel vaccination", "travel documents", "travel agency fee", "tour operator", "travel booking fee",
"holiday resort", "adventure tour", "island trip", "beach trip", "mountain trip", "desert safari"
    ],
    "Shopping": [
        "shirt", "pant", "shoe", "clothes", "bag","dress","jeans",'frock',"watch","shopping", "online shopping", "store purchase", "retail purchase", "clothing", "clothes", "tshirt", "shirt", "jeans", "jacket",
"sweater", "hoodie", "dress", "skirt", "shorts", "leggings", "tracksuit", "sportswear", "ethnic wear", "kurta",
"saree", "blouse", "lehenga", "salwar", "dupata", "fashion wear", "winter wear", "summer clothes", "innerwear",
"lingerie", "socks", "handbag", "purse", "wallet", "backpack", "laptop bag", "travel bag", "belt", "cap",
"hat", "scarf", "gloves", "sunglasses", "watch", "smart watch", "bracelet", "necklace", "earrings", "ring",
"fashion accessories", "cosmetics shopping", "beauty products", "skincare products", "makeup kit",
"foundation", "lipstick", "eyeliner", "mascara", "compact powder", "perfume", "deodorant", "body spray",
"hair dryer", "hair straightener", "hair curler", "trimmer", "electric shaver", "grooming products",
"footwear", "shoes", "sports shoes", "running shoes", "formal shoes", "casual shoes", "sandals",
"slippers", "heels", "boots", "sneakers", "flip flops", "shoe polish", "shoe cleaner",
"electronics shopping", "mobile phone", "smartphone", "laptop", "tablet", "headphones", "earbuds",
"bluetooth speaker", "smart tv", "camera", "gaming console", "keyboard", "mouse", "computer accessories",
"phone charger", "power bank", "usb cable", "memory card", "pen drive", "hard disk",
"home shopping", "home decor", "wall art", "curtains", "bedsheet", "pillow", "blanket",
"carpet", "lamp", "table lamp", "floor lamp", "sofa cover", "table cover",
"kitchen shopping", "cookware", "frying pan", "pressure cooker", "nonstick pan",
"kitchen utensils", "spoon set", "knife set", "cutting board", "dinner set",
"water bottle", "lunch box", "storage container", "food container",
"appliance shopping", "mixer grinder", "microwave oven", "toaster",
"electric kettle", "induction stove", "air fryer", "refrigerator", "washing machine",
"vacuum cleaner", "iron box", "water purifier",
"toy shopping", "kids toys", "board games", "action figures", "dolls",
"remote car", "puzzle game", "lego toys", "educational toys",
"pet shopping", "pet food", "dog food", "cat food", "pet toys", "pet accessories",
"gift shopping", "gift items", "gift box", "birthday gift", "anniversary gift",
"festival shopping", "diwali shopping", "christmas shopping", "new year shopping"
    ],
    "Utilities": [
        "electricity", "water", "recharge", "internet", "wifi", "mobile","electricity bill", "water bill", "gas bill", "internet bill", "wifi bill", "broadband bill", "mobile bill",
"phone bill", "postpaid recharge", "prepaid recharge", "electricity recharge", "gas cylinder",
"lpg refill", "lpg booking", "water supply", "drainage bill", "sewerage bill", "municipal bill",
"house tax", "property tax", "maintenance bill", "society maintenance", "garbage collection fee",
"cleaning service", "electric repair", "plumber service", "internet installation", "wifi router",
"modem", "set top box", "cable tv bill", "dth recharge", "dish tv recharge", "tv subscription",
"netflix subscription", "amazon prime subscription", "hotstar subscription", "ott subscription",
"cloud storage subscription", "software subscription", "vpn subscription", "domain renewal",
"hosting renewal", "electric appliances repair", "ac service", "washing machine repair",
"refrigerator repair", "generator fuel", "solar maintenance", "inverter battery", "battery replacement",
"water purifier service", "ro filter replacement", "ro service", "water tank cleaning",
"housekeeping service", "security service", "internet upgrade", "mobile data recharge",
"wifi extender", "lan cable", "power extension", "surge protector", "electric fuse",
"light bulb", "led bulb", "tube light", "switch board", "electric wiring", "electric maintenance",
"plumbing materials", "water motor repair", "pump repair", "gas stove repair", "gas pipe replacement",
"electric meter bill", "smart meter recharge", "utility payment", "utility recharge",
"service charges", "maintenance charges", "service subscription", "home utility bill"
    ],
    "Personal Care": [
        "soap", "shampoo", "toothpaste", "cream","shampoo", "conditioner", "hair oil", "hair serum", "hair mask", "hair gel", "hair spray", "hair cream",
"face wash", "face cleanser", "face scrub", "face mask", "face pack", "moisturizer", "face cream",
"night cream", "day cream", "sunscreen", "sunblock", "body lotion", "body cream", "body butter",
"body wash", "soap", "bath soap", "hand wash", "hand sanitizer", "deodorant", "perfume",
"body spray", "roll on deodorant", "toothpaste", "toothbrush", "electric toothbrush",
"mouthwash", "dental floss", "tongue cleaner", "lip balm", "lip care", "lip scrub",
"lip moisturizer", "lipstick", "lip gloss", "makeup remover", "foundation", "compact powder",
"concealer", "blush", "eyeliner", "mascara", "eyebrow pencil", "makeup kit",
"makeup brush", "beauty blender", "nail polish", "nail polish remover", "nail cutter",
"nail file", "shaving cream", "shaving foam", "razor", "electric trimmer", "beard oil",
"beard balm", "after shave", "face toner", "face mist", "skin serum", "vitamin c serum",
"anti aging cream", "under eye cream", "dark circle cream", "pimple cream",
"acne treatment", "skin lotion", "body scrub", "foot cream", "foot scrub",
"foot file", "foot spray", "feminine hygiene", "sanitary pads", "tampons",
"menstrual cup", "intimate wash", "baby powder", "baby lotion", "baby oil",
"baby wipes", "grooming kit", "personal hygiene kit", "beauty care products"
    ]
}
import joblib

ml_model = joblib.load("expense_category_model.pkl")
def predict_category_ml(item_name):
    return ml_model.predict([item_name])[0]

import numpy as np

def predict_category(item_name):
    item_name_lower = item_name.lower()

    # 1️⃣ Keyword first
    for category, keywords in CATEGORY_KEYWORDS.items():
        for word in keywords:
            if word in item_name_lower:
                return category

    # 2️⃣ ML prediction
    prediction = ml_model.predict([item_name])[0]
    probabilities = ml_model.predict_proba([item_name])
    confidence = np.max(probabilities)

    print("ML:", prediction, "Confidence:", confidence)

    # 3️⃣ Low confidence protection
    if confidence < 0.55:
        return "Other"

    return prediction


def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn
def get_user_expenses(username):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT date, category, amount FROM expenses WHERE user = ? ORDER BY date DESC",
        (username,)
    )

    expenses = cursor.fetchall()
    conn.close()

    return expenses
conn = get_db_connection()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS profile (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT UNIQUE,
    full_name TEXT,
    income REAL,
    monthly_budget REAL,
    savings_goal REAL,
    preferred_categories TEXT
)
""")

conn.commit()
conn.close()
import sqlite3
from datetime import datetime


# -----------------------------
# DATABASE SETUP (Run Once)
# -----------------------------
def setup_database():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT,
            daily_limit REAL DEFAULT 1000
        )
    """)

    conn.commit()
    conn.close()

@app.route("/ask_gemini", methods=["POST"])
def ask_gemini():
    user_message = request.json["message"]

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_message
        )

        return jsonify({"reply": response.text})

    except Exception as e:
        return jsonify({"reply": "Error: " + str(e)})



from flask import send_from_directory
import os
@app.route("/")
def landing():
    return render_template("landing.html")

@app.route("/bill/<path:filename>")
def bill_image(filename):
    # Remove 'uploads/' if it comes in URL
    if filename.startswith("uploads/"):
        filename = filename.replace("uploads/", "")

    file_path = os.path.join("uploads", filename)

    if not os.path.exists(file_path):
        return "File not found", 404

    return send_from_directory("uploads", filename)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor()
        user = cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        ).fetchone()
        conn.close()

        if user:
            session["user_id"] = user["id"]
            session["user"] = user["username"]
            return redirect("/dashboard")
        else:
            return "Invalid username or password"

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, password)
            )
            conn.commit()
            conn.close()
            return redirect("/")
        except sqlite3.IntegrityError:
            conn.close()
            return "Username already exists. Try another."

    return render_template("register.html")

from datetime import date
from collections import Counter

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM expenses WHERE user=? ORDER BY date DESC",
        (session["user"],)
    )
    expenses = cursor.fetchall()

    cursor.execute(
        "SELECT * FROM bills WHERE user=? ORDER BY bill_date DESC",
        (session["user"],)
    )
    bills = cursor.fetchall()

    # 🔥 NEW: Get Daily Limit
    cursor.execute(
        "SELECT daily_limit FROM users WHERE username=?",
        (session["user"],)
    )
    result = cursor.fetchone()
    daily_limit = result["daily_limit"] if result and result["daily_limit"] else 0

    conn.close()

    # ---- STATS ----
    total_spent = round(sum(exp["amount"] for exp in expenses),2)
    expense_count = len(expenses)

    current_month = date.today().strftime("%Y-%m")
    month_spent = round(sum(
        exp["amount"] for exp in expenses if exp["date"].startswith(current_month)
    ),2)

    avg_daily = round(total_spent / expense_count, 2) if expense_count else 0

    categories = [exp["category"] for exp in expenses]
    top_category = Counter(categories).most_common(1)[0][0] if categories else "—"

    # 🔥 NEW: DAILY ALERT LOGIC
    today_str = date.today().isoformat()
    today_spent = sum(
        exp["amount"] for exp in expenses if exp["date"] == today_str
    )

    alert_level = None
    percent=0

    if daily_limit and daily_limit > 0:
        percent = (today_spent / daily_limit) * 100

        if percent >= 100:
            alert_level = "100"
        elif percent >= 50:
            alert_level = "50"
        elif percent >= 25:
            alert_level = "25"

    return render_template(
        "dashboard.html",
        expenses=expenses,
        bills=bills,
        total_spent=total_spent,
        month_spent=month_spent,
        avg_daily=avg_daily,
        expense_count=expense_count,
        top_category=top_category,
        alert_level=alert_level,          # 🔥 pass to template
        today_spent=today_spent,
        daily_limit=daily_limit,
        percent=percent
    )



def extract_amount_from_bill(image_path):
    text = pytesseract.image_to_string(Image.open(image_path))

    # Find numbers like 123.45 or 123
    matches = re.findall(r"\d+\.\d{2}|\d+", text)

    amounts = [float(m) for m in matches if float(m) > 10]

    return max(amounts) if amounts else 0.0

def extract_text_from_image(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]

    text = pytesseract.image_to_string(gray)
    return text
def extract_items_from_text(text):
    items = []

    ignore_words = [
        "total", "subtotal", "gst", "tax", "change","current reading","previous reading",
        "cash", "balance", "loyalty"
    ]

    for line in text.split("\n"):
        line = line.strip()

        if len(line) < 5:
            continue

        if any(word in line.lower() for word in ignore_words):
            continue

        # Match item + $price or price
        match = re.search(
            r"([A-Z][A-Z\s]{2,})\s*\$?\s*(\d+[.,]\d{2}|\d+)",
            line.upper()
        )

        if match:
            item = match.group(1).strip()
            price = match.group(2).replace(",", ".")

            try:
                price = float(price)
                if price > 0.5:
                    items.append((item.title(), price))
            except:
                pass

    return items

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        new_limit = float(request.form['daily_limit'])

        cursor.execute(
            "UPDATE users SET daily_limit=? WHERE id=?",
            (new_limit, session['user_id'])
        )
        conn.commit()
        flash("Daily limit updated successfully!", "success")
        conn.close()
        return redirect(url_for('settings'))

    # GET request
    user = cursor.execute(
        "SELECT daily_limit FROM users WHERE id=?",
        (session['user_id'],)
    ).fetchone()

    conn.close()

    return render_template(
        'settings.html',
        daily_limit=user['daily_limit'] if user else 0
    )
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")
from datetime import date

@app.route("/add-expense", methods=["GET", "POST"])
def add_expense():
    if "user" not in session:
        return redirect("/")

    if request.method == "POST":
        item = request.form["item"]
        amount = request.form["amount"]

        # ML category prediction
        category = predict_category(item)

        from datetime import date
        today = date.today().isoformat()

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO expenses (user, item, amount, category, date) VALUES (?, ?, ?, ?, ?)",
            (session["user"], item, amount, category, today)
        )
        conn.commit()
        conn.close()

        return redirect("/expenses")   # 👈 multipage redirect

    # GET request → show page
    return render_template("add_expense.html")


@app.route("/delete-expense/<int:id>", methods=["DELETE"])
def delete_expense(id):

    if "user" not in session:
        return jsonify({"success": False})

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM expenses WHERE id=? AND user=?",
        (id, session["user"])
    )

    conn.commit()
    conn.close()

    return jsonify({"success": True})
from collections import defaultdict
from flask import jsonify
from datetime import datetime, timedelta
import sqlite3
@app.route("/expense_summary")
def expense_summary():

    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id,item, date, category, amount FROM expenses WHERE user=?",
        (session["user"],)
    )
    rows = cursor.fetchall()

    monthly = {}
    daily = {}
    category_totals = {}
    expenses = []

    today_str = datetime.now().strftime("%Y-%m-%d")
    today_total = 0

    for row in rows:
        date = row["date"]
        category = row["category"]
        amount = row["amount"]

        # Monthly
        month = date[:7]
        monthly[month] = monthly.get(month, 0) + amount

        # Daily
        daily[date] = daily.get(date, 0) + amount

        # Category
        category_totals[category] = category_totals.get(category, 0) + amount

        # Today total
        if date == today_str:
            today_total += amount

        expenses.append({
            "id": row["id"],
            "item": row["item"],
            "date": date,
            "category": category,
            "amount": amount
        })

    # ===============================
    # POLYNOMIAL REGRESSION PREDICTION
    # ===============================

    past_dates = []
    past_values = []
    prediction_dates = []
    prediction_values = []
    suggestion = "Add more data for accurate prediction."

    if len(daily) >= 5:

        # Convert daily dict to sorted lists
        sorted_daily = sorted(daily.items())
        dates = [d[0] for d in sorted_daily]
        totals = [d[1] for d in sorted_daily]

        df = pd.DataFrame({
            "date": pd.to_datetime(dates),
            "total": totals
        })

        df["day_number"] = (df["date"] - df["date"].min()).dt.days

        X = df[["day_number"]]
        y = df["total"]

        poly = PolynomialFeatures(degree=2)
        X_poly = poly.fit_transform(X)

        model = LinearRegression()
        model.fit(X_poly, y)

        # Future 7 days
        future_days = np.arange(
            df["day_number"].max() + 1,
            df["day_number"].max() + 8
        ).reshape(-1, 1)

        future_poly = poly.transform(future_days)
        predictions = model.predict(future_poly)

        predictions = [max(0, round(val, 2)) for val in predictions]

        future_dates = [
            (df["date"].max() + timedelta(days=i)).strftime("%Y-%m-%d")
            for i in range(1, 8)
        ]
        # ===============================
# PREDICTION REASONING LOGIC
# ===============================

        reason = "Prediction based on historical spending trend."

        today = datetime.now()
        next_7_days = [today + timedelta(days=i) for i in range(1, 8)]

        for day in next_7_days:
            # Christmas
            if day.month == 12 and day.day == 25:
                reason = "Spending may increase due to Christmas season shopping."
                break

            # New Year
            if day.month == 1 and day.day == 1:
               reason = "Spending may increase due to New Year celebrations."
               break

            # Month End (Salary / Bill Payments)
            if day.day >= 27:
                reason = "Month-end expenses like bills and EMIs may increase spending."
    
            # Weekend Effect
            if day.weekday() in [5, 6]:
                reason = "Weekend spending trends detected. Leisure expenses may increase."
        # AI Suggestion
        avg_future = sum(predictions) / len(predictions)
        avg_past = df["total"].mean()

        if avg_future > avg_past:
            suggestion = "Spending is expected to increase next week. Consider reducing optional expenses."
        else:
            suggestion = "Spending trend looks stable. Maintain your financial discipline."

        past_dates = df["date"].dt.strftime("%Y-%m-%d").tolist()
        past_values = df["total"].tolist()
        prediction_dates = future_dates
        prediction_values = predictions

    # Focus Category
    focus_category = (
        max(category_totals, key=category_totals.get)
        if category_totals else "No category data"
    )

    conn.close()

    return jsonify({
        "monthly": monthly,
        "daily": daily,
        "category_totals": category_totals,
        "expense_list": expenses,
        "today_total": today_total,
        "past_dates": past_dates,
        "past_values": past_values,
        "prediction_dates": prediction_dates,
        "prediction_values": prediction_values,
        "focus_category": focus_category,
        "suggestion": suggestion,
        "reason": reason
    })

@app.route("/prediction")
def prediction():
    return render_template("prediction.html")
import re
from datetime import datetime
from flask import request, redirect, flash

@app.route("/add_sms_expense", methods=["POST"])
def add_sms_expense():

    if "user" not in session:
        return redirect("/")

    sms = request.form.get("sms_text")

    if not sms:
        return redirect("/dashboard")

    # --------------------
    # Extract Amount
    # --------------------
    amount_match = re.search(r'(Rs\.?|INR|₹)\s?(\d+(\.\d+)?)', sms)

    if amount_match:
        amount = amount_match.group(2)
    else:
        return redirect("/dashboard")

    # --------------------
    # Detect Category Smartly
    # --------------------
    sms_lower = sms.lower()

    if "credited" in sms_lower:
        category = "Income"
    elif "swiggy" in sms_lower or "zomato" in sms_lower:
        category = "Food"
    elif "amazon" in sms_lower or "flipkart" in sms_lower:
        category = "Shopping"
    elif "uber" in sms_lower or "ola" in sms_lower:
        category = "Travel"
    else:
        category = "UPI Expense"

    # --------------------
    # Extract Merchant
    # --------------------
    merchant_match = re.search(r'to\s([A-Za-z0-9\s&.-]+)', sms)

    if merchant_match:
        item = merchant_match.group(1).strip()
    else:
        item = "UPI Payment"

    # --------------------
    # Save to SAME database method you use
    # --------------------
    today = date.today().isoformat()

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO expenses (user, item, amount, category, date) VALUES (?, ?, ?, ?, ?)",
        (session["user"], item, amount, category, today)
    )

    conn.commit()
    conn.close()

    return redirect("/expenses")
@app.route("/add-bill", methods=["GET", "POST"])
def add_bill():
    if "user" not in session:
        return redirect("/login")

    if request.method == "POST":
        file = request.files["bill_image"]

        if file:
            from werkzeug.utils import secure_filename
            import time, os

            filename = secure_filename(str(int(time.time())) + "_" + file.filename)
            file_path = os.path.join("uploads", filename)
            file.save(file_path)

            # STEP 8.1 – Extract total amount
            amount = extract_amount_from_bill(file_path)

            # STEP 8.2 – Extract text + items
            text = extract_text_from_image(file_path)
            items = extract_items_from_text(text)

            conn = get_db_connection()
            cursor = conn.cursor()

            # Save bill
            cursor.execute("""
                INSERT INTO bills (user, bill_name, amount, category, bill_date, image_path)
                VALUES (?, ?, ?, ?, DATE('now'), ?)
            """, (
                session["user"],
                file.filename,
                amount,
                "Auto",
                filename
            ))

            # 🔥 STEP 8.3 – INSERT ITEMS INTO EXPENSES TABLE
            for item, price in items:
                category = predict_category_ml(item)


                cursor.execute("""
                    INSERT INTO expenses (user, item, amount, category, date)
                    VALUES (?, ?, ?, ?, DATE('now'))
                """, (
                    session["user"],
                    item,
                    price,
                    category
                ))



            conn.commit()
            conn.close()

        return redirect("/bills")

    return render_template("add_bill.html")


@app.route("/edit-expense/<int:id>", methods=["GET", "POST"])
def edit_expense(id):

    if "user" not in session:
        return redirect("/")

    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == "POST":

        item = request.form["item"]
        amount = request.form["amount"]
        category = request.form["category"]   # editable category
        date = request.form["date"]

        cursor.execute("""
            UPDATE expenses
            SET item=?, amount=?, category=?, date=?
            WHERE id=? AND user=?
        """, (item, amount, category, date, id, session["user"]))

        conn.commit()
        conn.close()

        return redirect("/expenses")

    cursor.execute(
        "SELECT * FROM expenses WHERE id=? AND user=?",
        (id, session["user"])
    )

    expense = cursor.fetchone()
    conn.close()

    return render_template("edit_expense.html", expense=expense)

@app.route("/expenses")
def view_expenses():
    if "user" not in session:
        return redirect("/")

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM expenses WHERE user = ? ORDER BY date DESC",
        (session["user"],)
    )
    expenses = cursor.fetchall()

    conn.close()

    return render_template("view_expenses.html", expenses=expenses)


@app.route("/bills")
def view_bills():
    if "user" not in session:
        return redirect("/login")

    search = request.args.get("search", "")
    category = request.args.get("category", "")
    sort = request.args.get("sort", "desc")

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM bills WHERE user = ?"
    params = [session["user"]]

    if search:
        query += " AND category LIKE ?"
        params.append(f"%{search}%")

    if category:
        query += " AND category = ?"
        params.append(category)

    if sort == "asc":
        query += " ORDER BY bill_date ASC"
    else:
        query += " ORDER BY bill_date DESC"

    cursor.execute(query, tuple(params))
    bills = cursor.fetchall()

    conn.close()

    return render_template("bills.html", bills=bills)
@app.route("/bill-view/<int:bill_id>")
def bill_view(bill_id):
    if "user" not in session:
        return redirect("/login")

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM bills WHERE id = ? AND user = ?",
        (bill_id, session["user"])
    )

    bill = cursor.fetchone()
    conn.close()

    if not bill:
        return "Bill not found", 404

    return render_template("bill_view.html", bill=bill)

@app.route("/delete-bill/<int:bill_id>")
def delete_bill(bill_id):
    if "user" not in session:
        return redirect("/login")

    conn = get_db_connection()
    cursor = conn.cursor()

    # get image name first
    cursor.execute(
        "SELECT image_path FROM bills WHERE id = ? AND user = ?",
        (bill_id, session["user"])
    )

    bill = cursor.fetchone()

    if bill:
        image_path = os.path.join("uploads", bill["image_path"])
        if os.path.exists(image_path):
            os.remove(image_path)

        cursor.execute(
            "DELETE FROM bills WHERE id = ? AND user = ?",
            (bill_id, session["user"])
        )
        conn.commit()

    conn.close()

    return redirect("/bills")
import requests
from flask import jsonify, request, render_template, session, redirect

SERP_API_KEY = "a401e99d7fa5f616662ec3bcb8aa3f509b542f75a14bcd21beef4f1a74481c8a"


@app.route("/offers")
def offers():
    if "user" not in session:
        return redirect("/login")

    return render_template("offers.html")

import requests


from flask import request, jsonify

@app.route("/search-offers")
def search_offers():

    product = request.args.get("product")

    url = "https://serpapi.com/search.json"

    params = {
        "engine": "google_shopping",
        "q": product,
        "api_key": SERP_API_KEY,
        "gl": "in",
        "hl": "en"
    }

    response = requests.get(url, params=params)
    data = response.json()

    offers = []

    # DEBUG
    print(data)

    if "shopping_results" in data:

        for item in data["shopping_results"]:

            offers.append({
                "title": item.get("title", "No title"),
                "price": item.get("price", "Price not available"),
                "source": item.get("source", "Unknown"),
                "image": item.get("thumbnail", "")
            })

    return jsonify(offers)
@app.route("/ai-deal")
def ai_deal():

    product = request.args.get("product")

    url = "https://serpapi.com/search.json"

    params = {
        "engine": "google_shopping",
        "q": product,
        "api_key": SERP_API_KEY,
        "gl": "in",
        "hl": "en"
    }

    response = requests.get(url, params=params)
    data = response.json()

    offers = []

    if "shopping_results" in data:

        for item in data["shopping_results"][:8]:

            price = item.get("price","0")

            price_num = ''.join(filter(str.isdigit, price))

            if price_num != "":
                price_num = int(price_num)
            else:
                price_num = 999999

            offers.append({
                "title": item.get("title"),
                "price": price,
                "price_num": price_num,
                "store": item.get("source"),
                "image": item.get("thumbnail")
            })

    # AI Logic → find best deal
    best_price = min(offers, key=lambda x: x["price_num"]) if offers else None

    return jsonify({
        "offers": offers,
        "best": best_price
    })
@app.route("/profile", methods=["GET", "POST"])
def profile():
    if "user" not in session:
        return redirect("/login")

    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        full_name = request.form["full_name"]
        income = request.form["income"]
        monthly_budget = request.form["monthly_budget"]
        savings_goal = request.form["savings_goal"]
        preferred_categories = request.form["preferred_categories"]

        cursor.execute("""
            INSERT INTO profile 
            (user, full_name, income, monthly_budget, savings_goal, preferred_categories)
            VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT(user) DO UPDATE SET
                full_name=excluded.full_name,
                income=excluded.income,
                monthly_budget=excluded.monthly_budget,
                savings_goal=excluded.savings_goal,
                preferred_categories=excluded.preferred_categories
        """, (
            session["user"],
            full_name,
            income,
            monthly_budget,
            savings_goal,
            preferred_categories
        ))

        conn.commit()

    cursor.execute("SELECT * FROM profile WHERE user = ?", (session["user"],))
    profile = cursor.fetchone()

    conn.close()

    return render_template("profile.html", profile=profile)
from flask import jsonify
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
import requests

def ask_llama(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "tinyllama",  # your local Ollama model
                "prompt": prompt,
                "stream": False,
                "options": {"num_predict": 500}  # limit length for speed
            }
        )
        data = response.json()
        return data.get("response", "No response from AI")
    except Exception as e:
        return f"Error: {str(e)}"

# 🔹 Chatbot Page Route
@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")

# 🔹 API Route for Chat Messages
@app.route("/ask_ai", methods=["POST"])
def ask_ai():
    user_message = request.json["message"]

    # Fetch last 10 expenses from DB (replace with your DB function)
    if "user" not in session:
        return jsonify({"response": "Please login first."})

    user_expenses = get_user_expenses(session["user"])[:10]

    # Format expenses
    expense_text = ""
    for e in user_expenses:
        expense_text += f"{e['date']}: {e['category']} - {e['amount']}\n"

    # Build prompt for Ollama
    final_prompt = f"""
You are a smart personal finance assistant.
User expenses:
{expense_text}

User question: {user_message}
Give clear, short advice based on their expenses.
"""

    # Ask the AI
    reply = ask_llama(final_prompt)

    # ✅ Return JSON with 'response' key
    return jsonify({"response": reply})
if __name__ == "__main__":
    app.run(debug=True)
