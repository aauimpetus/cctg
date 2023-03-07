# This script contains the questions used in this trivia game. 


# Defining questions:


init python:

    """
    A class for questions. 
    """
    class Question(object):

        """
        A constructor for a Question object. 
        @param question         a string containing the question
        @param a1               a string containing the first answer choice
        @param a2               a string containing the second answer choice
        @param a3               a string containing the third answer choice
        @param a4               a string containing the fourth answer choice
        @param correct          a string containing the same text for the correct answer choice
        @param point_value      an integer representing the question's point value (default is 1)
        """
        def __init__(self, question, a1, a2, a3, a4, correct, point_value = 1):
            self.question = question
            self.a1 = a1
            self.a2 = a2
            self.a3 = a3
            self.a4 = a4
            self.correct = correct
            self.point_value = point_value



# Instantiating Question objects:


# HEY YOU !!!! Don't forget to append these questions to question_list in question_list.rpy!

#QUESTIONS FROM RIVINE PLASTIC WASTE MEASUREMENTS!!!

define q1 = Question(question = "What is plastic soup?",
                        a1 = "Islands of plastic waste in the ocean",
                        a2 = "Accumulation of plastics in aquatic systems",
                        a3 = "Micro plastics in water",
                        a4 = "Plastics in the food chain",
                        correct = "Accumulation of plastics in aquatic systems")


define q2 = Question(question = "Rivers are accountable for the influx of plastic waste in oceans of …%",
                        a1 = "80%",
                        a2 = "50%",
                        a3 = "20%",
                        a4 = "10%",
                        correct = "80%")   


define q3 = Question(question = "A plastic bottle will be degraded in nature within how much time?",
                        a1 = "5 years",
                        a2 = "50 years",
                        a3 = "500 years",
                        a4 = "Never",
                        correct = "Never")   


define q4 = Question(question = "The effects of plastics in nature are:",
                        a1 = "Entanglement and ingestion by animals",
                        a2 = "Leaching of chemicals in to environment",
                        a3 = "Accumulation of plastics in the food chain",
                        a4 = "All of the above",
                        correct = "All of the above")   


define q5 = Question(question = "The production of plastics in the future is (compared to 2020) expected to…",
                        a1 = "Double in 2050",
                        a2 = "Triple in 2050",
                        a3 = "Grown exponentially (>5x) in 2050",
                        a4 = "Stay the same",
                        correct = "Grown exponentially (>5x) in 2050")   


define q6 = Question(question = "There is clear legislation on the amount of plastic waste in the environment",
                        a1 = "Yes",
                        a2 = "No",
                        a3 = "Maybe",
                        a4 = "42",
                        correct = "No")  


define q7 = Question(question = "What would be a reliable way to determine amount and composition of plastics in rivers?",
                        a1 = "Count and categorize floating plastics",
                        a2 = "Count and categorize plastics on shore plastics",
                        a3 = "Catch plastics from river streams and the count and categorize",
                        a4 = "All of the above",
                        correct = "All of the above")  


define q8 = Question(question = "Determining the amount and composition of plastic waste helps to develop solutions",
                        a1 = "Yes",
                        a2 = "No",
                        a3 = "Maybe",
                        a4 = "42",
                        correct = "Yes")   



# Don't forget to append these question objects to question_list in question_list.rpy!