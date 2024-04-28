#!/usr/bin/env python3

# Define the questions and their corresponding answers
questions_answers = {
    "31": {
        "103-line1.txt": "0",
        "103-line2.txt": "0"
    },
    "32": {
        "104-line1.txt": "1",
        "104-line2.txt": "1",
        "104-line3.txt": "yes",
        "104-line4.txt": "Yes",
        "104-line5.txt": "1"
    },
    "33": {
        "105-line1.txt": "262"
    },
    "34": {
        "106-line1.txt": "1",
        "106-line2.txt": "0",
        "106-line3.txt": "No",
        "106-line4.txt": "Yes",
        "106-line5.txt": "1"
    }
}

# Loop through each question and its answers
for question, answers in questions_answers.items():
    # Loop through each answer and write it to the corresponding file
    for file_name, answer in answers.items():
        with open(file_name, "w") as file:
            file.write(answer)