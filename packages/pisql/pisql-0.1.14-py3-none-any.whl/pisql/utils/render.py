from rich.console import Console

console = Console(markup=True, color_system="truecolor", emoji=True, record=True)

errors = Console(
    markup=True, color_system="truecolor",
    emoji=True, record=True, stderr=True)