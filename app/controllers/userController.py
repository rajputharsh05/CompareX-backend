import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
load_dotenv()
import os

target_url = os.getenv("TARGET_URL")

def get_userInfo(username: str):

    url = f"{target_url}{username}"

    headers = {
        "Accept": "*/*",
        "User-Agent": "Thunder Client (https://www.thunderclient.com)",
    }

    response = requests.get(url, headers=headers)


    soup = BeautifulSoup(response.text, 'html.parser')

    print(soup.text)

    constest_rating = soup.find_all(class_="text-label-1 dark:text-dark-label-1 flex items-center text-2xl")
    global_rank = soup.find_all(class_="text-label-1 dark:text-dark-label-1 font-medium leading-[22px]")
    total_constest_attended = soup.find_all(class_="hidden md:block")
    total_problem_solved = soup.find_all(class_="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 transform cursor-default text-center")
    easy_solved = soup.find_all(class_="flex w-full items-end text-xs")
    community_stats = soup.find_all(class_="flex items-center space-x-2 text-[14px]")

    fetched_info = {}

    fetched_info["constest_rating"] = [div.text for div in constest_rating]
    fetched_info["global_rank"] = [div.text for div in global_rank]
    fetched_info["total_constest_attended"] = [div.text for div in total_constest_attended]
    fetched_info["total_problem_solved"] = [div.text for div in total_problem_solved]
    fetched_info["easy_solved"] = [div.text for div in easy_solved]
    fetched_info["community_stats"] = [div.text for div in community_stats]

    print(fetched_info)

    return fetched_info

