from __future__ import annotations

from pydantic import BaseModel


class Response(BaseModel):
    success: bool


class ResError(Response):
    message: str


class ResOK(Response):
    site_id: int
    number_of_webhooks: int
    request_received_at: str
    request_fullfilled_at: str
    request_duration: float
