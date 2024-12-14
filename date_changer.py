from datetime import datetime
 
created_date = '19 March 2024'
issue_date = '29.04.24'

print(datetime.strptime(created_date, "%d %B %Y").strftime("%d-%m"))
print(datetime.strptime(issue_date, "%d.%m.%y").strftime("%d-%m"))

