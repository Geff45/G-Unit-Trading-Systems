# G-UNIT / ATLAS
# Architecture

Version 1.0
Status AUTHORITATIVE
Related Blueprint: docs/engineering/PROJECT_BLUEPRINT.md

---

## 1. PURPOSE

This document defines the architectural map of G-UNIT / ATLAS.

It describes:

- system boundaries
- major layers
- module responsibilities
- dependency direction
- architectural ownership
- development stages
- integration boundaries

This document describes WHAT the architecture is responsible for.

Detailed implementation belongs in the relevant module documentation.

---

## 2. ARCHITECTURAL VISION

ATLAS is a multi-asset market intelligence and trading platform.

Its responsibility is to:

1. observe market data
2. validate and normalize market information
3. construct instrument and asset-class state
4. identify relationships across markets
5. construct global market state
6. produce market intelligence
7. support trading decisions
8. apply risk controls
9. route approved decisions to execution venues
10. integrate external trading platforms through adapters

The architecture must remain broader than any single broker, platform, asset class, or execution venue.

MT4 is an execution/integration venue.

MT4 is not the architectural definition of ATLAS.

---

## 3. ARCHITECTURAL PRINCIPLES

### 3.1 Separation of Concerns

Each architectural layer owns a clearly defined responsibility.

A module should not perform work that belongs to another architectural boundary.

### 3.2 Dependency Direction

Dependencies should point toward stable contracts and lower-level foundations.

Higher-level intelligence should depend on defined interfaces rather than concrete external systems.

### 3.3 Contract First

Public behavior must be defined by contracts before implementation.

### 3.4 Validation First

External or uncertain data must be validated before entering trusted internal state.

### 3.5 Explicit Ownership

Every capability must have an identifiable architectural owner.

### 3.6 Testability

Core behavior must be testable without requiring live external systems.

### 3.7 Recoverability

Every milestone must leave the repository in a recoverable state.

### 3.8 No Speculative Architecture

Do not introduce abstractions merely because they might be useful later.

Architecture should evolve from identified capability requirements.

---

## 4. HIGH-LEVEL SYSTEM LAYERS

ATLAS is organized conceptually into the following layers:

EXTERNAL SYSTEMS
      |
      v
INTEGRATION / ADAPTERS
      |
      v
MARKET DATA
      |
      v
INSTRUMENT MODEL
      |
      v
MARKET STATE
      |
      v
MARKET INTELLIGENCE
      |
      v
TRADING ENGINE
      |
      v
RISK ENGINE
      |
      v
EXECUTION ENGINE
      |
      v
VENUE ADAPTERS
      |
      v
EXTERNAL EXECUTION VENUES

Cross-cutting foundations support these layers.

---

## 5. CORE FOUNDATION

The Core Foundation provides infrastructure required by the rest of the platform.

Responsibilities include:

- configuration
- dependency injection
- lifecycle management
- service registration
- logging
- errors
- common contracts
- application bootstrapping
- shared infrastructure

The Core Foundation must remain independent of trading-specific business logic.

---

## 6. MODULE FOUNDATION

The Module Foundation provides the structural conventions used by ATLAS modules.

Responsibilities include:

- module registration
- module lifecycle
- module metadata
- module boundaries
- module discovery
- shared module contracts

The Module Foundation must not become a dumping ground for business logic.

---

## 7. MARKET DATA

The Market Data layer is responsible for receiving and representing market observations.

Responsibilities include:

- providers
- snapshots
- timestamps
- symbols
- prices
- validation
- provider failures
- service results
- normalized market observations

Market Data must establish trusted internal representations before higher-level analysis consumes data.

Current development work is focused in this boundary.

---

## 8. INSTRUMENT MODEL

The Instrument Model represents tradable and observable instruments independently of a particular provider.

Responsibilities include:

- instrument identity
- asset classification
- symbol identity
- trading metadata
- venue relationships
- instrument specifications

The Instrument Model must not depend on a specific broker implementation.

---

## 9. MULTI-ASSET MARKET DATA

This layer expands market observation across asset classes.

Potential asset classes include:

- foreign exchange
- commodities
- indices
- equities
- fixed income
- cryptocurrencies
- other supported instruments

The architecture must allow new asset classes without redesigning the entire platform.

---

## 10. CROSS-ASSET RELATIONSHIP ENGINE

This layer represents relationships between instruments and markets.

Examples include:

- correlations
- relative strength
- inter-market relationships
- currency relationships
- commodity relationships
- index relationships
- macro-sensitive relationships

Relationships must be represented as explicit domain concepts rather than hidden inside individual trading strategies.

---

## 11. GLOBAL MARKET STATE

Global Market State combines validated observations and relationships into a broader representation of current market conditions.

It may eventually include:

