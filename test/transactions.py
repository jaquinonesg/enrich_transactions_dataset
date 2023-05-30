import csv
from io import StringIO


transaction1 = {
    "transaction_uti": "0000452AMARKITWIRE97461020",
    "isin": "EZN7BQZMQBR8",
    "notional": "5000000.0",
    "notional_currency": "GBP",
    "transaction_type": "Buy",
    "transaction_datetime": "2020-12-17T12:15:39Z",
    "rate": "0.0062469000",
    "lei": "213800MBWEIJDM5CU638",
}
transaction2 = {
    "transaction_uti": "1030244641MARKITWIRE0000000000000072110232",
    "isin": "EZNB2LV26CY9",
    "notional": "1.957E7",
    "notional_currency": "GBP",
    "transaction_type": "Sell",
    "transaction_datetime": "2020-12-16T14:38:43Z",
    "rate": "0.0131500000",
    "lei": "K6Q0W1PS1L1O4IQL9C32",
}
transaction3 = {
    "transaction_uti": "1030291281MARKITWIRE0000000000000080152595",
    "isin": "EZD7JRS42975",
    "notional": "6700000.0",
    "notional_currency": "GBP",
    "transaction_type": "Sell",
    "transaction_datetime": "2020-12-21T14:54:14Z",
    "rate": "0.0137000000",
    "lei": "XKZZ2JZF41MRHTR1V493",
}
transaction4 = {
    "transaction_uti": "0000452AMARKITWIRE26225363",
    "isin": "EZKK6069DP48",
    "notional": "1.41E7",
    "notional_currency": "GBP",
    "transaction_type": "Sell",
    "transaction_datetime": "2020-12-17T11:52:14Z",
    "rate": "0.0060063000",
    "lei": "MP6I5ZYZBEU3UXPYFY54",
}
transaction5 = {
    "transaction_uti": "0000452AMARKITWIRE106469723",
    "isin": "EZ65LX7J3NL1",
    "notional": "1.2E7",
    "notional_currency": "GBP",
    "transaction_type": "Buy",
    "transaction_datetime": "2020-12-15T14:17:29Z",
    "rate": "0.0094600000",
    "lei": "MP6I5ZYZBEU3UXPYFY54",
}
transaction6 = {
    "transaction_uti": "1030244641MARKITWIRE0000000000000072697124",
    "isin": "EZQW6HTFKNZ9",
    "notional": "1.951E7",
    "notional_currency": "GBP",
    "transaction_type": "Sell",
    "transaction_datetime": "2020-12-16T14:37:01Z",
    "rate": "0.0136050000",
    "lei": "K6Q0W1PS1L1O4IQL9C32",
}
transaction7 = {
    "transaction_uti": "0000452AMARKITWIRE150674490",
    "isin": "EZH7KHTJD052",
    "notional": "4.5E7",
    "notional_currency": "EUR",
    "transaction_type": "Buy",
    "transaction_datetime": "2019-09-27T12:32:11Z",
    "rate": "0.0042700000",
    "lei": "BFXS5XCH7N0Y05NIXW11",
}
transaction8 = {
    "transaction_uti": "1030244641MARKITWIRE0000000000000112880849",
    "isin": "EZ6W26XXZTS6",
    "notional": "1853000.0",
    "notional_currency": "GBP",
    "transaction_type": "Sell",
    "transaction_datetime": "2020-11-25T15:10:25Z",
    "rate": "0.0061606000",
    "lei": "K6Q0W1PS1L1O4IQL9C32",
}
transaction9 = {
    "transaction_uti": "0000452AMARKITWIRE190106524",
    "isin": "EZ848JR3VBM1",
    "notional": "6900000.0",
    "notional_currency": "EUR",
    "transaction_type": "Buy",
    "transaction_datetime": "2022-07-25T12:34:28Z",
    "rate": "0.0063300000",
    "lei": "BFXS5XCH7N0Y05NIXW11",
}
transaction10 = {
    "transaction_uti": "0000452AMARKITWIRE188040944",
    "isin": "EZ29LKLNM4G1",
    "notional": "2.4E7",
    "notional_currency": "EUR",
    "transaction_type": "Sell",
    "transaction_datetime": "2022-06-22T14:09:23Z",
    "rate": "0.0028900000",
    "lei": "BFXS5XCH7N0Y05NIXW11",
}
transaction11 = {
    "transaction_uti": "0000452AMARKITWIRE188631428",
    "isin": "EZDYJN1BK9K2",
    "notional": "4600000.0",
    "notional_currency": "EUR",
    "transaction_type": "Buy",
    "transaction_datetime": "2022-06-30T09:50:48Z",
    "rate": "0.0000600000",
    "lei": "4PQUHN3JPFGFNF3BB653",
}
transaction12 = {
    "transaction_uti": "10302389174A38DCE0DBA811E9B389B9699A7DC0CC",
    "isin": "EZ69M311SB39",
    "notional": "1.1E7",
    "notional_currency": "GBP",
    "transaction_type": "Buy",
    "transaction_datetime": "2015-03-04T12:00:00Z",
    "rate": "0.0011000000",
    "lei": "4PQUHN3JPFGFNF3BB653",
}
transaction13 = {
    "transaction_uti": "0000452AMARKITWIRE189502871",
    "isin": "EZWXNZCG4HW5",
    "notional": "5.0E7",
    "notional_currency": "EUR",
    "transaction_type": "Buy",
    "transaction_datetime": "2022-07-14T10:28:57Z",
    "rate": "0.0044800000",
    "lei": "BFXS5XCH7N0Y05NIXW11",
}
transaction14 = {
    "transaction_uti": "0000452AMARKITWIRE189056073",
    "isin": "EZ53S44K7JL2",
    "notional": "1.47E7",
    "notional_currency": "EUR",
    "transaction_type": "Buy",
    "transaction_datetime": "2022-07-07T12:12:38Z",
    "rate": "0.0023800000",
    "lei": "BFXS5XCH7N0Y05NIXW11",
}
transaction15 = {
    "transaction_uti": "0000452AMARKITWIRE73224269",
    "isin": "EZSJCJ5GMYW6",
    "notional": "8000000.0",
    "notional_currency": "GBP",
    "transaction_type": "Buy",
    "transaction_datetime": "2020-12-11T11:42:03Z",
    "rate": "0.0054013000",
    "lei": "BFXS5XCH7N0Y05NIXW11",
}
transaction16 = {
    "transaction_uti": "0000452AMARKITWIRE190106543",
    "isin": "EZF6Q1GFJ316",
    "notional": "7400000.0",
    "notional_currency": "EUR",
    "transaction_type": "Buy",
    "transaction_datetime": "2022-07-25T12:35:59Z",
    "rate": "0.0063300000",
    "lei": "BFXS5XCH7N0Y05NIXW11",
}
transaction17 = {
    "transaction_uti": "1030238917C2B4CB90B9D211E9984D070361192EBB",
    "isin": "EZ6Y30GC29Z2",
    "notional": "2.14E8",
    "notional_currency": "EUR",
    "transaction_type": "Buy",
    "transaction_datetime": "2019-08-08T11:50:00Z",
    "rate": "0.0004800000",
    "lei": "K6Q0W1PS1L1O4IQL9C32",
}
transaction18 = {
    "transaction_uti": "0000452AMARKITWIRE187215187",
    "isin": "EZ2KJCJ083B8",
    "notional": "6.0E7",
    "notional_currency": "EUR",
    "transaction_type": "Buy",
    "transaction_datetime": "2022-06-10T14:08:07Z",
    "rate": "0.0006300000",
    "lei": "BFXS5XCH7N0Y05NIXW11",
}
transaction19 = {
    "transaction_uti": "0000452AMARKITWIRE88889673",
    "isin": "EZTH907TJ6W0",
    "notional": "2.2E7",
    "notional_currency": "GBP",
    "transaction_type": "Buy",
    "transaction_datetime": "2020-12-17T12:05:48Z",
    "rate": "0.0058325000",
    "lei": "MP6I5ZYZBEU3UXPYFY54",
}
transaction20 = {
    "transaction_uti": "1030291281MARKITWIRE0000000000000112874138",
    "isin": "EZ9724VTXK48",
    "notional": "763000.0",
    "notional_currency": "GBP",
    "transaction_type": "Sell",
    "transaction_datetime": "2020-11-25T15:06:22Z",
    "rate": "0.0070956000",
    "lei": "XKZZ2JZF41MRHTR1V493",
}

