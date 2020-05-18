### Doing the same logic as the code with iter but just in a different way
# This file does not work as the code in getitem tries to get inside a generator by
# indexing into it , but this is not possible
# Also i tried indexing into it using the recipe suggested in
# https://stackoverflow.com/questions/6288016/generator-object-is-not-subscriptable-error

import itertools
from typing import Iterator
from datetime import date, timedelta

class DateIterator:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._total_dates = self._get_all_dates()

    def _get_all_dates(self) -> Iterator[date]:
        current_day = self.start_date
        while current_day <= self.end_date:
            yield current_day
            current_day += timedelta(days=1)

    def __len__(self):
        print("Calling the len function...")
        return len(self._total_dates)

    def __getitem__(self, index):
        print(f"Calling getitem with value of index as {index}")
        return next(itertools.islice(self._total_dates, index))

if __name__ == "__main__":
    date_iterator = DateIterator(date(2019, 1, 1), date(2019, 1, 15))
    for next_date in date_iterator:
        print(next_date)

    date_str = ",".join([str(new_date) for new_date in date_iterator])
    print(date_str)

    print(f"Checking the length of the collection {len(date_iterator)}")

    print(f"Checking if indexing works : {date_iterator[4]}")
