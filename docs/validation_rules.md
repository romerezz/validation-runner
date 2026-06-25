# Validation Rules

## Statuses

PENDING
RUNNING
PASSED
FAILED
CANCELLED

## Valid Transitions

PENDING -> RUNNING
PENDING -> CANCELLED

RUNNING -> PASSED
RUNNING -> FAILED

## Final States

PASSED
FAILED
CANCELLED

## Missing Run Behavior

Accessing a non-existent run fails.

## Rerun Behavior

Runs in final states cannot be executed again.

## Allowed Test Types

smoke
regression
negative