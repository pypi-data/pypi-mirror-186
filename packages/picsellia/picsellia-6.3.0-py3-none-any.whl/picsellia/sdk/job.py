import logging
import warnings
from time import sleep
from typing import List, Union

from beartype import beartype
from beartype.roar import BeartypeDecorHintPep585DeprecationWarning

from picsellia.decorators import exception_handler
from picsellia.exceptions import WaitingAttemptsTimeout
from picsellia.sdk.connexion import Connexion
from picsellia.sdk.dao import Dao
from picsellia.types.enums import JobStatus
from picsellia.types.schemas import JobSchema

logger = logging.getLogger("picsellia")
warnings.filterwarnings("ignore", category=BeartypeDecorHintPep585DeprecationWarning)


class Job(Dao):
    def __init__(self, connexion: Connexion, data: dict) -> None:
        Dao.__init__(self, connexion, data)

    @property
    def status(self) -> JobStatus:
        """Status of this (Job)"""
        return self._status

    def __str__(self):
        return "Job {} is currently in state {}"

    @exception_handler
    @beartype
    def sync(self) -> dict:
        r = self.connexion.get(f"/sdk/job/{self.id}").json()
        self.refresh(r)
        return r

    @exception_handler
    @beartype
    def refresh(self, data: dict) -> JobSchema:
        schema = JobSchema(**data)
        self._status = schema.status
        return schema

    @exception_handler
    @beartype
    def wait_for_done(self, blocking_time_increment: float = 1.0, attempts: int = 20):
        return self.wait_for_status(
            [
                JobStatus.SUCCESS,
                JobStatus.FAILED,
                JobStatus.TERMINATED,
            ],
            blocking_time_increment,
            attempts,
        )

    @exception_handler
    @beartype
    def wait_for_status(
        self,
        statuses: Union[str, JobStatus, List[Union[str, JobStatus]]],
        blocking_time_increment: float = 1.0,
        attempts: int = 20,
    ) -> JobStatus:
        if isinstance(statuses, JobStatus) or isinstance(statuses, str):
            statuses = [statuses]

        waited_statuses = [JobStatus.validate(status) for status in statuses]

        attempt = 0
        while attempt < attempts:
            self.sync()
            if self.status in waited_statuses:
                break

            sleep(blocking_time_increment)
            attempt += 1

        if attempt >= attempts:
            raise WaitingAttemptsTimeout(
                "Job is still not in the status you've been waiting for, after {} attempts."
                "Please wait a few more moment, or check"
            )

        return self.status
