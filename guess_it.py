import random
import time

def generate_unique_pairs():
    pairs = [(i, j) for i in range(1, 13) for j in range(i, 13)]
    random.shuffle(pairs)  # This line shuffles the pairs
    return pairs

def ask_question(pair):
    num1, num2 = pair
    correct_answer = num1 * num2

    user_answer = int(input(f"What is {num1} * {num2}? "))

    if user_answer == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"Sorry, that's incorrect. The answer is {correct_answer}.")
        return False

def main():
    pairs = generate_unique_pairs()

    correct_answers = 0
    total_questions = len(pairs)

    start_time = time.time()

    for pair in pairs:
        if ask_question(pair):
            correct_answers += 1
        print("Moving on to the next question...")

    end_time = time.time()
    elapsed_time = end_time - start_time
    score = 100 * correct_answers/total_questions
    print(f"Quiz completed! You answered {correct_answers} out of {total_questions} questions correctly or {score:.2f}%.")
    print(f"It took you {elapsed_time:.2f} seconds to complete the quiz.")

    f = open("quizLog.txt", "a")
    f.write(f"\nCorrect:{correct_answers},Time:{elapsed_time:.2f}")
    f.close()

if __name__ == "__main__":
    main()
