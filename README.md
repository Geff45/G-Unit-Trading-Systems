# G-Unit Trading Systems

G-Unit Trading Systems is a modular software platform under development for building, integrating, and operating advanced trading-system infrastructure.

The project combines the **Atlas platform** with the **Forge developer toolkit** to provide a structured foundation for configuration, dependency injection, services, hosting, lifecycle management, generators, CLI tooling, and future trading-system components.

> **Project status:** Foundation development
> **Current milestone:** F-222
> **Current checkpoint:** `b5aa612`

---

## Project Vision

The long-term objective is to establish a robust, modular architecture capable of supporting sophisticated trading-system components while maintaining strong separation of concerns, testability, extensibility, and controlled lifecycle management.

The platform is being developed incrementally through contract-driven milestones.

---

## Core Architecture

### Atlas

Atlas is the application/platform foundation.

Its responsibilities include:

* Configuration
* Dependency Injection
* Service management
* Hosting
* Application lifecycle
* Service scopes
* Hosted services
* Future platform modules

### Forge

Forge is the development and project-generation toolkit.

Its responsibilities include:

* Command-line tooling
* Command routing
* Command registration
* Command dispatch
* Project generation
* Plugin generation
* Scaffolding
* Templates
* Developer diagnostics

---

## Current Foundation

The current implementation has completed the following contracts:

| Milestone | Component                  | Status     |
| --------- | -------------------------- | ---------- |
| F-212     | Configuration Foundation   | ✅ Complete |
| F-213     | DI Foundation              | ✅ Complete |
| F-214     | Service Contracts          | ✅ Complete |
| F-215     | Service Registry           | ✅ Complete |
| F-216     | Service Resolution         | ✅ Complete |
| F-217     | Factory Registration       | ✅ Complete |
| F-218     | Service Scope              | ✅ Complete |
| F-219     | Service Lifecycle          | ✅ Complete |
| F-220     | Host DI                    | ✅ Complete |
| F-221     | Hosted Service DI          | ✅ Complete |
| F-222     | Service Provider Lifecycle | ✅ Complete |

---

## Dependency Injection

The DI foundation supports:

* Service registration
* Service descriptors
* Singleton lifetime
* Scoped lifetime
* Transient lifetime
* Factory registration
* Constructor dependency resolution
* Service scopes
* Hosted-service resolution
* Provider lifecycle management
* Deterministic service cleanup

---

## Service Lifecycle

The provider and scopes support controlled cleanup of services.

Supported cleanup mechanisms include:

* Context-manager exit
* `close()`
* `dispose()`

Disposal is designed to be idempotent, and disposed providers/scopes reject further service resolution.

---

## Host Architecture

The host foundation integrates:

* Application services
* Dependency Injection
* Service providers
* Service scopes
* Hosted services
* Startup lifecycle
* Shutdown lifecycle

The architecture is designed so application components can be resolved through the same service infrastructure rather than relying exclusively on manual object construction.

---

## Forge CLI

Forge provides a command-oriented development interface.

The current foundation includes:

```text
forge/
├── cli/
├── commands/
├── framework/
├── generators/
└── tests/
```

The CLI architecture separates routing, command dispatch, commands, generators, and supporting framework infrastructure.

---

## Testing

The project uses `pytest` for automated testing.

Current verified checkpoint:

```text
Python:  3.14.6
pytest:  9.1.1

244 tests collected
244 tests passed
0 tests failed
```

Run the test suite with:

```powershell
python -m pytest -v
```

For a shorter result:

```powershell
python -m pytest -q
```

---

## Development Workflow

Development follows a contract-first approach.

### Standard workflow

```text
Architecture
    ↓
Contract
    ↓
Test
    ↓
Implementation
    ↓
Regression
    ↓
Verification
    ↓
Commit
    ↓
Documentation
```

Each significant architectural milestone should have corresponding tests and documentation.

---

## Repository Discipline

Before committing a production change:

```powershell
git status --short
git diff --check
python -m pytest -q
git diff --cached --check
```

Changes should be reviewed before being committed.

Backups may be retained during active development for rollback and recovery purposes, but should not be accidentally included in production commits.

---

## Current Checkpoint

The current foundation was committed as:

```text
b5aa612
feat: complete Forge CLI and DI foundation through F-222
```

Verification:

```text
244 passed
```

---

## Project Status

### Completed

* Forge CLI foundation
* Command routing
* Command registry
* Command dispatch
* Generators
* Scaffolding
* Configuration foundation
* Dependency Injection foundation
* Service registration
* Service resolution
* Factory registration
* Service scopes
* Service lifecycle
* Host DI
* Hosted-service DI
* Provider lifecycle

### In Development

The next development phases will extend the platform beyond the current foundation while preserving the established contract-first architecture.

Specific future milestones will be defined in `ROADMAP.md`.

---

## Documentation

| File             | Purpose                                     |
| ---------------- | ------------------------------------------- |
| `README.md`      | Project overview and developer entry point  |
| `ROADMAP.md`     | Development milestones and future direction |
| `BUILD-MANIFEST` | Verified build and milestone record         |
| `LICENSE`        | Software ownership and usage terms          |

---

## Disclaimer

G-Unit Trading Systems is a software-development project.

Completion of framework or infrastructure components does not imply that any trading strategy, financial model, execution system, or risk-management system is complete, validated, or suitable for live financial use.

---

## License

G-Unit Trading Systems is proprietary software unless otherwise expressly stated.

See `LICENSE` for the applicable terms.
