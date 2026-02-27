Power BI Report Creation and Distribution Guide


This README outlines the end-to-end process of building a Power BI report and sharing it using automated export features.

Prerequisites

- Power BI Desktop: For report authoring.

- Power BI Service (Pro or Premium): Required for automated sharing and exporting.

- Power Automate: (Optional) For automated scheduling to email or Slack.


---

Step 1: Create the Report

1. Get Data: Open Power BI Desktop and click Get Data. Select your source (SQL, Excel, Web, etc.).

2. Model the Data: Go to the Model View to create relationships between tables if necessary.

3. Build Visuals: Drag fields into the Report View canvas. Use a mix of charts (Bar, Line, Maps) and Slicers for interactivity.

4. Format: Ensure the page size is set correctly. Go to Format page > Canvas settings.
	- Tip: Use 16:9 for PowerPoint compatibility or Letter/A4 for PDF optimization.



---

Step 2: Publish to Power BI Service

1. Save your .pbix file.

2. Click the Publish button in the Home ribbon.

3. Select your Workspace and click Select.

4. Once finished, click the link to open the report in the Power BI Service (web version).


Step 3: Advanced Automation (Power Automate)


To save the PDF to a folder (SharePoint/OneDrive) or send it via Teams, use a Power Automate flow:


1. Create a new Scheduled Cloud Flow.

2. Add the action: Export to File for Power BI Reports.

3. Configure the parameters:
	- Workspace: Your workspace name.

	- Report: Your report name.

	- Export Format: PDF or PPTX.


4. Add a "New Step" to deliver the file:
	- Office 365 Outlook: "Send an email (V2)" with the exported content as an attachment.

	- SharePoint: "Create file" to save the export to a document library.


Sample Power Automate Script Logic


	Trigger: Recurrence (Every Monday at 9:00 AM)
	Action: Export To File for Power BI Reports (Format: PDF)
	Action: Send an email (V2)
	  - To: stakeholder@example.com
	  - Subject: Weekly Performance Report
	  - Attachments Name: Report.pdf
	  - Attachments Content: [Body from Export step]
    

Troubleshooting Tips

- File Size: If your report has many pages, the export may take several minutes.

- Visuals Not Supported: Some custom visuals or R/Python visuals may not render in the exported file.

- Permissions: Ensure the "Export to PDF" and "Export to PowerPoint" settings are enabled in your Power BI Admin Portal.
