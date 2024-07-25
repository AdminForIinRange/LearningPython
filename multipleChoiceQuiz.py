question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What is the capital of France?\n(a) Paris\n(b) Rome\n(c) London\n\n"
]

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questionList = [  # Each item in the array/list stores the question and answer inside a class
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a")
]

def run_test(questionList):
    score = 0

    for question in questionList:  # Remember, think of it like map(), replace 'i' with 'question' (singular). 
        #So now it's just for each individual item (question) in questionList which has 3 items
        ans = input(question.prompt)  # In this case, 'question' becomes an instance of the Question class, so when you do question.prompt,
        #you are accessing the 'prompt' attribute of that instance
        if ans == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questionList)))

run_test(questionList)









# # List of question prompts, each followed by multiple choice answers
# question_prompts = [
#     "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
#     "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
#     "What is the capital of France?\n(a) Paris\n(b) Rome\n(c) London\n\n"
# ]

# # Question class to store a question prompt and its correct answer
# class Question:
#     def __init__(self, prompt, answer):
#         self.prompt = prompt  # The question prompt
#         self.answer = answer  # The correct answer

# # List of Question objects, each initialized with a prompt and the correct answer
# questionList = [
#     Question(question_prompts[0], "a"),  # First question, correct answer is "a"
#     Question(question_prompts[1], "c"),  # Second question, correct answer is "c"
#     Question(question_prompts[2], "a")   # Third question, correct answer is "a"
# ]

# # Function to run the test
# def run_test(questionList):
#     score = 0  # Initialize score to 0

#     # Loop through each question in the list
#     for question in questionList:
#         # Prompt the user for their answer
#         ans = input(question.prompt)
        
#         # Check if the user's answer matches the correct answer
#         if ans == question.answer:
#             score += 1  # Increment score if the answer is correct
    
#     # Print the final score and the total number of questions
#     print("You got " + str(score) + "/" + str(len(questionList)))

# # Call the run_test function to execute the test
# run_test(questionList)
