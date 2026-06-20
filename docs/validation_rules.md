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

All transitions not listed above are invalid.

## Final States

PASSED
FAILED
CANCELLED

## Finished Contract

Final states return True from is_finished().

PENDING and RUNNING return False.

## Missing Run Behavior

Accessing a non-existent run fails.

## Rerun Behavior

Runs in final states cannot be executed again.