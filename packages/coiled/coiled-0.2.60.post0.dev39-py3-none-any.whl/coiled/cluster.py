import enum
import logging

import dask
from dask.distributed import Client
from distributed.deploy.adaptive import Adaptive

from .utils import COILED_LOGGER_NAME

logger = logging.getLogger(COILED_LOGGER_NAME)


@enum.unique
class CredentialsPreferred(enum.Enum):
    LOCAL = "local"
    # USER = 'user'
    ACCOUNT = "account"  # doesn't work, should be fixed or deprecated/removed someday
    NONE = None


class CoiledAdaptive(Adaptive):
    def __init__(self, cluster, **kwargs):
        super().__init__(cluster, **kwargs)
        target_duration = kwargs.get("target_duration")
        if target_duration:
            with Client(self.cluster) as client:
                client.run_on_scheduler(
                    lambda: dask.config.set(
                        {"distributed.adaptive.target-duration": target_duration}
                    )
                )

    async def scale_up(self, n):
        logger.info(f"Adaptive scaling up to {n} workers.")
        await self.cluster.scale_up(n)

    async def scale_down(self, workers):
        if not workers:
            return
        logger.info(f"Adaptive is removing {len(workers)} workers: {workers}.")
        await self.cluster.scale_down(workers)
