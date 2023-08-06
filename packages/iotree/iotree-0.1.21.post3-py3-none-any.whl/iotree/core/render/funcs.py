import rich
import warnings
from pathlib import Path
from itertools import cycle

from typing import Any, Callable, List, Dict, Iterable, Optional, Tuple, Union
from rich.console import Console
from rich.progress import (
    Progress, BarColumn, TextColumn,
    TimeRemainingColumn, TimeElapsedColumn,
    SpinnerColumn
)

from iotree.utils.paths import (
    package_dir, base_dir, config_dir, safe_config_load
)

symbols, themes, user_infos, local_config = safe_config_load()


def call_any(funcs: List[Callable], *args, **kwargs) -> Any:
    """Try all functions in a list until one succeeds."""
    for f in funcs:
        try:
            return f(*args, **kwargs)
        except Exception as e:
            continue
    if "msg" in kwargs:
        raise ValueError(f'All functions failed. {kwargs["msg"]}')
    else:
        msg = [
            f"\n - {funcs[0].__name__} failed with args: {args} and kwargs: {kwargs}" for f in funcs
        ]
        msg = "f'All functions failed:" + "".join(msg)
        raise ValueError(msg)
    

def format_user_theme(theme: Dict[str,str]) -> Dict[str,str]:
    """Format a user theme to be used by rich."""
    must_have = [
        "description", "complete",
        "finished", "remaining",
        "message"]
    
    default = {
        "description": "bold purple",
        "complete": "bold green3",
        "finished": "bold green3",
        "remaining": "bold pink3",
        "message": "magenta",
        "spinner": "dots",
        "bar_width": 70,
    }
    
    for mh in must_have:
        if mh in theme:
            default[mh] = theme[mh]
        for k, v in theme.items():
            if k.endswith(mh):
                default[k] = v
    return default

def apply_progress_theme(
    theme: Dict[str, str],
    console: Console = None,
    ) -> Progress:
    """Apply a theme to the progress bar."""
    theme = format_user_theme(theme)
    
    return Progress(
                SpinnerColumn(theme["spinner"]),
                TextColumn("{task.description}", justify="right", style=theme.get("task.description", theme["description"])),
                BarColumn(bar_width=None),
                "[progress.percentage]{task.percentage:>3.1f}%",
                TimeElapsedColumn(),
                TimeRemainingColumn(),
                console=console,
            )
    

def basic_pbar(
    console: Console = None,
    ) -> Progress:
    return apply_progress_theme(theme=format_user_theme({}), console=console)

def rich_func(func, *args, **kwargs) -> Any:
    """Run a function with rich progress bar."""
    args = [], kwargs = {}
    theme = kwargs.pop("theme") if "theme" in kwargs else format_user_theme({})
    console = kwargs.pop("console") if "console" in kwargs else Console()
    pbar = kwargs.pop("progress") if "progress" in kwargs else apply_progress_theme(theme=theme, console=console)
    with pbar:
        task_id = pbar.add_task(f"Running {func.__name__}", total=None)
        try:
            result = func(*args, **kwargs)
            pbar.update(task_id, advance=100)
        except Exception as e:
            pbar.console.print(f"[bold red]Error while running {func.__name__}[/bold red]")
            pbar.console.print(e)
            pbar.update(task_id, advance=100)
            raise e
    return result
    
        
    
def rich_func_chainer(
    funcs: List[Callable], params: List[Any],
    condition_innerloop: Optional[Callable] = lambda *params: False,
    *args, **kwargs
    ) -> Iterable[Tuple[Union[int, None], Any]]:
    """Run a list of functions with rich progress bar.
    
    If you want to customize the progress bar, you can pass a `progress` keyword argument.
    If you want to customize the console, you can pass a `console` keyword argument.
    If you want a specific color theme or style for the progress bar, you can pass a `theme` keyword argument.
    
    Args:
        funcs (List[Callable]): A list of functions to run.
        params (List[Any]): A list of parameters to pass to each function. They must be in the same order as the functions.
        condition_innerloop (Optional[Callable], optional): A function that takes as input the same parameters as the i-th callback and returns a boolean.
            If true, an inner loop will be run until the same callback returns False. Defaults to None.
        *args: Arguments to pass to each function. These will be passed to all functions.
        **kwargs: Keyword arguments to pass to each function. These will be passed to all functions.

    Returns:
        Iterable[Any]: An iterable of the results of each function + the index of the function that returned the result.
            if the function raised an exception, the index will be None, and the result will be the exception.
    """
    if not isinstance(funcs, Iterable):
        funcs = [funcs]
    if len(funcs) < len(params):
            funcs = funcs*len(params) if len(funcs) == 1 else cycle(funcs)
    else:
        warnings.WarningMessage("The number of functions must be < than number of parameters or must be the same.", "Incorrect Value", str(__file__), 0)
    
    progress = kwargs.pop("progress", None)
    console = kwargs.pop("console", None)
    theme = kwargs.pop("theme", None)
    
    if console is None:
        console = Console()
    if progress is None:
        if theme is None:
            progress = Progress(
                SpinnerColumn(),
                TextColumn("[bold purple]{task.description}", justify="left"),
                BarColumn(bar_width=None),
                "[progress.percentage]{task.percentage:>3.1f}%",
                TimeElapsedColumn(),
                TimeRemainingColumn(),
                console=console,
            )

        else:
            progress = apply_progress_theme(theme=theme, console=console)

    errs = []
    current_loop_task = None
    
    fmt_params = []
    callback_params = []
    for p in params:
        if not isinstance(p, Iterable):
            sp = p.name if isinstance(p, Path) else str(p)
            fmt_params.append(sp)
            callback_params.append([p])
        else:
            sp = ",".join([x.name if isinstance(x, Path) else str(x) for x in p])
            fmt_params.append(sp)
            callback_params.append(p)

    with progress:
        main_task = progress.add_task("Running functions", total=len(funcs))
        for i, f in enumerate(funcs):
            main_loop_task = progress.add_task(f"Running ƒ(●) := {f.__name__}({fmt_params[i]})", total=None)
            if condition_innerloop(*callback_params[i]):
                if not current_loop_task:
                    inner_loop_task = progress.add_task(f"Running inner task {f.__name__}", total=None)
                    current_loop_task = inner_loop_task
            else:
                if current_loop_task:
                    progress.remove_task(current_loop_task)
                    current_loop_task = None
                    progress.update(main_loop_task, complete=True)
                    progress.remove_task(main_loop_task)
                    main_loop_task = progress.add_task(f"Running ƒ(●) ≔ {f.__name__}({fmt_params[i]})", total=None)
            try:
                if isinstance(callback_params[i], list):
                    result = f(*callback_params[i], *args, **kwargs)
                elif isinstance(callback_params[i], dict):
                    result = f(*args, **callback_params[i], **kwargs)
                else:
                    result = f(callback_params[i], *args, **kwargs)
                
                progress.update(current_loop_task, complete=True) if current_loop_task else None
                progress.update(main_loop_task, complete=True) if not current_loop_task else None
                progress.update(main_task, advance=1)
                progress.remove_task(main_loop_task)
                progress.remove_task(current_loop_task) if current_loop_task else None
                progress.refresh()

                yield i, result

            except Exception as e:
                progress.console.print(f"[bold red]Error while running {f.__name__}[/bold red]")
                progress.console.print(e)
                progress.update(main_loop_task, complete=True)
                progress.update(main_task, advance=1)
                errs.append(e)
                yield None, e
            
    if errs:
        fmt_errs = '\n - '.join([str(e) for e in errs])
        raise ValueError(f"Errors while running functions: {fmt_errs}")