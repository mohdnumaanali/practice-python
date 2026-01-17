def total_bill(amount, tip_percentage):
    tip = amount * (tip_percentage / 100)
    final = amount + tip
    return final

print(f"Final amount to pay: ${total_bill(200, 10)}") # 10% tip on 200