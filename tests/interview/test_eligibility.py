from code.interview.eligibility import Eligibility as E

# Test cases that pass
# Current logic: if active and no restrictions,
# then it doesn't matter if acquired or not, it's eligible.


def test_eligibility_is_active_was_acquired_no_restrictions():
    isActive = True
    wasAcquired = True
    hasRestrictions = False

    result = E.runEligibilityChecks(isActive, wasAcquired, hasRestrictions)
    assert result == 1
    result2 = E.runEligibilityChecksV2(isActive, hasRestrictions)
    assert result == 1


def test_eligibility_is_active_not_acquired_no_restrictions():
    isActive = True
    wasAcquired = False
    hasRestrictions = False

    result = E.runEligibilityChecks(isActive, wasAcquired, hasRestrictions)
    assert result == 1
    result2 = E.runEligibilityChecksV2(isActive, hasRestrictions)
    assert result == 1


# Test cases that fail
# Current logic: if not active or has restrictions,
# nothing else matters: it's not eligible.


def test_eligibility_is_active_was_acquired_has_restrictions():
    isActive = True
    wasAcquired = True
    hasRestrictions = True

    result = E.runEligibilityChecks(isActive, wasAcquired, hasRestrictions)
    assert result == 0
    result2 = E.runEligibilityChecksV2(isActive, hasRestrictions)
    assert result == 0


def test_eligibility_is_active_not_acquired_has_restrictions():
    isActive = True
    wasAcquired = False
    hasRestrictions = True

    result = E.runEligibilityChecks(isActive, wasAcquired, hasRestrictions)
    assert result == 0
    result2 = E.runEligibilityChecksV2(isActive, hasRestrictions)
    assert result == 0


def test_not_active_was_acquired_has_restrictions():
    isActive = False
    wasAcquired = True
    hasRestrictions = True

    result = E.runEligibilityChecks(isActive, wasAcquired, hasRestrictions)
    assert result == 0
    result2 = E.runEligibilityChecksV2(isActive, hasRestrictions)
    assert result == 0


def test_not_active_was_acquired_no_restrictions():
    isActive = False
    wasAcquired = True
    hasRestrictions = False

    result = E.runEligibilityChecks(isActive, wasAcquired, hasRestrictions)
    assert result == 0
    result2 = E.runEligibilityChecksV2(isActive, hasRestrictions)
    assert result == 0


def test_not_active_not_acquired_has_restrictions():
    isActive = False
    wasAcquired = False
    hasRestrictions = True

    result = E.runEligibilityChecks(isActive, wasAcquired, hasRestrictions)
    assert result == 0
    result2 = E.runEligibilityChecksV2(isActive, hasRestrictions)
    assert result == 0


def test_not_active_not_acquired_no_restrictions():
    isActive = False
    wasAcquired = False
    hasRestrictions = False

    result = E.runEligibilityChecks(isActive, wasAcquired, hasRestrictions)
    assert result == 0
    result2 = E.runEligibilityChecksV2(isActive, hasRestrictions)
    assert result == 0
