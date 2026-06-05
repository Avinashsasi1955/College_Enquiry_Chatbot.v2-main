from flask import Flask, render_template, request, redirect, session, jsonify
from db_config import get_connection
from difflib import get_close_matches
from datetime import datetime

app = Flask(__name__)
app.secret_key = "chatbot_secret_key"


# --------------------- ROUTES -----------------------

@app.route('/')
def home():
    return redirect('/login')


# ---- USER AUTH ----
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = cur.fetchone()
        conn.close()

        if user:
            session['user_id'] = user['user_id']
            session['username'] = user['username']
            return redirect('/chat')
        else:
            return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
        conn.commit()
        conn.close()

        return redirect('/login')
    return render_template('register.html')


# ---- ADMIN AUTH ----
@app.route('/admin', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM admin WHERE username=%s AND password=%s", (username, password))
        admin = cur.fetchone()
        conn.close()

        if admin:
            session['admin'] = True
            return redirect('/admin/dashboard')
        else:
            return render_template('admin_login.html', error="Invalid admin credentials")
    return render_template('admin_login.html')


@app.route('/admin/dashboard')
def admin_dashboard():
    if not session.get('admin'):
        return redirect('/admin')

    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM faqs ORDER BY category")
    faqs = cur.fetchall()
    conn.close()

    return render_template('admin_dashboard.html', faqs=faqs)


# ---- ADD FAQ ----
@app.route('/admin/add_faq', methods=['POST'])
def add_faq():
    if not session.get('admin'):
        return redirect('/admin')

    question = request.form['question']
    answer = request.form['answer']
    category = request.form['category']
    keywords = request.form['keywords']

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO faqs (question, answer, category, keywords) VALUES (%s, %s, %s, %s)",
                (question, answer, category, keywords))
    conn.commit()
    conn.close()

    return redirect('/admin/dashboard')


# ---- CHATBOT ----
@app.route('/chat')
def chat():
    if not session.get('user_id'):
        return redirect('/login')
    return render_template('chat.html', username=session['username'])


@app.route('/get_response', methods=['POST'])
def get_response():
    user_query = request.form['message']

    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM faqs")
    faqs = cur.fetchall()
    conn.close()

    questions = [faq['question'] for faq in faqs]
    match = get_close_matches(user_query.lower(), [q.lower() for q in questions], n=1, cutoff=0.5)

    if match:
        matched_question = match[0]
        for faq in faqs:
            if faq['question'].lower() == matched_question:
                bot_reply = faq['answer']
                break
    else:
        bot_reply = "Sorry, I couldn’t find an answer for that. Please contact the admin."

    # Save to chat history
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO chat_history (user_id, user_query, bot_reply) VALUES (%s, %s, %s)",
                (session['user_id'], user_query, bot_reply))
    conn.commit()
    conn.close()

    return jsonify({'reply': bot_reply})

@app.route('/chat_history')
def get_chat_history():
    if 'user' not in session:
        return jsonify([])
    user_id = session['user']['id']
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT user_message, bot_reply, chat_timestamp FROM chat_history WHERE user_id=%s ORDER BY chat_timestamp ASC", (user_id,))
    chats = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(chats)



@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)
