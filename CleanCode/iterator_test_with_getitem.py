### Doing the same logic as the code with iter but just in a different way
# I have raised a question on stackoverflow :
# https://stackoverflow.com/questions/61712618/why-does-mypy-not-consider-a-class-as-iterable-if-it-has-len-and-getitem

from typing import List, Iterator
from datetime import date, timedelta

class DateIterator:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._total_dates = self._get_all_dates()

    def _get_all_dates(self) -> List[date]:
        dates = []
        current_day = self.start_date
        while current_day <= self.end_date:
            dates.append(current_day)
            current_day += timedelta(days=1)
        return dates

    def __len__(self) -> int:
        print("Calling the len function...")
        return len(self._total_dates)

    def __getitem__(self, index) -> date:
        print(f"Calling getitem with value of index as {index}")
        return self._total_dates[index]

if __name__ == "__main__":
    date_iterator = DateIterator(date(2019, 1, 1), date(2019, 1, 15))
    for new_date in date_iterator:
        print(new_date)

    date_str = ",".join([str(new_date) for new_date in date_iterator])
    print(date_str)

    print(f"Checking the length of the collection {len(date_iterator)}")

    print(f"Checking if indexing works : {date_iterator[4]}")
