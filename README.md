# G-Unit Trading Systems

G-Unit Trading Systems is a modular software platform under active development, designed to provide a structured foundation for market intelligence, trading infrastructure, risk management, and execution systems.

The project separates two major areas:

- **ATLAS** — the market intelligence and trading platform.
- **FORGE** — the developer toolkit for software development, command-line tooling, generators, and project scaffolding.

The platform is being built incrementally using contract-driven development, automated testing, modular architecture, and controlled engineering milestones.

> **Project status:** Active development
> **Current engineering focus:** Market-data contracts, validation, data-source abstractions, and source-registry behavior
> **Primary language:** Python

---

## Project Vision

The long-term objective is to develop a modular, multi-asset platform capable of integrating market data from different sources, interpreting market conditions, supporting trading decisions, managing risk, and connecting to execution venues.

The architecture is intended to support:

- Multiple asset classes and market-data providers.
- Standardized data-source and integration contracts.
- Market-state analysis and cross-market relationships.
- Market intelligence and analytical components.
- Trading and risk-management infrastructure.
- Execution adapters for supported venues.
- Testing, simulation, and backtesting capabilities.
- Modular extension without unnecessarily coupling system components.

These are architectural objectives, not a claim that every planned capability is already implemented or ready for live trading.

---

## Core Architecture

### ATLAS — Market Intelligence and Trading Platform

ATLAS is responsible for the market-facing and trading-related capabilities of the system.

Its architectural direction includes:

- Market-data integration and validation.
- Data-source abstractions and provider integration.
- Instrument and market-state models.
- Multi-asset market intelligence.
- Cross-asset analysis and relationships.
- Trading-system components.
- Risk-management infrastructure.
- Execution infrastructure and venue adapters.
- Future terminal, simulation, and backtesting capabilities.

ATLAS is designed to separate incoming data, normalized market representations, analytical logic, trading decisions, risk controls, and execution responsibilities.

### FORGE — Developer Toolkit

FORGE provides development tooling that supports the construction and maintenance of the wider platform.

Its responsibilities include:

- Command-line interface infrastructure.
- Command routing and dispatch.
- Command registration.
- Project and module generation.
- Plugin generation.
- Scaffolding and templates.
- Developer diagnostics.
- Supporting development workflows.

FORGE remains a distinct development-tooling area rather than being treated as part of ATLAS's market-intelligence or trading responsibilities.

---

## Engineering Foundation

The repository has established foundational infrastructure for modular Python applications, including work on:

- Configuration management.
- Dependency injection and service registration.
- Service descriptors and lifetimes.
- Constructor and factory-based dependency resolution.
- Service scopes and lifecycle management.
- Hosting and hosted-service integration.
- Command-line routing and dispatch.
- Generators and scaffolding.
- Automated tests and engineering documentation.

The exact implementation status of individual capabilities should be verified against the source code, tests, and current engineering records.

---

## Market Data Foundation

Market data is a major focus of the current development direction.

The architecture is intended to provide consistent contracts between data providers, integrations, and the rest of ATLAS.

Current development work includes:

- Data-source contracts.
- Source-registry behavior.
- Market-data snapshot validation.
- Symbol validity.
- Finite price and timestamp validation.
- Consistent interfaces for integrating future data providers.

The broader objective is to build a foundation that can support data from connected trading venues and external market-information sources while maintaining clear boundaries between providers and consuming components.

**Important:** A defined contract does not automatically mean that a production provider, live feed, or complete market-data pipeline is already available.

---

## Dependency Injection and Lifecycle Management

The core foundation includes work on dependency injection and controlled service lifecycles.

The design covers:

- Service registration and descriptors.
- Singleton, scoped, and transient lifetimes.
- Factory-based registration.
- Constructor dependency resolution.
- Service scopes.
- Hosted-service integration.
- Provider and scope cleanup.
- Host startup and shutdown responsibilities.

Lifecycle-related behavior is tested as part of the contract-driven development process. The precise guarantees of individual services should be confirmed against their current implementation and tests.

---

## FORGE CLI Structure

The FORGE command-line architecture separates interface concerns from command execution and generation logic.

The relevant areas include:

```text
forge/
├── cli/
├── commands/
├── framework/
├── generators/
└── tests/
```

This is an illustrative view of the FORGE structure, not a complete repository tree. The implementation may evolve as the toolkit develops.

---

## Development Workflow

Development follows a contract-first engineering approach.

```text
Architecture
    ↓
Contract
    ↓
Test
    ↓
Implementation
    ↓
Regression testing
    ↓
Verification
    ↓
Review
    ↓
Commit
    ↓
Documentation
```

Significant changes should be supported by appropriate tests and documentation. New milestones should follow an identified architectural or capability gap rather than being assigned arbitrarily.

### Local verification

Run the test suite from the repository root:

```powershell
python -m pytest -q
```

For more detailed test output:

```powershell
python -m pytest -v
```

Check the working tree before preparing a commit:

```powershell
git status --short
```

Check the diff for whitespace errors:

```powershell
git diff --check
```

These commands help verify the current working tree. A test result should be reported as verified only after the test command has actually completed.

---

## Repository Discipline

G-Unit follows a controlled development workflow intended to protect working code and maintain traceable changes.

- Review changes before committing.
- Run relevant tests after implementation changes.
- Keep architecture and milestone documentation aligned with actual progress.
- Preserve uncommitted work that has not been approved for inclusion.
- Inspect backup and recovery files before deciding whether they can be removed.
- Avoid including unrelated changes in a commit.
- Do not treat a successful test run as proof that the entire platform is production-ready.

---

## Project Status

G-Unit Trading Systems is under active development. Its architecture and implementation are being extended incrementally.

### Established foundation areas

- Core application infrastructure.
- Configuration and dependency-injection foundations.
- Service and hosting lifecycle components.
- FORGE CLI and generator infrastructure.
- Market-data contracts and validation work.
- Data-source and source-registry contracts.
- Automated testing and engineering documentation.

### Future development direction

Planned architectural areas include:

- Broader market-data provider integration.
- Instrument modeling.
- Multi-asset data processing.
- Cross-asset relationships.
- Global market-state analysis.
- Market-intelligence components.
- Trading and risk engines.
- Execution and venue adapters.
- ATLAS terminal capabilities.
- Backtesting and simulation.

These items describe the development direction; they should not be interpreted as completed features.

The authoritative architecture, project blueprint, current-state record, and milestone documentation should be consulted for detailed engineering decisions and the next approved milestone.

---

## Documentation

Important project records include:

| Document | Purpose |
|---|---|
| `README.md` | Project overview and entry point |
| `docs/architecture/ARCHITECTURE.md` | Architectural boundaries and system design |
| `docs/engineering/PROJECT_BLUEPRINT.md` | Authoritative project direction and development blueprint |
| `docs/roadmap/CURRENT_STATE.md` | Recorded engineering state |
| `docs/roadmap/MILESTONES.md` | Milestone history and development planning |
| `docs/engineering/DEVELOPMENT_WORKFLOW.md` | Development workflow |
| `docs/engineering/CHANGE_CONTROL.md` | Change-control guidance |
| `LICENSE` | Applicable software license terms |

Use the actual files in the repository as the source of truth if paths or document names change.

---

## Disclaimer

G-Unit Trading Systems is a software-development project.

The existence of market-data, trading, risk, or execution infrastructure does not establish that a trading strategy is profitable or that any component is suitable for live financial use. Data quality, execution behavior, operational reliability, security, and risk controls must be independently validated before deployment.

---

## License

See `LICENSE` for the applicable terms governing the software's use and distribution.
