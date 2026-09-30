# ATLAS Data Sources Capability Specification

**Status:** Draft for engineering review  
**Owner:** G-UNIT / ATLAS Engineering  
**Scope:** External data-source connectivity and multi-source market-data ingestion  
**Current architectural stage:** Stage 3 — Market Data Foundation  
**Baseline:** F-247 — Market Data Snapshot Symbol Validity

---

## 1. Purpose

This specification defines the capability gap created by the requirement for ATLAS to consume and manage many simultaneous external data sources while preserving the existing Market Data contracts.

ATLAS must be capable of receiving market, economic, order-flow, reference, news, and other external data without making the core architecture dependent on a single broker, platform, or provider.

The architecture must scale from a small number of sources to potentially 1,000+ configured sources without requiring one hard-coded service registration per source.

---

## 2. Requirements

ATLAS shall support:

1. Multiple external data sources operating simultaneously.
2. Multiple brokers connected simultaneously.
3. MT4 and MT5 broker integrations.
4. External APIs, feeds, files, and other user-provided sources.
5. Economic and macroeconomic sources such as FRED.
6. Financial-calendar and market-information sources.
7. External order-flow and market-microstructure sources.
8. Market-data sources for multiple asset classes.
9. Multiple sources representing the same instrument.
10. Source-specific observations retained separately before cross-source analysis.
11. Bid, ask, spread, timestamp, and other source-specific market conditions when supplied.
12. Source health, freshness, availability, and data-quality state.
13. Normalization into ATLAS canonical market observations.
14. Construction of candle, order-flow, and footprint representations where appropriate.
15. Cross-broker and cross-source comparison.
16. Cross-market and cross-asset analysis.
17. Separation of observed data from derived data and inferred analysis.
18. Future integration of additional sources through adapters rather than core architectural rewrites.

---

## 3. Product and Venue Independence

Binary/options-style trading is a generic ATLAS capability and shall not be hard-coded as a Deriv-only capability.

Deriv-specific Volatility Indices and other Deriv-specific instruments shall remain represented as venue/instrument-specific capabilities.

The architecture shall distinguish:

- instrument identity;
- instrument/product type;
- venue or broker;
- account;
- data source;
- execution adapter.

A trading strategy shall not need to contain venue-specific branches merely because the same product category may be available through different venues.

---

## 4. Current Architecture

The current Stage 3 Market Data foundation is intentionally small:

MarketDataService
    |
    v
MarketDataProvider
    |
    v
one configured provider/source
    |
    v
price / snapshot

The existing MarketDataProvider contract and MarketDataService ownership contracts are already covered by tests and must be preserved unless an explicit architectural change is approved.

The current DI container stores registrations by service type.

ServiceCollection
    _descriptors: dict[type, ServiceDescriptor]

The core DI container currently provides one registration per service type. It shall not be turned into the registry for hundreds or thousands of external data sources merely to satisfy this capability.

---


## 5. Capability Gap

The existing Market Data foundation does not yet represent:

- source identity;
- multiple simultaneous source instances;
- source capabilities;
- source lifecycle and connection state;
- source-specific market observations;
- broker-specific market conditions;
- cross-source comparison;
- source health and freshness;
- external economic, news, and alternative data;
- order-flow source integration;
- a scalable registry for many external sources.

The gap is therefore an External Data Sources and Integration capability, not a request to make MarketDataProvider itself responsible for every external system.

---


## 6. Ownership Boundary

The proposed ownership boundary is:

External Systems
        |
        v
Data Sources / Integration
        |
        v
Ingestion
        |
        v
Validation / Normalization
        |
        v
Canonical Market / External Data
        |
        +----> Market Data
        +----> Economic Data
        +----> Order Flow
        +----> Alternative Data
        |
        v
Market State / Intelligence

The Data Sources capability owns external connectivity and source-specific adaptation.

The Market Data capability owns canonical market-data contracts and market-data processing.

The Instrument Model owns canonical instrument identity and instrument metadata.

The Risk Engine owns account, exposure, margin, equity, and risk authorization.

The Execution Engine owns execution requests, routing, lifecycle, and venue interaction through adapters.

---



## 7. Source Model

A future source registry and configuration mechanism should represent each external source independently from the core DI service registry.

Conceptually, a configured source may contain:

DataSource
    identity
    source_type
    adapter
    capabilities
    configuration
    credential_reference
    connection_state
    health_state
    freshness_state
    rate_limit_state

The exact class names and interfaces are intentionally not finalized by this document. They must be established by the first concrete engineering contract and tests.

The source registry must be capable of holding many independent source instances without requiring one core DI registration per source.

---


## 8. Source Categories

ATLAS shall not force every external source through a price-specific interface.

### Market Sources

