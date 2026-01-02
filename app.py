from flask import Flask, render_template, request, redirect, url_for, jsonify
from firebase import db
from datetime import datetime

app = Flask(__name__)

# ---------- Time Formatter ----------


def format_time(dt):
    day = dt.day
    suffix = "th" if 11 <= day <= 13 else {
        1: "st", 2: "nd", 3: "rd"
    }.get(day % 10, "th")
    return dt.strftime(f"{day}{suffix} %b %I:%M %p")

# ---------- Home ----------


@app.route('/')
def index():
    users = []
    docs = db.collection('users').order_by('user_id').stream()

    for doc in docs:
        data = doc.to_dict()
        data['doc_id'] = doc.id
        users.append(data)

    return render_template('index.html', users=users)

# ---------- AJAX DUPLICATE CHECK ----------


@app.route('/check-duplicate', methods=['POST'])
def check_duplicate():
    email = request.json.get('email')
    contact = request.json.get('contact')
    users_ref = db.collection('users')

    if email and any(users_ref.where('email', '==', email).stream()):
        return jsonify({'status': 'email'})

    if contact and any(users_ref.where('contact', '==', contact).stream()):
        return jsonify({'status': 'contact'})

    return jsonify({'status': 'ok'})

# ---------- Create ----------


@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        contact = request.form['contact']

        users_ref = db.collection('users')

        last = users_ref.order_by(
            'user_id', direction='DESCENDING'
        ).limit(1).stream()

        last_id = 0
        for doc in last:
            last_id = doc.to_dict().get('user_id', 0)

        new_id = last_id + 1
        now = format_time(datetime.now())

        users_ref.add({
            'user_id': new_id,
            'name': name,
            'email': email,
            'contact': contact,
            'created_at': now,
            'updated_at': now
        })

        return redirect(url_for('index'))

    return render_template('add_user.html')

# ---------- Update ----------


@app.route('/edit/<doc_id>', methods=['GET', 'POST'])
def edit_user(doc_id):
    ref = db.collection('users').document(doc_id)

    if request.method == 'POST':
        ref.update({
            'name': request.form['name'],
            'email': request.form['email'],
            'contact': request.form['contact'],
            'updated_at': format_time(datetime.now())
        })
        return redirect(url_for('index'))

    return render_template('edit_user.html', user=ref.get().to_dict())

# ---------- Delete & REORDER IDS ----------


@app.route('/delete/<doc_id>')
def delete_user(doc_id):
    users_ref = db.collection('users')
    users_ref.document(doc_id).delete()

    # 🔁 Reassign IDs
    docs = list(users_ref.order_by('user_id').stream())
    for index, doc in enumerate(docs, start=1):
        users_ref.document(doc.id).update({'user_id': index})

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(port=8000, debug=True)
