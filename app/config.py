import os

from dotenv import load_dotenv
from motor_decorator import profile_clusters, add_cluster

# local running
dotenv_path = os.path.join(os.path.dirname(__file__), "../local/.env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# Mongo
MONGO_HOST_MAIN = os.getenv("MONGO_HOST_MAIN")
MONGO_PORT_MAIN = int(os.getenv("MONGO_PORT_MAIN"))
MONGO_USER_MAIN = os.getenv("MONGO_USER_MAIN")
MONGO_PASSWORD_MAIN = os.getenv("MONGO_PASSWORD_MAIN")

MONGO_HOST_LOCAL = os.getenv("MONGO_HOST_LOCAL")
MONGO_PORT_LOCAL = int(os.getenv("MONGO_PORT_LOCAL"))
MONGO_USER_LOCAL = os.getenv("MONGO_USER_LOCAL")
MONGO_PASSWORD_LOCAL = os.getenv("MONGO_PASSWORD_LOCAL")


def init_db_clusters() -> None:
    add_cluster("MAIN", MONGO_USER_MAIN, MONGO_PASSWORD_MAIN, MONGO_HOST_MAIN, MONGO_PORT_MAIN)
    add_cluster("LOCAL", MONGO_USER_LOCAL, MONGO_PASSWORD_LOCAL, MONGO_HOST_LOCAL, MONGO_PORT_LOCAL)
    profile_clusters(ping=True)


init_db_clusters()


def check_variables() -> None:
    all_elements = globals()

    variables = {
        element: value for element, value in all_elements.items()
        if isinstance(element, str) and element.isupper()
    }

    for variable, value in variables.items():
        if value is None:
            raise TypeError(f"Variable: {variable} is None. Check .env file path to loading.")


check_variables()

PROXY_ON = True

PROXY_LIST = [
    "http://Suip9R:DATUKesQuj@46.8.110.53:1050",
    "http://Suip9R:DATUKesQuj@77.83.149.112:1050",
    "http://Suip9R:DATUKesQuj@109.248.166.47:1050",
    "http://Suip9R:DATUKesQuj@109.248.167.22:1050",
    "http://Suip9R:DATUKesQuj@45.15.237.157:1050",
    "http://Suip9R:DATUKesQuj@45.87.253.204:1050",
    "http://Suip9R:DATUKesQuj@45.15.72.91:1050",
    "http://Suip9R:DATUKesQuj@46.8.222.213:1050",
    "http://Suip9R:DATUKesQuj@46.8.156.184:1050",
    "http://Suip9R:DATUKesQuj@45.151.145.215:1050",
    "http://Suip9R:DATUKesQuj@45.15.237.88:1050",
    "http://Suip9R:DATUKesQuj@188.130.218.138:1050",
    "http://Suip9R:DATUKesQuj@188.130.187.156:1050",
    "http://Suip9R:DATUKesQuj@194.156.97.40:1050",
    "http://Suip9R:DATUKesQuj@46.8.11.105:1050",
    "http://Suip9R:DATUKesQuj@45.140.55.201:1050",
    "http://Suip9R:DATUKesQuj@45.11.20.107:1050",
    "http://Suip9R:DATUKesQuj@109.248.167.94:1050",
    "http://Suip9R:DATUKesQuj@46.8.16.120:1050",
    "http://Suip9R:DATUKesQuj@46.8.193.198:1050",
    "http://Suip9R:DATUKesQuj@46.8.154.64:1050",
    "http://Suip9R:DATUKesQuj@45.142.253.114:1050",
    "http://Suip9R:DATUKesQuj@45.90.196.69:1050",
    "http://Suip9R:DATUKesQuj@109.248.14.24:1050",
    "http://Suip9R:DATUKesQuj@188.130.136.18:1050",
    "http://Suip9R:DATUKesQuj@192.144.31.248:1050",
    "http://Suip9R:DATUKesQuj@45.84.177.211:1050",
    "http://Suip9R:DATUKesQuj@31.40.203.148:1050",
    "http://Suip9R:DATUKesQuj@176.53.186.153:1050",
    "http://Suip9R:DATUKesQuj@188.130.184.34:1050",
    "http://Suip9R:DATUKesQuj@46.8.107.140:1050",
    "http://Suip9R:DATUKesQuj@45.134.253.236:1050",
    "http://Suip9R:DATUKesQuj@46.8.14.28:1050",
    "http://Suip9R:DATUKesQuj@194.32.229.38:1050",
    "http://Suip9R:DATUKesQuj@46.8.16.203:1050",
    "http://Suip9R:DATUKesQuj@45.15.73.18:1050",
    "http://Suip9R:DATUKesQuj@188.130.221.205:1050",
    "http://Suip9R:DATUKesQuj@45.87.252.99:1050",
    "http://Suip9R:DATUKesQuj@45.145.117.37:1050",
    "http://Suip9R:DATUKesQuj@188.130.143.77:1050",
    "http://Suip9R:DATUKesQuj@194.34.248.24:1050",
    "http://Suip9R:DATUKesQuj@176.53.186.95:1050",
    "http://Suip9R:DATUKesQuj@46.8.107.54:1050",
    "http://Suip9R:DATUKesQuj@45.81.137.247:1050",
    "http://Suip9R:DATUKesQuj@109.248.54.212:1050",
    "http://Suip9R:DATUKesQuj@46.8.154.216:1050",
    "http://Suip9R:DATUKesQuj@95.182.125.23:1050",
    "http://Suip9R:DATUKesQuj@77.83.148.158:1050",
    "http://Suip9R:DATUKesQuj@109.248.55.61:1050",
    "http://Suip9R:DATUKesQuj@45.142.253.48:1050",
    "http://Suip9R:DATUKesQuj@95.182.124.22:1050",
    "http://Suip9R:DATUKesQuj@188.130.189.147:1050",
    "http://Suip9R:DATUKesQuj@77.94.1.81:1050",
    "http://Suip9R:DATUKesQuj@188.130.128.30:1050",
    "http://Suip9R:DATUKesQuj@46.8.223.214:1050",
    "http://Suip9R:DATUKesQuj@46.8.11.186:1050",
    "http://Suip9R:DATUKesQuj@188.130.187.195:1050",
    "http://Suip9R:DATUKesQuj@46.8.17.216:1050",
    "http://Suip9R:DATUKesQuj@45.139.125.234:1050",
    "http://Suip9R:DATUKesQuj@109.248.143.214:1050",
    "http://Suip9R:DATUKesQuj@193.58.169.234:1050",
    "http://Suip9R:DATUKesQuj@45.84.176.54:1050",
    "http://Suip9R:DATUKesQuj@77.94.1.148:1050",
    "http://Suip9R:DATUKesQuj@185.181.244.88:1050",
    "http://Suip9R:DATUKesQuj@46.8.156.225:1050",
    "http://Suip9R:DATUKesQuj@45.81.137.72:1050",
    "http://Suip9R:DATUKesQuj@45.142.252.195:1050",
    "http://Suip9R:DATUKesQuj@31.40.203.198:1050",
    "http://Suip9R:DATUKesQuj@45.15.236.244:1050",
    "http://Suip9R:DATUKesQuj@194.156.92.27:1050",
    "http://Suip9R:DATUKesQuj@45.84.177.193:1050",
    "http://Suip9R:DATUKesQuj@92.119.193.31:1050",
    "http://Suip9R:DATUKesQuj@109.248.142.187:1050",
    "http://Suip9R:DATUKesQuj@176.53.186.81:1050",
    "http://Suip9R:DATUKesQuj@194.35.113.154:1050",
    "http://Suip9R:DATUKesQuj@194.32.237.180:1050",
    "http://Suip9R:DATUKesQuj@188.130.185.208:1050",
    "http://Suip9R:DATUKesQuj@176.53.186.7:1050",
    "http://Suip9R:DATUKesQuj@213.226.101.8:1050",
    "http://Suip9R:DATUKesQuj@45.135.32.124:1050",
    "http://Suip9R:DATUKesQuj@109.248.49.178:1050",
    "http://Suip9R:DATUKesQuj@188.130.129.124:1050",
    "http://Suip9R:DATUKesQuj@45.135.33.127:1050",
    "http://Suip9R:DATUKesQuj@45.145.116.21:1050",
    "http://Suip9R:DATUKesQuj@45.81.137.177:1050",
    "http://Suip9R:DATUKesQuj@45.142.253.198:1050",
    "http://Suip9R:DATUKesQuj@194.156.97.59:1050",
    "http://Suip9R:DATUKesQuj@45.145.119.222:1050",
    "http://Suip9R:DATUKesQuj@45.144.36.78:1050",
    "http://Suip9R:DATUKesQuj@45.15.236.122:1050",
    "http://Suip9R:DATUKesQuj@185.181.247.123:1050",
    "http://Suip9R:DATUKesQuj@45.15.237.96:1050",
    "http://Suip9R:DATUKesQuj@192.144.31.212:1050",
    "http://Suip9R:DATUKesQuj@194.156.97.126:1050",
    "http://Suip9R:DATUKesQuj@188.130.218.166:1050",
    "http://Suip9R:DATUKesQuj@45.84.177.189:1050",
    "http://Suip9R:DATUKesQuj@45.15.237.162:1050",
    "http://Suip9R:DATUKesQuj@45.145.118.48:1050",
    "http://Suip9R:DATUKesQuj@192.144.31.12:1050",
    "http://Suip9R:DATUKesQuj@45.81.137.25:1050"
]
