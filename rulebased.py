import re, random
from colorama import Fore, init

init(autoreset = True)

destination = {
"beaches":["bali","Maldives","Phuket"],
"mountains":["Swiss alps","Rocky Mountains","Himalaya"],
"cities":["Tokyo","Paris","New York"],
}

jokes = {
"Why dont programers like nature?Too many bugs",
"Why did the computer go to the doctor?Becasue it had a virus!",
"Why do travelers alwasy feel warm? Because of all their hot spots!",
}

def normalize_input(text):
    print(Fore.CYAN + "AI BOT: beaches,mountains, or cities?")
    preference = input(Fore.YELLOW + "you:")
    preference = normalize_input(preference)

    if preference in destination:
        suggestion = random.choice(destination[preference])
        print(Fore.GREEN +("AI BOT: Awesome! enjoy",suggestion,"!"))
        print(Fore.CYAN + "AI BOT: Do you like it? (Yes/NO)")
        answer = input(Fore.YELLOW + "YOU:").lower()

        if answer =="yes":
            print(Fore.GREEN + "AI BOT: awesome! enjoy",suggestion)
        elif answer == "no":
            print(Fore.RED + "AI BOT: lETS TRY ANOTHER.")
        