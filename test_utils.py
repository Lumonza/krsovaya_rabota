import pytest
from utils import load_data, sorted_operation, status_operations, masked_card_from, masked_account_from, change_date


def test_load_data():
    data = load_data()
    assert isinstance(data, list)


def test_sorted_operation():
    result = [{'id': 482520625, 'state': 'EXECUTED', 'date': '2019-11-13T17:38:04.800051',
               'operationAmount': {'amount': '62814.53', 'currency': {'name': 'руб.', 'code': 'RUB'}},
               'description': 'Перевод со счета на счет', 'from': 'Счет 38611439522855669794',
               'to': 'Счет 46765464282437878125'},
              {'id': 154927927, 'state': 'EXECUTED', 'date': '2019-11-19T09:22:25.899614',
               'operationAmount': {'amount': '30153.72', 'currency': {'name': 'руб.', 'code': 'RUB'}},
               'description': 'Перевод организации', 'from': 'Maestro 7810846596785568',
               'to': 'Счет 43241152692663622869'},
              {'id': 560813069, 'state': 'CANCELED', 'date': '2019-12-03T04:27:03.427014',
               'operationAmount': {'amount': '17628.50', 'currency': {'name': 'USD', 'code': 'USD'}},
               'description': 'Перевод с карты на карту', 'from': 'MasterCard 1796816785869527',
               'to': 'Visa Classic 7699855375169288'},
              {'id': 114832369, 'state': 'EXECUTED', 'date': '2019-12-07T06:17:14.634890',
               'operationAmount': {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}},
               'description': 'Перевод организации', 'from': 'Visa Classic 2842878893689012',
               'to': 'Счет 35158586384610753655'},
              {'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582',
               'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}},
               'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'}]

    assert sorted_operation(load_data()) == result


def test_status_operation():
    result = [{'id': 317987878, 'state': 'EXECUTED', 'date': '2018-01-13T13:00:58.458625',
               'operationAmount': {'amount': '55985.82', 'currency': {'name': 'USD', 'code': 'USD'}},
               'description': 'Перевод с карты на карту', 'from': 'Visa Classic 8906171742833215',
               'to': 'Visa Platinum 6086997013848217'},
              {'id': 634356296, 'state': 'EXECUTED', 'date': '2018-01-21T01:10:28.317704',
               'operationAmount': {'amount': '96900.90', 'currency': {'name': 'руб.', 'code': 'RUB'}},
               'description': 'Перевод со счета на счет', 'from': 'Счет 33407225454123927865',
               'to': 'Счет 79619011266276091215'},
              {'id': 260972664, 'state': 'EXECUTED', 'date': '2018-01-23T01:48:30.477053',
               'operationAmount': {'amount': '2974.30', 'currency': {'name': 'USD', 'code': 'USD'}},
               'description': 'Перевод с карты на карту', 'from': 'Visa Classic 3414396880443483',
               'to': 'Visa Gold 2684274847577419'},
              {'id': 147815167, 'state': 'EXECUTED', 'date': '2018-01-26T15:40:13.413061',
               'operationAmount': {'amount': '50870.71', 'currency': {'name': 'руб.', 'code': 'RUB'}},
               'description': 'Перевод с карты на счет', 'from': 'Maestro 4598300720424501',
               'to': 'Счет 43597928997568165086'},
              {'id': 893507143, 'state': 'EXECUTED', 'date': '2018-02-03T07:16:28.366141',
               'operationAmount': {'amount': '90297.21', 'currency': {'name': 'руб.', 'code': 'RUB'}},
               'description': 'Открытие вклада', 'to': 'Счет 37653295304860108767'}]
    assert status_operations(sorted_operation(load_data())) == result


def test_masked_account_from():
    result = [{'id': 317987878, 'state': 'EXECUTED', 'date': '2018-01-13T13:00:58.458625',
               'operationAmount': {'amount': '55985.82', 'currency': {'name': 'USD', 'code': 'USD'}},
               'description': 'Перевод с карты на карту', 'from': '8906 17** **** 3215',
               'to': 'Visa Platinum 6086997013848217'},
              {'id': 634356296, 'state': 'EXECUTED', 'date': '2018-01-21T01:10:28.317704',
               'operationAmount': {'amount': '96900.90', 'currency': {'name': 'руб.', 'code': 'RUB'}},
               'description': 'Перевод со счета на счет', 'from': '**7865', 'to': 'Счет 79619011266276091215'},
              {'id': 260972664, 'state': 'EXECUTED', 'date': '2018-01-23T01:48:30.477053',
               'operationAmount': {'amount': '2974.30', 'currency': {'name': 'USD', 'code': 'USD'}},
               'description': 'Перевод с карты на карту', 'from': '3414 39** **** 3483',
               'to': 'Visa Gold 2684274847577419'},
              {'id': 147815167, 'state': 'EXECUTED', 'date': '2018-01-26T15:40:13.413061',
               'operationAmount': {'amount': '50870.71', 'currency': {'name': 'руб.', 'code': 'RUB'}},
               'description': 'Перевод с карты на счет', 'from': '4598 30** **** 4501',
               'to': 'Счет 43597928997568165086'},
              {'id': 893507143, 'state': 'EXECUTED', 'date': '2018-02-03T07:16:28.366141',
               'operationAmount': {'amount': '90297.21', 'currency': {'name': 'руб.', 'code': 'RUB'}},
               'description': 'Открытие вклада', 'to': 'Счет 37653295304860108767'}]
    assert masked_card_from(status_operations(sorted_operation(load_data()))) == result


def test_change_date():
    result = [{'id': 317987878, 'state': 'EXECUTED', 'date': '13 01 2018',
               'operationAmount': {'amount': '55985.82', 'currency': {'name': 'USD', 'code': 'USD'}},
               'description': 'Перевод с карты на карту', 'from': '8906 17** **** 3215',
               'to': 'Visa Platinum 6086997013848217'}, {'id': 634356296, 'state': 'EXECUTED', 'date': '21 01 2018',
                                                         'operationAmount': {'amount': '96900.90',
                                                                             'currency': {'name': 'руб.',
                                                                                          'code': 'RUB'}},
                                                         'description': 'Перевод со счета на счет', 'from': '**7865',
                                                         'to': 'Счет 79619011266276091215'},
              {'id': 260972664, 'state': 'EXECUTED', 'date': '23 01 2018',
               'operationAmount': {'amount': '2974.30', 'currency': {'name': 'USD', 'code': 'USD'}},
               'description': 'Перевод с карты на карту', 'from': '3414 39** **** 3483',
               'to': 'Visa Gold 2684274847577419'}, {'id': 147815167, 'state': 'EXECUTED', 'date': '26 01 2018',
                                                     'operationAmount': {'amount': '50870.71',
                                                                         'currency': {'name': 'руб.', 'code': 'RUB'}},
                                                     'description': 'Перевод с карты на счет',
                                                     'from': '4598 30** **** 4501', 'to': 'Счет 43597928997568165086'},
              {'id': 893507143, 'state': 'EXECUTED', 'date': '03 02 2018',
               'operationAmount': {'amount': '90297.21', 'currency': {'name': 'руб.', 'code': 'RUB'}},
               'description': 'Открытие вклада', 'to': 'Счет 37653295304860108767'}]
    assert change_date(masked_card_from(status_operations(sorted_operation(load_data())))) == result