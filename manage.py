import os
import sys

class Main:
    def __init__(self):
        self.run()
        
    def setup_environment(self):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_server.settings')
        os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
        os.environ["PYTHONUNBUFFERED"] = "1"
        
    def run(self):
        self.setup_environment()
        try:
            from django.core.management import execute_from_command_line
            execute_from_command_line(sys.argv)
        except ImportError as exc:
            raise ImportError(
                "Exception while importing 'Django', please check the virtual environment and the dependencies installed."
            ) from exc

if __name__ == '__main__':
    Main()

