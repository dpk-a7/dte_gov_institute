import  requests, csv, pandas as pd
from bs4 import BeautifulSoup as bs 

regionName = 'Mumbai'
csvFileName = 'test.csv'



regionID = str(["Amravati", "Aurangabad", "Mumbai", "Nagpur", "Nashik", "Pune"].index(regionName)+1)
url = f"https://dte.maharashtra.gov.in/search-of-institute-results-2?RegionID={regionID}&RegionName={regionName}"

print("Request URL: ",url, end='\n\n')
page = requests.get(url)

content = page.content

soup = bs(content,features="lxml") 

# ====================<tag>  , <property>======================
Table = soup.find_all("table", {"class": "table-striped"})[0]


table_df = pd.read_html(str(Table), index_col=False)[0] 
table_df.to_csv(csvFileName) 

DF = []
link = "https://dte.maharashtra.gov.in/institute-summary?InstituteCode={}"
with open(csvFileName, 'r') as fr:
    dl = csv.reader(fr, delimiter=',')
    next(dl)
    head = next(dl)[1:]
    head.append("Links")
    DF.append(head)
    for _bd in dl:
        bd = _bd[1:]
        bd.append(link.format(bd[1]))
        DF.append(bd)
with open(csvFileName, 'w+', newline='') as CsvFile:
    csv_writer = csv.writer(CsvFile, delimiter=',')
    csv_writer.writerows(DF)
