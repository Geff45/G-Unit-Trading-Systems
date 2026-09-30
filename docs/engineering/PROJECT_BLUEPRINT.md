# G-UNIT / ATLAS

# Engineering Blueprint

**Version:** 1.0  
**Status:** AUTHORITATIVE  
**Current Branch:** `sprint-001-gcore-foundation`  
**Current Milestone:** F-247  
**Current Stage:** Stage 3 — Market Data Foundation

---

# 1. PURPOSE

This document is the permanent engineering navigation system for G-UNIT / ATLAS.

Its purpose is to answer four questions at all times:

1. Where are we?
2. What are we building now?
3. Why are we building it?
4. What exactly comes next?

No development milestone should be started merely because the previous milestone has finished.

The next milestone must be determined from:

ARCHITECTURE
    ↓
DEVELOPMENT STAGE
    ↓
CAPABILITY GAP
    ↓
ENGINEERING CONTRACT
    ↓
MILESTONE
    ↓
TEST
    ↓
IMPLEMENTATION
    ↓
VERIFICATION
    ↓
COMMIT
    ↓
STATE UPDATE

---

# 2. PRODUCT VISION

ATLAS is a multi-asset market intelligence and trading platform.

The platform observes financial markets as an interconnected system rather than treating each instrument as an isolated chart.

The long-term platform is designed to support:

- FX
- Equities
- Indices
- Government bonds
- Corporate bonds
- Futures
- Commodities
- Options
- ETFs and funds
- Digital assets where enabled
- Future supported instruments

The intended information flow is:

GLOBAL MARKET
    ↓
MARKET STATE
    ↓
ASSET-CLASS CONTEXT
    ↓
INSTRUMENT CONTEXT
    ↓
ANALYTICS
    ↓
TRADE IDEA
    ↓
RISK
    ↓
EXECUTION

---

# 3. CORE ARCHITECTURAL PRINCIPLE

ATLAS observes the market as an interconnected system, constructs global and asset-class market state, provides instrument-level analysis, and routes validated trading decisions through risk-controlled execution venues.

This principle governs future architecture decisions.

MT4 is an execution and integration venue.

MT4 is not the architectural definition of ATLAS.

---

# 4. TARGET ARCHITECTURE

                         ATLAS
                           |
                           v
                GLOBAL MARKET DATA
                           |
                           v
                 MARKET NORMALIZATION
                           |
                           v
              CROSS-ASSET RELATIONSHIPS
                           |
                           v
                 MARKET STATE ENGINE
                           |
                           v
                  MARKET INTELLIGENCE
                           |
             +-------------+-------------+
             |             |             |
             v             v             v
        TECHNICAL      QUANTITATIVE   FUNDAMENTAL
        ANALYTICS       ANALYTICS      ANALYTICS
             +-------------+-------------+
                           |
                           v
                    SIGNAL / IDEA
                       ENGINE
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
              +------------+------------+
              |            |            |
              v            v            v
             MT4      Other Venues    Future

---

# 5. DEVELOPMENT STAGES

## Stage 1 — Core Foundation

**Status:** COMPLETE

Responsibilities:

- project foundation
- configuration
- dependency injection
- core contracts
- service architecture
- testing foundation

---

## Stage 2 — Module Foundation

**Status:** COMPLETE

Responsibilities:

- module system
- module lifecycle
- module registration
- module discovery
- module management
- Forge-generated module foundation

---

## Stage 3 — Market Data Foundation

**Status:** CURRENT

Responsibilities:

- Market Data contracts
- providers
- snapshots
- queries
- service boundaries
- validation
- result semantics
- provider failure semantics
- immutable market observations

Current checkpoint:

**F-247 — Market Data Snapshot Symbol Validity**

---

## Stage 4 — Instrument Model

**Status:** NOT STARTED

Purpose:

Move from:

symbol + price + timestamp

toward:

