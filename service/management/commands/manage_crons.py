from concurrent.futures import ProcessPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import os

from service.management.crons import Cron1, Cron2

APP_ENVIRONMENT = os.getenv("APP_ENVIRONMENT", "dev")


class ManageCrons:
    def __init__(self):
        if APP_ENVIRONMENT != "local":
            self.scheduler = BackgroundScheduler()

            self.pool_cron1 = ProcessPoolExecutor(max_workers=1)
            self.pool_cron2 = ProcessPoolExecutor(max_workers=4)

            self.scheduler.add_job(
                self.submit_to_pool(self.pool_cron1, Cron1.initialize),
                CronTrigger(second="*/10"),
                id="job1",
            )
            self.scheduler.add_job(
                self.submit_to_pool(self.pool_cron2, Cron2.initialize),
                CronTrigger(second="20"),
                id="job2",
            )

            self.scheduler.start()
            print("[Scheduler] Cronjobs started with separate pools")

    def submit_to_pool(self, pool, func):
        def wrapper(*args, **kwargs):
            pool.submit(func, *args, **kwargs)
        return wrapper

    def shutdown(self):
        print("[Scheduler] Shutting down...")
        self.scheduler.shutdown(wait=False)
        self.pool_cron1.shutdown(wait=False, cancel_futures=True)
        self.pool_cron2.shutdown(wait=False, cancel_futures=True)
