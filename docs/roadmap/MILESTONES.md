# G-UNIT / ATLAS
# Milestone Governance

Version 1.0
Status AUTHORITATIVE
Related Blueprint: docs/engineering/PROJECT_BLUEPRINT.md
Related Workflow: docs/engineering/DEVELOPMENT_WORKFLOW.md
Related Roadmap: docs/roadmap/MASTER_ROADMAP.md

---

## 1. PURPOSE

This document defines the milestone system used by G-UNIT / ATLAS.

A milestone represents one controlled engineering capability.

A milestone is not simply a sequential number.

The milestone system exists to provide:

- traceability
- controlled scope
- testable progress
- recoverability
- architectural alignment
- clear Git history

---

## 2. WHAT IS A MILESTONE?

A milestone is a bounded engineering unit that moves the platform from one known capability state to another.

A valid milestone must have:

- a unique identifier
- a clear title
- an architectural stage
- an objective
- a capability gap
- a defined contract
- an implementation boundary
- tests
- verification criteria
- a Git checkpoint
- a project-state update

---

## 3. MILESTONE IDENTIFIERS

Milestone identifiers use the format:

F-XXX

Example:

F-247

The number provides historical traceability.

The number does not determine what should be built next.

Never create a milestone only because the previous milestone ended in a particular number.

---

## 4. MILESTONE SELECTION

Before assigning a new milestone identifier:

1. inspect the current state
2. inspect the architecture
3. inspect completed milestones
4. identify the remaining capability gap
5. identify the architectural owner
6. review existing abstractions
7. define the engineering contract
8. define the test boundary
9. assign the milestone identifier

The capability comes before the number.

---

## 5. REQUIRED MILESTONE RECORD

Every milestone should record:

Milestone ID:
Title:
Stage:
Objective:
Capability Gap:
Why It Is Required:
Current State:
Dependencies:
Architectural Owner:
Contract:
Allowed Production Files:
Allowed Test Files:
Protected Files:
Expected RED State:
Implementation Plan:
Expected GREEN State:
Regression Tests:
Git Review:
Commit:
Push:
State Update:

---

## 6. MILESTONE SCOPE

A milestone should be small enough to understand as one logical engineering capability.

Avoid combining unrelated work.

For example, do not combine:

- market data validation
- execution architecture
- terminal UI
- unrelated refactoring

into one milestone.

If multiple capabilities are discovered, split them into separate milestones unless the architecture proves they are inseparable.

---

## 7. MILESTONE CONTRACT

The milestone contract defines what must be true after completion.

The contract should specify:

- valid inputs
- invalid inputs
- expected outputs
- failure behavior
- ownership
- dependencies
- public interface
- lifecycle requirements where applicable

The contract must describe observable behavior.

It must not merely describe implementation details.

---

## 8. TEST REQUIREMENT

Every behavior-changing milestone requires tests.

The normal sequence is:

CONTRACT
    |
    v
TEST
    |
    v
RED
    |
    v
IMPLEMENT
    |
    v
GREEN
    |
    v
REGRESSION

The test must fail for the intended reason before implementation.

---

## 9. PROTECTED WORK

Every milestone must explicitly identify protected work.

Protected work may include:

- unrelated Forge changes
- backup files
- unfinished experiments
- other milestone work
- generated files intentionally retained
- uncommitted changes whose ownership is unknown

Protected work must not be modified simply to simplify the current milestone.

---

## 10. FILE BOUNDARY

Before implementation, identify the expected files.

Production files should be limited to what the capability requires.

Test files should verify the capability.

Documentation files should be changed only when the milestone requires a state or architectural update.

Unexpected file changes require investigation before commit.

---

## 11. EXPECTED RED STATE

Before implementation, the milestone test should normally fail.

The failure must demonstrate that the required capability does not yet exist.

Record:

- test name
- failure reason
- missing behavior

Do not modify the test simply to obtain a passing result.

---

## 12. IMPLEMENTATION RULE

Implementation must be the smallest production change that satisfies the contract.

Do not use the milestone as an opportunity for unrelated cleanup.

Avoid:

- speculative abstractions
- unrelated refactoring
- broad rewrites
- changes to protected work
- unnecessary dependency changes

---

## 13. EXPECTED GREEN STATE

After implementation:

- focused tests pass
- the milestone contract is satisfied
- existing behavior remains protected

A passing test alone does not prove milestone completion.

The implementation must also remain consistent with the architecture.

---

## 14. REGRESSION REQUIREMENT

After focused verification, run the relevant regression suite.

The purpose is to determine whether the new capability affected existing behavior.

A milestone cannot be considered complete if required regression tests remain failing without a documented reason.

---

## 15. GIT CHECKPOINT

Before committing:

git status --short
git diff --stat
git diff

Confirm that:

- only intended files changed
- protected work remains untouched
- tests are included
- no accidental deletions occurred
- no unrelated changes are included

Then create a focused commit.

---

## 16. PUSH REQUIREMENT

After the commit:

git push

Then verify:

git status --short --branch
git log -1 --oneline

The remote repository should contain the completed milestone checkpoint.

---

## 17. STATE UPDATE

Every completed milestone must update project state.

The state record should identify:

- current stage
- completed milestone
- current branch
- current commit
- tests passed
- architectural decisions
- remaining capability gap
- protected work
- next unresolved capability

This makes the repository recoverable even after a long break.

---

## 18. MILESTONE COMPLETION

A milestone is complete only when all required conditions are satisfied:

[ ] Capability identified
[ ] Architectural owner identified
[ ] Contract defined
[ ] Test written
[ ] RED verified
[ ] Implementation completed
[ ] Focused tests pass
[ ] Regression tests pass
[ ] Git diff reviewed
[ ] Commit created
[ ] Push completed
[ ] Project state updated

If any required item is incomplete, the milestone remains open.

---

## 19. CURRENT KNOWN MILESTONE

The current known checkpoint is:

F-247 - Market Data Snapshot Symbol Validity

Stage:

Stage 3 - Market Data Foundation

The next milestone must not be assumed.

The next capability must be determined from the current Market Data architecture and remaining capability gaps.

---

## 20. WHEN A MILESTONE MUST STOP

Stop milestone work when:

- the architectural owner is unclear
- the contract is unclear
- protected work may be affected
- unexpected files change
- the implementation requires unrelated refactoring
- tests reveal an architectural conflict
- the milestone scope becomes too large
- the next step requires an undocumented architectural decision

When stopped, record the reason before continuing.

---

## 21. MILESTONE HISTORY

Historical milestone records should remain traceable through:

- Git commits
- Git tags where appropriate
- test files
- project state documentation
- milestone documentation

Do not rewrite historical milestone meaning merely to simplify current navigation.

---

## 22. MILESTONE GOLDEN RULE

A milestone exists to prove one meaningful engineering capability.

The correct question is not:

"What number comes next?"

The correct question is:

"What capability is missing, where does it belong, and what evidence will prove that it works?"

---

# DOCUMENT CONTROL

Document: MILESTONES.md
Version: 1.0
Status: AUTHORITATIVE
Owner: G-UNIT / ATLAS Engineering
Purpose: Milestone definition and governance

This document must be updated when the project's milestone rules materially change.