Instrument
    |
    +-- identity
    +-- asset class
    +-- venue
    +-- currency
    +-- contract information
    +-- trading properties
    +-- relationships

This stage establishes the universal instrument concept.

---

## Stage 5 — Multi-Asset Market Data

Responsibilities:

- FX data
- equities
- indices
- bonds
- futures
- commodities
- other supported asset classes
- normalized market observations
- provider abstraction

---

## Stage 6 — Cross-Asset Relationship Engine

Responsibilities:

- correlation
- rolling correlation
- timeframe correlation
- beta
- relative strength
- spreads
- lead/lag
- volatility relationships
- divergence
- relationship stability

Correlation is treated as a statistical observation, not automatic causation or a trading instruction.

---

## Stage 7 — Global Market State

Responsibilities:

- growth
- inflation
- rates
- liquidity
- risk appetite
- volatility
- USD regime
- yield curve
- equity regime
- credit regime
- commodity regime

These are analytical states.

They are not hard-coded trading signals.

---

## Stage 8 — Market Intelligence

Responsibilities:

- technical analysis
- quantitative analysis
- fundamental analysis
- macro analysis
- event intelligence
- news
- research
- market context

---

## Stage 9 — Trading Engine

Responsibilities:

- strategy framework
- trade ideas
- signal generation
- confirmation
- market-context consumption
- opportunity evaluation

The Trading Engine must consume market context rather than only raw price candles.

---

## Stage 10 — Risk Engine

Responsibilities:

- position risk
- exposure
- portfolio risk
- drawdown controls
- position sizing
- trade limits
- execution constraints
- risk validation

---

## Stage 11 — Execution Engine

Responsibilities:

- order lifecycle
- execution requests
- execution responses
- order state
- fills
- execution errors
- execution reporting

---

## Stage 12 — MT4 Integration

MT4 becomes an adapter and execution venue.

Responsibilities:

- MT4 connectivity
- order routing
- market data integration where appropriate
- execution synchronization
- account state synchronization

---

## Stage 13 — ATLAS Terminal

The terminal becomes the human-facing market intelligence interface.

Primary areas:

- Market Map
- Analytics
- Trading
- News
- Research
- Risk
- Portfolio
- Alerts
- AI / Quant

---

## Stage 14 — Backtesting / Simulation

Responsibilities:

- historical data
- simulation
- strategy testing
- execution simulation
- risk simulation
- performance analysis

---

## Stage 15 — Production

Responsibilities:

- deployment
- observability
- monitoring
- logging
- health checks
- security
- recovery
- operational controls

---

# 6. MILESTONE RULE

Milestones are not created simply by incrementing the number.

Incorrect:

F-247 finished
    ↓
Create F-248

Correct:

F-247 finished
    ↓
What stage are we in?
    ↓
What capability is missing?
    ↓
What architectural boundary is required?
    ↓
What contract should establish it?
    ↓
Assign milestone ID

Therefore:

> The next milestone number is assigned only after the next architectural capability has been identified.

---

# 7. EVERY MILESTONE MUST HAVE A CONTRACT

Every milestone must contain:

- Milestone ID
- Title
- Stage
- Objective
- Why it exists
- Current state
- Dependencies
- Architectural contract
- Production files allowed to change
- Test files
- Protected files
- Expected red state
- Implementation plan
- Expected green state
- Regression tests
- Git review
- Commit message
- Push requirement
- State update

---

# 8. STANDARD DEVELOPMENT WORKFLOW

Every milestone follows this sequence.

## Step 1 — LOCATE

Determine:

- current branch
- current commit
- current milestone
- current stage
- working-tree changes
- protected work

---

## Step 2 — UNDERSTAND

Before changing code:

- read existing implementation
- read existing contracts
- read relevant tests
- read architecture
- read previous milestone

Never implement from memory.

---

## Step 3 — DEFINE CONTRACT

Write down:

> What must the system guarantee?

