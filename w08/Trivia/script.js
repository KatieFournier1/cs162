let answer_q1 = "Banana"
let q1_buttons = document.querySelectorAll("#question-1 > button");
let q1_result = document.querySelector("#question-1 > .answer-result");
for (let button of q1_buttons) {
    button.addEventListener("click", () => {
        if (button.innerHTML == answer_q1) {
            button.style.color = "green"
            q1_result.style.color = "green";
            q1_result.innerHTML = "Correct!";
        } else {
            button.style.color = "red"
            q1_result.style.color = "red";
            q1_result.innerHTML = "Incorrect";
        }
    })
}

let answer_q2 = "412"
let q2_text = document.querySelector("#question-2 > .answer-text");
let q2_submit_button = document.querySelector("#question-2 > button");
let q2_result = document.querySelector("#question-2 > .answer-result");
q2_submit_button.addEventListener("click", () => {
    if (q2_text.value == answer_q2) {
        q2_text.style.color = "green"
        q2_result.style.color = "green";
        q2_result.innerHTML = "Correct!";
    } else {
        q2_text.style.color = "red";
        q2_result.style.color = "red";
        q2_result.innerHTML = "Incorrect";
    }
})
