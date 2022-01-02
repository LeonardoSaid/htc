import traceback
import grpc

from connections.discount_grpc import discount_pb2_grpc, discount_pb2
from utils.exceptions import ServerException

from config.settings import LOGGER


class DiscountConnection:

    def __init__(self, host: str):
        self.host = host
        self.channel = grpc.insecure_channel(self.host)
        self.stub = discount_pb2_grpc.DiscountStub(self.channel)
        LOGGER.debug("Connected to Discount Service")

    def get_discount_percentage(self, product_id: int) -> float:
        try:
            query = discount_pb2.GetDiscountRequest(productID=product_id)
            response = self.stub.GetDiscount(query)
            return response.percentage

        except Exception as error:
            LOGGER.debug(traceback.format_exc())
            LOGGER.error(f"Failed to get discount percentage - {error}")
            raise ServerException from error
