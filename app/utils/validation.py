from fastapi import HTTPException
from fastapi import status

from .logging import logging


COLUMN_NAMES = [
    "transaction_uti",
    "isin",
    "notional",
    "notional_currency",
    "transaction_type",
    "transaction_datetime",
    "rate",
    "lei",
]


def input_is_csv(file):
    if not file.filename.endswith(".csv"):
        logging.error("Input file is not a CSV")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Input file must be CSV"
        )


def input_csv_is_not_empty(csv_data):
    if not csv_data:
        logging.error("Input file is empty")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Empty CSV file"
        )


def validate_column_names(csv_data):
    header = list(csv_data[0].keys()) if csv_data else []
    return all(field in header for field in COLUMN_NAMES)


def csv_has_required_columns(csv_data):
    if not validate_column_names(csv_data):
        logging.error("Input file has not the required columns")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid CSV column names. Required fields: "
            + ", ".join(COLUMN_NAMES),
        )
