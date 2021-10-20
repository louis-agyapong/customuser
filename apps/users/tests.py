from django.test import TestCase
from django.contrib.auth import get_user_model


class UsersManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email="normal@user.com",
            username="normal",
            first_name="Normal",
            last_name="User",
            password="foo",
        )
        self.assertEqual(user.email, "normal@user.com")
        self.assertEqual(user.first_name, "Normal")
        self.assertEqual(user.last_name, "User")
        self.assertEqual(user.username, "normal")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertEqual(str(user), "normal@user.com")

        with self.assertRaises(ValueError):
            User.objects.create_user(
                email="", password="foo", username="normal", first_name="Normal", last_name="User"
            )

    def test_create_superuser(self):
        User = get_user_model()
        superuser = User.objects.create_superuser(
            email="super@user.com", username="super", first_name="Super", last_name="User", password="foo"
        )
        self.assertEqual(superuser.email, "super@user.com")
        self.assertEqual(superuser.username, "super")
        self.assertEqual(superuser.first_name, "Super")
        self.assertEqual(superuser.last_name, "User")
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
        self.assertEqual(str(superuser), "super@user.com")

        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="super@user.com",
                password="foo",
                username="super",
                first_name="Super",
                last_name="User",
                is_staff=False,
            )
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="super@user.com",
                password="foo",
                username="super",
                first_name="Super",
                last_name="User",
                is_superuser=False,
            )

        with self.assertRaises(ValueError):
            User.objects.create_user(
                email="", password="foo", username="normal", first_name="Normal", last_name="User"
            )