Do not start with implementation.

---

## Step 4 — WRITE TEST

Create the contract test.

Expected initial state:

RED

The failure must demonstrate that the capability does not yet exist.

---

## Step 5 — IMPLEMENT MINIMUM CHANGE

Implement only what the contract requires.

Do not perform unrelated refactoring.

Do not clean unrelated files.

Do not modify Forge work unless the milestone explicitly requires it.

---

## Step 6 — FOCUSED TEST

Run only the new contract first.

Example:

python -m pytest tests/unit/<milestone_test>.py -v

Expected:

PASS

---

## Step 7 — REGRESSION

Run the relevant existing test group.

Then, where appropriate:

python -m pytest -q

Expected:

ALL PASS

---

## Step 8 — REVIEW DIFF

Run:

git status --short
git diff

Confirm:

- only intended files changed
- protected work remains untouched
- no backup files were modified
- no unrelated cleanup occurred

---

## Step 9 — COMMIT

Commit only the milestone work.

Example:

git add <specific files>
git commit -m "feat: establish <capability>"

---

## Step 10 — PUSH

Run:

git push

---

## Step 11 — UPDATE PROJECT STATE

Update:

- CURRENT_STATE.md
- MILESTONES.md

Record:

- completed milestone
- commit
- tests
- next stage
- next capability
- protected work

---

# 9. PROTECTED WORK RULE

The repository may contain unrelated Forge changes and backup files.

These must be treated as protected unless a future milestone explicitly claims them.

Current protected categories include:

- forge/
- *.backup_*
- forge/installers/

The engineering process must never automatically:

- git reset --hard
- git clean -fd
- delete backup files
- overwrite unrelated Forge changes
- commit unrelated working-tree changes

without explicit project authorization.

---

# 10. CURRENT MARKET DATA POSITION

The Market Data foundation has progressed through:

Provider Contract
    ↓
Provider Integration
    ↓
Concrete Provider
    ↓
Snapshot
    ↓
Snapshot Validation
    ↓
Timestamp Semantics
    ↓
Timestamp Validity
    ↓
Price Validity
    ↓
Symbol Validity

Current milestone:

F-247

Current repository checkpoint:

Branch:
sprint-001-gcore-foundation

HEAD:
0ae5d5d

Remote:
origin/sprint-001-gcore-foundation

---

# 11. HOW WE DETERMINE THE NEXT MILESTONE

After F-247:

DO NOT WRITE F-248 YET.

First perform an architecture review:

Market Data Foundation
    ↓
What capability is still missing?
    ↓
Does it belong to Market Data?
    ↓
Does it belong to Instrument Model?
    ↓
Does an existing contract already cover it?
    ↓
Is a new abstraction required?
    ↓
Define contract
    ↓
Assign milestone

This prevents artificial milestone numbers from driving architecture.

---

# 12. PROJECT NAVIGATION DOCUMENTS

The repository should contain:

docs/
|
+-- engineering/
|   +-- PROJECT_BLUEPRINT.md
|   +-- DEVELOPMENT_WORKFLOW.md
|   +-- CHANGE_CONTROL.md
|
+-- architecture/
|   +-- ARCHITECTURE.md
|
+-- roadmap/
    +-- MASTER_ROADMAP.md
    +-- MILESTONES.md
    +-- CURRENT_STATE.md

These become the project's navigation system.

---

# 13. CURRENT_STATE.md PURPOSE

This file answers:

> Where are we right now?

It should always contain:

- Branch
- HEAD
- Remote status
- Current stage
- Current milestone
- Last completed milestone
- Current architectural layer
- Completed capabilities
- Active development
- Next capability
- Protected work
- Test status
- Last commit
- Last verified date

---

# 14. MASTER ROADMAP PURPOSE

This file answers:

> Where is the entire project going?

It contains:

