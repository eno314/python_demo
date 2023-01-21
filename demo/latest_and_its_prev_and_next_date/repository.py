from abc import ABC, abstractmethod
import datetime
import sqlite3
from typing import List


class Repository(ABC):

    @abstractmethod
    def find_latest_date(self, target: datetime.date) -> datetime.date:
        pass

    @abstractmethod
    def find_prev_date(self, target: datetime.date) -> datetime.date:
        pass

    @abstractmethod
    def find_next_date(self, target: datetime.date) -> datetime.date:
        pass


class DemoRepository(Repository):

    def __init__(self, date_list: List[datetime.date]) -> None:
        self.conn = sqlite3.connect(":memory:")
        cur = self.conn.cursor()
        cur.execute(self._get_create_table_sql())
        if len(date_list) > 0:
            cur.execute(
                self._get_insert_table_sql(date_list),
                [self._date_to_saved(date) for date in date_list]
            )
        cur.close()
        self.conn.commit()

    def find_latest_date(self, target: datetime.date) -> datetime.date:
        sql = '''
            SELECT date FROM demo
            ORDER BY ABS(JULIANDAY(date) - JULIANDAY(?)) LIMIT 1;
        '''
        result = self._exec_fetchone_query(sql, [self._date_to_saved(target)])
        return self._fetchone_result_to_date(result)

    def find_prev_date(self, target: datetime.date) -> datetime.date:
        sql = '''
            SELECT date FROM demo
            WHERE date < (?)
            ORDER BY date DESC LIMIT 1;
        '''
        result = self._exec_fetchone_query(sql, [self._date_to_saved(target)])
        return self._fetchone_result_to_date(result)

    def find_next_date(self, target: datetime.date) -> datetime.date:
        sql = '''
            SELECT date FROM demo
            WHERE date > (?)
            ORDER BY date LIMIT 1;
        '''
        result = self._exec_fetchone_query(sql, [self._date_to_saved(target)])
        return self._fetchone_result_to_date(result)

    def _get_create_table_sql(self) -> str:
        return '''
            CREATE TABLE IF NOT EXISTS demo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date STRING NOT NULL
            );
        '''

    def _get_insert_table_sql(self, date_list: List[datetime.date]) -> str:
        placeholders = ','.join(['(?)' for _ in date_list])
        return 'INSERT INTO demo(date) values{}'.format(placeholders)

    def _exec_fetchone_query(self, sql, params):
        cur = self.conn.cursor()
        cur.execute(sql, params)
        result = cur.fetchone()
        cur.close()
        return result

    def _date_to_saved(self, date: datetime.date) -> str:
        return date.strftime('%Y-%m-%d')

    def _fetchone_result_to_date(self, result) -> datetime.date:
        if result is None:
            return None
        else:
            return datetime.date.fromisoformat(result[0])
