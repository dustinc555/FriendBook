from django.db import models


from django.contrib.auth.models import User # friend will reference the user authentication system

##### Friend #####
# users profile
class Friend(models.Model):

    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    show_info = models.BooleanField(default=False)


    level = models.IntegerField()
    diamonds = models.IntegerField() # game currency
    energy = models.PositiveIntegerField()

    attack = models.IntegerField()
    defense = models.IntegerField()

    diamond_gen = models.IntegerField(default=1)

    profile_image = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.user.username




##### Friend_Page_Comment ############
# this comment object is for friends #
# to comment on other friends pages  #
class Friend_Page_Comment(models.Model): # Relates to Friend model

    commenter = models.ForeignKey('Friend', related_name='+', on_delete=models.CASCADE)

    comment = models.TextField(max_length=300) # Large text input, max_length will be specified
                                 # in the form file.

    commented_on = models.ForeignKey('Friend', related_name='+', on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

##### Comment_Page_Comment ##########################
# much like the Friend_Page_Comment object but this #
# specific comment is meant to be made specifically #
# to be displayed on the comment page               #
# !!!!! AKA PLAZA !!!!!
class Comment_Page_Comment(models.Model):
    commenter = models.ForeignKey('Friend', on_delete=models.CASCADE)

    comment = models.TextField(max_length=300) # Large text input, max_length will be specified
                                 # in the form file.

    def __str__(self):
        return self.comment

# Similar to a friend page comment
# this comment has a commenter: 'friend' and commented_on 'Topic'
class Topic_Page_Comment(models.Model):

    commenter = models.ForeignKey('Friend', related_name='+', on_delete=models.CASCADE)

    comment = models.TextField(max_length=500)

    commented_on = models.ForeignKey('Topic', related_name='+', on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

class Topic(models.Model):

    creator = models.ForeignKey('Friend', related_name='+', on_delete=models.CASCADE)

    title = models.TextField(max_length=100)

    def __str__(self):
        return self.title


##### Item #####
class Item(models.Model):
    item_name = models.CharField(max_length=30)
    item_image = models.ImageField(null=True, blank=True)

    attack_boost = models.IntegerField(null=True, blank=True)
    defense_boost = models.IntegerField(null=True, blank=True)
    energy_boost = models.IntegerField(null=True, blank=True)

    diamond_gen_boost = models.IntegerField(null=True, blank=True)

    cost = models.IntegerField(default=0)

    def __str__(self):
        return self.item_name


class Purchase(models.Model):
    purchaser = models.ForeignKey('Friend', on_delete=models.CASCADE)

    item_bought = models.ForeignKey('Item', on_delete=models.CASCADE)

class Attack(models.Model):
    attack_success = models.BooleanField(default=False)

    attacker = models.ForeignKey('Friend', related_name='+', on_delete=models.CASCADE)
    defender = models.ForeignKey('Friend', related_name='+', on_delete=models.CASCADE)

    diamonds_stolen = models.IntegerField()

    def __str__(self):
        return '%s attacked by: %s. Diamonds stolen=%d' % (self.defender, self.attacker, self.diamonds_stolen)
