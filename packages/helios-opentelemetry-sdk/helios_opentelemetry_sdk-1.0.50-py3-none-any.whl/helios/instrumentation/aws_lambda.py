import os
from logging import getLogger

from opentelemetry.trace import INVALID_SPAN

from helios.instrumentation.base import HeliosBaseInstrumentor
from opentelemetry.propagate import extract
from opentelemetry import context, trace

_LOG = getLogger(__name__)


def custom_event_context_extractor(event):
    ctx = None
    if 'detail-type' in event:
        # Eventbridge case
        if 'detail' in event and 'headers' in event['detail']:
            headers = event['detail']['headers']
        if headers is None and 'headers' in event:
            headers = event['headers']
        if headers is not None:
            ctx = extract(headers)

    if 'headers' in event:
        ctx = extract(event['headers'])

    if ctx is not None and trace.get_current_span(ctx) != INVALID_SPAN:
        return ctx

    return context.Context()


class HeliosAwsLambdaInstrumentor(HeliosBaseInstrumentor):
    MODULE_NAME = 'opentelemetry.instrumentation.aws_lambda'
    INSTRUMENTOR_NAME = 'AwsLambdaInstrumentor'
    LAMBDA_HANDLER_ENV_VAR = '_HANDLER'

    def __init__(self):
        super().__init__(self.MODULE_NAME, self.INSTRUMENTOR_NAME)

    def instrument(self, tracer_provider=None, **kwargs):
        if self.get_instrumentor() is None:
            return

        # AWS Lambda handler env var indicator
        handler = os.environ.get(self.LAMBDA_HANDLER_ENV_VAR)
        if handler is None:
            return

        self.get_instrumentor().instrument(tracer_provider=tracer_provider, event_context_extractor=custom_event_context_extractor)
