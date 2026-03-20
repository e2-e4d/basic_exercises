"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime

import lorem


def generate_chat_history():
    # messages_amount = random.randint(200, 1000)
    messages_amount = random.randint(3, 7)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages


# 1. Вывести айди пользователя, который написал больше всех сообщений.
def most_active_user_id(messages):
    user_counts = {}
    for message in messages:        
        user_id = message['sent_by']
        if user_id not in user_counts:
            user_counts[user_id] = 1
        else:
            user_counts[user_id] += 1

    print(user_counts)
    return max(user_counts, key=user_counts.get)

# 2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
def most_replied_user_id(messages):
    reply_counts = {}
    for message in messages:
        message_reply_for = message['reply_for']
        if message_reply_for not in reply_counts:
            reply_counts[message_reply_for] = 1
        else:
            reply_counts[message_reply_for] += 1

    print(reply_counts)
    return max(reply_counts, key=reply_counts.get)  

# 3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
def most_viewed_user_ids(messages):
    pass    

# 4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
def peak_time_of_day(messages):
    pass

# 5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).
def longest_thread_starter_ids(messages):
    pass

if __name__ == "__main__":
    print(generate_chat_history())
    chat_messages = generate_chat_history()
    print('\n')
    print("1. Идентификатор пользователя, который написал больше всех сообщений:", most_active_user_id(chat_messages))
    print('\n')
    print("2. Идентификатор пользователя, на сообщения которого больше всего отвечали:", most_replied_user_id(chat_messages))
    print('\n')
    print("3. Идентификатор пользователей, сообщения которых видело больше всего уникальных пользователей:", most_active_user_id(chat_messages))
    print('\n')
    print("4. В чате больше всего сообщений:", most_active_user_id(chat_messages))
    print('\n')
    print("5. Идентификатор сообщения, которое стало началом для самого длинного треда", most_active_user_id(chat_messages))
