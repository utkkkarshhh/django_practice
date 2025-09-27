import os
from datetime import datetime


class Cron2:
    
    @classmethod
    def initialize(cls):
        print(f"[Cronjob2] Running task in PID {os.getpid()} : Time: {datetime.now()}")
