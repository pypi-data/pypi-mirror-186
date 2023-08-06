from typing import Any
from typing import Dict

# Maximum number of reruns for a pending resource that implements 'is_pending'.
DEFAULT_MAX_PENDING_RERUNS = 600


async def run(
    hub,
    plugin: str = "basic",
    pending_plugin: str = "default",
    max_pending_reruns: int = DEFAULT_MAX_PENDING_RERUNS,
    name: str = None,
    apply_kwargs: Dict[str, Any] = None,
):
    if apply_kwargs is None:
        apply_kwargs = {}
    apply_kwargs["name"] = name
    try:
        ret = await hub.reconcile[plugin].loop(
            pending_plugin,
            name=name,
            apply_kwargs=apply_kwargs,
            max_pending_reruns=max_pending_reruns,
        )
    finally:
        hub.idem.state.update_status(name, hub.idem.state.Status.FINISHED)

    return ret
