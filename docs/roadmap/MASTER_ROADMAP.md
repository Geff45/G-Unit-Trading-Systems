# G-UNIT / ATLAS
# Master Roadmap

Version 1.0
Status AUTHORITATIVE
Related Blueprint: docs/engineering/PROJECT_BLUEPRINT.md
Related Architecture: docs/architecture/ARCHITECTURE.md

---

## 1. PURPOSE

This document defines the long-term development roadmap for G-UNIT / ATLAS.

It provides the navigation path from the current engineering foundation toward the complete platform.

The roadmap describes major capabilities and development stages.

It does not replace milestone-level engineering contracts.

---

## 2. ROADMAP PRINCIPLE

The project must evolve through clearly defined capabilities.

The sequence is:

ARCHITECTURE
    |
    v
STAGE
    |
    v
CAPABILITY GAP
    |
    v
ENGINEERING CONTRACT
    |
    v
MILESTONE
    |
    v
IMPLEMENTATION
    |
    v
VERIFICATION
    |
    v
PROJECT STATE

A roadmap stage is not permission to implement everything inside that stage at once.

Each capability must still pass through the normal engineering workflow.

---

## 3. PRODUCT VISION

G-UNIT / ATLAS is intended to become a multi-asset market intelligence and trading platform capable of:

- consuming validated market data
- representing instruments across asset classes
- understanding relationships between markets
- constructing global market state
- producing structured market intelligence
- generating trading decisions
- applying risk controls
- routing approved execution requests
- integrating multiple execution venues
- supporting analysis, simulation, and operations

The platform should be modular, testable, recoverable, and extensible.

---

## 4. DEVELOPMENT STAGES

The roadmap consists of the following major stages:

1. Core Foundation
2. Module Foundation
3. Market Data Foundation
4. Instrument Model
5. Multi-Asset Market Data
6. Cross-Asset Relationship Engine
7. Global Market State
8. Market Intelligence
9. Trading Engine
10. Risk Engine
11. Execution Engine
12. MT4 Integration
13. ATLAS Terminal
14. Backtesting / Simulation
15. Production

Each stage has a distinct architectural purpose.

---

## 5. STAGE 1 - CORE FOUNDATION

Purpose:

Provide the infrastructure required for the rest of the platform.

Major capabilities include:

- configuration
- dependency injection
- service lifecycle
- application bootstrapping
- common contracts
- logging
- error handling
- testing foundations

Completion condition:

Core infrastructure can support higher-level modules without depending on trading-specific behavior.

---

## 6. STAGE 2 - MODULE FOUNDATION

Purpose:

Provide a consistent framework for ATLAS modules.

Major capabilities include:

- module identity
- module registration
- module lifecycle
- module metadata
- module discovery
- module contracts
- module integration conventions

Completion condition:

New ATLAS modules can be introduced through consistent architectural conventions.

---

## 7. STAGE 3 - MARKET DATA FOUNDATION

Purpose:

Establish trusted internal market observations.

Major capabilities include:

- market data providers
- market snapshots
- symbols
- prices
- timestamps
- validation
- provider failure handling
- service result semantics
- public market data contracts

Current known checkpoint:

F-247 - Market Data Snapshot Symbol Validity

The next capability must be selected from the remaining Market Data architectural gaps rather than by arbitrary milestone numbering.

---

## 8. STAGE 4 - INSTRUMENT MODEL

Purpose:

Create a stable domain representation of instruments.

Major capabilities may include:

- instrument identity
- asset class
- symbol identity
- venue relationships
- trading specifications
- instrument metadata
- instrument validation

The Instrument Model must remain independent from individual brokers or execution platforms.

---

## 9. STAGE 5 - MULTI-ASSET MARKET DATA

Purpose:

Expand validated market observation across supported asset classes.

Potential domains include:

- foreign exchange
- commodities
- indices
- equities
- fixed income
- cryptocurrencies

The architecture should allow additional asset classes without redesigning the core market data contracts.

---

## 10. STAGE 6 - CROSS-ASSET RELATIONSHIP ENGINE

Purpose:

Represent meaningful relationships between instruments and markets.

Major capabilities may include:

- correlation relationships
- relative strength
- inter-market relationships
- currency relationships
- commodity relationships
- index relationships
- macro-sensitive relationships

Relationships must become explicit domain concepts rather than hidden inside individual strategies.

---

## 11. STAGE 7 - GLOBAL MARKET STATE

Purpose:

Construct a coherent representation of current global market conditions.

Major capabilities may include:

- risk-on/risk-off state
- volatility state
- liquidity state
- market sessions
- cross-asset conditions
- macro-sensitive conditions
- market regime

Global Market State must consume validated upstream observations and relationships.

---

## 12. STAGE 8 - MARKET INTELLIGENCE

Purpose:

Transform market state into structured analytical information.

Major capabilities may include:

- market regime analysis
- directional bias
- structural analysis
- multi-timeframe analysis
- signal context
- market narratives
- analytical confidence

Market Intelligence must remain separate from execution.

---

## 13. STAGE 9 - TRADING ENGINE

Purpose:

Convert validated market intelligence into structured trading decisions.

