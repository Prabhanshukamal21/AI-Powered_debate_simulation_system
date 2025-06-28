"""# main.py
import logging
from langgraph.graph import StateGraph
from nodes.user_input_node import user_input_node
from nodes.agent_a_node import agent_a_node
from nodes.agent_b_node import agent_b_node
from nodes.memory_node import memory_node
from nodes.judge_node import judge_node
from utils.logger import setup_logger
from pathlib import Path

# Setup logger
log_file = Path("output/debate_log.txt")
setup_logger(log_file)
logger = logging.getLogger("debate")

# Global state
debate_state = {
    "topic": "",
    "round": 0,
    "agent_a_turns": [],
    "agent_b_turns": [],
    "transcript": [],
    "memory_a": "",
    "memory_b": "",
}

def build_graph():
    sg = StateGraph(dict)
    sg.add_node("UserInput", user_input_node)
    sg.add_node("AgentA", agent_a_node)
    sg.add_node("AgentB", agent_b_node)
    sg.add_node("Memory", memory_node)
    sg.add_node("Judge", judge_node)

    sg.set_entry_point("UserInput")

    for i in range(8):
        if i % 2 == 0:
            sg.add_edge("Memory" if i > 0 else "UserInput", "AgentA")
            sg.add_edge("AgentA", "Memory")
        else:
            sg.add_edge("Memory", "AgentB")
            sg.add_edge("AgentB", "Memory")

    sg.add_edge("Memory", "Judge")
    sg.set_finish_point("Judge")
    return sg.compile()

if __name__ == '__main__':
    flow = build_graph()
    logger.info("Starting Debate Simulation")
    flow.invoke(debate_state)
    logger.info("Debate Simulation Complete")"""

"""# main.py
from langgraph.graph import StateGraph
from nodes.user_input_node import user_input_node
from nodes.agent_a_node import agent_a_node
from nodes.agent_b_node import agent_b_node
from nodes.memory_node import memory_node
from nodes.judge_node import judge_node
from state.schema import DebateState
from utils.logger import setup_logger

logger = setup_logger("logs/debate.log")

def build_graph():
    sg = StateGraph(DebateState)
  # Use dict as state schema

    sg.add_node("UserInput", user_input_node)
    sg.add_node("AgentA", agent_a_node)
    sg.add_node("AgentB", agent_b_node)
    sg.add_node("Memory", memory_node)
    sg.add_node("Judge", judge_node)

    sg.set_entry_point("UserInput")

    # Explicit state control: 8 rounds (4 each)
    sg.add_edge("UserInput", "AgentA")
    sg.add_edge("AgentA", "Memory")
    sg.add_edge("Memory", "AgentB")
    sg.add_edge("AgentB", "Memory")
    sg.add_edge("Memory", "AgentA")
    sg.add_edge("AgentA", "Memory")
    sg.add_edge("Memory", "AgentB")
    sg.add_edge("AgentB", "Memory")
    sg.add_edge("Memory", "AgentA")
    sg.add_edge("AgentA", "Memory")
    sg.add_edge("Memory", "AgentB")
    sg.add_edge("AgentB", "Memory")
    sg.add_edge("Memory", "AgentA")
    sg.add_edge("AgentA", "Memory")
    sg.add_edge("Memory", "AgentB")
    sg.add_edge("AgentB", "Memory")

    sg.add_edge("Memory", "Judge")
    sg.set_finish_point("Judge")

    return sg.compile()

if __name__ == "__main__":
    flow = build_graph()
    initial_state = {
    "round": 0,
    "agent_a_turns": [],
    "agent_b_turns": [],
    "transcript": [],
    "memory_a": "",
    "memory_b": "",
    "topic": ""
}
    flow.invoke(initial_state)"""
from langgraph.graph import StateGraph, END
from nodes.agent_a_node import agent_a_node
from nodes.agent_b_node import agent_b_node
from nodes.judge_node import judge_node

# 🧠 Initial State
initial_state = {
    "round": 0,
    "agent_a_turns": [],
    "agent_b_turns": [],
    "transcript": [],
    "memory_a": "",
    "memory_b": "",
    "topic": input("Enter topic for debate: ")
}

# ✅ Conditional logic to stop after 4 rounds
def should_continue(state):
    if state["round"] >= 4:
        return "judge"
    return "agent_a"

# 🧠 Graph Setup
graph = StateGraph(dict)

# Add agent & judge nodes
graph.add_node("agent_a", agent_a_node)
graph.add_node("agent_b", agent_b_node)
graph.add_node("judge", judge_node)

# Flow logic
graph.set_entry_point("agent_a")
graph.add_edge("agent_a", "agent_b")
graph.add_conditional_edges("agent_b", should_continue)
graph.add_edge("judge", END)

# ✅ Compile and run
flow = graph.compile()
final_state = flow.invoke(initial_state)

# 🧾 Optional: Display full transcript
print("\n📜 Full Debate Transcript:")
for line in final_state["transcript"]:
    print(line)
