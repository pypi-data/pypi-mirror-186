import os

import pytest

from nowpayment import NowPayments


@pytest.fixture
def invoice_id(iid: str) -> str:
    """
    Invoice id fixture.
    :param iid: Invoice id.
    :return: Invoice id.
    """
    return iid


@pytest.fixture
def now_payments() -> NowPayments:
    """
    NOWPayments class fixture.
    :return: NOWPayments class.
    """
    return NowPayments(api_key=os.environ["API_KEY"])


def test_get_estimated_price(now_payments: NowPayments) -> None:
    """
    Test get_estimated_price method.
    :param now_payments: NOWPayments class.
    :return: None
    """
    assert now_payments.payment.get_estimated_price(
        20, "BTC", "USD"
    ).get("estimated_amount", None) is not None


def test_create_payment(now_payments: NowPayments) -> None:
    """
    Test create_payment method.
    :param now_payments: NOWPayments class.
    :return: None
    """
    assert now_payments.payment.create_payment(
        price_amount=20,
        price_currency="USD",
        pay_currency="TRX",
        ipn_callback_url="https://example.com",
        order_id="123456789",
    ).get("payment_id", None) is not None


def test_create_invoice(now_payments: NowPayments) -> None:
    """
    Test create_invoice method.
    :param now_payments: NOWPayments class.
    :return: None
    """
    # get and save invoice id
    invoice_id = now_payments.payment.create_invoice(
        price_amount=20,
        price_currency="USD"
    )
    assert invoice_id.get("invoice_id", None) is not None


def test_create_invoice_payment(now_payments: NowPayments) -> None:
    """
    Test create_invoice_payment method.
    :param now_payments: NOWPayments class.
    :return: None
    """
    assert now_payments.payment.create_invoice_payment(
        invoice_id="123456789",
        pay_currency="TRX",
    ).get("payment_id", None) is not None
