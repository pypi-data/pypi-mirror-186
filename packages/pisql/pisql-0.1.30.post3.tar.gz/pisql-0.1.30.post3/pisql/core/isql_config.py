import sys
from rich.prompt import Confirm, Prompt
from ..core.isql import iSQL
from ..utils.render import console, errors
from ..utils.local_store import iSqlConfig

iSqlCFG = iSqlConfig('pisql')

def interactive_init():
    config_store = iSqlCFG.getCU()
    yes = Confirm.ask("Do you want to configure a server now?", default=True)
    if yes:
        sql_server = Prompt.ask("Server name")
        sql_user = Prompt.ask("Username")
        sql_password = Prompt.ask("Password", password=True)
        sql_db = Prompt.ask("Database")
        config_store["server"] = sql_server
        config_store["servers"] = {
            sql_server: {
                "server": sql_server,
                "user": sql_user,
                "password": sql_password,
                "db": sql_db
            }
        }
        iSqlCFG.setCU(config_store)
    else:
        console.print(
            f"""[bold red]Exiting...[/]
            [dim yellow]You can configure a server later with [/][bold]pisql config[/]
            """
            )
        sys.exit(0)

def init_isql() -> iSQL:

    incomplete = False
    inexistant = False
    
    config_store = iSqlCFG.getCU()
    
    if not "server" in config_store or not "servers" in config_store:
        inexistant = True
        incomplete = True
    else:
        if not "server" in config_store:
            errors.print(
                f"""[bold red]No default server found in config[/]
                [dim yellow]Please specify a server with [/][bold]pisql config[/]
                """
                )
            incomplete = True
        elif not config_store["server"] in config_store["servers"]:
            errors.print(
                f"""[bold red]Default server not found in config[/]
                [dim yellow]Please specify a server with [/][bold]pisql config[/]
                """
                )
            incomplete = True
        else:

            config = config_store["servers"][config_store["server"]]
            if any(
                not x in config
                for x in ["server", "user", "password", "db"]
            ):
                errors.print(
                    f"""[bold red]Incomplete config[/]
                    [dim yellow]Please specify a server with [/][bold]pisql config[/]
                    """
                    )
                incomplete = True
            else:
                return iSQL(
                    server=config["server"],
                    user=config["user"],
                    password=config["password"],
                    db=config["db"]
                )
    if inexistant:
        errors.print(
            f"[bold]Welcome to [green]pisql[/][/]\n" +
            f"[bold][magenta]pisql[/bold] is a simple but rich command line interface for Sybase ASE[/]\n" +
            f"❗❗[blink bold red]No server found in config[/]\n[bold red]> Please configure a server first[/]"
            )
    if incomplete:
        console.print("[bold red]Incomplete config.[/] We will now ask you to configure a server")
        interactive_init()
        return init_isql()
