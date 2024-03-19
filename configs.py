from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "24140079"))
    API_HASH = getenv("API_HASH", "d4ba07c6bbfd05e8b52dd77880ff254b")
    BOT_TOKEN = getenv("BOT_TOKEN", "7161484675:AAExvBgDPmV6Yjy2TRJtM1P_7wco94t1jJQ")
    FSUB = getenv("FSUB", "i_i_r")
    CHID = int(getenv("CHID", "-1002066339648"))
    SUDO = list(map(int, getenv("SUDO", "6460393623,926877758").split(',')))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://bot:08550855@cluster0.m8ckqxo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()
