# Challenge_DataEngineer
Description of the project:
The scripts that are mentioned below are meant to fulfill the requirements stated in the sent challenge.
* Create_Database.py: This is the first script that must be ran. It creates the connection to your local server(SQL server) and creates a Test database if non existant.

* Create_Table_Trips.py: Next script to be executed. If it doesn't exist already, creates the Trips table with the columns provided in the Trips.csv file.

* Extract_to_Database.py: This script reads the Trips.csv file located in the same folder and extracts the rows from the file. After that, it inserts these records into the Trips table in the Test database.
If successful, it requests an email address where the user is going to be sent an email informing the ran finished properly on the current date.
This email will be sent from a test email address(testvm.challenge@gmail.com).
						
* Report_Weekly_Averages.py: Final script. It shows an input requiring the user to select between getting a report based on a rectangular Bounding Box (specifying 4 different points) or by Region.
If the first option is selected, it will show a table with the weekly average of trips that were origined inside the bounding box.
Else, it shows the weekly average of trips for the selected region.
	When selecting the report of a Bounding Box, the following points, extracted from the file, can be used as reference to create it:
	- POINT (10.00384920850646 53.65220121071665)
	- POINT (7.513135087952872 45.04417775442011)
	- POINT (14.65848565403607 50.11571340810843)
	- POINT (14.34394689715277 50.12299688052901)
							


Requirements:
* Install python (https://phoenixnap.com/kb/how-to-install-python-3-windows)
* Install anaconda3 (https://docs.anaconda.com/anaconda/install/windows/) 
* Install SQL Server Developer edition(https://www.microsoft.com/en-us/sql-server/sql-server-downloads)


For windows:
Clone repository
Go to command line
Cd to current repo location
Once located there, the scripts should be run with the following commands and order:
1) python Create_Database.py
2) python Create_Table_Trips.py
3) python Extract_to_Database.py
4) python Report_Weekly_Averages.py


Common issues when connecting to SQL server:

1- Inbound rule not created in Windows firewall (https://docs.sophos.com/esg/sgn/8-1/admin/en-us/esg/SafeGuard-Enterprise/tasks/DatabaseCheckFirewallSettings2008R2.html)

2- Remote connections not allowed to server:
	Use the following steps to enable remote connections to your SQL Server:
		- Open SQL Server Management Studio.
		- Right-click your server's name and select Properties.
		- Select Connections option
		- Tick the checkbox "Allow remote connections to this server."
		- Select OK.
		
3- If the SQL Server edition is different, the instance name of the server may change (e.g. Sql server Express edition will have an instance name of SQLEXPRESS). If that's the case, the connection string should be changed for every script.

