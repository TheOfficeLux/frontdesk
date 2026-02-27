import time
from pywinauto.application import Application

# 1. Start Power BI Desktop with your specific report
report_path = r"C:\Path\To\Your\Report.pbix"
app = Application(backend="uia").start(f'pbidesktop.exe "{report_path}"')

# 2. Connect to the window (wait for it to load)
# The title typically includes the filename
win = app.window(title_re=".*Power BI Desktop")
win.wait("visible", timeout=60)
time.sleep(10)  # Extra buffer for visuals to render

# 3. Use keyboard shortcuts to navigate the menu
# Alt+F (File) -> E (Export) -> P (To PDF)
win.type_keys("%fep")

# 4. Handle the export progress and 'Save As' window if it appears
# Note: Newer versions often save to the same folder automatically or open a dialog.
# If a dialog opens:
try:
    save_as = app.window(title="Save As")
    save_as.wait("visible", timeout=30)
    save_as.type_keys(r"C:\Path\To\Output\Report.pdf{ENTER}")
except Exception:
    print("No 'Save As' dialog appeared; check default export location.")
