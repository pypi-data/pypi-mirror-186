class Endpoints:

    class GDP:
        # Endpoints.GDP.nominal
        nominal = "https://www.economy.com/{}/nominal-gross-domestic-product"
        real = "https://www.economy.com/{}/real-gross-domestic-product"
        
        class consumption:
            class private:
                # Endpoints.GDP.consumption.private.nominal
                nominal = "https://www.economy.com/{}/private-consumption"
                real = "https://www.economy.com/{}/real-private-consumption"
            class gov:
                # Endpoints.GDP.consumption.gov.nominal
                nominal = "https://www.economy.com/{}/government-consumption"
                real = "https://www.economy.com/{}/real-government-consumption"

        class investment:
            # Endpoints.GDP.investment.nominal
            nominal = "https://www.economy.com/{}/investment"
            real = "https://www.economy.com/{}/real-investment"
            
    class Price:
        # Endpoints.Price.cpi
        cpi = "https://www.economy.com/{}/consumer-price-index-cpi"
        ppi = "https://www.economy.com/{}/producer-price-index-ppi"

    class Labour:
        # Endpoints.Labour.employment
        employment = "https://www.economy.com/{}/total-employment"
        unemployment = "https://www.economy.com/{}/unemployment"
        unemp_rate = "https://www.economy.com/{}/unemployment-rate"
        labour_force = "https://www.economy.com/{}/labor-force"
        
        class salaries:
            # Endpoints.Labour.salaries.nominal
            nominal = "https://www.economy.com/{}/wage-and-salaries/"
            real = "https://www.economy.com/{}/real-wages-and-salaries/"
    
    class Trade:

        # Endpoints.Trade.current_account
        current_account = "https://www.economy.com/{}/current-account-balance"
        balance_of_goods = "https://www.economy.com/{}/balance-of-goods"

        class net_exports:
            # Endpoints.Trade.net_exports.nominal
            nominal = "https://www.economy.com/{}/net-exports"
            real = "https://www.economy.com/{}/real-net-exports"

        class goods_and_services:
            class imports:
                # Endpoints.Trade.goods_and_services.imports.nominal
                nominal = "https://www.economy.com/{}/imports-of-goods-and-services"
                real = "https://www.economy.com/{}/real-imports-of-goods-and-services"
            class exports:
                # Endpoints.Trade.goods_and_services.exports.nominal
                nominal = "https://www.economy.com/{}/exports-of-goods-and-services"
                real = "https://www.economy.com/{}/real-exports-of-goods-and-services"

    class Government:
        external_debt = "https://www.economy.com/{}/gross-external-debt"
        
        class income:
            revenue = "https://www.economy.com/{}/government-revenues"
            expenditure = "https://www.economy.com/{}/government-expenditures"
            budget_balance = "https://www.economy.com/{}/government-budget-balance"

        class public_debt:
            gross = "https://www.economy.com/{}/outstanding-public-debt"
            domestic = "https://www.economy.com/{}/outstanding-public-debt-domestic"
            foreign = "https://www.economy.com/{}/outstanding-public-debt-foreign"

    class Markets:
        lending_rate = "https://www.economy.com/{}/lending-rate"
        money_market_rate = "https://www.economy.com/{}/money-market-rate"

    class Housing:
        price_index = "https://www.economy.com/{}/house-price-index"
        dwelling_stocks = "https://www.economy.com/{}/dwelling-stocks"

        class house_value:
            existing = "https://www.economy.com/{}/house-price-value-for-existing-homes"
            new = "https://www.economy.com/{}/house-price-value-for-new-homes"
        
        class permits:
            residential = "https://www.economy.com/{}/residential-building-permits"
    
    class Consumer:
        confidence = "https://www.economy.com/{}/consumer-confidence"
        income = "https://www.economy.com/{}/personal-income"
        
        class retail_sales:
            nominal = "https://www.economy.com/{}/retail-sales"
            real = "https://www.economy.com/{}/real-retail-sales"
    class Business:
        confidence = "https://www.economy.com/{}/business-confidence"
        capacity_utilisation = "https://www.economy.com/{}/capacity-utilization"
        industrial_production = "https://www.economy.com/{}/industrial-production"

        class inventory_change:
            nominal = "https://www.economy.com/{}/change-in-inventories"
            real = "https://www.economy.com/{}/real-change-in-inventories"

    class Demographics:
        births = "https://www.economy.com/{}/births"
        deaths = "https://www.economy.com/{}/deaths"
        population = "https://www.economy.com/{}/population"
        net_migration = "https://www.economy.com/{}/net-migration"