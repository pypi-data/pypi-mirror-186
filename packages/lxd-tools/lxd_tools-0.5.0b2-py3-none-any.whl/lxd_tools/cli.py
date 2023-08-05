import sys
from contextlib import closing
from typing import Optional

from click import Path, command, option, version_option
from pylxd import Client

from .constant import ShowResource
from .resources import print_resources

__all__ = [
    'run_print_resources',
]


@command(
    help='Tool for displaying  LXD containers actual resources.',
)
@version_option()
@option(
    '-e',
    '--endpoint',
    help='LXD endpoint to connect to.',
    default=None,
)
@option(
    '-c',
    '--cert-filepath',
    type=Path(dir_okay=False),
    default=None,
    help='LXD certificate file path to connect over endpoint.',
)
@option(
    '-k',
    '--key-filepath',
    type=Path(dir_okay=False),
    default=None,
    help='LXD private key file path to connect over endpoint.',
)
@option(
    '--verify-cert / --no-verify-cert',
    default=True,
    show_default=True,
    help='Verify LXD certificate.',
)
@option(
    '--gib / --gb',
    default=False,
    show_default=True,
    help='Print units in gibibytes (2 degree) or gigabytes (10 degree).',
)
@option(
    '--only-containers',
    is_flag=True,
    default=False,
    show_default=True,
    help='Print only LXD containers resources.',
)
@option(
    '--only-virtual-machines',
    is_flag=True,
    default=False,
    show_default=True,
    help='Print only LXD virtual machines resources.',
)
def run_print_resources(  # pylint: disable=too-many-arguments
    endpoint: Optional[str],
    cert_filepath: Optional[str],
    key_filepath: Optional[str],
    verify_cert: bool,
    gib: bool,
    only_containers: bool,
    only_virtual_machines: bool,
):
    if only_containers and only_virtual_machines:
        print(
            'You should define one of "--only-*" options, but you defined '
            'both.',
        )
        sys.exit(1)

    show_resource = ShowResource.BOTH

    if only_containers:
        show_resource = ShowResource.CONTAINER

    elif only_virtual_machines:
        show_resource = ShowResource.VIRTUAL_MACHINE

    client = Client(
        endpoint=endpoint,
        cert=None if (
            cert_filepath is None or key_filepath is None
        ) else (cert_filepath, key_filepath),
        verify=verify_cert,
    )

    with closing(client.api.session):
        print_resources(
            client,
            gib,
            show_resource,
        )
