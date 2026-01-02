from flask import Flask, render_template, request
from subjects import SUBJECT_LIST, DAYS, SLOTS, TIMETABLE

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', subjects=SUBJECT_LIST)

@app.route('/generate', methods=['POST'])
def generate():
    selected_subjects = request.form.getlist('subjects')

    filtered_tt = {}

    for day, slots in TIMETABLE.items():
        for slot, details in slots.items():
            if details["subject"] in selected_subjects:
                filtered_tt.setdefault(day, {})[slot] = details

    return render_template(
        'timetable.html',
        days=DAYS,
        slots=SLOTS,
        timetable=filtered_tt
    )

if __name__ == '__main__':
    app.run(debug=True)
