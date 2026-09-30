# G-UNIT / ATLAS
# Change Control

Version 1.0
Status AUTHORITATIVE
Related Blueprint: docs/engineering/PROJECT_BLUEPRINT.md
Related Workflow: docs/engineering/DEVELOPMENT_WORKFLOW.md

---

## 1. PURPOSE

This document defines how engineering changes are controlled in G-UNIT / ATLAS.

The purpose is to keep the repository:

- understandable
- recoverable
- traceable
- testable
- architecturally consistent

Every meaningful change must have a clear reason.

---

## 2. CHANGE PRINCIPLE

A change must answer:

1. Why is this change required?
2. What capability does it provide?
3. Which architectural boundary owns it?
4. Which files are allowed to change?
5. What tests prove the change?
6. What existing behavior must remain protected?

If these questions cannot be answered, stop before implementation.

---

## 3. CHANGE TYPES

Changes normally fall into these categories:

### FEATURE

Introduces a new capability.

Example:

feat: add market data snapshot validation

### FIX

Corrects behavior that violates an existing contract.

Example:

fix: reject invalid market snapshot timestamps

### TEST

Adds or improves verification without changing production behavior.

Example:

test: add symbol validity contract

### REFACTOR

Changes internal structure without intentionally changing behavior.

Refactoring requires a clear reason and must preserve existing contracts.

### DOCUMENTATION

Changes project documentation, architecture records, workflows, or state tracking.

Example:

docs: establish engineering workflow

---

## 4. SCOPE CONTROL

Every milestone must have a defined scope.

The scope should identify:

- objective
- production files
- test files
- documentation files
- dependencies
- protected files
- expected behavior

Do not expand scope during implementation without recording why the scope changed.

---

## 5. PROTECTED WORK

Existing unrelated work must be preserved.

Protected work includes:

- unrelated Forge changes
- backup files
- unfinished experiments
- uncommitted work belonging to another milestone
- generated files that are intentionally retained
- changes whose ownership has not yet been established

Never delete or overwrite protected work merely to obtain a clean working tree.

---

## 6. FORBIDDEN RECOVERY ACTIONS

Do not use these commands as normal cleanup:

git reset --hard

git clean -fd

Do not delete backup files to make Git status look clean.

Do not force checkout over unknown local changes.

If the repository contains unexpected changes:

STOP.

Inspect first.

---

## 7. FILE OWNERSHIP

Before modifying a file, determine which architectural area owns it.

Ask:

- Which module owns this behavior?
- Is this a public API?
- Is this an internal implementation?
- Is this a test contract?
- Is this documentation?
- Is this infrastructure?
- Is another milestone already modifying it?

A file should not be changed simply because it is convenient.

---

## 8. CHANGE BOUNDARY

A milestone should normally change only the files necessary to implement its capability.

Unrelated cleanup belongs to another change.

Avoid combining:

- feature work
- large refactoring
- formatting changes
- unrelated bug fixes
- documentation restructuring

into one milestone unless there is a documented architectural reason.

---

## 9. CONTRACT PRESERVATION

Existing contracts are protected unless the milestone explicitly changes them.

Before changing a contract:

1. identify the existing behavior
2. identify consumers
3. identify existing tests
4. document the new intended behavior
5. update affected tests
6. verify regressions

Do not silently change public behavior.

---

## 10. TEST PROTECTION

Every production behavior change should have verification.

Prefer:

- focused contract tests
- deterministic tests
- public behavior tests
- regression tests

Do not weaken tests simply to make implementation pass.

If an existing test conflicts with a new requirement, determine whether:

- the requirement is wrong
- the test is outdated
- the contract genuinely changed

Then document the decision.

---

## 11. GIT REVIEW

Before every milestone commit:

git status --short
git diff --stat
git diff

Verify:

- intended files only
- no accidental deletions
- no unrelated modifications
- tests included
- documentation included where required
- protected work untouched

A clean diff is part of engineering verification.

---

## 12. COMMIT BOUNDARY

One commit should normally represent one logical engineering capability.

A commit should be:

- focused
- explainable
- testable
- recoverable

Avoid mixing unrelated milestones into one commit.

---

## 13. PUSH AND RECOVERY

After a successful commit:

git push

The remote repository provides a recovery checkpoint.

After pushing, verify:

git status --short --branch
git log -1 --oneline

Record the resulting commit in the project state documentation.

---

## 14. ARCHITECTURAL CHANGE

An architectural change requires additional review.

Examples:

- introducing a new core abstraction
- changing module boundaries
- changing dependency direction
- changing public interfaces
- changing lifecycle ownership
- changing persistence or transport architecture

Do not introduce architectural changes accidentally inside a small feature milestone.

---

## 15. WHEN A CHANGE SHOULD STOP

Stop immediately when:

- ownership is unclear
- required files are unexpectedly modified
- tests contradict the contract
- the architecture does not clearly support the proposed change
- implementation requires unrelated refactoring
- protected work may be affected
- the next milestone cannot be justified

Stopping is preferable to creating irreversible project confusion.

---

## 16. CHANGE REVIEW CHECKLIST

Before implementation:

[ ] Objective defined
[ ] Capability identified
[ ] Architectural owner identified
[ ] Scope defined
[ ] Protected files identified
[ ] Contract defined
[ ] Test defined

Before commit:

[ ] Focused tests pass
[ ] Regression tests pass
[ ] Git status reviewed
[ ] Git diff reviewed
[ ] Protected work preserved
[ ] Commit scope is focused

After commit:

[ ] Commit verified
[ ] Push completed
[ ] Remote state verified
[ ] Project state updated

---

## 17. GOLDEN RULE

Never make a change merely because the code can be changed.

Make the change because the architecture requires a clearly defined capability, the contract explains what must be true, and tests provide evidence that the behavior is correct.

---

# DOCUMENT CONTROL

Document: CHANGE_CONTROL.md
Version: 1.0
Status: AUTHORITATIVE
Owner: G-UNIT / ATLAS Engineering
Purpose: Engineering change governance

This document must be updated when the project's change-control rules materially change.
