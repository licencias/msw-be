import MySQLdb
import sshtunnel

sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0

with sshtunnel.SSHTunnelForwarder(
    ('ssh.pythonanywhere.com'),
    ssh_username='MikoFerdinand8080', ssh_password='casa89403670',
    remote_bind_address=('MikoFerdinand8080.mysql.pythonanywhere-services.com', 3306)
) as tunnel:
    connection = MySQLdb.connect(
        user='MikoFerdinand808',
        passwd='casa89403670',
        host='127.0.0.1', port=tunnel.local_bind_port,
        db='MikoFerdinand808$algoritmos4us',
    )

    connection.close()
    session = connection.cursor()
    
