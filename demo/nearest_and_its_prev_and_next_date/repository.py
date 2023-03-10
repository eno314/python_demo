from abc import ABC, abstractmethod
from datetime import date
import sqlite3
from typing import List


class Repository(ABC):

    @abstractmethod
    def find_nearest_date(self, target: date) -> date:
        pass

    @abstractmethod
    def find_prev_date(self, target: date) -> date:
        pass

    @abstractmethod
    def find_next_date(self, target: date) -> date:
        pass

    @abstractmethod
    def find_sorted_all_dates(self) -> List[date]:
        pass


class DemoRepository(Repository):

    def __init__(self) -> None:
        self.conn = sqlite3.connect(":memory:")
        cur = self.conn.cursor()
        cur.execute(self._get_create_table_sql())
        cur.close()
        self.conn.commit()

    def __del__(self) -> None:
        self.conn.close()

    def add_dates(self, dates: List[date]) -> None:
        cur = self.conn.cursor()
        cur.execute(
            self._get_insert_table_sql(dates),
            [self._date_to_saved(date) for date in dates]
        )
        cur.close()
        self.conn.commit()

    def find_nearest_date(self, target: date) -> date:
        sql = '''
            SELECT date FROM demo
            ORDER BY ABS(JULIANDAY(date) - JULIANDAY(?)) LIMIT 1;
        '''
        result = self._exec_fetchone_query(sql, [self._date_to_saved(target)])
        return self._fetchone_result_to_date(result)

    def find_prev_date(self, target: date) -> date:
        sql = '''
            SELECT date FROM demo
            WHERE date < (?)
            ORDER BY date DESC LIMIT 1;
        '''
        result = self._exec_fetchone_query(sql, [self._date_to_saved(target)])
        return self._fetchone_result_to_date(result)

    def find_next_date(self, target: date) -> date:
        sql = '''
            SELECT date FROM demo
            WHERE date > (?)
            ORDER BY date LIMIT 1;
        '''
        result = self._exec_fetchone_query(sql, [self._date_to_saved(target)])
        return self._fetchone_result_to_date(result)

    def find_sorted_all_dates(self) -> List[date]:
        sql = '''
            SELECT DISTINCT date FROM demo
            ORDER BY date;
        '''
        cur = self.conn.cursor()
        cur.execute(sql)
        results = cur.fetchall()
        cur.close()
        return [self._saved_to_date(result[0]) for result in results]

    def _get_create_table_sql(self) -> str:
        return '''
            CREATE TABLE IF NOT EXISTS demo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date STRING NOT NULL
            );
        '''

    def _get_insert_table_sql(self, date_list: List[date]) -> str:
        placeholders = ','.join(['(?)' for _ in date_list])
        return 'INSERT INTO demo(date) values{}'.format(placeholders)

    def _exec_fetchone_query(self, sql, params):
        cur = self.conn.cursor()
        cur.execute(sql, params)
        result = cur.fetchone()
        cur.close()
        return result

    def _fetchone_result_to_date(self, result):
        if result is None:
            return None
        else:
            return self._saved_to_date(result[0])

    def _date_to_saved(self, date: date) -> str:
        return date.strftime('%Y-%m-%d')

    def _saved_to_date(self, saved: str) -> date:
        return date.fromisoformat(saved)
