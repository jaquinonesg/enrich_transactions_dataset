import csv
from io import StringIO

from fastapi import APIRouter
from fastapi import File
from fastapi import UploadFile
from fastapi.responses import PlainTextResponse

from ..utils import validation
from ..utils.process_data import add_data
from ..utils.process_data import generate_csv


router = APIRouter(prefix="/enrich_data", tags=["Enrich data"])


@router.post(path="/")
async def enrich_data(file: UploadFile = File(...)):
    """Adds legal_name, bic and transaction_cost to each line of a csv of transactions

    Parameters
    ----------
    ## csv file
        It should contain the headers:
        transaction_uti, isin, notional, notional_currency, transaction_type,
        transaction_datetime, rate, lei,

    Returns
    ----------
    ## csv file
        with legal_name, bic and transaction_cost added
    """

    validation.input_is_csv(file)
    contents = await file.read()
    csv_data = list(csv.DictReader(StringIO(contents.decode("utf-8"))))
    validation.input_csv_is_not_empty(csv_data)
    validation.csv_has_required_columns(csv_data)

    csv_data = await add_data(csv_data)
    csv_buffer = generate_csv(csv_data)

    return PlainTextResponse(
        csv_buffer.getvalue(),
        headers={"Content-Disposition": "attachment; filename=updated_csv.csv"},
    )
