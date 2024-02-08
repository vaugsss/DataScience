# DataScience
Hello and welcome to my personal repository :) This will contain my tests and works using Python, R, SQL and another tools.

Project MonitorSpace.py
- This is was requirement which my team in Kyndryl had. There is a spacemonitor tool developed by IBM which creates a report with the required information about IMS databases. This report is designed to run under Mainframe systems and it does not have a interface so friendly and data analysys tools like Excel or PowerBI are not able to filter and use it. 
So I created a Python code which can open a txt file direct downloaded from Mainframe and modifies the report so we can have a friendly view and more able usage for Power Bi and Excel. This is in place in Kyndryl and we are using as much we update the Power BI graphs.
This code can be used for any system who has IMS Databases and the IMS Database Solution Pack from IBM installed. The report is made by the utility FABKSPMN: https://www.ibm.com/docs/en/ims-dbsolutionpack/2.2?topic=language-fabkspmn-jcl and the output for that is available on the SPMNRPT dataset - here is a sample from IBM. https://www.ibm.com/docs/en/ims-dbsolutionpack/2.2?topic=set-space-analysis-by-data-report
In my case, the costumers has weekly jobs running on schedule, producing this report. The output is saved in generation dataset with 15 generations available. Then, this dataset can be download or sent via e-mail. Saving it in a txt file, you can open Python in your PC an run over it.
