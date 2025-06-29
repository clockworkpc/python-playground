from typing import Dict

eligibilities = {"NOT_ELIGIBLE": 0, "ELIGIBLE": 1}


class Eligibility:

    def runEligibilityChecks(isActive, wasAcquired, hasRestrictions):
        """Determine eligibility based on inputs"""
        if not isActive:
            if wasAcquired:
                if hasRestrictions:
                    return eligibilities["NOT_ELIGIBLE"]
                elif not wasAcquired:
                    return eligibilities["ELIGIBLE"]
                else:
                    return eligibilities["NOT_ELIGIBLE"]
            else:
                return eligibilities["NOT_ELIGIBLE"]
        elif not hasRestrictions:
            if not wasAcquired:
                return eligibilities["ELIGIBLE"]
            elif not isActive:
                return eligibilities["NOT_ELIGIBLE"]
            else:
                return eligibilities["ELIGIBLE"]
        elif not wasAcquired:
            return eligibilities["NOT_ELIGIBLE"]
        return eligibilities["NOT_ELIGIBLE"]

    def runEligibilityChecksV2(isActive, hasRestrictions):
        """Refactored method that preserves original logic"""
        if not isActive:
            return eligibilities["NOT_ELIGIBLE"]

        if hasRestrictions:
            return eligibilities["NOT_ELIGIBLE"]

        return eligibilities["ELIGIBLE"]

    def runEligibilityChecksV3(bool: isActive, bool: hasRestrictions) -> bool:
        """Refactored method that preserves original logic
        and expresses it as simply as possible.
        It returns a boolean instead of 1 or 0, which would break downstream code, but if that accords with the larger brief, this would be overall better.
        Two separate guard clauses for easier testing and debugging"""

        if not isActive:
            return False

        if hasRestrictions:
            return False

        return True

    def runEligibilityChecksV3(bool: isActive, bool: hasRestrictions) -> Dict:
        """Refactored method that preserves original logic
        and expresses it as simply as possible.
        It returns a dictionary instead of an integer, which would break downstream code, but if that accords with the larger brief, this would be overall better.
        Two separate guard clauses for easier testing and debugging"""

        # Starting state protects against mistaken approval
        result = {"eligibility": False, "reason": None}

        if not isActive:
            result["reason"] = "not isActive"
            return result
        elif hasRestrictions:
            result["reason"] = "hasRestrictions"
            return result

        # Only if the code gets past the guard clauses
        result["reason"] = "isActive and not hasRestrictions"
        result["eligibility"] = True
        return result

    def runEligibilityChecksV3(isActive, wasAcquired, hasRestrictions):
        """Refactored method that takes wasAcquired into account"""

        if not isActive:
            return eligibilities["NOT_ELIGIBLE"]

        if wasAcquired:
            return eligibilities["ELIGIBLE"]

        if not wasAcquired:
            if hasRestrictions:
                return eligibilities["NOT_ELIGIBLE"]
            else:
                return eligibilities["ELIGIBLE"]
