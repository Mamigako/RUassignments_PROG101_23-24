class Question:
    def __init__(self, question, answer="") -> None:
        self.__question_str = question
        self.__answer_str = answer


    def get_question(self):
        return self.__question_str
    

    def check_answer(self, guess):
        return guess.lower() == self.__answer_str.lower()


    def __str__(self):
        return "Q: {0} A: {1}".format(self.__question_str, self.__answer_str)


    def __repr__(self):
        return "Question({0}, {1})".format(self.__question_str, self.__answer_str)
    