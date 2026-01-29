"""Print today's Shanghai weather using wttr.in (no API key needed)."""

from __future__ import annotations

import urllib.parse
import urllib.request


def get_weather(location: str = "Shanghai") -> str:
    # wttr.in format codes:
    # %l location, %c condition, %t temp, %h humidity, %w wind
    fmt = "%l:+%c+%t+%h+%w"
    url = f"https://wttr.in/{urllib.parse.quote(location)}?format={urllib.parse.quote(fmt)}"

    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "mytesting-shanghai-weather/1.0 (+https://github.com/syujp888-ui/mytesting)",
        },
    )

    with urllib.request.urlopen(req, timeout=10) as resp:
        return resp.read().decode("utf-8").strip()


def main() -> None:
    print(get_weather("Shanghai"))


if __name__ == "__main__":
    main()
