# from conduit.apps import profiles
# from conduit.apps.profiles.models import Profile
import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models
from conduit.apps.core.models import TimestampedModel

role_choice=(
    ('admin','Admin'),
    ('mod','Moderator'),
    ('user','User'),
)

class UserManager(BaseUserManager):
    """
    Django requires that custom users define their own Manager class. By
    inheriting from `BaseUserManager`, we get a lot of the same code used by
    Django to create a `User`. 

    All we have to do is override the `create_user` function which we will use
    to create `User` objects.
    """

    def create_user(self, username, email,is_management,office_code, password=None,):
        """Create and return a `User` with an email, username and password."""
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')
        # user = self.model(username=username, email=self.normalize_email(email))
        user = self.model(username=username, email=self.normalize_email(email),is_management=is_management,office_code=office_code)
        user.set_password(password)
        user.is_staff = True
        user.save()
        
        return user

    def create_superuser(self,username,email, is_management,office_code, password,):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user( username,email,is_management=is_management,office_code=office_code)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin,TimestampedModel):

    username = models.CharField(db_index=True, max_length=255, unique=True)

    email = models.EmailField(db_index=True, unique=True)
    office_code=models.CharField(db_index=True,max_length=3,blank=True,null=True,unique=True)

    # When a user are create it's default active status should be "False".
    # That's why nobody can access db after create user without DB admin permission.
    # DB admin need change the active status.

    is_active = models.BooleanField(default=False)

    # The `is_staff` flag is expected by Django to determine who can and cannot
    # log into the Django admin site. For most users this flag will always be
    # false.
    is_staff = models.BooleanField(default=True)
    is_management = models.BooleanField(default=False, blank=True, null=True)
    user_role = models.CharField(choices=role_choice, max_length=5, default='user')
    # # A timestamp representing when this object was created.
    # created_at = models.DateTimeField(auto_now_add=True)

    # # A timestamp reprensenting when this object was last updated.
    # updated_at = models.DateTimeField(auto_now=True)

    # More fields required by Django when specifying a custom user model.

    # The `USERNAME_FIELD` property tells us which field we will use to log in.
    # In this case we want it to be the email field.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()

    def __str__(self):
        """
        Returns a string representation of this `User`.

        This string is used when a `User` is printed in the console.
        """
        return self.email

    @property
    def token(self):
        """
        Allows us to get a user's token by calling `user.token` instead of
        `user.generate_jwt_token().

        The `@property` decorator above makes this possible. `token` is called
        a "dynamic property".
        """
        return self._generate_jwt_token()

    def get_full_name(self):
        """
        This method is required by Django for things like handling emails.
        Typically this would be the user's first and last name. Since we do
        not store the user's real name, we return their username instead.
        """
        return self.username

    def get_short_name(self):
        """
        This method is required by Django for things like handling emails.
        Typically, this would be the user's first name. Since we do not store
        the user's real name, we return their username instead.
        """
        return self.username

    def _generate_jwt_token(self):
        """
        Generates a JSON Web Token that stores this user's ID and has an expiry
        date set to 60 days into the future.
        """
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            # 'exp': int(dt.strftime('%s'))
            'exp': dt.utcfromtimestamp(dt.timestamp())
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')