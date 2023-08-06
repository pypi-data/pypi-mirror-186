import logging
import os
from contextlib import contextmanager
from logging import StreamHandler

from azure.monitor.opentelemetry.exporter import AzureMonitorTraceExporter
from opentelemetry import context, trace
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.trace.sampling import ALWAYS_ON
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator

logger = logging.getLogger(__name__)
logger.addHandler(StreamHandler())

TRACING_IS_CONFIGURED = False


def configure_tracing():
    global TRACING_IS_CONFIGURED
    if TRACING_IS_CONFIGURED:
        # tracing should only be set up once
        # to avoid duplicated trace handling.
        # Global variables is the pattern used
        # by opentelemetry, so we use the same
        return

    # Azure Function doesn't seem to be able to
    # inherit the tracer provider from the worker,
    # so we need to set it up manually for now
    # (this is not a problem for the logging provider
    # for some reason).
    # - we set the service name manually since otherwise,
    # the Cloud Role Name will be shown as 'unknown_service'
    # in App Insights.
    # (https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-enable?tabs=net#set-the-cloud-role-name-and-the-cloud-role-instance)
    # - We use the ALWAYS ON sampler since otherwise,
    # spans will not be recording upon creation
    # (https://anecdotes.dev/opentelemetry-on-google-cloud-unraveling-the-mystery-f61f044c18be)
    resource = Resource.create({SERVICE_NAME: os.getenv("WEBSITE_SITE_NAME")})
    trace.set_tracer_provider(
        TracerProvider(
            sampler=ALWAYS_ON,
            resource=resource,
        )
    )

    # setup azure monitor trace exporter to send telemetry to App Insights
    try:
        trace_exporter = AzureMonitorTraceExporter()
    except ValueError:
        # if no App Insights instrumentation key is set (e.g. when running unit tests),
        # the exporter creation will fail. In this case we skip it
        logger.warning(
            "Cant set up tracing to App Insights, as no instrumentation key is set."
        )
    else:
        span_processor = BatchSpanProcessor(trace_exporter)
        trace.get_tracer_provider().add_span_processor(span_processor)

    TRACING_IS_CONFIGURED = True


@contextmanager
def set_trace_context(trace_parent: str, trace_state: str = ""):
    """Context manager for setting the trace context

    Args:
        trace_parent (str): Trace parent ID
        trace_state (str, optional): Trace state. Defaults to "".
    """
    carrier = {"traceparent": trace_parent, "tracestate": trace_state}
    ctx = TraceContextTextMapPropagator().extract(carrier=carrier)

    token = context.attach(ctx)  # attach context before run
    try:
        yield
    finally:
        context.detach(token)  # detach context after run


def get_tracer(name: str):
    tracer = trace.get_tracer(name)
    return tracer
