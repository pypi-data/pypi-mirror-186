from logging import getLogger
from helios.base.span_attributes import SpanAttributes
from helios.instrumentation.base import HeliosBaseInstrumentor
from helios.instrumentation.base_http_instrumentor import HeliosBaseHttpInstrumentor

_LOG = getLogger(__name__)


class HeliosGrpcClientInstrumentor(HeliosBaseHttpInstrumentor):
    MODULE_NAME = 'helios.grpc_instrumentation'
    INSTRUMENTOR_NAME = 'GrpcInstrumentorClient'

    def __init__(self):
        super().__init__(self.MODULE_NAME, self.INSTRUMENTOR_NAME)

    def instrument(self, tracer_provider=None, **kwargs):
        if self.get_instrumentor() is None:
            return

        self.get_instrumentor().instrument(
            tracer_provider=tracer_provider,
            request_hook=self.request_hook,
            response_hook=self.response_hook)

    @staticmethod
    def request_hook(span, request) -> None:
        try:
            if span is None:
                return

            HeliosBaseInstrumentor.set_payload_attribute(
                span, SpanAttributes.RPC_REQUEST_BODY, str(request))

        except Exception as error:
            _LOG.debug('grpc request instrumentation error: %s.', error)

    @staticmethod
    def response_hook(span, response) -> None:
        try:
            if span is None:
                return

            HeliosBaseInstrumentor.set_payload_attribute(
                span, SpanAttributes.RPC_RESPONSE_BODY, str(response))

        except Exception as error:
            _LOG.debug('grpc response instrumentation error: %s.', error)


class HeliosGrpcServerInstrumentor(HeliosBaseHttpInstrumentor):
    MODULE_NAME = 'helios.instrumentation.grpc'
    INSTRUMENTOR_NAME = 'GrpcInstrumentorServer'

    def __init__(self):
        super().__init__(self.MODULE_NAME, self.INSTRUMENTOR_NAME)

    def instrument(self, tracer_provider=None, **kwargs):
        if self.get_instrumentor() is None:
            return

        self.get_instrumentor().instrument(tracer_provider=tracer_provider)
