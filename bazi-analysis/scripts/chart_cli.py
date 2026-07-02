#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import argparse
import json
from typing import Any

from bazi_engine import generate_chart


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate a BaZi chart with the bundled 实战派 skill engine.")
    parser.add_argument("--calendar", "--calendar-type", dest="calendar_type", default="solar", help="solar/阳历 or lunar/农历")
    parser.add_argument("--year", type=int, required=True)
    parser.add_argument("--month", type=int, required=True)
    parser.add_argument("--day", type=int, required=True)
    parser.add_argument("--hour", type=int, default=0)
    parser.add_argument("--minute", type=int, default=0)
    parser.add_argument("--second", type=int, default=0)
    parser.add_argument("--gender", default="male", help="male/男 or female/女")
    parser.add_argument("--name", default="")
    parser.add_argument("--leap-month", action="store_true", help="Use when the lunar month is leap month.")
    parser.add_argument("--sect", type=int, default=2, choices=[1, 2])
    parser.add_argument("--yun-sect", type=int, default=1, choices=[1, 2])
    parser.add_argument("--da-yun-count", type=int, default=10)
    parser.add_argument("--json", action="store_true", help="Output full JSON instead of plain text.")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    data: dict[str, Any] = {
        "calendar_type": args.calendar_type,
        "year": args.year,
        "month": args.month,
        "day": args.day,
        "hour": args.hour,
        "minute": args.minute,
        "second": args.second,
        "gender": args.gender,
        "name": args.name,
        "is_leap_month": args.leap_month,
        "sect": args.sect,
        "yun_sect": args.yun_sect,
        "da_yun_count": args.da_yun_count,
    }
    chart = generate_chart(data)
    if args.json:
        print(json.dumps(chart, ensure_ascii=False, indent=2))
    else:
        print(chart["plain_text"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
