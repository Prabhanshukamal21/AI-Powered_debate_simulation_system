"""
def agent_b_node(state):
    responses = [
        "Regulation could stifle philosophical progress and autonomy.",
        "AI evolves differently from biology or medicine.",
        "Ethics require open exploration, not confinement.",
        "History shows overregulation delays societal evolution."
    ]
    i = len(state["agent_b_turns"])
    response = responses[i]
    print(f"[Round {state['round']+1}] Philosopher: {response}")
    return {
        "agent_b_turns": state["agent_b_turns"] + [response],
        "transcript": state["transcript"] + [("Philosopher", response)],
        "round": state["round"] + 1
    }
"""
"""from state.schema import DebateState

def agent_b_node(state: DebateState) -> dict:
    responses = [
        "Regulation could stifle philosophical progress and autonomy.",
        "AI ethics evolve faster than regulation can adapt.",
        "Overregulation risks freezing beneficial innovation.",
        "History shows overregulation often delays societal evolution."
    ]

    b_turns = state["agent_b_turns"]
    transcript = state["transcript"]
    round_num = state["round"]

    i = len(b_turns)
    if i >= len(responses):
        response = "Philosopher has no further arguments."
    else:
        response = responses[i]

    print(f"[Round {round_num + 1}] Philosopher: {response}")

    return {
        "agent_b_turns": b_turns + [response],
        "transcript": transcript + [("Philosopher", response)],
        "round": round_num + 1
    }
"""
def agent_b_node(state):
    responses = [
        "Regulation could stifle philosophical progress and autonomy.",
        "AI evolves differently from biology or medicine.",
        "Ethics require open exploration, not confinement.",
        "History shows overregulation delays societal evolution."
    ]
    
    # Safe fallback in case previous step wiped the key
    b_turns = state.get("agent_b_turns", [])
    transcript = state.get("transcript", [])

    i = len(b_turns)
    if i >= len(responses):
        response = "Philosopher has no further arguments."
    else:
        response = responses[i]
    
    print(f"[Round {state['round'] + 1}] Philosopher: {response}")
    
    # Safely return full state with updated parts
    return {
        **state,
        "agent_b_turns": b_turns + [response],
        "transcript": transcript + [f"[Round {state['round'] + 1}] Philosopher: {response}"],
        "round": state["round"] + 1
    }
