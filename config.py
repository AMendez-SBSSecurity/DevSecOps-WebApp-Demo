#Texts
import configparser

TEXT_TITLE_INDEX = "WebApp-Demo"
TEXT_EMPTY_PAGE = ["Hello World","To see the information, please deploy your app"]
TEXT_NAME_ITEM_MENU = ["List","Charts"]
TEXT_TITLE_CONTENT_TABLE = "List of clients"
TEXT_TITLE_CONTENT_CHART = "Charts"

config = configparser.ConfigParser()
config.read("app.properties")
print("#############")



#ENABLE APP
SHOW_APP = bool(config['Page']['appState'])
print(SHOW_APP)