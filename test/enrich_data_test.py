import pytest
from app.utils.validation import COLUMN_NAMES


@pytest.mark.anyio
@pytest.mark.parametrize(
    "filename",
    [
        "test/input_files/wrong_type.xml",
        "test/input_files/wrong_type.json",
    ],
)
async def test_wrong_filetype(async_client, filename):
    with open(filename, "rb") as file:
        files = {"file": (filename, file, "text/csv")}
        response = await async_client.post("/enrich_data/", files=files)

    assert response.status_code == 400
    assert response.json().get("detail") == "Input file must be CSV"


@pytest.mark.anyio
@pytest.mark.parametrize(
    "filename",
    [
        "test/input_files/empty.csv",
    ],
)
async def test_empty_file(async_client, filename):
    with open(filename, "rb") as file:
        files = {"file": (filename, file, "text/csv")}
        response = await async_client.post("/enrich_data/", files=files)

    assert response.status_code == 400
    assert response.json().get("detail") == "Empty CSV file"


@pytest.mark.anyio
@pytest.mark.parametrize(
    "filename",
    [
        "test/input_files/wrong_columns.csv",
    ],
)
async def test_wrong_column_names(async_client, filename):
    with open(filename, "rb") as file:
        files = {"file": (filename, file, "text/csv")}
        response = await async_client.post("/enrich_data/", files=files)

    expected_detail = "Invalid CSV column names. Required fields: " + ", ".join(
        COLUMN_NAMES
    )
    assert response.status_code == 400
    assert response.json().get("detail") == expected_detail
