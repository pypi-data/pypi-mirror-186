class Keys:
    API_KEY = "PKP7SP9B0PTMLPWYUNNE"
    SECRET_KEY = "YQ2NrcMosATo4bHKcy0a9u4DkXPpcFxUEk6D1Z2g"
    BASE_URL = "https://paper-api.alpaca.markets"
    VERSION = "v2"

class Endpoints:
    def __init__(self):
        self.data = self.Data()
        self.trading = self.Trading()
            
    class Data:
        def __init__(self):
            self.ROOT_URL = "https://data.alpaca.markets/v2"
            self.TRADE_URL = self.ROOT_URL+"GET/v2/stocks/{symbol}/trades"
            self.QUOTES_URL = self.ROOT_URL+"GET/v2/stocks/{symbol}/quotes"
            self.BARS_URL = self.ROOT_URL+"GET/v2/stocks/{symbol}/bars"

    class Trading:
            def __init__(self):
                self.PAPER_ENDPOINT = "https://paper-api.alpaca.markets"