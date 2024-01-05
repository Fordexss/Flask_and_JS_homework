import sqlite3


def add_question(question, answers, correct):
    msg = ""
    with sqlite3.connect("app.db") as conn:
        try:
            cr = conn.cursor()
            cr.execute("INSERT INTO test (question, answers, correct) VALUES (?, ?, ?)",
                       (question, answers, correct))
            conn.commit()
            msg = "Record success added"
        except Exception as e:
            conn.rollback()
            print(e)
            msg = "Error in insert operation"
    return msg


def get_questions():
    res = None
    with sqlite3.connect("app.db") as conn:
        conn.row_factory = sqlite3.Row
        cr = conn.cursor()
        cr.execute("SELECT * FROM test")
        res = cr.fetchall()
        print(res)
    return res


def get_correct_answer(question):
    with sqlite3.connect("app.db") as conn:
        conn.row_factory = sqlite3.Row
        cr = conn.cursor()
        cr.execute("SELECT answers FROM test WHERE question=?", (question,))
        row = dict(cr.fetchone())

        if row and 'answers' in row:
            correct_value = row['answers']
            return correct_value.split(',') if correct_value is not None else None
        else:
            return None
