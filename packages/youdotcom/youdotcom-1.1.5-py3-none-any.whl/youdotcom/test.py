from youchat import Chat



chat = Chat.send_message(webdriver_path="/usr/bin/chromedriver", message="how is your day?")

print(chat)
