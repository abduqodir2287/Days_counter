from datetime import datetime

def days_left(year: int, month: int, day: int):
    try:
        desired_date = datetime(year, month, day)
    except ValueError:
        return {"result": "Введена некорректная дата"}
    current_date = datetime.now()
    result = desired_date - current_date
    days = result.days
    seconds = result.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    if days >= 0:
        return {
            "result":
                f"До {day}.{month}.{year} остались {days} дней,"
                f" {hours} часов, {minutes} минут, {seconds} секунд."
        }
    return {"result": "Этот день уже прошел"}