Stage 1  → Core
Stage 2  → Modules
Stage 3  → Market Data
Stage 4  → Instruments
Stage 5  → Multi-Asset Data
Stage 6  → Cross-Asset
Stage 7  → Market State
Stage 8  → Intelligence
Stage 9  → Trading
Stage 10 → Risk
Stage 11 → Execution
Stage 12 → MT4
Stage 13 → Terminal
Stage 14 → Backtesting
Stage 15 → Production

---

# 15. MILESTONES.md PURPOSE

This file answers:

> What has actually been built?

Each entry records:

- F-XXX
- Title
- Stage
- Objective
- Status
- Commit
- Tests
- Date

No milestone is considered complete merely because code exists.

It is complete only when:

Contract
    +
Test
    +
Implementation
    +
Regression
    +
Git Review
    +
Commit
    +
Push
    +
State Update

are complete.

---

# 16. THE "I AM LOST" PROCEDURE

If development becomes confusing, STOP coding.

Run:

git status --short --branch
git log -1 --oneline
git log --oneline -15

Then inspect:

- CURRENT_STATE.md
- MILESTONES.md
- MASTER_ROADMAP.md
- PROJECT_BLUEPRINT.md

Then determine:

WHERE AM I?
    ↓
WHAT WAS LAST COMPLETED?
    ↓
WHAT STAGE AM I IN?
    ↓
WHAT CAPABILITY IS MISSING?
    ↓
WHAT IS THE NEXT CONTRACT?

Only after those questions are answered should coding resume.

---

# 17. DEFINITION OF DONE

A milestone is CLOSED only when:

- [ ] Contract defined
- [ ] Test written
- [ ] Test initially fails for the intended reason
- [ ] Minimum implementation completed
- [ ] Focused tests pass
- [ ] Relevant regression tests pass
- [ ] Full suite passes where required
- [ ] Git diff reviewed
- [ ] Protected work confirmed untouched
- [ ] Commit created
- [ ] Commit pushed
- [ ] CURRENT_STATE updated
- [ ] MILESTONES updated
- [ ] Next capability identified

---

# 18. GOLDEN RULES

## Rule 1

Architecture before implementation.

## Rule 2

Contract before code.

## Rule 3

Test before implementation.

## Rule 4

One capability at a time.

## Rule 5

No arbitrary milestone numbers.

## Rule 6

No unrelated refactoring.

## Rule 7

Never destroy uncommitted work.

## Rule 8

Every completed milestone must be reproducible.

## Rule 9

The repository is the source of truth.

## Rule 10

When lost, stop and reconstruct state — never guess.

---

# 19. IMMEDIATE PROJECT STATUS

PROJECT:
G-UNIT / ATLAS

BRANCH:
sprint-001-gcore-foundation

HEAD:
0ae5d5d

CURRENT STAGE:
Stage 3 — Market Data Foundation

LAST COMPLETED:
F-247 — Market Data Snapshot Symbol Validity

CURRENT ACTION:
Establish permanent engineering blueprint

NEXT ACTION:
Determine the next architectural capability from the repository

DO NOT:
Invent F-248

DO NOT:
Modify unrelated Forge work

DO NOT:
Continue coding until the next contract is identified

---

# 20. DEVELOPMENT PHILOSOPHY

The project is not developed by asking:

> What file should we create next?

It is developed by asking:

> What capability does the architecture require next?

Then:

Capability
    ↓
Boundary
    ↓
Contract
    ↓
Test
    ↓
Implementation
    ↓
Verification
    ↓
Milestone
    ↓
State

This is the permanent engineering loop for G-UNIT / ATLAS.

---

# DOCUMENT CONTROL

**Document:** PROJECT_BLUEPRINT.md  
**Version:** 1.0  
**Status:** AUTHORITATIVE  
**Owner:** G-UNIT / ATLAS Engineering  
**Purpose:** Permanent project navigation and engineering governance

This document must be updated when the project's architecture, development stages, milestone process, or engineering governance materially changes.
