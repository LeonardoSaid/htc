class MockStub:
    @staticmethod
    def GetDiscount(*arg, **kwargs):
        return MockResponse()


class MockResponse:
    percentage: int = 0.05
