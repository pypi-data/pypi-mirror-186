
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

from gol_voos import html_scraper, util, dates
from selenium import webdriver
import time



class Query:
    def __init__(self, origem, destino, data_ida):
        self.origem = origem
        self.destino = destino
        self.data_original = data_ida # Data no formato DD/MM/YYYY armazenada
        dates.check_date_is_valid(data_ida)
        dates.check_date_is_in_future(data_ida)
        self.data_ida = data_ida.replace('/', '-')

    def __str__(self):
        return f'Origem: {self.origem}, Destino: {self.destino}, Data de ida: {self.data_original}'

    def __repr__(self):
        return str(self)


def read_html(url, driver):
    driver.get(url)
    wait = WebDriverWait(driver, timeout = 60, poll_frequency = 0.5)

    try:
        wait.until(html_scraper.is_page_loaded)
    except:
        print('Timeout, trying again')
        try:
            driver.refresh()
            wait.until(html_scraper.is_page_loaded)
        except:
            print('Timeout again, returning None')
            return None

    if not html_scraper.is_page_loaded_and_has_flights(driver):
        return None
    html = driver.page_source
    return html


def get_flight_data_from_card(card_html, query):
    ''' Given a card html, returns a dictionary with flight data.
        Returns None if the flight is sold out.'''
    flight_dict = dict()
    if html_scraper.is_flight_sold_out(card_html):
        return None
    prices = html_scraper.get_prices_from_card(card_html)
    flight_dict['preco-light'] = prices[0]
    flight_dict['preco-plus'] = prices[1]
    flight_dict['preco-max'] = prices[2]
    flight_dict['partida'] = html_scraper.get_departure_time_from_card(card_html, query.origem)
    flight_dict['chegada'] = html_scraper.get_arrival_time_from_card(card_html, query.destino)
    flight_dict['duração'] = html_scraper.get_flight_duration_from_card(card_html)
    flight_dict['paradas'] = html_scraper.get_num_conexoes(card_html)
    flight_dict['codigo-voo'] = html_scraper.get_cod_voo(card_html)
    flight_dict['poltronas-livres'] = html_scraper.get_num_poltronas_livres(card_html)
    return flight_dict


def get_data_from_single_query(query, driver, verbose=False):
    url = util.query_to_url(query)

    if verbose:
        time_start = time.time()
        print(f'Query: {query.origem} -> {query.destino} ({query.data_ida})')
        print(f'URL: {url}')
    
    html = read_html(url, driver)
    if html is None:
        return((query, []))

    flight_card_list = html_scraper.get_flight_card_list(html)
    flights_from_query = []
    for card in flight_card_list:
        if card is not None:
            flights_from_query.append(get_flight_data_from_card(card, query))

    if verbose:
        print(f'Found {len(flights_from_query)} flights')
        print('List of flights:')
        for flight in flights_from_query:
            print(flight)
        time_end = time.time()
        print(f'Tempo de execução: {(time_end - time_start):.2f} segundos')
        print()
    
    return flights_from_query


def get_flight_data(query_list, driver, verbose=False):
    '''
    Given a list of queries in the format (origem, destino, MM/DD/YYYY),
    returns a list of tuples with queries and flight data.
    TODO: sleep_time is the minimum time to wait between requests.
    '''
    scraped_data = []
    for query in query_list:
        scraped_data.append(get_data_from_single_query(query, driver, verbose))
    return scraped_data


class FlightScraper:
    def __init__(self, options=None, verbose=False):
        self.verbose = verbose
        self.options = options
        
        if self.options is None:
            self.options = Options()
            self.options.page_load_strategy = 'eager' # makes driver.get() faster
        try:
            self.driver = webdriver.Chrome(options=self.options)
        except:
            print('Chrome driver not found. Downloading...')
            util.download_chrome_driver()
            self.driver = webdriver.Chrome(options=self.options)
        self.driver.set_window_size(1280, 720) # If window size is too small, the wrong page will load
        self.driver.minimize_window()

    def scrape(self, query_list):
        '''
        Given a list of queries in the format (origem, destino, MM/DD/YYYY),
        returns a list of tuples with queries and flight data.
        '''
        return get_flight_data(query_list, self.driver, verbose=self.verbose)

    def close(self):
        self.driver.quit()

def main():
    # Query list example:
    origem = 'BSB'
    destino = 'VCP'
    dates = ['04/02/2023', '05/02/2023', '10/02/2023']
    queries = [Query(origem, destino, date) for date in dates]
    queries = [Query('IOS', 'MGF', '14/02/2023')] + queries
    myScraper = FlightScraper(verbose=True)
    result = myScraper.scrape(queries)

if __name__ == '__main__':
    main()
