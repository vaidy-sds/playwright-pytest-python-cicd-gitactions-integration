import pytest
from playwright.sync_api import BrowserContext


@pytest.fixture(autouse=True)
def trace_test(context: BrowserContext):
    context.tracing.start(
        name="playwright_trace",
        screenshots=True,
        snapshots=True,
        sources=True
    )
    yield
    context.tracing.stop(path="trace.zip")