processed_transaction1 = {
    "transaction_uti": "0000452AMARKITWIRE97461020",
    "isin": "EZN7BQZMQBR8",
    "notional": "5000000.0",
    "notional_currency": "GBP",
    "transaction_type": "Buy",
    "transaction_datetime": "2020-12-17T12:15:39Z",
    "rate": "0.0062469000",
    "lei": "213800MBWEIJDM5CU638",
    "legal_name": "LLOYDS BANK CORPORATE MARKETS PLC",
    "bic": "LLCMGB22XXX",
    "transaction_costs": -4968765.5,
}
processed_transaction2 = {
    "transaction_uti": "1030244641MARKITWIRE0000000000000072110232",
    "isin": "EZNB2LV26CY9",
    "notional": "1.957E7",
    "notional_currency": "GBP",
    "transaction_type": "Sell",
    "transaction_datetime": "2020-12-16T14:38:43Z",
    "rate": "0.0131500000",
    "lei": "K6Q0W1PS1L1O4IQL9C32",
    "legal_name": "J.P. MORGAN SECURITIES PLC",
    "bic": "JPMSGB2LXXX",
    "transaction_costs": -19312654.5,
}
processed_transaction3 = {
    "transaction_uti": "1030291281MARKITWIRE0000000000000080152595",
    "isin": "EZD7JRS42975",
    "notional": "6700000.0",
    "notional_currency": "GBP",
    "transaction_type": "Sell",
    "transaction_datetime": "2020-12-21T14:54:14Z",
    "rate": "0.0137000000",
    "lei": "XKZZ2JZF41MRHTR1V493",
    "legal_name": "CITIGROUP GLOBAL MARKETS LIMITED",
    "bic": "SBILGB2LXXX",
    "transaction_costs": -6608210.0,
}
processed_transaction4 = {
    "transaction_uti": "0000452AMARKITWIRE26225363",
    "isin": "EZKK6069DP48",
    "notional": "1.41E7",
    "notional_currency": "GBP",
    "transaction_type": "Sell",
    "transaction_datetime": "2020-12-17T11:52:14Z",
    "rate": "0.0060063000",
    "lei": "MP6I5ZYZBEU3UXPYFY54",
    "legal_name": "HSBC BANK PLC",
    "bic": "MIDLGB22XXX",
    "transaction_costs": -14015311.17,
}
processed_transaction5 = {
    "transaction_uti": "0000452AMARKITWIRE106469723",
    "isin": "EZ65LX7J3NL1",
    "notional": "1.2E7",
    "notional_currency": "GBP",
    "transaction_type": "Buy",
    "transaction_datetime": "2020-12-15T14:17:29Z",
    "rate": "0.0094600000",
    "lei": "MP6I5ZYZBEU3UXPYFY54",
    "legal_name": "HSBC BANK PLC",
    "bic": "MIDLGB22XXX",
    "transaction_costs": -11886480.0,
}
processed_transaction6 = {
    "transaction_uti": "1030244641MARKITWIRE0000000000000072697124",
    "isin": "EZQW6HTFKNZ9",
    "notional": "1.951E7",
    "notional_currency": "GBP",
    "transaction_type": "Sell",
    "transaction_datetime": "2020-12-16T14:37:01Z",
    "rate": "0.0136050000",
    "lei": "K6Q0W1PS1L1O4IQL9C32",
    "legal_name": "J.P. MORGAN SECURITIES PLC",
    "bic": "JPMSGB2LXXX",
    "transaction_costs": -19244566.45,
}
processed_transaction7 = {
    "transaction_uti": "0000452AMARKITWIRE150674490",
    "isin": "EZH7KHTJD052",
    "notional": "4.5E7",
    "notional_currency": "EUR",
    "transaction_type": "Buy",
    "transaction_datetime": "2019-09-27T12:32:11Z",
    "rate": "0.0042700000",
    "lei": "BFXS5XCH7N0Y05NIXW11",
    "legal_name": "ABN AMRO Bank N.V.",
    "bic": "ABNANL2AXXX",
    "transaction_costs": 10493641686.182669,
}
processed_transaction8 = {
    "transaction_uti": "1030244641MARKITWIRE0000000000000112880849",
    "isin": "EZ6W26XXZTS6",
    "notional": "1853000.0",
    "notional_currency": "GBP",
    "transaction_type": "Sell",
    "transaction_datetime": "2020-11-25T15:10:25Z",
    "rate": "0.0061606000",
    "lei": "K6Q0W1PS1L1O4IQL9C32",
    "legal_name": "J.P. MORGAN SECURITIES PLC",
    "bic": "JPMSGB2LXXX",
    "transaction_costs": -1841584.4082,
}
processed_transaction9 = {
    "transaction_uti": "0000452AMARKITWIRE190106524",
    "isin": "EZ848JR3VBM1",
    "notional": "6900000.0",
    "notional_currency": "EUR",
    "transaction_type": "Buy",
    "transaction_datetime": "2022-07-25T12:34:28Z",
    "rate": "0.0063300000",
    "lei": "BFXS5XCH7N0Y05NIXW11",
    "legal_name": "ABN AMRO Bank N.V.",
    "bic": "ABNANL2AXXX",
    "transaction_costs": 1083147393.364929,
}
processed_transaction10 = {
    "transaction_uti": "0000452AMARKITWIRE188040944",
    "isin": "EZ29LKLNM4G1",
    "notional": "2.4E7",
    "notional_currency": "EUR",
    "transaction_type": "Sell",
    "transaction_datetime": "2022-06-22T14:09:23Z",
    "rate": "0.0028900000",
    "lei": "BFXS5XCH7N0Y05NIXW11",
    "legal_name": "ABN AMRO Bank N.V.",
    "bic": "ABNANL2AXXX",
    "transaction_costs": 8280498269.896193,
}
processed_transaction11 = {
    "transaction_uti": "0000452AMARKITWIRE188631428",
    "isin": "EZDYJN1BK9K2",
    "notional": "4600000.0",
    "notional_currency": "EUR",
    "transaction_type": "Buy",
    "transaction_datetime": "2022-06-30T09:50:48Z",
    "rate": "0.0000600000",
    "lei": "4PQUHN3JPFGFNF3BB653",
    "legal_name": "MORGAN STANLEY & CO. INTERNATIONAL PLC",
    "bic": "MSLNGB2XXXX",
    "transaction_costs": -4599724.0,
}
processed_transaction12 = {
    "transaction_uti": "10302389174A38DCE0DBA811E9B389B9699A7DC0CC",
    "isin": "EZ69M311SB39",
    "notional": "1.1E7",
    "notional_currency": "GBP",
    "transaction_type": "Buy",
    "transaction_datetime": "2015-03-04T12:00:00Z",
    "rate": "0.0011000000",
    "lei": "4PQUHN3JPFGFNF3BB653",
    "legal_name": "MORGAN STANLEY & CO. INTERNATIONAL PLC",
    "bic": "MSLNGB2XXXX",
    "transaction_costs": -10987900.0,
}
processed_transaction13 = {
    "transaction_uti": "0000452AMARKITWIRE189502871",
    "isin": "EZWXNZCG4HW5",
    "notional": "5.0E7",
    "notional_currency": "EUR",
    "transaction_type": "Buy",
    "transaction_datetime": "2022-07-14T10:28:57Z",
    "rate": "0.0044800000",
    "lei": "BFXS5XCH7N0Y05NIXW11",
    "legal_name": "ABN AMRO Bank N.V.",
    "bic": "ABNANL2AXXX",
    "transaction_costs": 11110714285.714287,
}
processed_transaction14 = {
    "transaction_uti": "0000452AMARKITWIRE189056073",
    "isin": "EZ53S44K7JL2",
    "notional": "1.47E7",
    "notional_currency": "EUR",
    "transaction_type": "Buy",
    "transaction_datetime": "2022-07-07T12:12:38Z",
    "rate": "0.0023800000",
    "lei": "BFXS5XCH7N0Y05NIXW11",
    "legal_name": "ABN AMRO Bank N.V.",
    "bic": "ABNANL2AXXX",
    "transaction_costs": 6161770588.235294,
}
processed_transaction15 = {
    "transaction_uti": "0000452AMARKITWIRE73224269",
    "isin": "EZSJCJ5GMYW6",
    "notional": "8000000.0",
    "notional_currency": "GBP",
    "transaction_type": "Buy",
    "transaction_datetime": "2020-12-11T11:42:03Z",
    "rate": "0.0054013000",
    "lei": "BFXS5XCH7N0Y05NIXW11",
    "legal_name": "ABN AMRO Bank N.V.",
    "bic": "ABNANL2AXXX",
    "transaction_costs": 1473124914.3724658,
}
processed_transaction16 = {
    "transaction_uti": "0000452AMARKITWIRE190106543",
    "isin": "EZF6Q1GFJ316",
    "notional": "7400000.0",
    "notional_currency": "EUR",
    "transaction_type": "Buy",
    "transaction_datetime": "2022-07-25T12:35:59Z",
    "rate": "0.0063300000",
    "lei": "BFXS5XCH7N0Y05NIXW11",
    "legal_name": "ABN AMRO Bank N.V.",
    "bic": "ABNANL2AXXX",
    "transaction_costs": 1161636334.9131124,
}
processed_transaction17 = {
    "transaction_uti": "1030238917C2B4CB90B9D211E9984D070361192EBB",
    "isin": "EZ6Y30GC29Z2",
    "notional": "2.14E8",
    "notional_currency": "EUR",
    "transaction_type": "Buy",
    "transaction_datetime": "2019-08-08T11:50:00Z",
    "rate": "0.0004800000",
    "lei": "K6Q0W1PS1L1O4IQL9C32",
    "legal_name": "J.P. MORGAN SECURITIES PLC",
    "bic": "JPMSGB2LXXX",
    "transaction_costs": -213897280.0,
}
processed_transaction18 = {
    "transaction_uti": "0000452AMARKITWIRE187215187",
    "isin": "EZ2KJCJ083B8",
    "notional": "6.0E7",
    "notional_currency": "EUR",
    "transaction_type": "Buy",
    "transaction_datetime": "2022-06-10T14:08:07Z",
    "rate": "0.0006300000",
    "lei": "BFXS5XCH7N0Y05NIXW11",
    "legal_name": "ABN AMRO Bank N.V.",
    "bic": "ABNANL2AXXX",
    "transaction_costs": 95178095238.09523,
}
processed_transaction19 = {
    "transaction_uti": "0000452AMARKITWIRE88889673",
    "isin": "EZTH907TJ6W0",
    "notional": "2.2E7",
    "notional_currency": "GBP",
    "transaction_type": "Buy",
    "transaction_datetime": "2020-12-17T12:05:48Z",
    "rate": "0.0058325000",
    "lei": "MP6I5ZYZBEU3UXPYFY54",
    "legal_name": "HSBC BANK PLC",
    "bic": "MIDLGB22XXX",
    "transaction_costs": -21871685.0,
}
processed_transaction20 = {
    "transaction_uti": "1030291281MARKITWIRE0000000000000112874138",
    "isin": "EZ9724VTXK48",
    "notional": "763000.0",
    "notional_currency": "GBP",
    "transaction_type": "Sell",
    "transaction_datetime": "2020-11-25T15:06:22Z",
    "rate": "0.0070956000",
    "lei": "XKZZ2JZF41MRHTR1V493",
    "legal_name": "CITIGROUP GLOBAL MARKETS LIMITED",
    "bic": "SBILGB2LXXX",
    "transaction_costs": -757586.0572,
}

