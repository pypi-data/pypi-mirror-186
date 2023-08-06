"""Access OnSite data through FileMaker's JDBC integration"""

from __future__ import annotations

from importlib.resources import files

import jaydebeapi


class OnSiteServices:  # pylint: disable=too-few-public-methods
    """A class wrapping an ODBC connection to OnSite.

    This class wraps an ODBC connection to OnSite.
    """

    def __init__(self, connection_url: str, username: str, password: str):
        self._connection_url: str = connection_url
        self.__username: str = username
        self.__password: str = password

    def _connect(
        self,
    ):
        return jaydebeapi.connect(
            "com.filemaker.jdbc.Driver",
            self._connection_url,
            [self.__username, self.__password],
            str(files("darbiadev_onsite").joinpath("vendor/fmjdbc.jar")),
        )

    def make_query(
        self,
        sql: str,
        parameters: tuple[str | int, ...] | None,
    ) -> list[dict[str, str | int | float]]:
        """Make a query to the OnSite DB(s)"""
        if parameters is None:
            parameters = ()
        with self._connect() as connection:
            cursor = connection.cursor()
            cursor.execute(sql, parameters)

            columns = [column[0] for column in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]
