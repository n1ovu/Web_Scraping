import mechanicalsoup
import pandas as pd
import sqlite3

browser = mechanicalsoup.StatefulBrowser()
browser.open("https://en.wikipedia.org/wiki/Comparison_of_Linux_distributions")

# extract table headers
th = browser.page.find_all("th", attrs={"class": "table-rh"})
distribution = [value.text.replace("\n", "") for value in th]
distribution = distribution[:96]

# extract table data
td = browser.page.find_all("td")
columns = [value.text.replace("\n", "") for value in td]
columns = columns[6:1062]

column_names = ["Founder",
                "Maintainer",
                "Initial_Release_year",
                "Current_Stable_Version",
                "Security_Updates",
                "Release_Date",
                "System_Distribution_Commiment",
                "Forked_From",
                "Target_Audience",
                "Cost",
                "Status"]

dictionary = {"Distribution": distribution}

for idx, key in enumerate(column_names):
    dictionary[key] = columns[idx:][::11]

df = pd.DataFrame(data=dictionary)

# insert data into a database
connection = sqlite3.connect('linux_distro.db')
cursor = connection.cursor()

cursor.execute("CREATE TABLE linux (Distribution, " + ",".join(
    column_names)+")")
for i in range(len(df)):
    cursor.execute("INSERT INTO linux values (?,?,?,?,?,?,?,?,?,?,?,?)",
                   df.iloc[i])

connection.commit()

connection.close()
