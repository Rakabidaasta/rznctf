# I-like-MS-Word

Условия таска: 
```
Флаг спрятан в файле. Прояви смекалку! ;-)

Подробнее про категорию "Стеганография" можно прочитать тут:
https://kmb.cybber.ru/stego/main.html
```
---

Задача похожая на `TrueWord`.

Открываем документ, видим: `flag{flag_is_somewhere_here}`. (это не флаг)

Открываем docx как zip-архив. Видим папку `customXml` - нам точно надо её исследовать. В `item1.xml` :

```
<b:Sources SelectedStyle="\APA.XSL" StyleName="APA" xmlns:b="http://schemas.openxmlformats.org/officeDocument/2006
/bibliography" xmlns="http://schemas.openxmlformats.org/officeDocument/2006
/bibliography"><b:Source><b:Tag>rznCTF2020</b:Tag><b:SourceType>Misc</b:SourceType><b:Guid>{623C0B9A-F12C-498C-8DDE
-C35D5F06976C}</b:Guid><b:Author><b:Author><b:NameList><b:Person><b:Last>CTF</b:Last></b:Person></b:NameList><
/b:Author></b:Author><b:Title>flag</b:Title><b:Year>2020</b:Year><b:City>Рязань</b:City><b:Publisher>Kvant-CTF<
/b:Publisher><b:PublicationTitle>(word_secret-key_2020)</b:PublicationTitle><b:Month>апрель</b:Month><b:Day>25-26<
/b:Day><b:CountryRegion>Россия</b:CountryRegion><b:RefOrder>1</b:RefOrder></b:Source></b:Sources>
```

---

Флаг : `<flag_rznctf:(word_secret-key_2020)>`
