import aminofix
from threading import Thread
from rich.console import Console
from menu import *
client = aminofix.Client()
console = Console()

def login(email, password):
    try:
        client.login(email = email, password = password)
        console.print(f'[bold red][NMT][/bold red] Logged in as {client.get_user_info(client.userId).nickname}.')
    except:
        console.print_exception(show_locals=False)

def get_path(link):
    path = client.get_from_code(link).path.split("/")
    comId = path[0].removeprefix("x")
    chatId = path[2]
    return [comId, chatId]

def path_community(link):
    if get_path(link)[0] not in str(client.sub_clients().comId):
        client.join_community(get_path(link)[0])
        console.print(f'[bold red][NMT][/bold red] Joined {client.get_community_info(get_path(link)[0]).name}.')
        sub_client = aminofix.SubClient(get_path(link)[0], profile = client.profile)
        return sub_client
    else:
        console.print(f'[bold red][NMT][/bold red] {client.get_user_info(client.userId).nickname} is already a member of {client.get_community_info(get_path(link)[0]).name}.')
        sub_client = aminofix.SubClient(get_path(link)[0], profile = client.profile)
        return sub_client

def path_chat(link, sub_client):
    if get_path(link)[1] not in str(sub_client.get_chat_threads().chatId):
        sub_client.join_chat(get_path(link)[1])
        console.print(f'[bold red][NMT][/bold red] Joined {sub_client.get_chat_thread(get_path(link)[1]).title}.')
        chatId = get_path(link)[1]
        return chatId
    else:
        console.print(f'[bold red][NMT][/bold red] Already a member of {sub_client.get_chat_thread(get_path(link)[1]).title}.')
        chatId = get_path(link)[1]
        return chatId

def spam(chatId, sub_client, message, messageType):
    with console.status("[bold red]Now spamming...") as status:
        while True:
            threads = [Thread(target = sub_client.send_message, args=(chatId, message, messageType)) for x in range(100)]
            for t in threads:
                t.start()

def main():
    option_list = main_menu()
    option = option_list[0]

    if option == "1":
        login(option_list[1], option_list[2])
        option_mc_mt = mt_mc_selection()

        if option_mc_mt == "2":
            link = console.input("[bold red][NMT][/bold red] Chat link. >>")
            comId = path_community(link)
            chatId = path_chat(link, comId)
            spam(chatId, comId, option_list[3], option_list[4])

        elif option_mc_mt == "1":
            thread_Ids = []
            threads_lists = []
            console.print("\n[bold red][NMT][/bold red] Enter links one by one, enter 0 to continue.\n")
            while True:
                i = str(console.input("[bold red][NMT][/bold red] >> "))
                if i == "0": 
                    print("\n")
                    break
                else:
                    chatId = get_path(i)[1]
                    comId = get_path(i)[0]
                    thread_Ids.append(chatId)
            thread_Ids.sort()

            if comId not in str(client.sub_clients().comId):
                client.join_community(comId)
                console.print(f'[bold red][NMT][/bold red] Joined {client.get_community_info(comId).name}.')
                sub_client = aminofix.SubClient(comId, profile = client.profile)
            else:
                console.print(f'[bold red][NMT][/bold red] {client.get_user_info(client.userId).nickname} is already a member of {client.get_community_info(comId).name}.')
                sub_client = aminofix.SubClient(comId, profile = client.profile)

            for chatId in thread_Ids:
                if chatId not in str(sub_client.get_chat_threads().chatId):
                    sub_client.join_chat(chatId)
                    console.print(f'[bold red][NMT][/bold red] Joined {sub_client.get_chat_thread(chatId).title}.')
                else:
                    console.print(f'[bold red][NMT][/bold red] Already a member of {sub_client.get_chat_thread(chatId).title}.')

            with console.status("[bold red]Now spamming...") as status:
                while True:
                    for chatId in thread_Ids:
                        threads_lists.append(list(Thread(target = sub_client.send_message, args=(chatId, option_list[3], option_list[4])) for x in range(100)))
                    for i in range(len(threads_lists)):
                        for j in range(len(threads_lists[i])):
                            threads_lists[i][j].start()
                    threads_lists.clear()

    elif option == "2":
        login(option_list[1], option_list[2])
        option_mc_mt = mt_mc_selection()

        if option_mc_mt == "2":
            print("\n")
        
            com = client.sub_clients()
            for name, comId in zip(com.name, com.comId):
                console.print(f'[bold white]{name}[/bold white] - [italic yellow]{comId}[/italic yellow]')

            comId = int(console.input("[bold red][NMT][/bold red] Community Id. >> "))
            print("\n")
            sub_client = aminofix.SubClient(comId = comId, profile = client.profile)

            chat = sub_client.get_chat_threads(start = 0, size = 100)
            for title, chatId in zip(chat.title, chat.chatId):
                console.print(f'[bold white]{title}[/bold white] - [italic yellow]{chatId}[/italic yellow]')

            chatId = str(console.input("[bold red][NMT][/bold red] Chat Id. >> "))
            print("\n")
            spam(chatId, sub_client, option_list[3], option_list[4])

        elif option_mc_mt == "1":
            thread_Ids = []
            threads_lists = []
            print("\n")
        
            com = client.sub_clients()
            for name, comId in zip(com.name, com.comId):
                console.print(f'[bold white]{name}[/bold white] - [italic yellow]{comId}[/italic yellow]')

            comId = int(console.input("[bold red][NMT][/bold red] Community Id. >> "))
            print("\n")
            
            sub_client = aminofix.SubClient(comId, profile = client.profile)

            chat = sub_client.get_chat_threads(start = 0, size = 100)
            for title, chatId in zip(chat.title, chat.chatId):
                console.print(f'[bold white]{title}[/bold white] - [italic yellow]{chatId}[/italic yellow]')
            console.print("\n[bold red][NMT][/bold red] Enter chatIds one by one, enter 0 to continue.\n")

            while True:
                chatId = str(console.input("[bold red][NMT][/bold red] >> "))
                if chatId == "0":
                    print("\n")
                    break
                else:
                    thread_Ids.append(chatId)
            thread_Ids.sort()

            with console.status("[bold red]Now spamming...") as status:
                while True:
                    for chatId in thread_Ids:
                        threads_lists.append(list(Thread(target = sub_client.send_message, args=(chatId, option_list[3], option_list[4])) for x in range(100)))
                    for i in range(len(threads_lists)):
                        for j in range(len(threads_lists[i])):
                            threads_lists[i][j].start()
                    threads_lists.clear()