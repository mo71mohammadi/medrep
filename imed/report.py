import pymongo
import xlsxwriter

Client = pymongo.MongoClient('localhost', 27017)
db = Client['imed']
col = db['generaP']

Company = col.find()

wb = xlsxwriter.Workbook("export_product.xlsx")
general = wb.add_worksheet()
model = wb.add_worksheet()
irc = wb.add_worksheet()

count = 0
gRow = 0
mRow = 0
ircRow = 0

for company in Company:
    print(company)
    gid = gRow + 1
    general.write(gRow, 0, gid)
    # general.write(gRow, 1, company['company'])
    general.write(gRow, 2, company['product'])
    general.write(gRow, 3, company['enName'])
    general.write(gRow, 4, company['category'])
    general.write(gRow, 5, company['UMDNS'])
    # general.write(gRow, 6, company['manuName'])
    # general.write(gRow, 7, company['countryLegal'])
    general.write(gRow, 8, company['eqType'])
    gRow += 1
    for item in company['models']:
        mid = mRow + 1
        model.write(mRow, 0, mid)
        model.write(mRow, 1, gid)
        model.write(mRow, 2, item['Model'])
        model.write(mRow, 3, item['RegBrand'])
        model.write(mRow, 4, item['manuNameOEM'])
        model.write(mRow, 5, item['countryOEM'])
        model.write(mRow, 6, item['cmp_name'])
        model.write(mRow, 7, item['cmp_Code'])
        if item['FANI']['عمومی']:
            if 'FaName' in item['FANI']['عمومی']:
                model.write(mRow, 8, item['FANI']['عمومی']['FaName'])
            if 'EnName' in item['FANI']['عمومی']:
                model.write(mRow, 9, item['FANI']['عمومی']['EnName'])
            if 'Describe' in item['FANI']['عمومی']:
                model.write(mRow, 10, item['FANI']['عمومی']['Describe'])
            if 'Legal' in item['FANI']['عمومی']:
                model.write(mRow, 11, item['FANI']['عمومی']['Legal'])
            if 'Country_Legal' in item['FANI']['عمومی']:
                model.write(mRow, 12, item['FANI']['عمومی']['Country_Legal'])
            if 'companyType' in item['FANI']['عمومی']:
                model.write(mRow, 13, item['FANI']['عمومی']['companyType'])
            if 'Foriati' in item['FANI']['عمومی']:
                model.write(mRow, 14, item['FANI']['عمومی']['Foriati'])
            if 'Unit' in item['FANI']['عمومی']:
                model.write(mRow, 15, item['FANI']['عمومی']['Unit'])
            if 'Usability' in item['FANI']['عمومی']:
                model.write(mRow, 16, item['FANI']['عمومی']['Usability'])
            if 'CommonName' in item['FANI']['عمومی']:
                model.write(mRow, 17, item['FANI']['عمومی']['CommonName'])
            if 'LableName' in item['FANI']['عمومی']:
                model.write(mRow, 18, item['FANI']['عمومی']['LableName'])
            if 'Brand' in item['FANI']['عمومی']:
                model.write(mRow, 19, item['FANI']['عمومی']['Brand'])
            if 'Catalog' in item['FANI']['عمومی']:
                model.write(mRow, 20, item['FANI']['عمومی']['Catalog'])
        print(item['FANI'])
        mRow += 1
        for IRC in item['IRCs']:
            irc.write(ircRow, 0, ircRow+1)
            irc.write(ircRow, 1, mid)
            irc.write(ircRow, 2, IRC['IRC'])
            irc.write(ircRow, 3, IRC['DescriptionFa'])
            irc.write(ircRow, 4, IRC['Description'])
            irc.write(ircRow, 5, IRC['GTIN'])
            ircRow += 1

wb.close()
