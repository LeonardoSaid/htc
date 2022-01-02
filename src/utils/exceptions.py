class ServerException(Exception):
    """ Raises when a server fails to respond to a request """


class ProductNotFoundException(Exception):
    """ Raises when a product is not found in the database """


class InvalidProductException(Exception):
    """ Raises when there is an invalid product in the cart checkout """


class EmptyCartException(Exception):
    """ Raises when the service gets a checkout request with no products listed """
