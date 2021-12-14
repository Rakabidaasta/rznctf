# CryptoWord

Условия таска:
```
Задания в категории crypto — криптография.
Вам необходимо что-то расшифровать и в результате получить флаг.
Более подробную информацию можно найти тут: https://kmb.cybber.ru/crypto/main.html
```

Файл из задания [здесь](https://github.com/Rakabidaasta/rznctf/blob/master/CryptoWord/write_text.vbe)

---

`write_text` - это .vbe файл сценария на Windows. Меняем расширение: `write_text.vbe`.

Гуглим что такое vbe, находим, что это Encoded VBS

Затем ищем `VBE to VBS`. Используем онлайн утилиту (например [эту](https://master.ayra.ch/vbs/vbs.aspx)).

Получаем: 
```
if True Then
msgbox"Hi! How are you?",16,"rznctf"
Else
msgbox"<flag_rznctf:(_get_some_vbscript_)>",16,"rznctf"
End If
```

---

Флаг : `<flag_rznctf:(_get_some_vbscript_)>`
