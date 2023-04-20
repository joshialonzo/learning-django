from pathlib import Path
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Create messages to send to several recruiters"

    def _validate_data_dir(self):
        # Home dir
        home_path = Path.home()
        # Data dir
        data_path = home_path / "data"
        if not data_path.exists():
            print("Creating data dir...")
            data_path.mkdir()
        self.data_path = data_path
    
    def _validate_job_seeker_dir(self):
        # Job seeker dir
        job_seeker_path = self.data_path / "job_seeker"
        if not job_seeker_path.exists():
            print("Creating job_seeker dir...")
            job_seeker_path.mkdir()
        self.job_seeker_path = job_seeker_path

    def _validate_messages_file(self):
        # Messages file
        messages_path = self.job_seeker_path / "messages.csv"
        if not messages_path.exists():
            print("It does not exist messages.csv file...")
        self.messages_path = messages_path

    def handle(self, *args, **options):
        self._validate_data_dir()
        self._validate_job_seeker_dir()
        self._validate_messages_file()
        
        print("File does exist:", self.messages_path)
