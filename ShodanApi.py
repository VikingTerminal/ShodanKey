import requests
from bs4 import BeautifulSoup
import shodan
import time

def print_with_typing_effect(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def input_with_typing_effect(prompt):
    print_with_typing_effect(prompt)
    user_input = input()
    return user_input

def shodan_information(api_key, target):
    try:
        api = shodan.Shodan(api_key)
        result = api.host(target)

        print_with_typing_effect(f"\033[92mIP: {result['ip_str']}\033[0m")
        print_with_typing_effect(f"\033[96mOrganizzazione: {result.get('org', 'N/A')}\033[0m")
        print_with_typing_effect(f"\033[96mPaese: {result.get('country_name', 'N/A')}\033[0m")
        print_with_typing_effect(f"\033[96mPorte aperte: {', '.join(map(str, result['ports']))}\033[0m")

        return result

    except shodan.APIError as e:
        print_with_typing_effect(f"\033[91mErrore Shodan: {e}\033[0m")
        return None

# Le altre funzioni rimangono inalterate

def main():
    try:
        shodan_api_key = input_with_typing_effect("\033[94mInserisci la tua chiave API Shodan:\033[0m ")
        target = input_with_typing_effect("\033[94mInserisci l'IP o il dominio di destinazione (scrivi 'exit' per uscire):\033[0m ")

        if target.lower() == 'exit':
            print_with_typing_effect("\033[93mGrazie per aver provato questo tool. Guarda altri tools su t.me/VikingTerminal.\033[0m")
        else:
            domain_or_ip = target.split('://')[-1].split('/')[0] if '://' in target else target

            shodan_result = shodan_information(shodan_api_key, domain_or_ip)
            web_scraping_result = web_scraping_information(domain_or_ip)

            save_option = input_with_typing_effect("\033[94mVuoi salvare i risultati in un file txt? (yes/no):\033[0m ").lower()
            if save_option == 'yes':
                filename = input_with_typing_effect("\033[94mInserisci il nome del file (senza estensione): \033[0m") + ".txt"
                if shodan_result:
                    save_to_file(filename, str(shodan_result))
                if web_scraping_result:
                    save_to_file(filename, str(web_scraping_result), append=True)

    except Exception as e:
        print_with_typing_effect(f"\033[91mErrore generale: {e}\033[0m")

if __name__ == "__main__":
    main()
