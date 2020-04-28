# CTFGame

Условия задачи:
```
The task category speaks for itself...
For stable operation, you may need to install Microsoft Visual C++ 2015 or later:)
```
---

Первоначально очень сильно смущает категория таска. Кажется, что сейчас будет что-то типа PPC или REV, но, к счастью, нет :)

Откроем exe как архив. Покопаемся в файликах. Заметим, что часто появляется слово `hash`. Так как категория таска WEB, параллельно будем искать в файлах `http` или `212.26.237.212`. 

В файле `requester.odj` находим `http://212.26.237.212:2222/api.getflag?hash=0` и `http://212.26.237.212:2222/api.bring?platform_id=0&need_bring=0`. Помучаем последную ссылочку, изменяя параметры `platform_id` и `need_bring`. 

`http://212.26.237.212:2222/api.bring?platform_id=2&need_bring=1` выдаёт следующее : `API Error: Need "md5_gamename_plus_platform_id_hash" param`

gamename = CTFGame, platform_id = 2

Находим необходимый md5 хэш, подставляем его в `http://212.26.237.212:2222/api.getflag?hash=0` вместо 0.

Получаем: `http://212.26.237.212:2222/api.getflag?hash=19123a334468ba662c8a85d99834f7bf`
В коде страницы: 

```
<flag_ctf:(cdg2hd1hq24vg1t0x00al9y2)></flag_ctf:(cdg2hd1hq24vg1t0x00al9y2)>
```
---

Флаг : `<flag_ctf:(cdg2hd1hq24vg1t0x00al9y2)>`
