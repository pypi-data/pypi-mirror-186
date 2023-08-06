import uuid


def unique_id_generator():
    """ Generate unique ID for result. """
    u_id = uuid.uuid1()
    u_id = str(u_id).replace("-", "")

    return u_id
