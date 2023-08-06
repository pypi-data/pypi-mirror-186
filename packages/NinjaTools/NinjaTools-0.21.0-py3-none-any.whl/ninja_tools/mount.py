import os
from contextlib import contextmanager


def get_mounted_drives():
    drive_letter = os.popen('wmic logicaldisk get name').read().strip()
    drive_letter = drive_letter.split('\n')

    # Remove blank line elements from drive_letter
    drive_letter = [x.replace(' ', '').replace(':', '') for x in drive_letter if x]

    # Remove 'Name' from drive_letter
    drive_letter.pop(0)
    return drive_letter


@contextmanager
def network_share_auth(share, username=None, password=None, drive_letter='auto', verbose=False):
    """Context manager that mounts the given share using the given
    username and password to the given drive letter when entering
    the context and unmounts it when exiting."""

    if drive_letter == 'auto':
        drive_letter = get_mounted_drives()
        drive_letter = [x for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if x not in drive_letter][0]

    drive_letter = drive_letter.upper()
    cmd_parts = ["NET USE %s: %s" % (drive_letter, share)]

    if password:
        cmd_parts.append(password)
    if username:
        cmd_parts.append("/USER:%s" % username)

    if verbose:
        os.system(" ".join(cmd_parts))
    else:
        os.system(" ".join(cmd_parts) + " > NUL")

    try:
        yield drive_letter
    finally:
        if verbose:
            os.system("NET USE %s: /DELETE" % drive_letter)
        else:
            os.system("NET USE %s: /DELETE > NUL" % drive_letter)
