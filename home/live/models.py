from django.db import models

class userlogin(models.Model):
    lid=models.IntegerField(primary_key=True)
    lname = models.CharField(max_length=42)
    email = models.EmailField()
    password = models.CharField(max_length=250)
    access=models.BooleanField()
    def __str__(self):
        return f"{self.lid}  |  {self.lname}  |  {self.email}"
class ticketprofile(models.Model):
    tid=models.IntegerField(primary_key=True)
    tname = models.CharField(max_length=42)

    def __str__(self):
        return f"{self.tid}"
class Userprofile(models.Model):
    uid=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=42)
    def __str__(self):
        return f"{self.uid}"


class Messages(models.Model):

    description = models.TextField()
    sender_name = models.ForeignKey(Userprofile, on_delete=models.CASCADE, related_name='sender')
    receiver_name = models.ForeignKey(Userprofile, on_delete=models.CASCADE, related_name='receiver')
    time = models.TimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"To: {self.receiver_name} From: {self.sender_name}"

    class Meta:
        ordering = ('timestamp',)
class openticket(models.Model):

    description = models.TextField()
    osender_name = models.ForeignKey(Userprofile, on_delete=models.CASCADE, related_name='osender')
    oreceiver_name = models.ForeignKey(Userprofile, on_delete=models.CASCADE, related_name='oreceiver')
    time = models.TimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"To: {self.oreceiver_name} From: {self.osender_name}"

    class Meta:
        ordering = ('timestamp',)
class closeticket(models.Model):

    description = models.TextField()
    csender_name = models.ForeignKey(Userprofile, on_delete=models.CASCADE, related_name='csender')
    creceiver_name = models.ForeignKey(Userprofile, on_delete=models.CASCADE, related_name='creceiver')
    time = models.TimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"To: {self.creceiver_name} From: {self.csender_name}"

    class Meta:
        ordering = ('timestamp',)