Major capabilities may include:

- strategy evaluation
- setup detection
- signal generation
- trade decision construction
- strategy state
- decision metadata

Trading decisions must remain subject to downstream risk controls.

---

## 14. STAGE 10 - RISK ENGINE

Purpose:

Provide centralized risk authorization.

Major capabilities may include:

- position sizing
- exposure limits
- portfolio limits
- trade validation
- risk rules
- risk authorization
- risk state

The Trading Engine must not bypass centralized risk controls where those controls apply.

---

## 15. STAGE 11 - EXECUTION ENGINE

Purpose:

Translate approved decisions into execution requests.

Major capabilities may include:

- order construction
- execution routing
- execution state
- acknowledgements
- execution failures
- supported retry behavior
- execution lifecycle

The Execution Engine should remain independent of any one external trading platform.

---

## 16. STAGE 12 - MT4 INTEGRATION

Purpose:

Connect ATLAS to MetaTrader 4 as an external execution venue.

Major capabilities may include:

- MT4 adapter
- communication boundary
- order translation
- execution responses
- position state
- connection state
- failure handling

MT4-specific behavior must remain inside the integration boundary.

MT4 must not become a dependency of the core domain architecture.

---

## 17. STAGE 13 - ATLAS TERMINAL

Purpose:

Provide an operator-facing interface for the platform.

Major capabilities may include:

- global market state
- instrument analysis
- market intelligence
- trading decisions
- risk state
- execution state
- system health
- operational controls

The terminal should consume stable application interfaces rather than directly manipulating low-level infrastructure.

---

## 18. STAGE 14 - BACKTESTING / SIMULATION

Purpose:

Provide controlled environments for evaluating strategies and system behavior.

Major capabilities may include:

- historical market replay
- strategy simulation
- execution simulation
- risk simulation
- performance analysis
- scenario testing
- deterministic testing

Simulation should reuse production contracts where practical.

---

## 19. STAGE 15 - PRODUCTION

Purpose:

Prepare ATLAS for controlled real-world operation.

Major capabilities may include:

- deployment
- observability
- operational monitoring
- security
- configuration management
- failure recovery
- data integrity
- operational procedures
- release management

Production readiness must be demonstrated rather than assumed.

---

## 20. STAGE COMPLETION RULE

A stage is complete only when:

- required architectural capabilities exist
- public contracts are defined
- required tests pass
- dependencies are understood
- regression behavior is verified
- documentation is updated
- Git history is recoverable
- project state identifies the next capability

A stage is not complete merely because its source files exist.

---

## 21. ROADMAP CHANGE RULE

The roadmap may evolve as engineering discoveries are made.

However, changes must be justified by:

- architectural discovery
- new capability requirements
- dependency changes
- technical constraints
- production requirements

Do not add roadmap stages merely to increase milestone counts.

---

## 22. NEXT-CAPABILITY RULE

At the end of each milestone, identify the next unresolved capability.

Do not automatically create the next milestone number.

The next milestone must emerge from:

CURRENT STATE
    +
ARCHITECTURE
    +
CAPABILITY GAP
    +
ENGINEERING CONTRACT

This rule prevents milestone-driven development from replacing architecture-driven development.

---

## 23. CURRENT POSITION

Current development stage:

Stage 3 - Market Data Foundation

Current known milestone:

F-247 - Market Data Snapshot Symbol Validity

Current branch:

sprint-001-gcore-foundation

The repository remains the source of truth for implementation state.

---

## 24. ROADMAP NAVIGATION

When deciding what to build next, inspect in this order:

1. CURRENT_STATE.md
2. ARCHITECTURE.md
3. PROJECT_BLUEPRINT.md
4. DEVELOPMENT_WORKFLOW.md
5. CHANGE_CONTROL.md
6. MASTER_ROADMAP.md
7. Existing source code
8. Existing tests
9. Git history

This order prevents coding from becoming the source of architectural decisions.

---

## 25. WHEN THE PROJECT IS LOST

If project context becomes unclear:

STOP IMPLEMENTATION.

Determine:

- current branch
- current commit
- current stage
- last completed milestone
- completed capabilities
- unresolved capability
- protected work
- next architectural boundary

Then update project state before continuing.

Never guess the project's position.

---

## 26. ROADMAP GOVERNANCE

This roadmap is authoritative for long-term direction.

It does not authorize implementation by itself.

Implementation still requires:

- architectural ownership
- capability definition
- engineering contract
- tests
- milestone scope
- verification
- Git review

The roadmap answers:

WHERE ARE WE GOING?

The architecture answers:

HOW IS THE SYSTEM ORGANIZED?

The workflow answers:

HOW DO WE BUILD?

The change-control document answers:

HOW DO WE PROTECT THE SYSTEM WHILE CHANGING IT?

The current-state document answers:

WHERE ARE WE NOW?

---

# DOCUMENT CONTROL

Document: MASTER_ROADMAP.md
Version: 1.0
Status: AUTHORITATIVE
Owner: G-UNIT / ATLAS Engineering
Purpose: Long-term development navigation

This document must be updated when the project's long-term development direction materially changes.
