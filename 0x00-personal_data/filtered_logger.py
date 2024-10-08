#!/usr/bin/env python3
"""
Method to filter logging
"""
import logging
import re
from typing import List
import mysql.connector
import os


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    filter logging
    """
    for field in fields:
        message = re.sub(rf'{field}=(.*?){separator}',
                         f'{field}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        format record

        Args:
            record (logging.LogRecord): record to format

        Returns:
            str: record after formatting
        """
        message = record.msg
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  message, self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)


def get_logger() -> logging.Logger:
    """
    return a logger object

    Returns:
        logger: a logger object
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    logger.addHandler(logging.StreamHandler())
    logger.handlers[0].setFormatter(RedactingFormatter(List(PII_FIELDS)))
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    return a connector to the database

    Returns:
        mysql.connector.connection.MySQLConnection: connector to the database
    """
    return mysql.connector.connect.MySQLConnection(
        host=os.getenv('PERSONAL_DATA_DB_HOST', "localhost"),
        database=os.getenv('PERSONAL_DATA_DB_NAME'),
        user=os.getenv('PERSONAL_DATA_DB_USERNAME', "root"),
        password=os.getenv('PERSONAL_DATA_DB_PASSWORD', "")
    )


def main() -> None:
    """Main Function"""
    db_connection = get_db()
    cursor = db_connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users;")
    logger_object = get_logger()
    for row in cursor.fetchall:
        msg = "; ".join(f"{key}={value}" for key, value in row.items())
        logger_object.info(msg)
    cursor.close()
    db_connection.close()


if __name__ == "__main__":
    main()
