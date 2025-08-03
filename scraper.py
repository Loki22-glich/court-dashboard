# scraper.py
import requests
from bs4 import BeautifulSoup

def fetch_case_data(case_type, case_number, filing_year):
    url = "https://services.ecourts.gov.in/ecourtindia_v6/?p=casestatus/index"

    payload = {
        "state_code": "HR",
        "dist_code": "FBD",
        "court_code": "HRFBD0001",  # Example court
        "case_type": case_type,
        "case_number": case_number,
        "case_year": filing_year
    }

    headers = {
        "User-Agent": "Mozilla/5.0",
    }

    session = requests.Session()
    response = session.post(url, data=payload, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Now parse key fields
    try:
        parties = soup.find("td", text="Petitioner Vs. Respondent").find_next("td").text.strip()
        filing_date = soup.find("td", text="Filing Number & Date").find_next("td").text.strip()
        next_hearing = soup.find("td", text="Next Hearing Date").find_next("td").text.strip()
        pdf_link = soup.find("a", text="View")["href"]

        data = {
            "Parties": parties,
            "Filing Date": filing_date,
            "Next Hearing": next_hearing,
            "PDF": "https://services.ecourts.gov.in" + pdf_link
        }

        return data, response.text

    except Exception as e:
        raise Exception("Unable to parse case data. Case might not exist or format has changed.")
