from django.contrib.auth.models import User
from core.models import ExModel
from django.db import models
from core import helper
from .constants import Gender, NotificationTypes


class UserProfile(ExModel):
    """
    Model class for user profile details
    """
    GENDER = helper.prop2pair(Gender)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    receive_notifications = models.BooleanField(default=False)
    gender = models.CharField('Gender', max_length=20, default='male', choices=GENDER)
    native_location = models.TextField(default='Delhi', null=False, blank=False)
    bio = models.TextField(null=True, blank=True)
    School = models.TextField(null=True, blank=True)
    Work = models.TextField(null=True, blank=True)
    emergency_contact = models.CharField(max_length=20, null=True, blank=True)
    work_email = models.CharField(max_length=100, null=True, blank=True)
    dob = models.CharField('DOB', max_length=20, null=True, blank=True)
    preferred_language = models.CharField('Language', max_length=100, default='English')
    preferred_currency = models.CharField('Currency', max_length=100, default='Indian rupee')
    time_zone = models.CharField('Time Zone', max_length=100, default='(UTC +5:30)')
    languages = models.TextField(null=True, blank=True)
    vat_number = models.CharField(max_length=100, null=True, blank=True)
    emergency_contact = models.TextField(null=True, blank=True)
    shipping_address = models.TextField(null=True, blank=True)
    guest_profiles = models.TextField(null=True, blank=True)

    def __str__(self):
        return "%s" % self.user.email


class ResetPassword(ExModel):
    """
    Model class for forget password storing details
    """
    email = models.EmailField(null=False, blank=False)
    user = models.ForeignKey(User, related_name='reset_password', on_delete=models.CASCADE)
    expired = models.BooleanField(default=False)
    token = models.CharField(null=False, blank=False, max_length=100)

    def __str__(self):
        return "%s" % self.user.email


class AuditEntry(ExModel):
    """
    Model class for storing login details
    """
    action = models.CharField(max_length=64)
    ip = models.GenericIPAddressField(null=True)
    username = models.CharField(max_length=256, null=True)

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.action, self.username, self.ip)


class PhoneNumber(ExModel):
    """
    Model class for storing phone number details
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)


class Languages(ExModel):
    """
    Model class for storing language details
    """
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UserLanguages(ExModel):
    """
    Model class for storing user language details
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.ForeignKey(Languages, on_delete=models.CASCADE)


class VatVerification(ExModel):
    """
    Model class for storing vat verification details
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    member_state = models.CharField(max_length=100)
    vat_number = models.CharField(max_length=100)
    registration_name = models.CharField(max_length=100)
    address1 = models.TextField()
    address2 = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)


class EmergencyContact(ExModel):
    """
    Model class for storing emergency contact details
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)


class ShippingAddress(ExModel):
    """
    Model class for storing emergency contact details
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    address1 = models.TextField()
    address2 = models.TextField(null=True, blank=True)
    postal_code = models.CharField(max_length=100)


class GuestProfile(ExModel):
    """
    Model class for storing profile details
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)


class Reviews(ExModel):
    """
    Model class for storing review details
    """
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='host_reviews')
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewer_reviews')
    review_content = models.TextField()
    abuse_comment = models.BooleanField(default=False)


class Reference(ExModel):
    """
    Model class for storing review details
    """
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='host_references')
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewer_references')
    reference_content = models.TextField()
    host_approval = models.BooleanField(default=False)


class Notification(ExModel):
    """
    Model class for storing notification details
    """
    NotificationTypes = helper.prop2pair(NotificationTypes)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    notification_type = models.CharField('NotificationType', max_length=20, choices=NotificationTypes)
    email = models.BooleanField(default=True)
    push_notifications = models.BooleanField(default=True)
    text_messages = models.BooleanField(default=True)
