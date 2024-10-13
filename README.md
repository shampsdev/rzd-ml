### Использование

```bash
# Создание виртуального окружения и установка зависимостей
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

```bash
# Запуск предсказания
python main.py --src train/dataset/hr_bot_noise --dst train/dataset
```
Нужно подождать, когда подгрузится модель от huggingface. Это требуется только в первый раз, модель сохранится в кеше `~/.cache/huggingface`. Можно скачать её отдельно.

### Самопроверка

Результат самопроверки можно найти в ноутбуке `train/predict.ipynb`. Предсказание датасета `luga` с вычисление метрик `F1` и `WER`. (`0.81` и `0.13` соответственно).

### Обучение

Подготовка: нужно скачать датасет [отсюда](https://lodmedia.hb.bizmrg.com/case_files/1144817/train_dataset_train_rzhd_pult.zip). Вытащить директорию DATASET. Переименовать в dataset и поместить в директорию `train/dataset`.

Происходит в два этапа

Генерация датасета с текстом вычисленным Speech2Text моделью. `train/gen_transcriptions.ipynb`.

Обучение классификатора на этих данных. `train/text2label.ipynb`, `train/text2attr.ipynb`.

Обученные модели сохраняются в `train/trained`.

Проверка на `luga` в файле `predict.ipynb`.