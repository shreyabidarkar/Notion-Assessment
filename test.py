import requests, json
import pandas as pd
from pandas import json_normalize
import re
import numpy as np

token = 'secret_8S6G5rUoMgTWpbiMEz2iybjbePMyPdOg6urGn1Kagrg'
databaseId = 'c68e5afc5e55436b926df98300fd138f'

headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2022-02-22"
}

def parse_rating():
    colnames = ['Book name', 'Member name', 'Book rating']
    df = pd.read_csv('ratings.csv', names=colnames, header=None)

    # Removed extra whitespaces

    df_re_1 = df.replace(to_replace=' +', value=' ', regex=True)
    df_re_1['Book name'] = df_re_1['Book name'].str.strip()
    df_re_1['Member name'] = df_re_1['Member name'].str.strip()

    # Change to camel case
    df_re_1['Book name'] = df_re_1['Book name'].str.title()

    # Check for rating between 0 and 5 inclusive
    df_re_2 = df_re_1[df_re_1['Book rating'] >= 0]
    df_re_2 = df_re_1[df_re_1['Book rating'] <= 5]

    # Multiple ratings for the same member and book, we should only use the last one
    df_re_2 = df_re_2[df_re_2.duplicated(subset=['Book name', 'Member name'], keep="last")]

    df3 = df_re_2.groupby('Book name', as_index=False)['Book rating'].mean()
    df4 = df_re_2.groupby('Book name', as_index=False).apply(lambda df_re_2: sum(df_re_2['Book rating'] == 5))
    df4.columns = df4.columns.fillna('Favorites')

    result = pd.merge(df3, df4)
    result = result.sort_values(by=['Favorites'], ascending=False)

    return result


def readDatabase(databaseId, headers):
    readUrl = f"https://api.notion.com/v1/databases/{databaseId}/query"

    res = requests.request("POST", readUrl, headers=headers)
    # print(res.text)
    #
    # print(res.content)

    print(res.status_code)
    #print(res.text)

    data = res.json()
    df = pd.DataFrame.from_dict(res)
    with open('./db.json', 'w', encoding ='utf8') as f:
        json.dump(data, f, ensure_ascii = False)
    # data2 = json.load(open('db.json'))
    #
    # df = pd.DataFrame(data2)
    print(df)

    with open('./db.json', 'w', encoding ='utf8') as f:
        json.dump(data, f, ensure_ascii = False)



def createPage(databaseId, headers, book_name, book_rating, favorite):
    createUrl = 'https://api.notion.com/v1/pages'

    newPageData = {
      "parent": {
        "database_id": databaseId
      },
      "properties": {
        "Book name": {
          "title": [
            {
              "text": {
                "content": book_name
              }
            }
          ]
        },
        "Book rating": {
          "rich_text": [
            {
              "type": "text",
              "text": {
                "content": str(book_rating)
              }
            }
          ]
        },
        "Favorite": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {
                        "content": str(favorite)
                    }
                }
            ]
        }
      }
    }


    data = json.dumps(newPageData)

    res = requests.request("POST", createUrl, headers=headers, data=data)

    print(res.status_code)
    print(res.text)

result = parse_rating()

for index, row in result.iterrows():
    book_name = row['Book name']
    book_rating = row['Book rating']
    favorites = row['Favorites']

    createPage(databaseId, headers, book_name, book_rating, favorites)

#readDatabase(databaseId, headers)
createPage(databaseId, headers, 'ssssss', '1', '2')