from abc import ABC, abstractmethod
from datetime import date
import sqlite3
from typing import List


class Repository(ABC):

    @abstractmethod
    def find_latest_date(self, target: date) -> date:
        pass

    @abstractmethod
    def find_prev_date(self, target: date) -> date:
        pass

    @abstractmethod
    def find_next_date(self, target: date) -> date:
        pass

    @abstractmethod
    def find_all_date_list(self) -> List[date]:
        pass


class DemoRepository(Repository):

    def __init__(self, date_list: List[date]) -> None:
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

    def find_latest_date(self, target: date) -> date:
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

    def find_all_date_list(self) -> List[date]:
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
