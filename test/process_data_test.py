import pytest
from app.utils.process_data import calculate_transaction_cost
from app.utils.process_data import generate_csv
from app.utils.process_data import get_api_data
from fastapi import HTTPException

from .transactions import test_data_before_generate_csv
from .transactions import test_transactions


@pytest.mark.parametrize(
    "country, notional, rate",
    [("USA", " 763000.0", "0.0070956000"), ("", "5000000.0", "0.0062469000")],
)
def test_wrong_country_calculate_transaction_cost(country, notional, rate):
    with pytest.raises(HTTPException) as exc_info:
        calculate_transaction_cost(country, notional, rate)

    assert exc_info.value.status_code == 400
    assert "Error: Unexpected country" in str(exc_info.value.detail)


@pytest.mark.parametrize(
    "country, notional, rate", [("NL", 24000000.0, 0), ("NL", 14700000.0, 0)]
)
def test_zero_rate_NL_calculate_transaction_cost(country, notional, rate):
    with pytest.raises(HTTPException) as exc_info:
        calculate_transaction_cost(country, notional, rate)

    assert exc_info.value.status_code == 400
    assert "Error: Division by zero" in str(exc_info.value.detail)


@pytest.mark.parametrize(
    "country, notional, rate",
    [
        ("GB", 763000.0, 0.0070956000),
        ("GB", 5000000.0, 0.0062469000),
        ("GB", 19570000.0, 0.0131500000),
        ("NL", 24000000.0, 0.0028900000),
        ("NL", 14700000.0, 0.0023800000),
    ],
)
def test_calculate_transaction_cost(country, notional, rate):
    transaction_cost = 0
    if country == "GB":
        transaction_cost = notional * rate - notional
    elif country == "NL":
        transaction_cost = abs(notional * (1 / rate) - notional)

    assert calculate_transaction_cost(country, notional, rate) == transaction_cost


@pytest.mark.anyio
@pytest.mark.parametrize("transaction, processed_transaction", test_transactions)
async def test_get_api_data(transaction, processed_transaction):
    assert await get_api_data(transaction) == processed_transaction


@pytest.mark.parametrize("data, csv_buffer", test_data_before_generate_csv)
def test_generate_csv(data, csv_buffer):
    assert generate_csv(data).getvalue() == csv_buffer.getvalue()
