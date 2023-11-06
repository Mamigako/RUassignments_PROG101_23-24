from question import Question

class ChoiceQuestion(Question):

    def __init__(self, question) -> None:
        super().__init__(question)
        self.__answers = []


    def get_question(self):
        answer_choises = super().get_question()+"\n"
        
        for index,value in enumerate(self.__answers):
        
            if index == len(self.__answers)-1:
                answer_choises += "{0}. {1}".format(index+1, value)

            else:
                answer_choises += "{0}. {1}\n".format(index+1, value)

        return answer_choises


    def add_choice(self, answer, correct):
        if correct:
            self.__answer_str = answer

        self.__answers.append(answer)


    def check_answer(self, guess):
        try:
            return self.__answer_str == self.__answers[int(guess)-1]
        
        except IndexError:
            return False

    def __str__(self):
        return super().__str__() + str(self.__answers.index(self.__answer_str)+1)
