import time
from pywinauto.application import Application

report_path = r"C:\Users\briad\OneDrive - Momentum Credit\Documents\Cyber Shujaa Data and AI\Assignments\powerbiassignment.pbix"
pdf_output = r"C:\Users\briad\OneDrive - Momentum Credit\Documents\Cyber Shujaa Data and AI\Assignments\powerbiassignment.pdf"

# Start Power BI
app = Application(backend="uia").start(f'"C:\\Program Files\\Microsoft Power BI Desktop\\bin\\PBIDesktop.exe" "{report_path}"')

# Wait for main window
win = app.window(title_re=".*Power BI Desktop")
win.wait("visible", timeout=120)
time.sleep(15)  # wait for visuals to fully render

# Open Export to PDF
win.type_keys("%f")      # Alt + F
time.sleep(1)
win.type_keys("e")       # Export
time.sleep(1)
win.type_keys("p")       # Export to PDF
time.sleep(5)

# Handle Save As dialog
save_as = app.window(title_re="Save As")
save_as.wait("visible", timeout=60)
save_as.type_keys(pdf_output)
save_as.type_keys("{ENTER}")

print("PDF Export Triggered Successfully")
