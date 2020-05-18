# This code is perfectly fine and has no issues.

from typing import Iterator
from datetime import date, timedelta

class DateIterator:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def __iter__(self) -> Iterator[date]:
        """Generators automatically have their own __next__ method hence we don't define it."""
        print("Inside iter method ...")
        current_day = self.start_date
        while current_day <= self.end_date:
            yield current_day
            current_day += timedelta(days=1)


if __name__ == "__main__":
    start_date = date(2019, 1, 1)
    end_date = date(2019, 1, 15)
    date_iterator = DateIterator(start_date, end_date)
    for current_day in date_iterator:
        print(current_day)

    date_str = ",".join([str(today) for today in date_iterator])
    print(date_str)

    # # These two don't work( I guess we have to define __len__ and __getitem__ on it)
    # print(f"Checking if indexing works : {date_iterator[4]}")
    #
    # print(f"The length of dates are : {len(date_iterator)}")
