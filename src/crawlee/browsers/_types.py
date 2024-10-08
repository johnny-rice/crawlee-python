from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from playwright.async_api import Page

BrowserType = Literal['chromium', 'firefox', 'webkit']


@dataclass
class CrawleePage:
    """Represents a page object within a browser, with additional metadata for tracking and management."""

    id: str
    browser_type: BrowserType
    page: Page
