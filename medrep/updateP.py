import requests
data = '''
-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[status]"

1
-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[withPrescription]"

0
-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[onlyDoctorUser]"

0
-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[nameEn]"

ACETAMINOPHEN/CAFFEINE/ASA  162.5mg/32.5mg/325mg ORAL TABLET
-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[brandEn]"

A.C.A®
-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[nameFa]"

آ.ث.آ  162.5mg/32.5mg/325mg قرص خوراکی
-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[brandFa]"

آ .ث .آ ®
-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[erxCode]"

eRx100002
-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[genericCode]"

1
-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[motherCode]"

1121338323793542
-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[categories][]"

118
-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[insurances][]"

1
-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[insurances][]"

2
-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[insurances][]"

3
-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[licenceOwner]"

البرز دارو
-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[brandOwner]"

البرز دارو
-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[brandOwnerCountry]"

ایران
-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[producer]"

البرز دارو
-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[producerCountry]"

ایران
-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[nameInteractive]"


-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[packing]"

100
-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[form]"

قرص
-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[pregnancyCategory]"


-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[videoId]"


-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[ircCodes][0][irc]"

9154715040124503
-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[ircCodes][1][irc]"

6714482393597688
-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[barcodes][0][barcode]"

06260152410148
-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[barcodes][1][barcode]"

6260111340486
-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[barcodes][2][barcode]"

08023603112163
-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[features][0][name]"

شکل قرص
-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[features][0][value]"

گرد دو رنگ
-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[description]"


-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[warnings]"


-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[adverseEffects]"


-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[interactions]"


-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[tips]"


-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[pharmacology]"


-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[mechanism]"


-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[uses]"


-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[submit]"


-----------------------------20437880921670650111230420482
Content-Disposition: form-data; name="pouyasoft_bundle_item[_token]"

EkWU6oyfoyQyWNRfStue8nhBVvFnAFA9rZkAeDFJAr0
-----------------------------20437880921670650111230420482--

'''
edit = requests.post("https://medrep.ir/admin/item/3/edit", data=data)

print(edit.text)