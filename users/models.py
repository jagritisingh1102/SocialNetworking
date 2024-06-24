from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    friends = models.ManyToManyField('self', symmetrical=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class FriendRequest(models.Model):
    from_user = models.ForeignKey(
        CustomUser, related_name='sent_requests', on_delete=models.CASCADE
    )
    to_user = models.ForeignKey(
        CustomUser, related_name='received_requests', on_delete=models.CASCADE
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['from_user', 'to_user'], name='unique_friend_request'
            )
        ]

    def __str__(self):
        return f"{self.from_user} -> {self.to_user}"
