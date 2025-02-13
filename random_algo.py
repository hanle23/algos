import random


def shuffle_fisher(items):
    for i in range(len(items) - 1, -1, -1):
        currRandom = random.randint(0, len(items) - 1)
        if currRandom == i:
            continue
        items[i], items[currRandom] = items[currRandom], items[i]
    return items


def shuffle_card(items):
    for _ in range(15):
        start = random.randint(0, int(len(items) // 4))
        end = random.randint(int(len(items) // 2), int(len(items) // 1.33))
        top = items[0: start]
        mid_stack = items[start:end]
        bottom = items[end:]
        top.extend(bottom)
        top.extend(mid_stack)
        items = top
    return items


def main():
    pass


if __name__ == "__main__":
    main()
