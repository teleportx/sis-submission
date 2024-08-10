# Посылки ЛКШ
Бот для отправки уведомлений о изменении статуса посылок в ЛКШ.

### Команды
 - subscribe - Подписаться на посылки определенного человека
 - queue - Узнать количество посылок в очереди

## Как это работает?

Одной из самых больших сложностей было обеспечить хостинг бота с доступом к ejudge'у (который хостится локально в ЛКШ).
Решением стало проброс VPN до сервера на котором будет стоять бот.

На привезеный с собой роутер был установлен L2TP/IPSec клиент, который и подключался к серверу.
Объединить локальные сети, но получить доступ к ejudge не получилось из-за того, что он находился во внешеней по отношению роутеру с VPN'ом сети.
Сколько бы я не пытался настроить маршруты до ejudge у меня не получилось.
Поэтому был придуман костыль в виде поднятого на роутере nginx сервера.

Теперь, настроив на nginx reverse proxy, получается получить доступ к ejudge с удаленного сервера.
Дело остается за малым и с помощью парсера собирается информация с сводной таблицы параллели, и при изменении отсылается нужным пользователям.
