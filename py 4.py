def monkey_banana():
    states = [
        "Monkey at Door, Box at Window, Monkey Hungry",
        "Monkey at Window, Box at Window, Monkey Hungry",
        "Monkey on Box, Box at Window, Monkey Hungry",
        "Monkey on Box, Box at Window, Monkey Full"
    ]
    actions = [
        "Monkey walks to Window",
        "Monkey pushes Box to Window",
        "Monkey climbs on Box",
        "Monkey grabs Bananas"
    ]
    for i in range(len(states)):
        print(f"State: {states[i]}")
        if i < len(actions):
            print(f"Action: {actions[i]}\n")

monkey_banana()
