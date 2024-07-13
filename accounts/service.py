

def create_transaction(obj):
    old_balance = obj.account_id.balance
    obj.account_balance = old_balance

    if obj.amount < 0 and obj.account_id.balance == 0:
        raise Exception('На балансе недостаточно денег!')
    elif obj.amount < 0 and abs(obj.amount) > obj.account_id.balance:
        raise Exception('На балансе недостаточно денег!')
    else:
        obj.account_id.balance += obj.amount

    obj.account_id.save()


def delete_transaction(obj):
    if obj.amount < 0:
        obj.account_id.balance += abs(obj.amount)
    elif obj.amount > 0:
        obj.account_id.balance -= obj.amount

    obj.account_id.save()
