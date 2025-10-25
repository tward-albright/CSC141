# 8-9
def show_messages(messages):
    for message in messages:
        print(message)


messages = ["Hi there!", "This is for CSC141.", "[insert something insightful here]"]
show_messages(messages)


# 8-10 & 8-11
def send_messages(queue, sent_messages):
    while queue:
        message = queue.pop()
        print(f"Got message: {message}")
        sent_messages.append(message)


sent = []
send_messages(messages, sent)
# send_messages(messages[:], sent) # 8-11
