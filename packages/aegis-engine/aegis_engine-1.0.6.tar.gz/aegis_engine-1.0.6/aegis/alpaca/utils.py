import alpaca.config as config
import alpaca_trade_api as tradeapi

class Alpaca:
    def __init__(self):
        self.api = tradeapi.REST(
            key_id = config.Keys.API_KEY,
            secret_key = config.Keys.SECRET_KEY,
            base_url = config.Keys.BASE_URL,
            api_version = config.Keys.VERSION)

    def get_trades(self, symbol, n, len):
        trades = self.get_barset(symbol)

    def get_account(self):
        account = self.api.get_account()
        return account

    def get_order(self, order_id):
        return self.api.get_order(order_id)

    def list_orders(self, **kwargs):
        return self.api.list_orders(**kwargs)

    def submit_order():
        pass

    def cancel_order(self, order_id):
        return self.api.cancel_order(order_id)

    def cancel_all_orders(self):
        return self.api.cancel_all_orders()

    def list_positions(self):
        return self.api.list_positions()
    
    def get_position(self, symbol):
        return self.api.get_position(symbol)

    def list_assets(self, status = "active", asset_class = "us-equity"):
        """
        Can change asset_class to None to see all assets!
        """
        #assets = self.api.list_assets(status, asset_class)
        # for some godamn reason the above doesn't work, need to re-instantiate
        assets = Alpaca().api.list_assets()
        return assets

    def get_asset(self, symbol):
        return self.api.get_asset(symbol)

    def get_clock(self):
        return self.api.get_clock()

    def get_calender(self):
        return self.api.get_calendar()

    def get_portfolio_history(self):
        pass