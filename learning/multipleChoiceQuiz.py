question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What is the capital of France?\n(a) Paris\n(b) Rome\n(c) London\n\n"
]

# In Python, classes are used to define the structure and behavior of objects. 
# They are not inherently type-safe, meaning that they do not enforce type constraints on the data they hold.
# Instead, classes in Python are more about encapsulating data and behavior together.

# When you create an instance of a class, you are creating an object that holds data (attributes) and can perform actions (methods) defined by the class.
#  Here is a simple example to illustrate this:

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







