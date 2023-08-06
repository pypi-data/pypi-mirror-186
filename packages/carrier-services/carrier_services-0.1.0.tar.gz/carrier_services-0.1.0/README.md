# carrier-services
Get carrier services from shipping lines.

## Installation
From [PyPI](https://pypi.org/project/carrier-services/):

    python -m pip install carrier-services

## Setup
The following setup must be done before running:
1. Install Google Chrome. Chrome version 109 or newer is required.
2. Create below environment variables in your OS environment:
    * `CS_SMTP_HOST`: SMTP host for sending notification emails
    * `CS_CONFLUENCE_TOKEN`: Token for uploading carrier service master to Wiki
<br/><br/>
3. Update below directory paths in `site-packages/carrier_services/utils/config.toml` for directory location of data files and log files. For example:
    ```
    [environment]
    directory.data = ""    # /home/user1/carrier_services/data"
    directory.log = ""     # /home/user1/carrier_services/log"
    ```
    If left empty, <user_home>/carrier_services/data & <user_home>/carrier_services/log will be used: 

## How to Use
carrier-services is a console application, named `carrier_services`.

    >>> python -m carrier_services
