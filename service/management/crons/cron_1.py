import os
from datetime import datetime


class Cron1:
    
    @classmethod
    def initialize(cls):
        print(f"[Cronjob1] Running task in PID {os.getpid()} : Time: {datetime.now()}")
