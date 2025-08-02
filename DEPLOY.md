# 🚀 Деплой lbazaGr Dashboard

## Автоматический деплой на Streamlit Cloud

### Шаг 1: Настройка Streamlit Cloud
1. Перейдите на [share.streamlit.io](https://share.streamlit.io)
2. Войдите через GitHub аккаунт
3. Нажмите "New app"
4. Выберите репозиторий: `dimariyalil/groklbaza`
5. Ветка: `cursor/initial-project-foundation-setup-4187` или `main`
6. Файл: `app.py`
7. Нажмите "Deploy!"

### Шаг 2: Ссылка на приложение
После деплоя вы получите ссылку вида:
```
https://dimariyalil-groklbaza-app-xxxx.streamlit.app/
```

### Альтернативные варианты деплоя:

#### Hugging Face Spaces
1. Перейдите на [huggingface.co/spaces](https://huggingface.co/spaces)
2. Создайте новый Space с типом "Streamlit" 
3. Загрузите файлы проекта
4. Получите ссылку: `https://huggingface.co/spaces/YOUR_USERNAME/lbazagr`

#### GitHub Codespaces (для разработки)
1. Откройте репозиторий на GitHub
2. Нажмите "Code" → "Codespaces" → "Create codespace"
3. В терминале:
   ```bash
   pip install -r requirements.txt
   streamlit run app.py
   ```
4. Получите ссылку в Codespaces

## 📱 Быстрый доступ

После настройки любого из вариантов, приложение будет доступно по прямой ссылке без установки!

**Функциональность онлайн:**
- ✅ Интерактивные дашборды
- ✅ Загрузка файлов Excel/CSV  
- ✅ KPI метрики в реальном времени
- ✅ Фильтрация и поиск данных
- ✅ Collapsible меню навигации

## 🔧 Автоматизация

GitHub Actions автоматически тестирует приложение при каждом push и подготавливает его к деплою.