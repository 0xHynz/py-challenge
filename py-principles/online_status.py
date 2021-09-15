statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}


def online_count(status):
    return [online for online in status.values()].count('online')


if __name__ == "__main__":
    print(online_count(statuses))
