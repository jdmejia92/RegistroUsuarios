import psycopg2
from psycopg2 import DatabaseError
from decouple import config
import sshtunnel


def get_connection():
    try:
        # SSH Tunnel
        """ tunnel = sshtunnel.SSHTunnelForwarder(
            ("sshserver"), 
            ssh_username="username", 
            ssh_password="password", 
            remote_bind_address=("ipadress", "port")
        )

        tunnel.start() """

        return psycopg2.connect(
            host=config('PGSQL_HOST'),
            user=config('PGSQL_USER'),
            password=config('PGSQL_PASSWORD'),
            database=config('PGSQL_DATABASE')
        )
    except DatabaseError as ex:
        raise ex
