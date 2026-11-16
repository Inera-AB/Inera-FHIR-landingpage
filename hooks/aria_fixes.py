"""
MkDocs hook: inject aria-hidden="true" into Material's CSS-hack toggle inputs.

Material uses hidden <input type="checkbox"> elements as CSS toggles for the
hamburger drawer, search overlay and TOC panel. These are purely presentational
and must be hidden from the accessibility tree so screen readers and WAVE do
not flag them as missing/empty/duplicate form labels.

JavaScript cannot solve this because WAVE analyses the DOM before scripts run.
"""

import re


def on_post_page(output: str, **kwargs) -> str:
    # __drawer and __search have autocomplete="off"
    for id_val in ("__drawer", "__search"):
        output = re.sub(
            rf'(id="{id_val}"[^>]*?)(\s*/?>)',
            r'\1 aria-hidden="true"\2',
            output,
        )
    # __toc does not have autocomplete so match more broadly
    output = re.sub(
        r'(id="__toc"[^>]*?)(\s*/?>)',
        r'\1 aria-hidden="true"\2',
        output,
    )
    return output
