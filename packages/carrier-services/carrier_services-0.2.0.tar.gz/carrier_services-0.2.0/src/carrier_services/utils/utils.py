import csv
import logging
import os
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from importlib import resources
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def csv_to_dict(csv_file: str) -> dict:
    csv_dict = {}
    with open(csv_file, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            csv_dict[row["Key"]] = row["Value"]
    return csv_dict


def get_driver(headless: bool = False) -> webdriver:
    options = Options()
    # options.add_experimental_option("detach", True)
    # Bypass the USB: usb_device_handle_win.cc:1046 Failed to read descriptor from node connection:
    # A device attached to the system is not functioning.(0x1F) error
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_experimental_option("prefs", {"download.default_directory": OUTPUT_DIR})
    #???options.page_load_strategy = "normal"
    if headless:
        options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--start-maximized")
    # options.add_argument("--ignore-certificate-errors")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    return driver


def send_notification(host: str, port: int, email_config: dict, body: str, files: list) -> None:
    msg = MIMEMultipart()
    mail_from = email_config["from"]
    mail_to = email_config["to"]
    mail_cc = email_config["cc"]
    subject = email_config["subject"]

    msg["from"] = mail_from
    msg["to"] = mail_to
    if mail_cc: msg["cc"] = mail_cc
    msg["subject"] = subject
    msg.attach(MIMEText(body, "html"))
    for file in files:
        with open(file, "rb") as f:
            attachment = MIMEApplication(f.read())
            attachment.add_header("Content-Disposition", "attachment", filename=Path(file).name)
            msg.attach(attachment)

    with smtplib.SMTP(host=host, port=port) as smtp:
        smtp.send_message(msg)


def setup_directory(config: dict, pkg_name: str, dir_name: str) -> Path:
    # Use path in config.toml if available, otherwise use <home-path>\automations\<PKG>\<name>
    if config["environment"]["directory"][dir_name]:
        directory = Path(config["environment"]["directory"][dir_name])
    else:
        directory = Path.home().joinpath(pkg_name, dir_name)
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def format_log_message(msg: str = "") -> str:
    return msg.replace("\n", "\\n")


def get_logger(name: str, log_level: int, log_format: str, log_file: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    formatter = logging.Formatter(log_format)
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    # Add handlers
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger


def get_environment(env_vars: list) -> dict:
    environment = {}
    for env_var in env_vars:
        environment[env_var] = os.environ[env_var]
    return environment


def get_config(pkg_name: str) -> dict:
    config = {}
    if len(sys.argv) <= 1:
        cfg_file = "config.toml"
    else:
        cfg_file = f"config.{sys.argv[1]}.toml"
    config = tomllib.loads(resources.read_text(f"{pkg_name}.utils", cfg_file, encoding="utf-8"))
    return config

