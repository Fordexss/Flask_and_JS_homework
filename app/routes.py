from flask import Blueprint, render_template, request, redirect

from app.db import add_question, get_questions, get_correct_answer

bp = Blueprint("tests", __name__)


@bp.route("/")
def root():
    poll_data = get_questions()
    poll_data = [dict(row) for row in poll_data]
    return render_template("poll.html", data=poll_data, number_of_ques=len(poll_data))


@bp.route("/add_test", methods=["GET", "POST"])
def add_test():
    if request.method == "GET":
        return render_template("add_test.html")
    else:
        number_of_ques = int(request.form.get("numberOfQuestions"))
        for number in range(1, number_of_ques + 1):
            question = request.form.get(f"question{number}")
            answers = request.form.get(f"answers{number}")
            correct = request.form.get(f"correct{number}")
            add_question(question, answers, correct)
        return redirect("/")


@bp.route("/poll")
def poll():
    number_of_ques = int(request.args.get('numberOfQues', 0))
    correct_answers = 0

    for key, value in request.args.items():
        if "field" in key:
            number, question = key.split('_')

            correct_answer = get_correct_answer(question)

            print(f"value: {value}")
            print(f"set {correct_answer}")

            if correct_answer is not None:
                test_answer = set(correct_answer)

                if value in test_answer:
                    correct_answers += 1

    result_text = f"Ви відповіли правильно на {correct_answers} з {number_of_ques} питань."
    return render_template("thankyou.html", result=result_text)

