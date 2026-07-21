from intelligence.ai_engine import AIEngine

ai = AIEngine()

print(ai.status())

print()

print(ai.models.registry.register(
    "AtlasGPT",
    "Local",
    "1.0"
))

print(ai.models.load_model("AtlasGPT"))

print()

ai.memory.remember(
    "market",
    "Bullish"
)

print(ai.memory.recall("market"))

print()

ai.prompts.register(
    "trade",
    "Analyse {pair} on {timeframe}"
)

print(
    ai.prompts.generate(
        "trade",
        pair="EURUSD",
        timeframe="H1"
    )
)

print()

print(
    ai.reasoning.analyze(
        "Should we buy EURUSD?"
    )
)

print()

print(
    ai.inference.infer(
        "EURUSD Data"
    )
)

print()

print(
    ai.learning.train(
        "Historical EURUSD"
    )
)