from datetime import date


def parse_date(future_date_input):
    future_date = future_date_input.split(" ")
    year, month, day = int(future_date[2]), int(future_date[1]), int(future_date[0])
    return year, month, day


if __name__ == "__main__":
    print("-" * 50)
    event = input("Input the name of the event: ")
    future_date_input = input("Input the date you are waiting for (example: 21 05 2019): ")
    year, month, day = parse_date(future_date_input)
    
    today = date.today()
    future_date = date(year, month, day)
    print(f'\n{(future_date - today).days} days until "{event}" ')
    print("-" * 50)

