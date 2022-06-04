from django.test import TestCase
from library.models import Author, Book, Contact



class TestModels(TestCase):
    def test_book_has_an_author(self):
        book = Book.objects.create(title="The man in the high castle")
        philip = Author.objects.create(first_name="Philip", last_name="K. Dick")
        juliana = Author.objects.create(first_name="Juliana", last_name="Crain")
        book.authors.set([philip.pk, juliana.pk])
        #philip.book_set.add(book)
        #juliana.book_set.add(book)
        self.assertEqual(book.authors.count(), 2)
        self.assertEqual(str(book), "The man in the high castle")
        self.assertEqual(str(philip), "Philip K. Dick")


class TestStudentContactForm(TestCase):
    def test_can_send_message(self):
        data = {
            "first_name": "Juliana",
            "last_name": " Crain",
            "message": "Would love to talk about Philip K. Dick",
        }
        response = self.client.post("/contact/", data=data)
        self.assertEqual(Contact.objects.count(), 1)