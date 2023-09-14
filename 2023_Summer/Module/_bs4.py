html_doc="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ilk web sayfam</title>
</head>
<body>
    <h1 id="header">
        Python Course
    </h1>

    <div class="group1">
        <h2>
            Programming
        </h2>

        <ul>
            <li>
                Menu1
            </li>

            <li>
                Menu2
            </li>

            <li>
                Menu3
            </li>
        </ul>
    </div>

    <div class="group2">
        <h2>
            Modules
        </h2>
        <ul>
            <li>
                Menu1
            </li>

            <li>
                Menu2
            </li>

            <li>
                Menu3
            </li>
        </ul>
    </div>
</body>
</html>
"""

from bs4 import BeautifulSoup

soup=BeautifulSoup(html_doc,'html.parser')#html/xml dokümanı olabilir

result=soup.prettify()#html dokümaınını düzenleme işlemi
result=soup.title
result=soup.head
result=soup.h1.string
result=soup.h2
result=soup.findAll('h2')[1]#2. h2yi çağırır
result=soup.div
result=soup.findAll('div')[1].ul.li
result=soup.div.findChildren()#body -parent--- h1 ve div-
print(result)