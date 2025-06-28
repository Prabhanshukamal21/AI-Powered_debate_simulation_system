def user_input_node(state):
    topic = input("Enter topic for debate: ")
    print(f"Starting debate between Scientist and Philosopher on: {topic}\n")
    return {"topic": topic}
