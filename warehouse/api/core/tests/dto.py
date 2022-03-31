from dataclasses import dataclass


@dataclass
class InputDto:
    @dataclass
    class RequestDto:
        product_id: int
        quantity: int
    request: RequestDto


@dataclass
class OutputDto:
    product_id: int
    quantity: int
