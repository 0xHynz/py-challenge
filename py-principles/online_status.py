
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}


def online_count(status):
    online = 0
    for name in status:
        if (lambda user: status[user] == "online")(name):
           online += 1

    return online

if __name__=="__main__":
   online_count(statuses)
