from textwrap import shorten

def memory_node(state):
    summary_a = " ".join(s for speaker, s in state.transcript if speaker == "Scientist")
    summary_b = " ".join(s for speaker, s in state.transcript if speaker == "Philosopher")
    return {
        "memory_a": shorten(summary_b, width=200),
        "memory_b": shorten(summary_a, width=200)
    }
