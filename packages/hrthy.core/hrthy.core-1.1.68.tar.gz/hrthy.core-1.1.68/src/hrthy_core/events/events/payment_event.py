from hrthy_core.events.events.base_event import BaseEvent, CompanyBasePayload


class PaymentConfirmedPayload(CompanyBasePayload):
    total_licenses: int


class PaymentConfirmedEvent(BaseEvent):
    type = 'PaymentConfirmedEvent'
    payload: PaymentConfirmedPayload
