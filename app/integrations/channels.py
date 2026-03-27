from abc import ABC, abstractmethod


class ChannelAdapter(ABC):
    channel_name: str

    @abstractmethod
    def send_message(self, recipient: str, body: str) -> dict:
        raise NotImplementedError

    @abstractmethod
    def fetch_updates(self) -> list[dict]:
        raise NotImplementedError


class PlaceholderAdapter(ChannelAdapter):
    def __init__(self, channel_name: str):
        self.channel_name = channel_name

    def send_message(self, recipient: str, body: str) -> dict:
        return {
            "status": "queued",
            "channel": self.channel_name,
            "recipient": recipient,
            "body": body,
            "note": "Placeholder adapter. Integrate vendor SDK/API later.",
        }

    def fetch_updates(self) -> list[dict]:
        return [{"channel": self.channel_name, "event": "no-op-placeholder"}]


ADAPTER_REGISTRY = {
    channel: PlaceholderAdapter(channel)
    for channel in ["email", "whatsapp", "telegram", "viber", "messenger", "instagram"]
}
