from ..core.isql import iSQL
from ..utils.local_store import iSqlConfig

iSqlCFG = iSqlConfig(app_name='pisql')

config_store = iSqlCFG.gCU()

def init_isql() -> iSQL:
    if not "server" in config_store or not "servers" in config_store:
        errors.print(
            f"""[bold]Welcome to [green]pisql[/][/]
            [bold][magenta]pisql[/bold] is a simple but rich command line interface for Sybase ASE[/]\n
            ❗❗[blink bold red]No server found in config[/]\n
            [bold red]> Please configure a server first[/]
            """
            )
        yes = Confirm.ask("Do you want to configure a server now?", default=True)
        if yes:
            sql_server = Prompt.ask("Server name")
            sql_user = Prompt.ask("Username")
            sql_password = Prompt.ask("Password", password=True)
            sql_db = Prompt.ask("Database")
            config_store["server"] = sql_server
            config_store["servers"] = {
                sql_server: {
                    "user": sql_user,
                    "password": sql_password,
                    "db": sql_db
                }
            }
            isqlcfg.setCU(config_store)
        else:
            console.print(
                f"""[bold red]Exiting...[/]
                [dim yellow]You can configure a server later with [/][bold]pisql config[/]
                """
                )
            sys.exit(0)
    else:
        if not "server" in config_store:
            errors.print(
                f"""[bold red]No default server found in config[/]
                [dim yellow]Please specify a server with [/][bold]pisql config[/]
                """
                )
            sys.exit(0)
        elif not config_store["server"] in config_store["servers"]:
            errors.print(
                f"""[bold red]Default server not found in config[/]
                [dim yellow]Please specify a server with [/][bold]pisql config[/]
                """
                )
            sys.exit(0)
        else:
            config = config_store["servers"][config_store["server"]]
            return iSQL(**config)
