rates={"USD": 1.0, "EUR": 0.92, "JPY": 155.5} 
def convert(amt,from_currency,to_currency):
    usd = amt / rates[from_currency]
    convert=usd*rates[to_currency]
    return convert
print(convert(100,"USD","EUR"))