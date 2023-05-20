from utils import load_data, masked_card_from, masked_account_from, change_date, sorted_operation, status_operations
from pprint import pprint

def main():
    data = load_data()
    status = status_operations(data)
    sort_data = sorted_operation(status)
    number_card = masked_card_from(sort_data)
    number_account = masked_account_from(number_card)
    check_date = change_date(number_account)
    return check_date
pprint(main())








    # for id in range(5):
    #     return load_data[id], end="\n\n"   ввыод последних пяти
