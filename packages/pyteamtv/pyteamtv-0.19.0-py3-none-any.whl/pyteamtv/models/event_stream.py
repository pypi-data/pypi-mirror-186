from .teamtv_object import TeamTVObject


class EventStream(TeamTVObject):
    @property
    def event_stream_id(self):
        return self._event_stream_id

    @property
    def endpoint_urls(self):
        return self._endpoint_urls

    def __repr__(self):
        return f"<EventStream event_stream_id={self.event_stream_id}>"

    def _use_attributes(self, attributes: dict):
        self._event_stream_id = attributes["eventStreamId"]
        self._endpoint_urls = attributes["endpointUrls"]

        super()._use_attributes(attributes)
