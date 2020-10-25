import requests
import pytest

url_ddg = "https://api.duckduckgo.com"
president_text = []
us_presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson", "Van Buren", "Harrison", "Tyler",
                 "Polk", "Taylor", "Fillmore", "Pierce", "Buchanan", "Lincoln", "Johnson", "Grant", "Hayes", "Garfield",
                 "Arthur", "Cleveland", "McKinley", "Roosevelt", "Taft", "Wilson", "Harding", "Coolidge", "Hoover", "Truman",
                 "Eisenhower", "Kennedy", "Nixon", "Ford", "Carter", "Reagan", "Bush", "Clinton", "Obama", "Trump"]


def test_us_presidents():
    resp = requests.get(url_ddg + "/?q=presidents+of+the+united+states&format=json")
    rsp_text = resp.json()
    for x in rsp_text["RelatedTopics"]:
        president_text.append("{Text}".format(**i))
    for p in us_presidents:
        assert any(p in x for x in president_text)



# def test_us_presidents():
#     resp = requests.get(url_ddg + "/?q=presidents+of+the+united+states&format=json")
#     rsp_data = resp.json()
#     assert "NO" in rsp_data["RelatedTopics"]

# url_ddgPres = "https://api.duckduckgo.com/?q=presidents+of+the+united+states&format=json"
#
# response = requests.get(url_ddgPres)
# rsp_data = response.json()
# # print(rsp_data["RelatedTopics"])
#
# for i in rsp_data["RelatedTopics"]:
#     president_text.append("{Text}".format(**i))
#     # print("{Text}".format(**i))
#
# # print(president_text)
# for x in us_presidents:
#     if any(x in y for y in president_text):
#         print(x)
