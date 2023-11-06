class Exam:
    def __init__(self) -> None:
        self.__questions = []
        self.__score = 0


    def add_question(self, question):
        self.__questions.append(question)
    

    def take(self):
        for question in self.__questions:
            print(question.get_question())

            guess = input()
            correct = question.check_answer(guess)

            print(correct)
            print()
            if correct:
                self.__score += 1


    def get_points(self):
        return self.__score
    

    def get_num_questions(self):
        return len(self.__questions)

    
    def __str__(self) -> str:
        all_questions = ""
        for index,question in enumerate(self.__questions):
            if index == len(self.__questions)-1:
                all_questions += str(question)
            
            else:
                all_questions += str(question)+"\n"

        return all_questions

            
