from db import mapping

def get_users(session):
    response = session.execute(mapping.get_users)
    response = response.fetchall()
    return response