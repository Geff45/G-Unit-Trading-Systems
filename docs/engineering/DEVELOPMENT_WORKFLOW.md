# G-UNIT / ATLAS
# Development Workflow

**Version:** 1.0
**Status:** AUTHORITATIVE
**Related Blueprint:** `docs/engineering/PROJECT_BLUEPRINT.md`

---

## 1. Purpose

This document defines the standard development workflow for G-UNIT / ATLAS.

Its purpose is to ensure that development remains:

- predictable
- traceable
- test-driven
- architecture-first
- milestone-controlled
- recoverable when interrupted
- protected from unrelated changes

No production capability should be implemented outside this workflow unless explicitly authorized.

---

## 2. The Development Loop

Every capability follows this sequence:

LOCATE
  |
  v
UNDERSTAND
  |
  v
DEFINE CONTRACT
  |
  v
WRITE TEST
  |
  v
RED
  |
  v
IMPLEMENT
  |
  v
FOCUSED VERIFICATION
  |
  v
REGRESSION VERIFICATION
  |
  v
GIT REVIEW
  |
  v
COMMIT
  |
  v
PUSH
  |
  v
UPDATE PROJECT STATE

The sequence is intentional.

Do not skip directly from an idea to implementation.

---

## 3. STEP 1 - LOCATE

Before changing code, identify exactly where the capability belongs.

Answer:

1. Which development stage does this belong to?
2. Which architectural layer owns it?
3. Which existing module is responsible?
4. Does the required abstraction already exist?
5. What files currently implement the relevant behavior?
6. What tests already cover the area?
7. Are there protected or unrelated changes in the working tree?

Useful commands:

git status --short --branch
git log -1 --oneline
git log --oneline -15

Then inspect the relevant directories and tests.

Do not modify anything during the locating phase.

---

## 4. STEP 2 - UNDERSTAND

Read the existing implementation and tests before designing a change.

Determine:

- current behavior
- existing contracts
- dependencies
- public APIs
- validation rules
- error semantics
- lifecycle behavior
- existing test expectations
- architectural ownership

The goal is to understand what already exists before creating anything new.

### Rule

Never create a new abstraction simply because the desired behavior is missing.

First determine whether an existing abstraction can correctly own the behavior.

---

## 5. STEP 3 - DEFINE THE ENGINEERING CONTRACT

Before implementation, define the smallest contract required for the capability.

A contract should specify:

- inputs
- outputs
- valid states
- invalid states
- validation rules
- failure behavior
- ownership
- dependencies
- public interface
- lifecycle requirements where applicable

The contract must be understandable independently of the implementation.

### Contract Principle

WHAT must be true

not

HOW the code happens to achieve it.

---

## 6. STEP 4 - WRITE THE TEST

Create the smallest test that expresses the contract.

The test should verify observable behavior rather than implementation details.

Prefer:

- public APIs
- explicit inputs
- explicit outputs
- explicit failures
- deterministic behavior

Avoid tests that depend unnecessarily on:

- private implementation details
- internal variable names
- incidental object structure
- unrelated modules

---

## 7. STEP 5 - RED

Run the new focused test before implementing the capability.

Expected result:

FAIL

This confirms that the test is actually testing something that does not yet exist.

Record the failure reason.

A RED test is a development checkpoint, not a failure of the project.

### Rule

Do not modify the test merely to make it pass.

If the contract is wrong, stop and correct the contract before implementation.

---

## 8. STEP 6 - IMPLEMENT

Implement the smallest production change required to satisfy the contract.

Rules:

1. Do not refactor unrelated code.
2. Do not redesign neighboring modules without architectural justification.
3. Do not add speculative features.
4. Do not modify protected Forge work.
5. Do not clean up unrelated files.
6. Do not introduce abstractions without an identified architectural need.

The implementation should be the minimum necessary to move the focused test from RED to GREEN.

---

## 9. STEP 7 - FOCUSED VERIFICATION

Run the specific test created for the capability.

Expected result:

PASS

If it fails:

1. inspect the failure
2. determine whether the contract or implementation is wrong
3. correct the smallest necessary issue
4. rerun the focused test

Do not immediately run the entire repository suite after every tiny change.

First establish local correctness.

---

## 10. STEP 8 - REGRESSION VERIFICATION

After the focused test passes, run the relevant existing test suite.

Then run the broader project suite when the milestone requires it.

Expected result:

ALL RELEVANT TESTS PASS

Regression testing answers:

Did this capability break something that already worked?

---

## 11. STEP 9 - GIT REVIEW

Before committing, inspect the working tree.

Run:

git status --short
git diff --stat
git diff

Confirm:

- only intended files changed
- no backup files were modified
- no unrelated Forge changes were included
- no generated junk was included
- no accidental deletions occurred
- tests are included where required

If unexpected changes appear:

STOP.

Do not commit until their ownership is understood.

---

## 12. STEP 10 - COMMIT

Create a focused commit representing one logical capability.

Preferred format:

<type>: <capability>

Examples:

feat: add market data snapshot validation
test: add market data timestamp contract
docs: establish engineering workflow
fix: reject invalid market symbols

Avoid vague commits such as:

updates
changes
work
fixes
new stuff

A commit should allow someone to understand what changed without opening every file.

---

## 13. STEP 11 - PUSH

After the commit is verified:

git push

The remote repository becomes the recoverable checkpoint.

After pushing, verify:

git status --short --branch
git log -1 --oneline

Expected state:

working tree clean
branch synchronized with remote

Protected unrelated work may intentionally remain outside the commit according to project rules.

---

## 14. STEP 12 - UPDATE PROJECT STATE

Every completed milestone must update the project navigation state.

At minimum record:

- current stage
- completed milestone
- current branch
- current commit
- tests passed
- architectural decision
- next unresolved capability
- protected/unrelated work if relevant

This prevents the project from losing its place.

---

## 15. MILESTONE WORKFLOW

A milestone follows:

ARCHITECTURAL GAP
      |
      v
CAPABILITY DEFINITION
      |
      v
ENGINEERING CONTRACT
      |
      v
TEST
      |
      v
RED
      |
      v
IMPLEMENTATION
      |
      v
GREEN
      |
      v
REGRESSION
      |
      v
GIT REVIEW
      |
      v
COMMIT
      |
      v
PUSH
      |
      v
STATE UPDATE

A milestone is not simply a number.

For example:

F-247 -> F-248

is not sufficient justification.

The next milestone must represent a real architectural capability.

---

## 16. HOW TO SELECT THE NEXT MILESTONE

Before creating a new milestone:

1. Review the current architecture.
2. Review the current stage.
3. Review completed milestones.
4. Identify the missing capability.
5. Determine which architectural boundary owns it.
6. Check whether an abstraction already exists.
7. Define the contract.
8. Only then assign the milestone identifier.

This prevents arbitrary milestone numbering.

---

## 17. WHAT TO DO WHEN LOST

If project context becomes unclear, stop coding.

Run:

git status --short --branch
git log -1 --oneline
git log --oneline -15

Then inspect:

docs/engineering/PROJECT_BLUEPRINT.md
docs/engineering/DEVELOPMENT_WORKFLOW.md
docs/roadmap/CURRENT_STATE.md
docs/roadmap/MASTER_ROADMAP.md

Answer these questions:

1. Where am I?
2. What was the last completed milestone?
3. What stage am I in?
4. What capability is currently missing?
5. What contract should be defined next?
6. Which files are protected?
7. What is the next test?

Only resume implementation after these questions are answered.
