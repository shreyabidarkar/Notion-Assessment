import requests, json
import pandas as pd

token = 'secret_8S6G5rUoMgTWpbiMEz2iybjbePMyPdOg6urGn1Kagrg'
databaseId = 'c68e5afc5e55436b926df98300fd138f'

headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2022-02-22"
}

def readDatabase(databaseId, headers):
    readUrl = f"https://api.notion.com/v1/databases/{databaseId}/query"

    res = requests.request("POST", readUrl, headers=headers)
    print(res.status_code)
    #print(res.text)
    df = pd.DataFrame.from_dict(res)
    print(df)

    data = res.json()

    with open('./db.json', 'w', encoding ='utf8') as f:
        json.dump(data, f, ensure_ascii = False)


def createPage(databaseId, headers, book_name, book_rating, favorite):
    createUrl = 'https://api.notion.com/v1/pages'

    # newPageData = {
    #     "parent": {"database_id": databaseId},
    #     "properties": {
    #         "Description": {
    #             "title": [
    #                 {
    #                     "text": {
    #                         "content": "Review"
    #                     }
    #                 }
    #             ]
    #         },
    #         "Value": {
    #             "rich_text": [
    #                 {
    #                     "text": {
    #                         "content": "Amazing"
    #                     }
    #                 }
    #             ]
    #         },
    #         "Status": {
    #             "rich_text": [
    #                 {
    #                     "text": {
    #                         "content": "Active"
    #                     }
    #                 }
    #             ]
    #         }
    #     }
    # }

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
                "content": book_rating
              }
            }
          ]
        },
        "Favorite": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {
                        "content": favorite
                    }
                }
            ]
        }
      }
    }


    data = json.dumps(newPageData)
    # print(str(uploadData))

    res = requests.request("POST", createUrl, headers=headers, data=data)

    print(res.status_code)
    print(res.text)

def updatePage():
    pass

readDatabase(databaseId, headers)
#createPage(databaseId, headers, 'ssssss', '1', '2')

def readCsv():
    df = pd.read_csv('ratings.csv')
    print(df)
# readCsv()