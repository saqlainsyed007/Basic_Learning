from django.contrib import admin
from .models import Question, Choice
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


# This is done because the choice has foreign key relation to Question.
#   (refer mopdels.py)By this mechanism we can define the choices that
#   relate to the particular question when adding the question itself.
# Each Choice is related to particular Question
class ChoiceInline(admin.TabularInline):  # or StackedInline
    model = Choice  # Name of the class to relate(that contains Foreign Key).
    extra = 2  # Number of options to display.


# Must extend model admin to make objects editable in the admin site.
class QuestionAdmin(admin.ModelAdmin):
    # fieldsets is used to divide model variables into groups.
    # 1st arguement is group_name and second is fields in the group.
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    # 'classes': ['collapse'] will make the group minimised.
    #  We can expand to add values.
    #  Only the fields used will be modifyable. Others won't appear.

    # Add the classes having ForeignKey relation to Question.
    # (Refer models.py) Eg: This allows you to add all the choices for a
    # particular question while adding a question itself. You need not add a
    # question, then add choices and relate them to some Question.
    inlines = [ChoiceInline]

    # The things that are to be displayed when viewing Question's Table in
    # admin site
    list_display = ('question_text', 'pub_date', 'was_published_recently')

# Register the Question to the admin site to edit from admin
admin.site.register(Question, QuestionAdmin)

# We can also use admin.site.register(Question) to stimulate default behavoiur
# It would contains all and only fields of question only.
# To register Choice use admin.site.register(Choice). Since this has a foreign
#   key, it will automatically make that a select drop down with all available
#   Question's.


# To add extra fields to user.
class UserInline(admin.StackedInline):
    model = UserProfile
    # (Refer models.py) User Profile contains Image and CompanyName


# Must extend UserAdmin to stimulate user like behaviour and not just a normal
# model
class UserAdministrator(UserAdmin):
    inlines = [UserInline]


# Unregister the default user behaviour
admin.site.unregister(User)
# Register custom user behavoiur
admin.site.register(User, UserAdministrator)
