# class Email:
#     def __init__(self, sender,receiver,content):
#         self.sender = sender # instance atributes
#         self.receiver = receiver
#         self.content = content
#         self.is_sent = False
#
#     def send(self):
#         self.is_sent = True
#
#     def get_info(self):
#         return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"
#
#
# emails = []
# line = input()
# while line != "Stop":
#   #  sender, receiver, content = line.split() # kogato znaem na kolko chasti da go razdelim
#     tokens = line.split(" ")
#     sender = tokens[0]
#     receiver = tokens[1]
#     content = tokens[2]
#     email = Email(sender, receiver, content)
#     emails.append(email)
#     line = input()
#
# send_emails = list(map(lambda x: int(x), input().split(", ")))
# for x in send_emails:
#     emails[x].send()
#
# for email in emails:
#     print(email.get_info())


class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


command_input = input()
emails = []
while command_input != "Stop":
    command_args = command_input.split()
    s = command_args[0]
    r = command_args[1]
    c = command_args[2]
    email = Email(s, r, c)
    emails.append(email)

    command_input = input()

indexes = list(map(int, input().split(", ")))

for i in range(len(emails)):
    curr_email = emails[i]
    if i in indexes:
        curr_email.send()

    current_email_info = curr_email.get_info()
    print(current_email_info)