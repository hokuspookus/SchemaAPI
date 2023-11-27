from typing import Union
import requests
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
		CORSMiddleware,
		allow_origins=origins,
		allow_credentials=True,
		allow_methods=["*"],
		allow_headers=["*"],
)

def getRenderKey():
		url = "https://web.skola24.se/api/get/timetable/render/key"

		headers = {
				'Host': 'web.skola24.se',
				'Cookie': 'ASP.NET_SessionId=o0kadfvlouaannqpyiomivys',
				'Sec-Ch-Ua-Mobile': '?0',
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.141 Safari/537.36',
				'Content-Type': 'application/json',
				'Accept': 'application/json, text/javascript, */*; q=0.01',
				'X-Scope': '8a22163c-8662-4535-9050-bc5e1923df48',
				'X-Requested-With': 'XMLHttpRequest',
				'Sec-Ch-Ua-Platform': '',
				'Origin': 'https://web.skola24.se',
				'Sec-Fetch-Site': 'same-origin',
				'Sec-Fetch-Mode': 'cors',
				'Sec-Fetch-Dest': 'empty',
				'Referer': 'https://web.skola24.se/timetable/timetable-viewer/falkoping.skola24.se/%C3%85llebergsgymnasiet/',
				'Accept-Encoding': 'gzip, deflate',
				'Accept-Language': 'en-US,en;q=0.9',
		}

		response = requests.post(url=url, headers=headers, data='null')

		key = json.loads(response.text)['data']['key']

		return key

def getLessons():
		url = "https://web.skola24.se/api/render/timetable"

		headers = {
				'Host': 'web.skola24.se',
				'Content-Length': '675',
				'Sec-Ch-Ua': '',
				'Sec-Ch-Ua-Mobile': '?0',
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.141 Safari/537.36',
				'Content-Type': 'application/json',
				'Accept': 'application/json, text/javascript, */*; q=0.01',
				'X-Scope': '8a22163c-8662-4535-9050-bc5e1923df48',
				'X-Requested-With': 'XMLHttpRequest',
				'Sec-Ch-Ua-Platform': '',
				'Origin': 'https://web.skola24.se',
				'Sec-Fetch-Site': 'same-origin',
				'Sec-Fetch-Mode': 'cors',
				'Sec-Fetch-Dest': 'empty',
				'Referer': 'https://web.skola24.se/timetable/timetable-viewer/falkoping.skola24.se/%C3%85llebergsgymnasiet/',
				'Accept-Encoding': 'gzip, deflate',
				'Accept-Language': 'en-US,en;q=0.9',
				'Connection': 'close',
		}

		data = {
				"renderKey": getRenderKey(),
				"host": "falkoping.skola24.se",
				"unitGuid": "MzI1M2YxZjYtODM2OC1mN2EzLWE4Y2QtZWNmNjFiYTU2ZTk0",
				"schoolYear": "dc85b431-3067-41a5-970d-d332ea1dd9e6",
				"startDate": None,
				"endDate": None,
				"scheduleDay": 0,
				"blackAndWhite": False,
				"width": 1223,
				"height": 550,
				"selectionType": 4,
				"selection": "4-XCvraOSnw4dOwyE2ClD3gJyjlexw4Hl-OIdz0i-uGETtZwzWN-1tb2WPruKxNiTIlWV4LyJrKP5JCCsscspz0bCR-PxezB3Wg7ZSM6F84RSr6-1mqhFIkatTGh4ncY",
				"showHeader": False,
				"periodText": "",
				"week": 47,
				"year": 2023,
				"privateFreeTextMode": False,
				"privateSelectionMode": None,
				"customerKey": ""
		}

		response = requests.post(url=url, headers=headers, json=data)

		lessons = json.loads(response.text)['data']['lessonInfo']

		return lessons


@app.get("/")
def read_root():
		return {"Hello": "Worlds"}


@app.get("/get/render/key")
async def returnRenderKey():
		return { "key": getRenderKey() }


@app.get("/get/lessons")
async def returnLessons():
		return getLessons()