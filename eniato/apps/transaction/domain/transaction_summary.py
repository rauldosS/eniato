class TransactionSummary:

    def __init__(self, attributes={}):
        self.period = attributes.get('period')
        self.daily_balances = attributes.get('daily_balances')
        self.period_balance = attributes.get('period_balance')
        self.expected_period_balance = attributes.get('expected_period_balance')
        self.balance = attributes.get('balance')
        self.total_income = attributes.get('total_income')
        self.total_expense = attributes.get('total_expense')
        self.total_expected_income = attributes.get('total_expected_income')
        self.total_expected_expense = attributes.get('total_expected_expense')
        self.expected_balance = attributes.get('expected_balance')
