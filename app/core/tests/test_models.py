from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def testCreateUserWithEmailSuccessful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@test.com'
        password = 'test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def testNewUserEmailNormalize(self):
        """Test the email for a new user is normalized"""
        email = 'test@TEST.com'
        password = 'test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email.lower())

    def testNewUserInvalidEmail(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def testCreateNewSuperuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@test.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)