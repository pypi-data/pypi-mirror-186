import polars as pl
import shutil
import typer
import os
from pathlib import Path
from typing import List, Tuple, Dict, Union, Optional, Any, Iterator, TypeVar

from iotree.core.render.funcs import basic_pbar, rich_func_chainer


from pisql.core.isql import iSQL, check_sql, iSqlDF
from pisql.core.isql_config import init_isql, iSqlCFG
from pisql.utils.render import console, errors

from pisql.utils.paths import (
    base_dir, tests_dir, package_dir, assets_dir, data_dir, pisql_home
)

isql = init_isql()

run = typer.Typer(
    name="run",
    help=f"""Activates query mode: execute queries  against a Sybase ASE database . Is able to process many .sql files  and even directories ",  
    [yellow][bold]Aliases:[/] q , :: [/]  

    [green][bold]Example:[/]  

    >>> pisql q ++ name.sql cool.sql[/] [dim]# Execute multiple files[/]
    """,
    rich_markup_mode="rich",
    rich_help_panel="rich",
)

def splitSqlScript(sqlScriptFile: Union[str, Path, os.PathLike]) -> List[Path]:
    """Split a SQL script into a list of queries"""
    sqlScriptFile = Path(sqlScriptFile)
    raw = open(sqlScriptFile, "r").read()
    queries = raw.replace("go", "GO").split("GO")

    if not isinstance(queries, list):
        return [sqlScriptFile]
    elif len(queries) <= 2:
        if not all( check_sql(query) for query in queries):
            return [sqlScriptFile]

    queries = [query.strip() for query in queries if check_sql(query.strip()) ]
    filenames = [sqlScriptFile.stem+"-subquery-"+str(idx)+".sql" for idx in range(len(queries))]
    
    tmpdir = pisql_home.joinpath('tmp')
    tmpdir.mkdir(exist_ok=True)

    pathnames = [tmpdir.joinpath(filename) for filename in filenames]
    for pathname, query in zip(pathnames, queries):
        with open(pathname, "w+") as f:
            f.write(query)
    return pathnames

def cleanSplitScriptDir(pathnames: List[Path]) -> None:
    """Clean up the temporary directory of split SQL scripts"""
    for pathname in pathnames:
        os.remove(pathname)
    tmpdir = pisql_home.joinpath('tmp')
    shutil.rmtree(tmpdir)


@run.command(name="//", help="Execute a query  against a Sybase ASE database . Accepts a dir  of .sql files  or a list of files")
def runall(
    args : List[Path],
    outdir: Path = typer.Option(None, "--outdir", "-o", help="Output directory for results"),
    ) -> None:
    """Execute a query  against a Sybase ASE database . Accepts a dir  of .sql files  or a list of files"""
    files = []
    tmpfiles = []

    outdir = pisql_home / "results" if outdir is None else Path(outdir).resolve()
    outdir = outdir.parent if outdir.is_file() else outdir
    outdir.mkdir(exist_ok=True)

    for arg in args:
        arg = Path(arg).resolve()
        if arg.is_dir():
            files += [file for file in arg.iterdir() if file.suffix == ".sql"]
        elif arg.is_file():
            splitRes = splitSqlScript(arg)
            if splitRes is None:
                files.append(arg)
            else:
                files += splitRes
                if len(splitRes) > 1:
                    tmpfiles += splitRes
        else:
            raise ValueError(f"Invalid file or directory : {arg}")
    
    last_idx = 0
    callback = lambda *args : "subquery" in args[0].name
    for idx, df in rich_func_chainer(isql.run_sql_file, files, console=console, condition_innerloop=callback):
        if idx is None:
            errors.print(f"🔥 Error: {df}")
            write_idx = last_idx+1 if last_idx > 0 else 0
            open(outdir / f"error-{files[write_idx].stem}.log", "w+").write(str(df))
            continue
        else:
            df.write_parquet( outdir / f"results-{files[idx].stem}.parquet", compression="lz4")
            open(outdir / f"{files[idx].stem}.raw", "w+").write(isql.raw)
            last_idx = idx
    
    cleanSplitScriptDir(tmpfiles)
    console.print(f"✅ Done, Results saved to {pisql_home / 'results'}")


@run.command(name="++", help="Execute a list of queries  against a Sybase ASE database . Accepts a dir  of .sql files  or a list of files")
def runallAlias(
    args : List[str],
    ) -> None:
    """Execute a query  against a Sybase ASE database . Accepts a dir  of .sql files  or a list of files"""
    runall(args=args)


def listTablesServer() -> None:
    """List all tables  in the server """
    querytxt = """
    SELECT t.name as table_name, c.name as column_name
    FROM sysobjects t, syscolumns c
    WHERE t.id = c.id AND t.type IN ('U', 'V')
    """
    df = isql.query(querytxt)
    console.print(df)
    df.write_parquet(pisql_home / "results" / "tables.parquet", compression="lz4")

@run.command(name="tables?", help="List all tables  in the server . [bold yellow]Alias: `?`[/]")
def listTables() -> None:
    """List all tables  in the server """
    listTablesServer()

@run.command(name="?", help="List all tables  in the server ", hidden=True)
def listTables() -> None:
    """List all tables  in the server  [bold yellow]Alias: `tables?`[/]"""
    listTablesServer()
