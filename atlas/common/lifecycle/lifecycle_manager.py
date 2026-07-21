"""
Atlas AI Operating System
=========================

Lifecycle Manager

Responsible for controlling every Atlas service lifecycle.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Tuple

from common.lifecycle.lifecycle_state import LifecycleState
from common.lifecycle.lifecycle_validator import is_valid_transition


class LifecycleManager:

    def __init__(self):

        self._state = LifecycleState.CREATED

        self._history: List[
            Tuple[datetime, LifecycleState]
        ] = [
            (datetime.utcnow(), self._state)
        ]

    # ----------------------------------
    # Properties
    # ----------------------------------

    @property
    def state(self) -> LifecycleState:
        return self._state

    @property
    def history(self):

        return list(self._history)

    # ----------------------------------
    # Transition
    # ----------------------------------

    def transition_to(
        self,
        new_state: LifecycleState
    ):

        if not is_valid_transition(
            self._state,
            new_state
        ):

            raise RuntimeError(

                f"Illegal transition "

                f"{self._state.name}"

                f" -> "

                f"{new_state.name}"
            )

        self._state = new_state

        self._history.append(

            (
                datetime.utcnow(),

                new_state
            )
        )

    # ----------------------------------

    def current(self):

        return self._state

    # ----------------------------------

    def previous(self):

        if len(self._history) < 2:
            return None

        return self._history[-2][1]

    # ----------------------------------

    def reset(self):

        self._state = LifecycleState.CREATED

        self._history.clear()

        self._history.append(

            (
                datetime.utcnow(),

                self._state
            )
        )