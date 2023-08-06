from idem.reconcile.init import DEFAULT_MAX_PENDING_RERUNS


# Reconciliation loop stops after MAX_RERUNS_WO_CHANGE reruns without change for failed states.
# This is to make sure we do not retry forever on failures that cannot be fixed by
# reconciliation.
MAX_RERUNS_WO_CHANGE = 3


def is_pending(hub, ret: dict, state: str = None, **pending_kwargs) -> bool:
    """
    Default implementation of pending plugin
    Returns 'True' when the state is still 'pending' and reconciliation is required.

    If the state implements is_pending() call the state's implementation,
    otherwise state is pending until 'result' is 'True' and there are no 'changes'
    for normal flows, state is pending until 'result' is 'True' for resource recreation flow.
    Return false if the last consecutive runs produced the same result ('False') and 'changes',
    to stop reconciliation.

    :param hub: The hub
    :param ret: (dict) Returned structure of a run
    :param state: (Text, Optional) The name of the state
    :param pending_kwargs: (dict, Optional) May include 'reruns_wo_change_count' 'reruns_count' 'max_pending_reruns'
    :return: bool
    """
    # When the state implements is_pending, we should let it determine when
    # to stop the reconciliation re-runs. However we should stop after time to make
    # sure we do not reconcile forever.
    max_reruns = (
        pending_kwargs.get("max_pending_reruns", DEFAULT_MAX_PENDING_RERUNS)
        if pending_kwargs
        else DEFAULT_MAX_PENDING_RERUNS
    )

    if (
        state is not None
        and hub.states[state] is not None
        and callable(getattr(hub.states[state], "is_pending", None))
    ):
        # For safety we should limit re-runs with a very large number
        if pending_kwargs and pending_kwargs.get("reruns_count", 0) >= max_reruns:
            return False

        return hub.states[state].is_pending(ret=ret, state=state, **pending_kwargs)

    # We should not execute errors more than three times w/o changes in result
    if (
        pending_kwargs
        and pending_kwargs.get("reruns_wo_change_count", 0) >= MAX_RERUNS_WO_CHANGE
    ):
        return False

    # for resource recreation flow, we should consider only whether the result is True or not.
    if ret.get("recreation_flow", False):
        return not ret["result"] is True

    return not ret["result"] is True or bool(ret["changes"])
