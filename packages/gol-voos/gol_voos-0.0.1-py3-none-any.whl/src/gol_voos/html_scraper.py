from bs4 import BeautifulSoup
import re

def is_page_loaded_and_has_no_flights(driver):
    html = driver.page_source
    return html.find("Infelizmente não existem voo ou lugares disponíveis para a data solicitada.") != -1

def is_page_loaded_and_has_flights(driver):
    html = driver.page_source
    return html.find("Refazer busca de voo") != -1

def is_page_loaded(driver):
    return is_page_loaded_and_has_flights(driver) or is_page_loaded_and_has_no_flights(driver)

def get_flight_card_list(html):
     # get all divs in which the class name starts with "flight-card", uses regex
    soup = BeautifulSoup(html, 'html.parser')
    flight_card_list_primeira_metade = soup.find_all('div', {"aria-controls" : re.compile(r'^flight-')})
    flight_card_list_segunda_metade = soup.find_all('div', {"id" : re.compile(r'^flight-')})
    flight_card_list = [str(card_primeira) + str(card_segunda) for card_primeira, card_segunda in zip(flight_card_list_primeira_metade, flight_card_list_segunda_metade)]
    return flight_card_list

def is_flight_sold_out(card_html):
    # TODO: Check if this needs implementation
    return False

def get_prices_from_card(card_html):
    prices_found = re.findall(r'R\$\s\d*\.?\d+,\d+', str(card_html))
    prices = [int(price.replace('R$', '').replace(',', '').replace('.', ''))/100 for price in prices_found]
    return prices[1:] # Primeiro preço é repetido

def get_departure_time_from_card(card_html, origin):
    departure_time = re.findall(fr'{origin}\s-\s(\d+:\d+)', str(card_html))
    return departure_time[0]

def get_arrival_time_from_card(card_html, destination):
    arrival_time = re.findall(fr'{destination}\s-\s(\d+:\d+)', str(card_html))
    return arrival_time[0]

def get_flight_duration_from_card(card_html):
    flight_times = re.findall(r'\d+:\d+', str(card_html))
    flight_duration = flight_times[2]
    return flight_duration

def get_cod_voo(card_html):
    cod_voo = re.findall(r'flight-G(\d+)', str(card_html))
    return cod_voo[0]

def get_num_conexoes(card_html):
    num_conexoes = re.findall(r'(\d+)\sparad', str(card_html))
    if len(num_conexoes) == 0:
        return 0
    return int(num_conexoes[0])

def get_num_poltronas_livres(card_html):
    num_poltronas_livres = re.findall(r'(\d+)\sassento', str(card_html))
    if len(num_poltronas_livres) == 0:
        return 0
    return int(num_poltronas_livres[0])
    

    