"""
Auxiliary module to build the CLI commands
"""

import typer

from nuvla_cli.action_entity_cmd import list, create, remove, start, stop, locate
from nuvla_cli.entity_action_cmd import edge, fleet, user


def build_action_entity(app_cli: typer.Typer) -> None:
    """
    Builds the action entity commands around cli_app parameter

    :param app_cli: Main CLI app to build the commands upon
    :return: None
    """

    # Add commands
    app_cli.add_typer(create.app, name='create', help='Creates a new Nuvla entity: '
                                                      'edge, fleet, user')
    app_cli.add_typer(list.app, name='list', help='Lists Nuvla Components')
    app_cli.add_typer(remove.app, name='remove', help='Deletes a Nuvla entity: edge, '
                                                      'fleet')
    app_cli.add_typer(locate.app, name='locate',
                      help='Geo-locates an edge or fleet within a'
                           'country')
    app_cli.add_typer(start.app, name='start',
                      help='Runs a NuvlaEdge engine or imitates one'
                           'when dummy')
    # app_cli.add_typer(user.app, name='user')
    app_cli.add_typer(stop.app, name='stop', help='Stops a NuvlaEdge engine (or fleet)')

    app_cli.registered_commands += user.app.registered_commands


def build_entity_action(app_cli: typer.Typer) -> None:
    """
    Build the entity-action command around cli_app parameter
    :param app_cli: Main CLI app to build the commands upon
    :return: None
    """
    app_cli.add_typer(edge.app, name='edge', help='Edge management commands')
    app_cli.add_typer(fleet.app, name='fleet', help='Fleet management commands')
    app_cli.add_typer(user.app, name='user', help='User management commands')
    app_cli.registered_commands += user.app.registered_commands
