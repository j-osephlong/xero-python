# coding: utf-8

"""
    Xero AppStore API

    These endpoints are for Xero Partners to interact with the App Store Billing platform  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class SubscriptionItem(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "end_date": "datetime",
        "id": "str",
        "price": "Price",
        "product": "Product",
        "quantity": "int",
        "start_date": "datetime",
        "status": "str",
        "test_mode": "bool",
    }

    attribute_map = {
        "end_date": "endDate",
        "id": "id",
        "price": "price",
        "product": "product",
        "quantity": "quantity",
        "start_date": "startDate",
        "status": "status",
        "test_mode": "testMode",
    }

    def __init__(
        self,
        end_date=None,
        id=None,
        price=None,
        product=None,
        quantity=None,
        start_date=None,
        status=None,
        test_mode=None,
    ):  # noqa: E501
        """SubscriptionItem - a model defined in OpenAPI"""  # noqa: E501

        self._end_date = None
        self._id = None
        self._price = None
        self._product = None
        self._quantity = None
        self._start_date = None
        self._status = None
        self._test_mode = None
        self.discriminator = None

        if end_date is not None:
            self.end_date = end_date
        self.id = id
        self.price = price
        self.product = product
        if quantity is not None:
            self.quantity = quantity
        self.start_date = start_date
        self.status = status
        if test_mode is not None:
            self.test_mode = test_mode

    @property
    def end_date(self):
        """Gets the end_date of this SubscriptionItem.  # noqa: E501

        Date when the subscription to this product will end  # noqa: E501

        :return: The end_date of this SubscriptionItem.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this SubscriptionItem.

        Date when the subscription to this product will end  # noqa: E501

        :param end_date: The end_date of this SubscriptionItem.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def id(self):
        """Gets the id of this SubscriptionItem.  # noqa: E501

        The unique identifier of the subscription item.  # noqa: E501

        :return: The id of this SubscriptionItem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubscriptionItem.

        The unique identifier of the subscription item.  # noqa: E501

        :param id: The id of this SubscriptionItem.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def price(self):
        """Gets the price of this SubscriptionItem.  # noqa: E501


        :return: The price of this SubscriptionItem.  # noqa: E501
        :rtype: Price
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this SubscriptionItem.


        :param price: The price of this SubscriptionItem.  # noqa: E501
        :type: Price
        """
        if price is None:
            raise ValueError(
                "Invalid value for `price`, must not be `None`"
            )  # noqa: E501

        self._price = price

    @property
    def product(self):
        """Gets the product of this SubscriptionItem.  # noqa: E501


        :return: The product of this SubscriptionItem.  # noqa: E501
        :rtype: Product
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this SubscriptionItem.


        :param product: The product of this SubscriptionItem.  # noqa: E501
        :type: Product
        """
        if product is None:
            raise ValueError(
                "Invalid value for `product`, must not be `None`"
            )  # noqa: E501

        self._product = product

    @property
    def quantity(self):
        """Gets the quantity of this SubscriptionItem.  # noqa: E501

        The quantity of the item. For a fixed product, it is 1. For a per-seat product, it is a positive integer. For metered products, it is always null.  # noqa: E501

        :return: The quantity of this SubscriptionItem.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this SubscriptionItem.

        The quantity of the item. For a fixed product, it is 1. For a per-seat product, it is a positive integer. For metered products, it is always null.  # noqa: E501

        :param quantity: The quantity of this SubscriptionItem.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def start_date(self):
        """Gets the start_date of this SubscriptionItem.  # noqa: E501

        Date the subscription started, or will start. Note: this could be in the future for downgrades or reduced number of seats that haven't taken effect yet.   # noqa: E501

        :return: The start_date of this SubscriptionItem.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this SubscriptionItem.

        Date the subscription started, or will start. Note: this could be in the future for downgrades or reduced number of seats that haven't taken effect yet.   # noqa: E501

        :param start_date: The start_date of this SubscriptionItem.  # noqa: E501
        :type: datetime
        """
        if start_date is None:
            raise ValueError(
                "Invalid value for `start_date`, must not be `None`"
            )  # noqa: E501

        self._start_date = start_date

    @property
    def status(self):
        """Gets the status of this SubscriptionItem.  # noqa: E501

        Status of the subscription item. Available statuses are ACTIVE, CANCELED, and PENDING_ACTIVATION.   # noqa: E501

        :return: The status of this SubscriptionItem.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SubscriptionItem.

        Status of the subscription item. Available statuses are ACTIVE, CANCELED, and PENDING_ACTIVATION.   # noqa: E501

        :param status: The status of this SubscriptionItem.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError(
                "Invalid value for `status`, must not be `None`"
            )  # noqa: E501
        allowed_values = [
            "ACTIVE",
            "CANCELED",
            "PENDING_ACTIVATION",
            "None",
        ]  # noqa: E501

        if status:
            if status not in allowed_values:
                raise ValueError(
                    "Invalid value for `status` ({0}), must be one of {1}".format(  # noqa: E501
                        status, allowed_values
                    )
                )

        self._status = status

    @property
    def test_mode(self):
        """Gets the test_mode of this SubscriptionItem.  # noqa: E501

        If the subscription is a test subscription  # noqa: E501

        :return: The test_mode of this SubscriptionItem.  # noqa: E501
        :rtype: bool
        """
        return self._test_mode

    @test_mode.setter
    def test_mode(self, test_mode):
        """Sets the test_mode of this SubscriptionItem.

        If the subscription is a test subscription  # noqa: E501

        :param test_mode: The test_mode of this SubscriptionItem.  # noqa: E501
        :type: bool
        """

        self._test_mode = test_mode