Examples include broker quotes, MT4 market data, MT5 market data, exchange feeds, reference price feeds, tick data, and candle data.

### Order-Flow Sources

Examples include bid/ask flow, trade-flow data, volume data, footprint-compatible feeds, and other market-microstructure sources.

### Economic Sources

Examples include FRED, economic calendars, and macroeconomic datasets.

### News and Alternative Sources

Examples include financial news APIs, sentiment sources, positioning data, and user-provided alternative datasets.

Each category may have different canonical contracts and capabilities.

---


## 9. Multi-Broker Requirement

ATLAS shall support multiple brokers concurrently.

The same canonical instrument may have multiple broker-specific representations.

Example:

Canonical Instrument: EURUSD

Broker A / MT4
    bid
    ask
    spread
    timestamp
    execution conditions

Broker B / MT5
    bid
    ask
    spread
    timestamp
    execution conditions

External Reference
    price
    timestamp

ATLAS shall preserve source identity instead of prematurely collapsing observations into one value.

The fact that two sources represent the same market does not imply that their quotes, contract specifications, spreads, liquidity, margin, or execution conditions are identical.

---


## 10. Cross-Broker Analysis

ATLAS shall eventually be capable of deriving cross-source observations including, where supported by available data:

- price deviation;
- bid deviation;
- ask deviation;
- spread comparison;
- spread expansion;
- quote freshness;
- timestamp divergence;
- missing or stale quotes;
- abnormal deviations;
- execution latency;
- slippage;
- rejection and failure patterns.

A difference between sources shall be treated as an observed or derived condition, not automatically labeled as broker manipulation.

Potential manipulation or feed-quality concerns shall be represented as an anomaly or investigation signal supported by measurable evidence.

---


## 11. Account and Risk Separation

Account state shall not be modeled as ordinary market data.

Account-specific information may include:

- balance;
- equity;
- free margin;
- used margin;
- leverage;
- open exposure;
- positions;
- broker-specific margin requirements;
- instrument-specific trading constraints.

The eventual decision flow is:

Market Conditions
        +
Instrument / Contract Conditions
        +
Account State
        +
Risk Rules
        |
        v
Execution Eligibility
        |
        v
Execution Request

The Market Data layer shall not decide whether a trade is safe or authorized.

---


## 12. Canonical Data Pipeline

The target data pipeline is:

External Sources
      |
      v
Source Adapters
      |
      v
Raw / Source-Native Data
      |
      v
Validation
      |
      v
Normalization
      |
      v
Canonical Observations
      |
      +------------------+
      |                  |
      v                  v
Market Data       Economic / Other Data
      |
      +---------+--------+
      |         |
      v         v
Candles     Order Flow
                    |
                    v
                 Footprint
                    |
                    v
          Market Microstructure
                    |
                    v
          Cross-Market Analysis
                    |
                    v
           Global Market State
                    |
                    v
             ATLAS Intelligence

The pipeline must preserve the distinction between source-native observations and ATLAS-derived representations.

---


## 13. Observed, Derived, and Inferred Data

ATLAS shall distinguish three levels of information.

### Observed

Data directly received from an external source, such as a broker bid/ask quote, tick, candle, order-flow record, or economic release.

### Derived

Data computed from observations, such as spread, delta, cumulative delta, imbalance, footprint aggregation, volatility, or cross-source deviation.

### Inferred

Higher-level analytical conclusions, such as a possible market regime, directional bias, absorption interpretation, or anomaly interpretation.

A derived or inferred value must not be represented internally as if it were directly observed data.

Where possible, derived and inferred data should retain references to the observations and processing steps from which they were produced.

---


## 14. Order-Flow and Footprint Requirements

Python shall be used for market-data processing and computational transformations where appropriate.

ATLAS shall eventually support construction of candle-level and order-flow or footprint representations from available source data.

Potential derived structures include:

OrderFlow
    buy_volume
    sell_volume
    delta
    cumulative_delta
    imbalance
    absorption_estimate

Footprint
    instrument
    timeframe
    price_levels
        price
        buy_volume
        sell_volume
        delta
        imbalance

The exact semantics depend on the quality and granularity of the source data.

ATLAS shall not claim true order-flow information when only proxy data is available.

---


## 15. Execution Architecture

Market intelligence and execution shall remain separate.

The target flow is:

Market Intelligence
        |
        v
Trading Decision
        |
        v
Risk Assessment
        |
        v
Instrument / Contract Validation
        |
        v
Execution Request
        |
        v
Venue Adapter
        |
        +----+-----+------+
        |          |      |
       MT4        MT5   Deriv

The same instrument may be observed through multiple brokers while only one, several, or none are eligible for execution according to market conditions, account state, risk controls, and execution constraints.

Strategies shall not hard-code broker-specific execution logic.

