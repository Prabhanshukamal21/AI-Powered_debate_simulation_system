"""def agent_a_node(state):
    responses = [
        "AI must be regulated due to high-risk applications.",
        "Public safety must come before rapid innovation.",
        "Like medicine, AI can impact lives directly.",
        "Regulation builds trust and accountability."
    ]
    i = len(state["agent_a_turns"])
    response = responses[i]
    print(f"[Round {state['round']+1}] Scientist: {response}")
    return {
        "agent_a_turns": state["agent_a_turns"] + [response],
        "transcript": state["transcript"] + [("Scientist", response)],
        "round": state["round"] + 1
    }"""
def agent_a_node(state):
    responses = [
        "AI must be regulated due to high-risk applications.",
        "Public safety must come before rapid innovation.",
        "Like medicine, AI can impact lives directly.",
        "Regulation builds trust and accountability."
    ]

    a_turns = state["agent_a_turns"]
    transcript = state["transcript"]
    round_num = state["round"]


    i = len(a_turns)
    response = responses[i]

    print(f"[Round {round_num + 1}] Scientist: {response}")

    return {
        "agent_a_turns": a_turns + [response],
        "transcript": transcript + [("Scientist", response)],
        "round": round_num + 1
    }
