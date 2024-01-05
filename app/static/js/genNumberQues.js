function removeAll(selectBox) {
    while (selectBox.options.length > 0) {
        selectBox.remove(0);
    }
}

function generateOptions(questionNum=undefined){
    const select = document.getElementById(`correct${questionNum}`);
    let answers = document.getElementById(`answers${questionNum}`).value.split(',')
    console.log(answers)
    //
    removeAll(select)
    if (answers) {
        answers.forEach((answer) => {
            let newOption = new Option(answer, answer);
            select.add(newOption, undefined)
        })
    }
    // for (let numOfQues = 1; numOfQues <= answers.length; numOfQues++) {
}


function generateQuestions() {
    let numberOfQuestions = document.getElementById("numberOfQuestions").value
    let questionContainer = document.getElementById("questionContainer")

    questionContainer.innerHTML = ''

    for (let i = 1; i <= numberOfQuestions; i++) {
        let labelQuestion = document.createElement('label')
        labelQuestion.textContent = 'Question ' + i + ':'

        let inputQuestion = document.createElement('input')
        inputQuestion.type='text'
        inputQuestion.name='question' + i
        inputQuestion.id='question' + i

        let labelAnswers = document.createElement('label')
        labelAnswers.textContent = 'Answers (separated by coma)' + i + ':'

        let inputAnswers = document.createElement('input')
        inputAnswers.onchange= () => {generateOptions(i);};
        // inputAnswers.setAttribute("onchange", function(){generateOptions(i);});
        inputAnswers.type='text'
        inputAnswers.name='answers' + i
        inputAnswers.id='answers' + i

        let labelCorrectAnswer = document.createElement('label')
        labelCorrectAnswer.textContent = 'Correct answer for ' + i + ':'

        let selectCorrectAnswer = document.createElement('select')
        // selectCorrectAnswer.onclick=generateOptions
        selectCorrectAnswer.name='correct' + i
        selectCorrectAnswer.id='correct' + i

        questionContainer.appendChild(labelQuestion)
        questionContainer.appendChild(document.createElement('br'))
        questionContainer.appendChild(inputQuestion)
        questionContainer.appendChild(document.createElement('br'))

        questionContainer.appendChild(labelAnswers)
        questionContainer.appendChild(document.createElement('br'))
        questionContainer.appendChild(inputAnswers)
        questionContainer.appendChild(document.createElement('br'))

        questionContainer.appendChild(labelCorrectAnswer)
        questionContainer.appendChild(document.createElement('br'))
        questionContainer.appendChild(selectCorrectAnswer)
        questionContainer.appendChild(document.createElement('br'))
    }
}