test_transactions = [
    (transaction1, processed_transaction1),
    (transaction2, processed_transaction2),
    (transaction3, processed_transaction3),
    (transaction4, processed_transaction4),
    (transaction5, processed_transaction5),
    (transaction6, processed_transaction6),
    (transaction7, processed_transaction7),
    (transaction8, processed_transaction8),
    (transaction9, processed_transaction9),
    (transaction10, processed_transaction10),
    (transaction11, processed_transaction11),
    (transaction12, processed_transaction12),
    (transaction13, processed_transaction13),
    (transaction14, processed_transaction14),
    (transaction15, processed_transaction15),
    (transaction16, processed_transaction16),
    (transaction17, processed_transaction17),
    (transaction18, processed_transaction18),
    (transaction19, processed_transaction19),
    (transaction20, processed_transaction20),
]


def build_csv(data):
    fieldnames = data[0].keys()
    csv_buffer = StringIO()
    writer = csv.DictWriter(csv_buffer, fieldnames=fieldnames)
    writer.writeheader()

    for row in data:
        writer.writerow(row)

    return csv_buffer


data_before_csv = [
    processed_transaction1,
    processed_transaction2,
    processed_transaction3,
    processed_transaction4,
    processed_transaction5,
    processed_transaction6,
    processed_transaction7,
    processed_transaction8,
    processed_transaction9,
    processed_transaction10,
    processed_transaction11,
    processed_transaction12,
    processed_transaction13,
    processed_transaction14,
    processed_transaction15,
    processed_transaction16,
    processed_transaction17,
    processed_transaction18,
    processed_transaction19,
    processed_transaction20,
]

data_before_csv = [processed_transaction1, processed_transaction2]

test_data_before_generate_csv = [(data_before_csv, build_csv(data_before_csv))]
