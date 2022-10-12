class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
chat = []
chat.append(Cat("Milou",7))
chat.append(Cat("chatti",9))
chat.append(Cat("bella",4))

def chatAge (chats):
    chat = chats[0]
    for i in chats :
        if i.age > chat.age :
            chat = i
    return chat
Chat = chatAge(chat)
print("Le chat le plus âgé est ",Chat.name, " et a ",Chat.age, "ans")
