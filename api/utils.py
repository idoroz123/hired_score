import csv
import json
import urllib.request
import ssl
from datetime import datetime


def get_candidates_json() -> dict:
    url = "https://recruiting-test-resume-data.hiredscore.com/allcands-full-api_hub_b1f6-acde48001122.json"
    context = ssl._create_unverified_context()
    web_url = urllib.request.urlopen(url, context=context)
    data = web_url.read()
    encoding = web_url.info().get_content_charset("utf-8")
    json_data = json.loads(data.decode(encoding))
    return json_data

def read_candidates_csv_file() -> dict:
    data = []
    with open("linkedin_source_b1f6-acde48001122.csv", mode="r", encoding="utf-8") as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]  
    return data

def calculate_gap(start_date: str, end_date: str) -> str:
    date_format = "%b/%d/%Y"
    
    try:
        start = datetime.strptime(start_date, date_format)
        end = datetime.strptime(end_date, date_format)
        
        gap = (start - end).days 
        return str(gap).replace("-", "") + " days"
    except ValueError:
        return "Invalid Date Format"


def format_experience(experiences: list) -> dict[str, str]:
    experience_list = []
    # reversing the list to calculate from first job to latests
    experiences.reverse() 
    for i in range(len(experiences)):
        experience_dict = experiences[i].copy()
        experience = {}
        title = experience_dict.get("title", "")
        start_date = experience_dict.get("start_date", "")
        end_date = experience_dict.get("end_date", "")
        
        # Calculate gap only for the previous job and the current one
        if i > 0:
            prev_end_date = experiences[i-1].get("end_date", "")
            experience["gap"] = calculate_gap(prev_end_date, start_date)
        else:
            experience["gap"] = ""  # No gap for the first job
        
        experience["title"] = title
        experience["start_date"] = start_date
        experience["end_date"] = end_date
        experience_list.append(experience)
    
    return experience_list


def get_linked_in_url(phone_number: str, csv_data:dict[str, str]) -> str:
    res = None
    for data in csv_data:
        if data.get("Phone Number") == phone_number:
            res = data.get("Linkedin", "")
        return res