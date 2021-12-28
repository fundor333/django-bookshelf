from django.test import TestCase

from djbookshelf.exceptions import ISBNNoBookFoundException
from djbookshelf.utility import get_book_from_isbn


class TestUtility(TestCase):
    def test_isbn(self):
        result = {
            "title": "Il caso di Charles Dexter Ward",
            "author": "Howard Phillips Lovecraft",
            "publication_date": "2007",
            "image": "http://books.google.com/books/content?id=sXO4PAAACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api",
        }
        self.assertEqual(result, get_book_from_isbn("9788817016308"))
        self.assertEqual(result, get_book_from_isbn("8817016306"))

        with self.assertRaises(ISBNNoBookFoundException):
            get_book_from_isbn("881701eeeee6306")
