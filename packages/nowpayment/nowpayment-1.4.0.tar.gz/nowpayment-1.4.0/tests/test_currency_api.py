import os

import pytest

from nowpayment import NowPayments


@pytest.fixture
def now_payments() -> NowPayments:
    """
    NOWPayments class fixture.
    :return: NOWPayments class.
    """
    return NowPayments(api_key=os.environ["API_KEY"])


def test_get_api_status(now_payments: NowPayments) -> None:
    """
    Test get_api_status method.
    :param now_payments: NOWPayments class.
    :return: None
    """
    assert now_payments.get_api_status()["message"] == "OK"


def test_get_available_currencies(now_payments: NowPayments) -> None:
    """
    Test get_available_currencies method.
    :param now_payments: NOWPayments class.
    :return: None
    """
    assert now_payments.currency.get_available_currencies().get("currencies", None) is not None


def test_get_available_currencies_v2(now_payments: NowPayments) -> None:
    """
    Test get_available_currencies_v2 method.
    :param now_payments: NOWPayments class.
    :return: None
    """
    assert now_payments.currency.get_available_currencies_v2().get("currencies", None) is not None


def test_get_available_checked_currencies(now_payments: NowPayments) -> None:
    """
    Test get_available_checked_currencies method.
    :param now_payments: NOWPayments class.
    :return: None
    """
    assert now_payments.currency.get_available_checked_currencies().get("selectedCurrencies", None) is not None
