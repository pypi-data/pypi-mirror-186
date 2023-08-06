from importlib import resources
from time import sleep

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager

from carrier_services import P44_CS_HEADERS
from carrier_services.utils import csv_to_dict, get_driver

# Global variables
PKG = "carrier_services"
CARRIER_CODE = "IAAU"
TIMEOUT_PAGE_LOAD = 20
TIMEOUT_INTERNAL = 2
CODE_TABLE_UNLOCODE = csv_to_dict(str(resources.path(f"{PKG}.resources",
                                                     f"code_table_unlocode_{str.lower(CARRIER_CODE)}.csv")))
WEEKDAY = {"MON": 0, "TUE": 1, "WED": 2, "THU": 3, "FRI": 4, "SAT": 5, "SUN": 6}


def get_unlocode(name: str) -> str:
    if name in CODE_TABLE_UNLOCODE:
        return CODE_TABLE_UNLOCODE[name]
    else:
        if "PORT KLANG" in name:
            return "MYPKG"
        else:
            return name


def calculate_tt(start_day: str, end_day: str, same_day_as_zero: bool = True) -> int:
    tt = 0
    if start_day in WEEKDAY and end_day in WEEKDAY:
        tt = WEEKDAY[end_day] - WEEKDAY[start_day]
        if tt < 0: tt += 7
        if tt == 0 and not same_day_as_zero: tt += 7
    return tt


def scrape(url: str) -> str:
    page_source = ""
    driver = get_driver()
    driver.get(url)
    print(f"---> Opening {url}...")
    wait = WebDriverWait(driver, TIMEOUT_PAGE_LOAD)
    # Wait until the page is completely loaded by checking if the "Back to top" button is available
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class = 'btn_top']")))
    sleep(TIMEOUT_INTERNAL)
    page_source = driver.page_source
    driver.close()
    return page_source


def parse(page_source: str) -> pd.DataFrame:
    pses = []
    df = pd.DataFrame(columns=P44_CS_HEADERS)
    soup = BeautifulSoup(page_source, "html.parser")

    # Service code, Trade name, Service name
    svc_data = {}
    svc_grps = soup.find_all("ul", class_="listStyle2")     # e.g., Intra-Asia (Japan Service)
    for svc_grp in svc_grps:
        trade = svc_grp.previous_sibling    # e.g., Intra-Asia (Japan Service)
        svcs = svc_grp.find_all("li")   # e.g., New Super 1 Service (NS1)
        for svc in svcs:
            # TODO: Process svc_str only if non-empty and match pattern
            svc_str = svc.text.strip()
            svc_name = svc_str[:svc_str.rfind("(") - 1]
            svc_code = svc_str[svc_str.rfind("(") + 1: -1]
            svc_data[svc_code] = [trade.text, svc_name]

    # Service table
    tables = soup.find_all("table", class_="table_style3 routes overview")
    if len(tables) > 0:
        dfs = pd.read_html(str(tables))
        # For each service
        for table_index, df in enumerate(dfs):
            # if table_index != 10:
            #     continue
            # print(df)
            # print("-------------------------------------")
            col_count = -1
            order = -1
            change_mode = ""
            alliance_id = ""
            alliance_pool_id = ""
            trade_id = ""
            oi_service_id = ""
            carrier_id = CARRIER_CODE
            service_code = ""
            service_id = ""
            # No direction provided on Interasia website
            service = ""
            direction = ""
            if not "Rolling Schedule" in df.values:
                frequency = "WEEKLY"
            else:
                frequency = "OTHER"
            related_ids = ""
            prev_port_etd_day = ""
            tt = 0
            for (colName, colData) in df.items():
                col_count += 1
                # 1st column contains no port stop information but service code only
                if col_count == 0:
                    service_code = colData.values[0]
                    service_id = service_code + " [L]"
                    trade_id = svc_data.get(service_code, ["", ""])[0]
                    service = svc_data.get(service_code, ["", ""])[1]
                    direction = ""
                else:
                    port_code = get_unlocode(colData.values[0])
                    eta_day = colData.values[1]
                    etd_day = colData.values[2]
                    tt_within_port = calculate_tt(start_day=eta_day, end_day=etd_day)
                    if prev_port_etd_day:
                        tt_between_ports = calculate_tt(start_day=prev_port_etd_day, end_day=eta_day)
                    else:
                        tt_between_ports = 0
                    prev_port_etd_day = etd_day
                    # Output "L" record
                    order += 1
                    tt += tt_between_ports
                    # print(service_id, service, direction, eta_day, port_code, order, tt, "L")
                    pses.append([change_mode, alliance_id, alliance_pool_id, trade_id, oi_service_id,
                                     carrier_id, service_id, service, direction, frequency,
                                     eta_day, port_code, order, tt, "L",
                                     related_ids])

                    # Output "D" record
                    order += 1
                    tt += tt_within_port
                    # print(service_id, service, direction, etd_day, port_code, order, tt, "D")
                    pses.append([change_mode, alliance_id, alliance_pool_id, trade_id, oi_service_id,
                                     carrier_id, service_id, service, direction, frequency,
                                     etd_day, port_code, order, tt, "D",
                                     related_ids])
                    df = pd.DataFrame(pses, columns=P44_CS_HEADERS)
    return df
