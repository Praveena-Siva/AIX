train_data = [
    ("I got full marks in the test today!", "Happy"),
    ("We won the college cricket match", "Happy"),
    ("My friends planned a surprise party for me", "Happy"),
    ("The food in the canteen was really tasty", "Happy"),
    ("I am so excited for the weekend trip", "Happy"),
    ("Our project got selected for the exhibition", "Happy"),
    ("I finally learned how to ride a bicycle", "Happy"),
    ("Mom made my favourite sweets today", "Happy"),
    ("I lost my phone on the bus", "Sad"),
    ("I failed in the mathematics exam", "Sad"),
    ("My best friend is moving to another city", "Sad"),
    ("It rained and our picnic was cancelled", "Sad"),
    ("I missed the last bus and felt very upset", "Sad"),
    ("My laptop stopped working before the submission", "Sad"),
    ("I felt lonely during the long holidays", "Sad")
]


def count_moods(data):
    happy = 0
    sad = 0

    for sentence, mood in data:
        if mood == "Happy":
            happy += 1
        else:
            sad += 1

    return happy, sad


print(count_moods(train_data))


happy_words = ["marks", "won", "friends"]
sad_words = ["lost", "failed", "lonely"]


def guess_mood(sentence):
    sentence = sentence.lower()
    words = sentence.split()

    happy = 0
    sad = 0

    for word in words:
        word = word.strip(".,!?;:")

        if word in happy_words:
            happy += 1

        if word in sad_words:
            sad += 1

    if happy >= sad:
        return "Happy"
    else:
        return "Sad"


practice_data = [
    ("I won a medal in the sports meet", "Happy"),
    ("I lost my notebook before the exam", "Sad"),
    ("My friends gave me a lovely surprise", "Happy"),
    ("The train was late and I felt upset", "Sad"),
    ("Today was a great day", "Happy")
]


correct = 0

for sentence, actual in practice_data:
    predicted = guess_mood(sentence)

    print(sentence)
    print("Actual:", actual)
    print("Predicted:", predicted)

    if predicted == actual:
        correct += 1

accuracy = (correct / len(practice_data)) * 100

print("Correct answers:", correct)
print("Accuracy:", accuracy, "%")


def learn_scores(data):
    scores = {}

    for sentence, mood in data:
        words = sentence.lower().split()

        for word in words:
            word = word.strip(".,!?;:")

            if word not in scores:
                scores[word] = 0

            if mood == "Happy":
                scores[word] += 1
            else:
                scores[word] -= 1

    return scores


word_scores = learn_scores(train_data)


def guess_mood_learned(sentence):
    total = 0
    words = sentence.lower().split()

    for word in words:
        word = word.strip(".,!?;:")

        if word in word_scores:
            total += word_scores[word]

    if total > 0:
        return "Happy"
    else:
        return "Sad"


learned_correct = 0

for sentence, actual in practice_data:
    predicted = guess_mood_learned(sentence)

    print(sentence)
    print("Actual:", actual)
    print("Predicted:", predicted)

    if predicted == actual:
        learned_correct += 1

learned_accuracy = (learned_correct / len(practice_data)) * 100

print("Learned correct answers:", learned_correct)
print("Learned accuracy:", learned_accuracy, "%")
