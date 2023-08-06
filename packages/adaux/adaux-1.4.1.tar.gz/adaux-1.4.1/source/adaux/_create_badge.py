#!/usr/bin/env python
# Copyright (c) 2021-2023 Mario S. Könz; License: MIT
import sys


def main() -> None:
    assert len(sys.argv) == 4
    _, name, value, color = sys.argv  # pylint: disable=unbalanced-tuple-unpacking

    # colors from https://docs.gitlab.com/ee/ci/pipelines/settings.html#test-coverage-report-badge
    if color == "green":
        color = "#4c1"
    elif color == "lightgreen":
        color = "#a3c51c"
    elif color == "yellow":
        color = "#dfb317"
    elif color == "red":
        color = "#e05d44"
    elif color == "gray":
        color = "#e05d44"
    else:
        raise NotImplementedError(color)

    print(
        f"""
<svg xmlns="http://www.w3.org/2000/svg" width="116" height="20">
  <linearGradient id="b" x2="0" y2="100%">
    <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
    <stop offset="1" stop-opacity=".1"/>
  </linearGradient>

  <mask id="a">
    <rect width="116" height="20" rx="3" fill="#fff"/>
  </mask>

  <g mask="url(#a)">
    <path fill="#555" d="M0 0 h62 v20 H0 z"/>
    <path fill="{color} " d="M62 0 h54 v20 H62 z"/>
    <path fill="url(#b)" d="M0 0 h116 v20 H0 z"/>
  </g>

  <g fill="#fff" text-anchor="middle">
    <g font-family="DejaVu Sans,Verdana,Geneva,sans-serif" font-size="11">
      <text x="31" y="15" fill="#010101" fill-opacity=".3">
        {name}
      </text>
      <text x="31" y="14">
        {name}
      </text>
      <text x="89" y="15" fill="#010101" fill-opacity=".3">
        {value}
      </text>
      <text x="89" y="14">
        {value}
      </text>
    </g>
  </g>
</svg>
"""
    )


if __name__ == "__main__":
    main()
