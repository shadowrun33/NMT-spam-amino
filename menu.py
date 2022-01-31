from rich.console import Console
from rich.table import Table
def main_menu():
    console = Console()
    table = Table()
    ascii = """
███    ██ ███    ███ ████████ 
████   ██ ████  ████    ██    
██ ██  ██ ██ ████ ██    ██    
██  ██ ██ ██  ██  ██    ██    
██   ████ ██      ██    ██    
    """
    table.add_column("Options", header_style = "bold red", style = "green")
    table.add_column("Script by https://github.com/shadowrun33.", header_style= "italic yellow", style = "italic white")
    table.add_row("[bold red][1][/bold red]Use only chat(s) url.", "Preferable if you're using fake account and don't want to manualy join community and chat(s).")
    table.add_row("[bold red][2][/bold red]Choose community and chat(s) manually.", "The old way.")
    table.add_row("[bold red][0][/bold red]Exit.", "")
    console.print(ascii, style="bold red", highlight=False)
    console.print(table)
    option = console.input("[bold red][NMT][/bold red] Choose option. >> ")
    if option == "0": 
        exit()
    email = console.input("[bold red][NMT][/bold red] Email. >> ")
    password = console.input("[bold red][NMT][/bold red] Password. >> ")
    message = console.input("[bold red][NMT][/bold red] Message. >> ")
    messageType = console.input("[bold red][NMT][/bold red] Message type. >> ")
    return [option, email, password, message, messageType]

def mt_mc_selection():
    console = Console()
    table = Table()
    table.add_column("Options", header_style = "bold red", style = "green")
    table.add_column("", style = "italic white")
    table.add_row("[bold red][1][/bold red]Multiple chats spam.", "Spam in multiple chats from one community.")
    table.add_row("[bold red][2][/bold red]Single chat spam.", "Spam in one chat.")
    table.add_row("[bold red][0][/bold red]Exit.", "")
    console.print(table)
    option = console.input("[bold red][NMT][/bold red] Choose option. >> ")
    if option == "0": 
        exit()
    return option