import polars as pl
import orjson
import typer
import os


from pathlib import Path
from iotree.core.render.funcs import basic_pbar
from typing import List, Tuple, Dict, Union, Optional, Any, Iterator, TypeVar


from ..core.isql import iSQL
from ..utils.render import console, errors
from ..core.isql_config import init_isql
from ..utils.paths import (
    base_dir, tests_dir, package_dir, pisql_home
)

isql = init_isql()

exe = typer.Typer(
    name="execute",
    help=f"""Execute a query against a Sybase ASE database . Accepts a .sql file ",
    [yellow][bold]Alias:[/] exec, e, x[/]  
    [green][bold]Example:[/]  
    >>> pisql x name.sql[/]
    """,
    rich_markup_mode="rich",
    rich_help_panel="rich",
)


@exe.callback(invoke_without_command=True, no_args_is_help=True, help="Execute a query against a Sybase ASE database . Accepts a .sql file ")
def executer(
    file: str = typer.Argument(..., help="The .sql file  to execute"),
    out: str = typer.Option(None, "-o", "--out", "--out-file", help="The output file , defaults to rich table  on console"),
    ) -> None:
    """Execute a query  against a Sybase ASE database . Accepts a .sql file \n[yellow][bold]Aliases:[/] exec, e, x[/]
    
    Args:
        file (str): The .sql file  to execute
        out (str, optional): The output file , defaults to rich table on console. Defaults to None.

        Returns:
            None: None"""
    

    file = Path(file)
    file = file.resolve()

    if not file.exists():
        console.print(errors(f"File {file} does not exist"))
        raise typer.Exit(1)
    outdir = Path(out).resolve().parent if out else pisql_home / "results"
    outfile = Path(out).resolve().name if out else file.stem
    out.parent.mkdir(parents=True, exist_ok=True)

    with basic_pbar() as pbar:
        task = pbar.add_task(f"Executing {file.name}", total=None)
        df = isql.run_sql_file(file)

        pbar.update(task, advance=50)
        pbar.update(task, description=f"Writing results to {dir}")

        if out.lower() in ["console", "rich", "stdout"]:
            console.print(f"[bold yellow]Writing raw output to stdout only.[/]")
            records = orjson.loads(df.write_json(row_oriented=True))
            console.print(tableFromRecords(records, theme="default"))
        else:
            writepath = outdir / outfile
            open(f"{writepath}.raw", "w+").write(isql.raw)
            csv_out = df.write_csv(file=f"{writepath}.csv")
            parquet_out = df.write_parquet(file=f"{writepath}.parquet",  compression="lz4")
            records = orjson.loads(df.write_json(row_oriented=True))
            console.print(tableFromRecords(records, theme="default"))

        pbar.update(task, advance=50)
        pbar.update(task, description=f"✅ Done writing results to {dir}", completed=True)
        sys.exit(0)
