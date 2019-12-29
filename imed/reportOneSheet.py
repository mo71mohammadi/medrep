import pymongo
import xlsxwriter

Client = pymongo.MongoClient('localhost', 27017)
db = Client['imed']
col = db['generaP']

Company = col.find()

wb = xlsxwriter.Workbook("export_irc0.xlsx")
irc = wb.add_worksheet()
fani = wb.add_worksheet()

count = 0
gRow = 0
mRow = 0
ircRow = 0
faniRow = 0

for company in Company:
    gid = gRow + 1
    gRow += 1
    for item in company['models']:
        mid = mRow + 1
        mRow += 1
        for IRC in item['IRCs']:
            irc.write(ircRow, 0, company['product'])
            irc.write(ircRow, 1, company['enName'])
            irc.write(ircRow, 2, company['category'])
            irc.write(ircRow, 3, company['UMDNS'])
            irc.write(ircRow, 4, company['eqType'])
            irc.write(ircRow, 5, item['Model'])
            irc.write(ircRow, 6, item['RegBrand'])
            irc.write(ircRow, 7, item['manuNameOEM'])
            irc.write(ircRow, 8, item['countryOEM'])
            irc.write(ircRow, 9, item['cmp_name'])
            irc.write(ircRow, 10, item['cmp_Code'])
            if item['FANI']['عمومی']:
                if 'FaName' in item['FANI']['عمومی']:
                    irc.write(ircRow, 11, item['FANI']['عمومی']['FaName'])
                if 'EnName' in item['FANI']['عمومی']:
                    irc.write(ircRow, 12, item['FANI']['عمومی']['EnName'])
                if 'Describe' in item['FANI']['عمومی']:
                    irc.write(ircRow, 13, item['FANI']['عمومی']['Describe'])
                if 'Legal' in item['FANI']['عمومی']:
                    irc.write(ircRow, 14, item['FANI']['عمومی']['Legal'])
                if 'Country_Legal' in item['FANI']['عمومی']:
                    irc.write(ircRow, 15, item['FANI']['عمومی']['Country_Legal'])
                if 'companyType' in item['FANI']['عمومی']:
                    irc.write(ircRow, 16, item['FANI']['عمومی']['companyType'])
                if 'Foriati' in item['FANI']['عمومی']:
                    irc.write(ircRow, 17, item['FANI']['عمومی']['Foriati'])
                if 'Unit' in item['FANI']['عمومی']:
                    irc.write(ircRow, 18, item['FANI']['عمومی']['Unit'])
                if 'Usability' in item['FANI']['عمومی']:
                    irc.write(ircRow, 19, item['FANI']['عمومی']['Usability'])
                if 'CommonName' in item['FANI']['عمومی']:
                    irc.write(ircRow, 20, item['FANI']['عمومی']['CommonName'])
                if 'LableName' in item['FANI']['عمومی']:
                    irc.write(ircRow, 21, item['FANI']['عمومی']['LableName'])
                if 'Brand' in item['FANI']['عمومی']:
                    irc.write(ircRow, 22, item['FANI']['عمومی']['Brand'])
                if 'Catalog' in item['FANI']['عمومی']:
                    irc.write(ircRow, 23, item['FANI']['عمومی']['Catalog'])
            irc.write(ircRow, 24, IRC['IRC'])
            irc.write(ircRow, 25, IRC['DescriptionFa'])
            irc.write(ircRow, 26, IRC['Description'])
            irc.write(ircRow, 27, IRC['GTIN'])
            ircRow += 1
            # if len(item['FANI']) > 1:
            #     # print(item['FANI'])
            #     fani.write(faniRow, 0, IRC['IRC'])
            #     fani.write(faniRow, 1, IRC['DescriptionFa'])
            #     fani.write(faniRow, 2, IRC['Description'])
            #     fani.write(faniRow, 3, IRC['GTIN'])
            #
            #     count = 4
            #     if 'مشخصه های فنی' in item['FANI']:
            #         for fan in item['FANI']['مشخصه های فنی']:
            #             print(fan.strip())
            #             fani.write(faniRow, count, fan.strip())
            #             count += 1
            #             fani.write(faniRow, count, item['FANI']['مشخصه های فنی'][fan].strip())
            #             count += 1
            #     if 'مشخصه های ظاهری' in item['FANI']:
            #         for fan in item['FANI']['مشخصه های ظاهری']:
            #             print(fan.strip())
            #             fani.write(faniRow, count, fan.strip())
            #             count += 1
            #             fani.write(faniRow, count, item['FANI']['مشخصه های ظاهری'][fan].strip())
            #             count += 1
            #     faniRow += 1

wb.close()
