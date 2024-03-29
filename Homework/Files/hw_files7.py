"""
Дан телефонный справочник в формате JSON:
[
   {
      "имя":"...",
      "телефоны":[
         {
            "описание":"...",
            "номер":"..."
         },
        {
            "описание":"...",
            "номер":"..."
         }
      ]
   },
   …

Программа должна позволять (предоставлять функции):
- загружать информацию из справочника;
- выполнять поиск контактов по номеру телефона;
- выполнять поиск контактов по имени;
- добавлять контакт;
-  удалять контакты по имени;
-  удалять номер телефона из контактов;
- сохранять справочник в файл.
"""