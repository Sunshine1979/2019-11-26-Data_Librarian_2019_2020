# -*- coding: utf-8 -*-

dirty_isbns = [
    " ISBN 978-1449369415 ", 
    "ISBN___978-1491946008 ",
    "ISBN 978-1593276034"]


def clean_isbn(isbn):
    isbn = isbn.replace("ISBN", "")
    isbn = isbn.replace("_", "")
    isbn = isbn.strip()
    return isbn
    

for dirty_isbn in dirty_isbns:
    cleaned_isbn = clean_isbn(dirty_isbn)
    print(cleaned_isbn)
   

"""
x = clean_isbn("Birnesaft")

def sum_numbers(number_1, number_2):
    sum_of_numbers = number_1 + number_2
    return sum_of_numbers

result = sum_numbers(3, 9)
print(result)


def sum_numbers(blub, bla):
    sum_of_numbers = blub + bla
    return sum_of_numbers

result = sum_numbers(3, 9)
print(result)
"""

