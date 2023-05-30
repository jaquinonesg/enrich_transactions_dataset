import asyncio
import csv
from io import StringIO

import httpx
from fastapi import HTTPException

from .logging import logging


def calculate_transaction_cost(country: str, notional: float, rate: float) -> float:
    transaction_cost = 0

    if country == "GB":
        transaction_cost = notional * rate - notional
    elif country == "NL":
        if rate == 0:
            raise HTTPException(status_code=400, detail="Error: Division by zero")
        transaction_cost = abs(notional * (1 / rate) - notional)
    else:
        raise HTTPException(
            status_code=400, detail=f"Error: Unexpected country {country}"
        )

    return transaction_cost


async def get_api_data(transaction: dict) -> dict:
    # adds legal_nale, bic and transaction cost to each transaction
    # fill with empty string if the api response doesnt have the expected structure
    url = f"https://api.gleif.org/api/v1/lei-records?filter[lei]={transaction['lei']}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

        if response.status_code != 200:
            logging.warning(f"Petition to {url} failed")

        response_dict = response.json()
        try:
            attributes = response_dict["data"][0]["attributes"]
            legal_name = attributes["entity"]["legalName"]["name"]
            bic = attributes["bic"][0]
            country = attributes["entity"]["legalAddress"]["country"]
        except AttributeError:
            transaction["legal_name"] = ""
            transaction["bic"] = ""
            transaction["transaction_costs"] = ""

        transaction["legal_name"] = legal_name
        transaction["bic"] = bic
        transaction["transaction_costs"] = calculate_transaction_cost(
            country, float(transaction["notional"]), float(transaction["rate"])
        )

    return transaction


async def add_data(csv_data: list[dict]) -> list[dict]:
    # Adds data to the CSV by making asynchronous API calls
    MAX_CONCURRENT_TASKS = 20

    async def get_data_with_semaphore(semaphore, transaction):
        async with semaphore:
            await get_api_data(transaction)

    semaphore = asyncio.Semaphore(MAX_CONCURRENT_TASKS)
    tasks = []

    for transaction in csv_data:
        task = get_data_with_semaphore(semaphore, transaction)
        tasks.append(task)
    await asyncio.gather(*tasks)

    return csv_data


def generate_csv(data: list[dict]) -> StringIO:
    fieldnames = data[0].keys()
    csv_buffer = StringIO()
    writer = csv.DictWriter(csv_buffer, fieldnames=fieldnames)
    writer.writeheader()

    for row in data:
        writer.writerow(row)

    return csv_buffer
