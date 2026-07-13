class Author:
    """Represent an author who can sign contracts for books."""

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        """Return all contracts associated with this author."""
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        """Return all books associated with this author through contracts."""
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        """Create and return a new contract between this author and a book."""
        return Contract(self, book, date, royalties)

    def sign_contracts(self, book, date, royalties):
        """Alias for sign_contract to support the lab naming convention."""
        return self.sign_contract(book, date, royalties)

    def total_royalties(self):
        """Return the total royalties earned from all contracts for this author."""
        return sum(contract.royalties for contract in self.contracts())


class Book:
    """Represent a book that can have multiple authors through contracts."""

    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        """Return all contracts associated with this book."""
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        """Return all authors associated with this book through contracts."""
        return [contract.author for contract in self.contracts()]


class Contract:
    """Represent a contract between an author and a book."""

    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be an instance of Author")
        self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("Book must be an instance of Book")
        self._book = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("Date must be a string")
        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int) or isinstance(value, bool):
            raise Exception("Royalties must be an integer")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date):
        """Return all contracts that share the supplied date."""
        return [contract for contract in cls.all if contract.date == date]