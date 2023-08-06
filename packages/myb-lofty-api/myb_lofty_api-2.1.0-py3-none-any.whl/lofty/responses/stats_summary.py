class StatsSummary:
    def __init__(self, stats_summary_data: dict):
        self.total_invested: int = stats_summary_data.get('totalInvested')
        self.total_returns: int = stats_summary_data.get('totalReturns')
        self.total_purchased: int = stats_summary_data.get('totalPurchased')


