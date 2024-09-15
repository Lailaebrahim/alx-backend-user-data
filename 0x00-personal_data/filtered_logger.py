#!/usr/bin/env python3
"""
Method to filter logging
"""
import logging
import re
from typing import List


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
