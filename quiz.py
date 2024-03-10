# quiz.py
QUESTIONS = {
    "The territory of Porus who offered strong resistance to Alexander was situated between the rivers of": [
        "Jhelum and Chenab", "Sutlej and Beas", "Ravi and Chenab", "Ganga and Yamuna"
    ],
    "Which of the following is a non metal that remains liquid at room temperature?": [
        "Phosphorous",
        "Chlorine",
        "Bromine",
        "Helium",
    ],
    "Which of the following countries won the final of the triangular cricket series held in durban in February 1997?": [
        "India", "New zealand", "South africa", "Zimbabwe"
    ],
}

for question, alternatives in QUESTIONS.items():
    correct_answer = alternatives[0]
    sorted_alternatives = sorted(alternatives)
    for label, alternative in enumerate(sorted_alternatives):
        print(f"  {label}) {alternative}")

    answer_label = int(input(f"{question}? "))
    answer = sorted_alternatives[answer_label]
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")