class PaginationSortOrder:
    Descending = 'desc'
    Ascending = 'asc'


class PaginationOptions:
    def __init__(
            self,
            next: str = None,
            # unix time in milliseconds
            start: int = None,
            # unix time in milliseconds
            end: int = None,
            # Allegedly: BE will default this to 2000 items, limited by the max items returned by dynamo
            # However, it seems to return 500 each time even with a custom page_size specified
            page_size: int = 2000,
            # See PaginationSortOrder options - backend defaults to descending
            sort: str = PaginationSortOrder.Descending,
    ):
        self.next = next
        self.start = start
        self.end = end
        self.page_size = page_size
        self.sort = sort

    def to_params(self) -> dict:
        params = {}
        if self.next:
            params['next'] = self.next
        if self.start:
            params['start'] = self.start
        if self.end:
            params['end'] = self.end
        if self.page_size:
            params['pageSize'] = self.page_size
        if self.sort:
            params['sort'] = self.sort

        return params
