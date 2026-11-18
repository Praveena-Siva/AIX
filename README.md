#AIxCelerate – Mood Guesser
Project Description

A Python program that predicts whether a sentence is Happy or Sad using words and word scores.

Level 1: Count the Moods

The count_moods() function counts Happy and Sad sentences.

Output: (8, 7)

Level 2: Guess the Mood

The guess_mood() function checks words and predicts Happy or Sad.

Level 3: Testing

Accuracy: _____ %

The sentence closest to going wrong was a sentence containing unfamiliar words because they may not be in my word lists.
Adding more useful words and improving word matching would make my program better.
Learning Questions

1. What is the total score of "good party today", and is it Happy or Sad?

Answer: 2 + 1 = +3 (Happy).

2. What is the total score of "bad exam day", and is it Happy or Sad?

Answer: -2 + 0 - 1 = -3 (Sad).

3. Why did "exam" get a score of 0? Is it good or bad?

Answer: It appears equally in Happy and Sad sentences. So its score is 0. This is useful because it avoids favouring either mood.

4. Why is "not good" labelled Happy, and how can we fix it?

Answer: The program sees "good" as positive but ignores "not". We can fix this by checking negative words and handling negation.

Conclusion

I learned Python functions, loops, word scoring and basic sentiment analysis.

Technologies Used
Python
GitHub
