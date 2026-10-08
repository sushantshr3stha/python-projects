import json

with open("questions.json", "r") as f:
    questions = json.load(f)

score = 0

for q in questions:
    print(q["question"])
    for letter, option in zip("abcd", q["options"]):
        print(f"  {letter}. {option}")

    user_answer = input("Choose your answer: ").strip().lower()

    if user_answer == q["answer"]:
        print("Your answer was correct\n")
        score += 1
    else:
        print(f"Your answer was incorrect. The answer is: {q['answer']}\n")

print(f"You scored {score}/{len(questions)}")