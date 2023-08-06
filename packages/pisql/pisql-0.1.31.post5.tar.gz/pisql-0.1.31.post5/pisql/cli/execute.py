import polars as pl
import orjson
import typer
import os


from pathlib import Path
from iotree.core.render.funcs import basic_pbar
from typing import List, Tuple, Dict, Union, Optional, Any, Iterator, TypeVar


from pisql.core.isql import iSQL
from pisql.core.isql_config import init_isql
from pisql.utils.paths import (
    base_dir, tests_dir, package_dir
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
    override_default_dir: str = typer.Option(None, "-od", "--override-default-dir", help="Override the default directory . Defaults to `~/pisql`"),
    ) -> None:
    """Execute a query  against a Sybase ASE database . Accepts a .sql file \n[yellow][bold]Aliases:[/] exec, e, x[/]
    
    Args:
        file (str): The .sql file  to execute
        out (str, optional): The output file , defaults to rich table  on console. Defaults to None.
        override_default_dir (str, optional): Override the default directory . Defaults to `~/pisql`. Defaults to None.

        Returns:
            None: None"""
    

    file = Path(file)

    if not override_default_dir:
        dir = Path(os.path.expanduser("~")) / "pisql" / "results"
        dir.mkdir(parents=True, exist_ok=True)
    else:
        dir = Path(override_default_dir) if override_default_dir != "." else Path.cwd()
        dir.mkdir(parents=True, exist_ok=True)

    with basic_pbar() as pbar:
        task = pbar.add_task(f"Executing {file.name}", total=None)
        df = isql.run_sql_file(file)

        pbar.update(task, advance=50)
        pbar.update(task, description=f"Writing results to {dir}")

        csv_file = dir / f"{file.stem}.csv"
        parquet_file = dir / f"{file.stem}.parquet"
        raw_file = dir / f"{file.stem}.out"

        if out is None:
            open(raw_file, "w+").write(isql.raw)
            csv_out = df.write_csv(file=csv_file)
            parquet_out = df.write_parquet(file=parquet_file,  compression="lz4")
            records = orjson.loads(df.write_json(row_oriented=True))
            console.print(tableFromRecords(records, theme="default"))
        else:
            outfile = dir / file.name
            csv_out = df.write_csv(file=csv_file)
            parquet_out = df.write_parquet(file=parquet_file, compression="lz4")
            if out.lower() in ["json", "excel"]:
                errors.print(f"[bold red]Output format {out} not supported yet with the base version.[/]", style="bold red")
                errors.print(f"[dim yellow]Please install `pandas` to get excel support[/]")
                sys.exit(1)
        pbar.update(task, advance=50)
        pbar.update(task, description=f"✅ Done writing results to {dir}", completed=True)
        sys.exit(0)
