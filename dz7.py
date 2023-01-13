class LackOfFundsError(Exception):
    def __str__(self):
        return f"у вас недостатньо коштів для здійснення цієї операції"
def check_funds(amount_of_money, limit_value):
    if amount_of_money>limit_value:
        return "Недостаньо коштів"
    else:
        raise LackOfFundsError(amount_of_money)

funds=123
check_funds(funds,300)