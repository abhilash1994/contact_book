# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from models import Contact
from django.test import TestCase

# Create your tests here.

class ContactTestCase(TestCase):

    def test_contact(self):
        self.contact = Contact.objects.create(
            name="Abhilash",
            email="abhilash.gis@gmail.com",
            phone_number="9872389283490328990"
        )
        try:
            self.contact.full_clean()
            raise AssertionError(
                'Ensure this value has at most 15 characters (it has 19).'
            )
        except ValidationError as e:
            pass

    def test_contact_required_fields(self):
        try:
            self.contact = Contact.objects.create(
                name="Abhilash",
                phone_number="98723892"
            )
            raise AssertionError('Email field is required.')
        except Exception:
            pass
