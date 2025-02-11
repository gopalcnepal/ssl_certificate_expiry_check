
<!-- ABOUT THE PROJECT -->
## About The Project

On January 22, 2025, Let's Encrypt announced that they will be [Ending Support for Expiration Notification Emails](https://letsencrypt.org/2025/01/22/ending-expiration-emails/) starting June 4, 2025. 
So in this project, I want to create a Python script to monitor the list of domains you will provide and check its expiry date. Once it reaches the limit of days you have provided, the slack webhook notification is triggered using the  CICD pipeline.


### Built With

* [Python](https://www.python.org/)
* [Slack](https://slack.com/)


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Download and install Python 3 for your system [https://www.python.org/](https://www.python.org/)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/username/repo-name.git
   ```
2. Navigate to the project directory
   ```sh
   cd ssl_expiry_script/
   ```
3. Install requests python module
   ```sh
   pip3 install requests
   ```
3. Create OS environment variable for `DOMAINS`, `SLACK_WEBHOOK_URL`, `DAYS_LEFT`

4. Then run the script
   ```sh
   python3 ssl_check.py
   ```
