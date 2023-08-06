import typer
import os
from pathlib import Path
from typing import List, Tuple, Dict, Union, Optional, Any, Iterator

from ..core.isql_config import init_isql, iSqlCFG
from ..utils.render import console, errors

config = typer.Typer(
    name='config',
    help='Configure your regular SQL in/out folders 😎\n[bold][yellow]Aliases:[/bold] c, conf, cfg[/]',
    no_args_is_help=True,
    rich_help_panel="rich",
    rich_markup_mode='rich',
)


@config.command(name='set', help='Set a new config value for this machine')
def set_config(
    key: str = typer.Argument(..., help='The key to set the config for'),
    value: str = typer.Argument(..., help='The value to set the config for'),
):
    iSqlCFG.modifyCU(key, value)
    console.print(f'✅ [bold][green]Config set[/bold] for user [yellow]{iSqlCFG.user}:[/yellow] [red]{key}={value}[/red][/green]')

@config.command(name='get', help='Get a config value for a given user')
def get_config(
    key: str = typer.Argument(..., help='The key to get the config for'),
):
    config = iSqlCFG.getCU()
    value = config[key]
    console.print(f'✅ [bold][green]Config get[/bold] for user [yellow]{iSqlCFG.user}:[/yellow] [red]{key}={value}[/red][/green]')
    console.print(value)

@config.command(name='del', help='Delete a config value for a given user')
def del_config(
    user: str = typer.Argument(..., help='The user to delete the config for'),
    key: str = typer.Argument(..., help='The key to delete the config for'),
    ):
    iSqlCFG.delUserConfig(user, key)
    console.print(f'✅ [bold][green]Config deleted[/bold] for user [yellow]{user}:[/yellow] [red]{key}[/red][/green]')

@config.command(name='list', help='List all config values for a given user')
def list_config(
    user: str = typer.Argument(..., help='The user to list the config for'),
    ):
    config = iSqlCFG.gCU()
    console.print(f'✅ [bold][green]Config list[/bold] for user [yellow]{iSqlCFG.user}:[/yellow][/green]')
    console.print(config)

@config.command(name='reset', help='Reset the config for the current user')
def reset_config():
    iSqlCFG.reset()
    console.print(f'✅ [bold][green]Config reset[/bold] for user [yellow]{iSqlCFG.user}:[/yellow][/green]')

@config.command(name='ulist', help='List all config values for the current user')
def list_user_config():
    console.print(f'✅ [bold][green]Config list[/bold] for user [yellow]{iSqlCFG.user}:[/yellow][/green]')
    console.print(iSqlCFG.gCU())
