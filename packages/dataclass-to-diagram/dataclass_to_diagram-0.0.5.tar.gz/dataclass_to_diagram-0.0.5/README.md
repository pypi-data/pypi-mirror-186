[![PyPI version](https://badge.fury.io/py/dataclass-to-diagram.svg)](https://badge.fury.io/py/dataclass-to-diagram)

# dataclass_to_diagram

Создание диаграмм из датаклассов python

## Типы диаграмм

### С4

Описание - https://c4model.com/

Реализация на PlantUML - https://github.com/plantuml-stdlib/C4-PlantUML



Состоит из пакетов:

- main - основной пакет для запуска
- models - модели на основе dataclass для различных диаграмм
- exporters - экспорт моделей в текстовый формат
- converters - конвертирование текстового формата в изображение (svg, png, pdf, ...)



### exporters

#### dbml

Экспорт моделей БД (ERD) в формат [dbml](https://www.dbml.org/home/)



### converters

#### dbml-renderer

Конвертирует файл с разметкой dbml в svg-изображение.

Установка:

```bash
npm install -g @softwaretechnik/dbml-renderer
```







Библиотека для генерации диаграмм из текстового описания.

Диаграммы описываются объектами python. Далее геренируются изображения с помощью https://kroki.io.





## Как использовать

1. Создать две папки:

   - dia_src - папка с исходным описанием
   - dia_dist - папка со сгенерированными изображениями

2. В папке dia_src создаются py-файлы. Названия файлов - произвольные. Можно создавать подкаталоги - структура каталогов будет скопирована в целевую папку dia_dist. Примеры создания можно посмотреть в тестовых диаграммах [пакета](https://github.com/Konstantin-Dudersky/konstantin_docs/tree/main/test).

3. В одном файл должна быть только одна диаграмма. Название файла будет названием диаграммы.

4. Для генерации можно создать задачу poetepoet. Прописать в файле pyproject.toml:

   ```toml
   [tool.poetry.dependencies]
   konstantin_docs = "*"
   poethepoet = "*"
   
   [tool.poe.tasks]
   docs = {script = "konstantin_docs.main:generate_images('dia_src', 'dia_dist')"}
   ```

5. Запустить командой:

   ```sh
   poetry run poe docs
   ```

6. Дополнительно можно создать задачу в vscode. Для этого в файле .vscode/tasks.json:

   ```json
   {
     "version": "2.0.0",
     "tasks": [
       {
         "label": "docs",
         "type": "shell",
         "command": "poetry run poe docs"
       }
     ]
   }
   ```

   Запускать командой F1 -> Task: Run task -> docs

ERD

```bash
npm install -g @softwaretechnik/dbml-renderer
```



## Разработка

```bash
poetry build && poetry publish
```



