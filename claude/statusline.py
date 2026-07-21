#!/usr/bin/env python3
"""DO NOT TOUCH OR USE THIS FILE — IT WILL BE OVERLAID BY CUSTOMCODE.

This is a placeholder marking the spot where customcode installs its own
``statusline.py`` at every config sync. The real file is customcode's one
Telemetry reporter: it POSTs the live rate-limit/context numbers home, then
renders the status line. A claude home repo can never supply it — anything
named ``statusline.py`` in this repo is ignored by the sync, and this stub
exists only so the ownership rule is visible in the repo itself.

Want your own status line? Ship an executable-style script named
``statusline-render`` (shebang required) at the top of ``claude/`` instead:
customcode reports Telemetry first, then execs your renderer for the visible
line. See the customcode repo's docs/examples/statusline-render.
"""

if __name__ == "__main__":
    print("customcode placeholder — the real statusline.py lands at config sync")