Execution venues shall be integrated through adapters so that adding a venue does not redefine the ATLAS intelligence architecture.

---


## 16. Binary and Derivative Architecture

Binary and options-style trading shall be modeled as a generic product capability rather than a Deriv-only feature.

Derivative contracts may contain characteristics such as:

- direction;
- strike or barrier where applicable;
- expiry;
- duration;
- payout structure;
- stake;
- settlement rules;
- contract size;
- venue-specific constraints.

Risk logic for such products shall not blindly reuse spot-FX position-sizing assumptions.

Deriv Volatility Indices shall be modeled as Deriv-specific instruments or markets while remaining compatible with the generic instrument and venue architecture.

---


## 17. Scalability Requirement

The source architecture shall be designed so that adding a new source normally requires:

1. source configuration;
2. an adapter implementing an established source contract;
3. source-specific validation and mapping;
4. tests;
5. registration in the source registry or configuration mechanism.

Adding a source shall not require rewriting MarketDataService, RiskEngine, TradingEngine, or core DI infrastructure unless the source exposes a genuinely new architectural capability.

The number of configured sources shall not determine the number of core application-service types in the DI container.

The architecture must remain capable of supporting hundreds or potentially 1,000+ sources through configuration, adapters, and source-instance management.

---


## 18. Security and External Boundary

External systems are untrusted boundaries.

Credentials shall not be embedded directly in source adapters or committed into the repository.

External data must pass validation before becoming trusted canonical state.

Source failures, malformed responses, stale data, authentication failures, rate limits, connection failures, and protocol errors shall be represented explicitly rather than converted into fabricated market data.

Each source should be isolated so that failure of one source does not automatically invalidate unrelated sources.

Sensitive configuration should be referenced through secure configuration or credential mechanisms rather than stored as source-code constants.

---


## 19. Compatibility with Existing Contracts

The following existing Market Data contracts are preserved by this specification:

- F-231 Market Data query semantics;
- F-232 MarketDataProvider abstraction;
- F-233 provider integration;
- F-235 explicit provider configuration;
- F-236 MarketDataSnapshot contract;
- F-241 snapshot validation;
- F-242 provider failure semantics;
- F-243 service result semantics;
- F-244 timestamp semantics;
- F-245 timestamp validity;
- F-246 price validity;
- F-247 symbol validity.

No existing contract shall be removed merely to introduce the Data Sources capability.

Any change to an existing contract requires its own documented capability gap, engineering contract, tests, implementation, regression verification, and Git checkpoint.

---


## 20. Architectural Decision

The next architectural capability shall not be implemented by expanding MarketDataProvider into a universal multi-source interface.

The preferred direction is to introduce a dedicated Data Sources and External Integration boundary that can manage multiple source instances and adapt source-native data into ATLAS canonical contracts.

The core DI container shall remain responsible for application-service dependency injection rather than becoming the registry for 1,000+ external sources.

The Data Sources capability shall therefore have its own source-instance management model while remaining integrated with the existing application architecture.

The exact first implementation boundary remains subject to contract-first testing.

---


## 21. First Engineering Slice

The first implementation slice should be the smallest capability that proves:

1. multiple source identities can coexist;
2. source-specific observations remain distinguishable;
3. a source can declare its supported capabilities;
4. source failures do not corrupt canonical state;
5. the existing Market Data contracts remain intact.

The first slice shall not attempt to integrate FRED, MT4, MT5, Deriv, order-flow providers, and hundreds of sources simultaneously.

Those integrations shall follow the established adapter and source contracts after the foundation has been verified.

The first engineering contract must be selected from the capability gap rather than created by simply incrementing F-247.

---


## 22. Milestone Governance

This document defines the capability gap and architectural direction. It does not itself create an F-248 milestone.

Before implementation begins, engineering must define:

Capability Gap
    -> Ownership Boundary
    -> Engineering Contract
    -> First Test
    -> Minimum Implementation
    -> Regression Verification
    -> Milestone ID

The next milestone identifier must be selected only after this process.

## 23. Definition of Success

The Data Sources architecture is successful when ATLAS can add and operate multiple heterogeneous sources concurrently while:

- preserving source identity;
- validating external data;
- normalizing compatible observations;
- retaining source-specific information;
- supporting cross-source comparison;
- feeding canonical market and external-data pipelines;
- supporting downstream order-flow and footprint processing;
- remaining independent of any single broker or venue;
- supporting MT4, MT5, Deriv, and future venues through adapters;
- keeping generic binary/options-style capabilities separate from Deriv-specific instruments;
- keeping risk and account state separate from market data;
- scaling source onboarding without architectural rewrites.

---

**Document status:** Draft — architectural capability defined; implementation contract not yet finalized.

