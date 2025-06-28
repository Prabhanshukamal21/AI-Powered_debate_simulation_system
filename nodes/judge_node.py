"""def judge_node(state):
    print("\n[Judge] Summary of Debate:")
    for speaker, text in state["transcript"]:
        print(f"{speaker}: {text}")

    score_a = sum("regulat" in t.lower() or "safety" in t.lower() for t in state["agent_a_turns"])
    score_b = sum("autonomy" in t.lower() or "evolution" in t.lower() for t in state["agent_b_turns"])

    if score_a >= score_b:
        winner = "Scientist"
        reason = "Presented more grounded, risk-based arguments aligned with public safety principles."
    else:
        winner = "Philosopher"
        reason = "Advocated for broader ethical and societal exploration without constraint."

    print(f"\n[Judge] Winner: {winner}")
    print(f"Reason: {reason}")
    return {}
"""
"""def judge_node(state):
    transcript = state["transcript"]
    agent_a_turns = state["agent_a_turns"]

    agent_b_turns = state["agent_b_turns"]

    print("\n[Judge] Summary of Debate:")
    for speaker, text in transcript:
        print(f"{speaker}: {text}")

    # Simple scoring logic
    score_a = sum("regulat" in t.lower() or "safety" in t.lower() for t in agent_a_turns)
    score_b = sum("autonomy" in t.lower() or "evolution" in t.lower() for t in agent_b_turns)

    if score_a >= score_b:
        winner = "Scientist"
        reason = "Presented more grounded, risk-based arguments aligned with public safety principles."
    else:
        winner = "Philosopher"
        reason = "Advocated for broader ethical and societal exploration without constraint."

    print(f"\n[Judge] Winner: {winner}")
    print(f"Reason: {reason}")

    return {
        "winner": winner,
        "reason": reason
    }
"""
def judge_node(state):
    agent_a_turns = state.get("agent_a_turns", [])
    agent_b_turns = state.get("agent_b_turns", [])
    transcript = state.get("transcript", [])

    summary = "[Judge] Summary of Debate:"
    
    # Simple rule: more turns → winner
    if len(agent_a_turns) >= len(agent_b_turns):
        winner = "Scientist"
        reason = "Presented more grounded, risk-based arguments aligned with public safety principles."
    else:
        winner = "Philosopher"
        reason = "Challenged assumptions and defended open-ended exploration."

    result = f"[Judge] Winner: {winner}\nReason: {reason}"

    print("\n" + summary)
    print(result)

    transcript.append(summary)
    transcript.append(result)

    return {
        **state,
        "transcript": transcript
    }
