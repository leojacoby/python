import datetime
import random
import time

from questions import Add, Subtract, Multiply, Divide


class Quiz:
    questions = []
    correct = 0
    incorrect = 0
    times = []
    restart = None
    stop = None
    
    numbers = []
    for i in range(1, 13):
        numbers.append(i)

    def subtract_q(self):
        num1 = random.choice(self.numbers)
        num2 = random.randint(1, num1-1)
        return (num1, num2)

    
    def divide_q(self):
        prime = [1, 2, 3, 5, 7, 11]
        num1 = 1
        while num1 in prime:
            num1 = random.choice(self.numbers)

        divis = []
        for i in range(1, num1 + 1):
            if num1 % i == 0:
                divis.append(i)
        num2 = random.choice(divis)

        return num1, num2

    def __init__(self):
        operations = [Add, Subtract, Multiply, Divide]
        for _ in range(10):
            operation = random.choice(operations)
            if operation == Add or operation == Multiply:
                question = operation(random.choice(self.numbers), random.choice(self.numbers))
            elif operation == Subtract:
                results = self.subtract_q()
                question = Subtract(results[0], results[1])
            elif operation == Divide:
                results = self.divide_q()
                question = Divide(results[0], results[1])
                
            self.questions.append(question)

    def take_quiz(self):
        
        global restart, stop, times
        for i in self.questions:
            time.sleep(1)
            if self.ask(i):
                self.stop = datetime.datetime.now()
                self.times.append((self.stop - self.restart).seconds)
                time.sleep(1)
                print("correct")
                self.correct += 1
                elapsed = round((float((self.stop - self.restart).seconds) + float((self.stop - self.restart).microseconds/1000000)), 1)
                time.sleep(1)
                print("That problem took you {} seconds.".format(elapsed))
            else:
                self.stop = datetime.datetime.now()
                self.times.append((self.stop - self.restart).seconds)
                time.sleep(1)
                print("incorrect")
                self.incorrect += 1
                elapsed = round((float((self.stop - self.restart).seconds) + float((self.stop - self.restart).microseconds/1000000)), 1)
                time.sleep(1)
                print("That problem took you {} seconds.".format(elapsed))
        self.summary()

        
        
                

    def ask(self, question):
        global restart, stop, times
        self.restart = datetime.datetime.now()
        ans = input(question.text + ' = ')
        if ans == str(question.answer):
            return True
        else:
            return False

    def summary():
        elapsed = 0
        for i in self.times:
            elapsed += i
            
        time.sleep(1)
        print("You answered {}/10 problems correctly in {} seconds".format(self.correct, round(elapsed)))


Quiz().take_quiz()
        
