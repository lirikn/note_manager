# Валидация дат, статусов и уникальных ID.
from datetime import datetime, timedelta
import uuid


def validate_date(date):
    try:
        date = datetime.strptime(date, '%d-%m-%Y')
    except:
        return
    return date

def validate_status(status):
    return status in ('новая', 'в процессе', 'выполнено')

def generate_unique_id():
    return str(uuid.uuid4())



