# DollarGeneralScrape
Scraper for Data of the Dollar General Store

## Features
- Scrapes Dollar General Data for Informational purposes from https://www.dollargeneral.com/store-directory and puts them into excel and csv files.

## Data
There is a lot of data to process, so data is also provided in data.xlsx and data.csv.

## How to Use
1. Make sure to have python installed on your machine.

[Python Installation](https://www.python.org/downloads/)

2. cd into the project directory (wherever you saved it on your machine + "cd DollarScrape")

3. Create a virtual environment with "python -m venv venv" (assuming you've installed venv on your machine
   
5. Activate environment (should be "venv\Scripts\activate" on windows OR "source venv/bin/activate" on Mac assuming the environment is named venv)
   
7. Install the requirements with "pip install -r requirements.txt".

8. Adjust the config.py file in the util folder for whatever is needed. Tbh shouldn't need changing.

9. Run the program with "python main.py".
   
10. It will generate a csv/xlsx file.


## Disclaimer
Please note that web scraping may be subject to legal restrictions depending on the website's terms of service. It is recommended to review and comply with the website's policies before using this scraper. 

## License
This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/). Feel free to use, modify, and distribute this tool according to the terms of the license.

For any questions or feedback, please contact [flatwhitecoffey@gmail.com](mailto:flatwhitecoffey@gmail.com). Thank you for using ContactCongress!
