"""
Placeholder for extending authentication methods.
"""


def alt_authenticate(api, username, password):
    """
    Attempt to authenticate externally, if so configured.
    :returns:  None if authentication failed (or was not configured), or a {} containing
        values to apply to the user record, i.e. such things as an appropriate role to
        give the user, etc.'.
    """
