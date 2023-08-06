import logging
import timeit
import traceback
from datetime import datetime
from pathlib import Path
from string import Template
from time import sleep

import pandas as pd
from atlassian import Confluence

import carrier_services.iaau as iaau
from carrier_services import RUN_TIME, RUN_TIME_STR
from carrier_services.utils import get_config, get_environment, setup_directory
from carrier_services.utils import get_logger, format_log_message
from carrier_services.utils import send_notification


def process_iaau(output_file: Path) -> None:
    # global logs
    max_tries = CFG["iaau"]["max_tries"]
    retry_second = CFG["iaau"]["retry_second"]
    logger = logging.getLogger(name=CFG["logging"]["logger"])

    # Scraping
    cs_df = pd.DataFrame()
    for trial in range(1, max_tries + 1):
        try:
            page_source = iaau.scrape(CFG["iaau"]["url"])
            cs_df = iaau.parse(page_source)
            # if page_source:
            if len(cs_df) > 0:
                break
        except Exception as e:
            error_msg = format_log_message(traceback.format_exc() + " --- " + str(e))
            log = f"EXCEPTION: Scraping failed (Try: {trial}): {error_msg}"
            logger.error(log)
            logs.append(log)
            sleep(retry_second)
    log = f"Scraping completed. (Number of rows = {len(cs_df)})"
    logger.info(log)
    logs.append(log)

    if not cs_df.empty:
        # Export
        cs_df.to_csv(output_file, encoding="utf-8", index=False)
        log = f"Exporting data completed. (File = {output_file})"
        logger.info(log)
        logs.append(log)

        # Attach
        if CFG["wiki"]["enable"]:
            confluence = Confluence(url=CFG["wiki"]["url"], token=ENV["CS_CONFLUENCE_TOKEN"])
            result = confluence.attach_file(filename=str(output_file), page_id=CFG["iaau"]["output"]["page_id"],
                                            name=f'{CFG["iaau"]["output"]["filename"]}.csv',
                                            comment=RUN_TIME.strftime("%Y-%m-%d"))
        log = f'Attaching file to Wiki completed. (Enabled = {CFG["wiki"]["enable"]})'
        logger.info(log)
        logs.append(log)
    else:
        raise ValueError("No carrier service data can be retrieved.")


def main() -> None:
    # Init
    # global logs
    successful = False
    data_dir = setup_directory(CFG, PKG, "data")
    output_file = data_dir.joinpath(f'{CFG["iaau"]["output"]["filename"]}_{RUN_TIME_STR}.csv')
    log_dir = setup_directory(CFG, PKG, "log")
    log_file = log_dir.joinpath(CFG["logging"]["filename"].format(RUN_TIME_STR))
    logger = get_logger(name=CFG["logging"]["logger"], log_level=CFG["logging"]["level"],
                        log_format=CFG["logging"]["format"], log_file=str(log_file))
    start = timeit.default_timer()
    log = f"EXECUTION STARTED at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    logger.info(log)
    logs.append(log)

    try:
        # Process : IAAU
        process_iaau(output_file=output_file)
        successful = True
    except ValueError as e:
        log = f"EXCEPTION: Process failed: {str(e)}"
        logger.error(log)
        logs.append(log)
    except Exception as e:
        error_msg = format_log_message(traceback.format_exc() + " --- " + str(e))
        log = f"EXCEPTION: Process failed: {error_msg}"
        logger.error(log)
        logs.append(log)
    finally:
        # End
        elapsed = timeit.default_timer() - start
        log = f"EXECUTION ENDED at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} in {elapsed:0.1f} seconds!"
        logger.info(log)
        logs.append(log)

    # Sending notification email
    try:
        body_template = Template(CFG["email"]["body"])
        if successful:
            result_line = f'The process is completed <span style="font-weight:bold; color:green">' \
                          f'SUCCESSFULLY</span> in {elapsed:0.1f} seconds.'
        else:
            result_line = f'The process is <span style="font-weight:bold; color:red">' \
                          f'FAILED</span>. Please check the attached log for details.'
        log_summary = ""
        for log in logs:
            log_summary = log_summary + f'{log}<br>'
        body = body_template.substitute({"result_line": result_line, "log_summary": log_summary})
        attachments = []
        if log_file.exists():
            attachments.append(str(log_file))
        if output_file.exists():
            attachments.append(str(output_file))
        send_notification(host=ENV["CS_SMTP_HOST"], port=25, email_config=CFG["email"], body=body, files=attachments)
    except Exception as e:
        log = f"EXCEPTION: Sending notification email failed: {str(e)}"
        logger.error(log)


if __name__ == "__main__":
    # Global variables
    PKG = "carrier_services"
    CFG = get_config(PKG)
    ENV = get_environment(CFG["environment"]["variables"])
    logs = []
    main()
