from backend import chatbot as cb

tb = cb.ChatBot()

while True:
    userSays = input("> ")
    if userSays == "":
        break
    print(tb.get_response(userSays))

tb.close()