- risk-on/risk-off state
- liquidity conditions
- volatility conditions
- session state
- cross-asset conditions
- macro-sensitive state
- market regime

Global Market State must consume validated upstream information.

---

## 12. MARKET INTELLIGENCE

Market Intelligence transforms market state into higher-level analytical information.

Responsibilities may include:

- market regime analysis
- directional bias
- structural analysis
- signal context
- multi-timeframe analysis
- market narratives
- analytical confidence

Intelligence must remain separate from execution.

---

## 13. TRADING ENGINE

The Trading Engine converts validated market intelligence into trading decisions or decision candidates.

Responsibilities may include:

- strategy evaluation
- setup detection
- signal generation
- trade decision construction
- strategy state

The Trading Engine does not own final risk authorization or venue execution.

---

## 14. RISK ENGINE

The Risk Engine evaluates whether proposed trading decisions satisfy risk constraints.

Responsibilities include:

- position sizing constraints
- exposure limits
- portfolio limits
- trade validation
- risk rules
- risk authorization

The Trading Engine must not bypass the Risk Engine when risk authorization is required.

---

## 15. EXECUTION ENGINE

The Execution Engine converts approved decisions into execution requests.

Responsibilities include:

- order construction
- execution routing
- execution state
- acknowledgements
- failures
- retries where explicitly supported
- execution lifecycle

The Execution Engine should depend on venue adapters rather than directly embedding broker-specific behavior.

---

## 16. VENUE ADAPTERS

Venue adapters translate ATLAS execution contracts into external platform-specific interfaces.

Examples may include:

- MT4 adapter
- broker adapter
- exchange adapter
- other execution venue adapters

Venue-specific behavior belongs here.

It should not leak into the core trading architecture.

---

## 17. ATLAS TERMINAL

The ATLAS Terminal is a presentation and operator interface.

It may eventually provide:

- market state
- instrument analysis
- intelligence
- trading decisions
- risk state
- execution state
- system health
- operational controls

The terminal must consume defined application interfaces rather than directly manipulating low-level infrastructure.

---

## 18. BACKTESTING AND SIMULATION

Backtesting and simulation provide controlled environments for evaluating strategies and system behavior.

They should reuse core contracts where practical.

They must not require production execution venues for ordinary testing.

---

## 19. DEPENDENCY DIRECTION

The intended dependency direction is:

PRESENTATION
     |
APPLICATION / INTELLIGENCE
     |
DOMAIN / MARKET STATE
     |
MARKET DATA / INSTRUMENTS
     |
CORE FOUNDATION

External systems should connect through explicit adapters.

The core must not depend directly on external execution platforms.

---

## 20. EXTERNAL BOUNDARIES

External systems are considered untrusted boundaries.

Examples:

- brokers
- MT4
- market data providers
- exchanges
- files
- networks
- external APIs

External data must be validated before becoming trusted internal state.

External failures must be represented explicitly.

---

## 21. DEVELOPMENT STAGES

The architectural development sequence is:

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

A later stage must not silently redefine an earlier stage.

---

## 22. CURRENT ARCHITECTURAL POSITION

Current development is in:

Stage 3 - Market Data Foundation

Current known checkpoint:

F-247 - Market Data Snapshot Symbol Validity

The next milestone must not be selected by simply incrementing the identifier.

The next capability must be determined by reviewing:

- current market data contracts
- completed tests
- existing abstractions
- architectural ownership
- remaining capability gaps

---

## 23. ARCHITECTURAL CHANGE RULE

If implementation reveals that the current architecture cannot correctly own a capability:

STOP.

Do not force the feature into the wrong module.

Instead:

1. identify the architectural conflict
2. document the conflict
3. determine the correct ownership
4. define the required architectural change
5. test the new boundary
6. implement the smallest justified change

---

## 24. ARCHITECTURAL DECISION RULE

When two designs appear possible, prefer the design that:

- preserves clear ownership
- minimizes coupling
- protects existing contracts
- remains testable
- avoids unnecessary abstraction
- keeps external systems at boundaries
- can evolve without redesigning unrelated modules

Do not choose architecture based only on short-term implementation convenience.

---

## 25. ARCHITECTURAL REVIEW CHECKLIST

Before starting a new capability:

[ ] Correct architectural layer identified
[ ] Existing abstraction reviewed
[ ] Existing contracts reviewed
[ ] Dependency direction verified
[ ] External boundaries identified
[ ] Ownership established
[ ] Protected work identified
[ ] Test boundary established
[ ] No speculative abstraction introduced

---

# DOCUMENT CONTROL

Document: ARCHITECTURE.md
Version: 1.0
Status: AUTHORITATIVE
Owner: G-UNIT / ATLAS Engineering
Purpose: Authoritative high-level architectural map

This document must be updated when the system architecture or architectural boundaries materially change.
