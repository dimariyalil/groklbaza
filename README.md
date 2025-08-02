# lbazaGr AI Dashboard

Локальная AI-платформа для бизнеса на Python/Streamlit.

## 🌐 Онлайн демо

**Для деплоя на GitHub:**
1. [Streamlit Cloud](https://share.streamlit.io) - автоматический деплой
2. [Hugging Face Spaces](https://huggingface.co/spaces) - альтернативный хостинг
3. [GitHub Codespaces](https://github.com/codespaces) - разработка онлайн

📋 **Инструкции по деплою:** [DEPLOY.md](DEPLOY.md)

## 🚀 Быстрый старт

### Локально:
```bash
pip install -r requirements.txt
streamlit run app.py
```

### GitHub Codespaces:
```bash
# Откройте репозиторий → Code → Codespaces → Create codespace
pip install -r requirements.txt
streamlit run app.py
```

## 📊 Функциональность

### Основные разделы:
- **🏠 Home** — KPI метрики и тренды
- **📊 Reports** — загрузка файлов, анализ данных, фильтры  
- **🤖 AI Analysis** — чат с ИИ, агенты, рекомендации
- **👥 HR** — база сотрудников, KPI, рекрутинг
- **🧠 ML Analytics** — AutoML, прогнозы, аномалии
- **📂 Archives** — история данных, поиск, экспорт
- **⚙️ Settings** — настройки, API ключи, бэкапы

## 🔄 Этапы разработки

- ✅ **Этап 1**: Базовая настройка и структура
- ✅ **Этап 2**: MVP UI с collapsible меню и базовым функционалом
- 🔄 **Этап 3**: Интеграция AI-агентов
- 🔄 **Этап 4**: HR-модуль
- 🔄 **Этап 5**: ML-компоненты

## 🛠️ Технологии

- **Frontend**: Streamlit
- **Data**: Pandas, Plotly
- **AI**: Anthropic Claude
- **Files**: Excel/CSV support
- **Deploy**: GitHub Actions, Streamlit Cloud

## 🔧 CI/CD

GitHub Actions автоматически тестирует приложение и подготавливает к деплою при каждом push.