from typing import List

class DebateState:
    def __init__(
        self,
        round: int = 0,
        agent_a_turns: List[str] = None,
        agent_b_turns: List[str] = None,
        memory_a: str = "",
        memory_b: str = "",
        topic: str = "",
        transcript: List[str] = None,
    ):
        self.round = round
        self.agent_a_turns = agent_a_turns or []
        self.agent_b_turns = agent_b_turns or []
        self.memory_a = memory_a
        self.memory_b = memory_b
        self.topic = topic
        self.transcript = transcript or []
