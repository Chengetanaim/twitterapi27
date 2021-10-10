from django.db import models


class Tweet(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=200)
    owner = models.ForeignKey('auth.User', related_name='tweets', on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['date']


class Comment(models.Model):
    tweet = models.ForeignKey(Tweet, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='commenties', on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['date']

