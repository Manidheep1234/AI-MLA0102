knowledge_base = {
    "mammal(A)": ["vertebrate(A)"],
    "vertebrate(A)": ["animal(A)"],
    "vertebrate(A),flying(A)": ["bird(A)"],
    "vertebrate('duck')": [],
    "flying('duck')": [],
    "mammal('cat')": []
}

def backward_chaining(goal):
    for rule, conclusions in knowledge_base.items():
        for conclusion in conclusions:
            if goal == conclusion:
                print(f"{goal} is derived from {rule}")
                return True
    print(f"{goal} cannot be derived from the knowledge base")
    return False

backward_chaining("animal(A)")

