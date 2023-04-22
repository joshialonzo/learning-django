from workers.models.worker import Worker


class Recruiter(Worker):

    class Meta:
        ordering = ["first_name", "last_name"]
        verbose_name_plural = "recruiters"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
