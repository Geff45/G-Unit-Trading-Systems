import re


def validate_class_name(name: str) -> None:
    if not isinstance(name, str) or not name:
        raise ValueError("Invalid class name.")

    if not re.fullmatch(r"[A-Z][A-Za-z0-9]*", name):
        raise ValueError(
            f"Invalid class name '{name}'."
        )


def validate_module_name(name: str) -> None:
    if not isinstance(name, str) or not name:
        raise ValueError("Invalid module name.")

    if not re.fullmatch(r"[a-z_][a-z0-9_]*", name):
        raise ValueError(
            f"Invalid module name '{name}'."
        )


def to_module_name(class_name: str) -> str:
    """
    Convert a PascalCase class name to snake_case module name.

    Examples:
        TradeEngine   -> trade_engine
        TradeEngine2  -> trade_engine2
        MarketService -> market_service
        RiskEngine     -> risk_engine
    """

    validate_class_name(class_name)

    # Handle acronym boundaries:
    # HTTPServer -> http_server
    name = re.sub(
        r"([A-Z]+)([A-Z][a-z])",
        r"\1_\2",
        class_name,
    )

    # Handle normal PascalCase boundaries:
    # MarketService -> Market_Service
    name = re.sub(
        r"([a-z0-9])([A-Z])",
        r"\1_\2",
        name,
    )

    return name.lower()