class MockStub:
    @staticmethod
    def GetDiscount(*arg, **kwargs):  # pylint: disable=W0613
        return MockResponse()


class MockResponse:  # pylint: disable=R0903
    percentage: int = 0.05
