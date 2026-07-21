"""
Atlas AI Engine
"""

from intelligence.memory_engine import MemoryEngine
from intelligence.prompt_engine import PromptEngine
from intelligence.reasoning_engine import ReasoningEngine
from intelligence.learning_engine import LearningEngine
from intelligence.inference_engine import InferenceEngine
from intelligence.model_manager import ModelManager


class AIEngine:

    def __init__(self):

        self.memory = MemoryEngine()
        self.prompts = PromptEngine()
        self.reasoning = ReasoningEngine()
        self.learning = LearningEngine()
        self.inference = InferenceEngine()
        self.models = ModelManager()

    def status(self):

        return {
            "engine": "Atlas AI",
            "status": "running"
        }