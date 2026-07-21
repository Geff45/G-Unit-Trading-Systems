"""
Atlas World Model
=================
Stores the current understanding of the market.
"""


class WorldModel:

    def __init__(self):

        self.market_state = {}

        self.instrument_states = {}

        self.macro_state = {}

        self.sentiment_state = {}

        self.liquidity_state = {}

        self.execution_state = {}

        self.risk_state = {}

    def reset(self):

        self.market_state.clear()

        self.instrument_states.clear()

        self.macro_state.clear()

        self.sentiment_state.clear()

        self.liquidity_state.clear()

        self.execution_state.clear()

        self.risk_state.clear()