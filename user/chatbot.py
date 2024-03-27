class ChatBot:
    def __init__(self, responses):
        self.responses = responses

    def respond(self, user_input):
        if user_input in self.responses:
            return self.responses[user_input]
        else:
            return "I'm sorry, I don't understand that."
