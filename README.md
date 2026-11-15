
# 🦠 COVID-19 Dashboard

An interactive COVID-19 dashboard built with **Python**, **Dash**, and **Plotly**.
Track cases, recoveries, and deaths, and explore state-level and commodity data through interactive charts.

## ✨ Features

- 📊 **Summary cards** for total cases, active cases, recovered cases, and deaths
- 🧪 **Commodity chart** showing totals for All, Mask, Sanitizer, and Oxygen, grouped by status
- 🥧 **Pie chart** showing how records are distributed by status or zone (Red, Blue, Green, Orange)
- 🗺️ **State chart** with a dropdown to switch between Total, Hospitalized, Recovered, and Deceased counts
- 📱 **Responsive layout** built on Bootstrap 5 grid classes

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 **Python** | Core programming language |
| ⚡ **Dash** | Builds the interactive web app and callbacks |
| 📈 **Plotly** | Bar, pie, and interactive charts |
| 🐼 **pandas** | Loads and aggregates the CSV dataset |
| 🔢 **NumPy** | Numerical support for data handling |
| 🎨 **Bootstrap 5** | Layout grid, cards, and styling (via CDN) |
| 🦄 **Gunicorn** | Production WSGI server |
| ☁️ **Render** | Cloud hosting for the live app |
| 🐙 **Git & GitHub** | Version control and code hosting |
| 💻 **VS Code** | Development environment |

## 📁 Project Structure

```
Covid-dashboard/
├── app.py                           # Data, layout, and callbacks
├── covid_demo_2000_state_last.csv   # Dataset (2000 rows)
├── requirements.txt                 # Python dependencies
└── .gitignore                       # Files excluded from Git
```


🔗 **Live demo:https://covid-dashboard-1-2lgw.onrender.com

## 📄 Data

The dashboard reads `covid_demo_2000_state_last.csv` on startup. Keep the file in the same folder as `app.py`.

Columns used include `Status`, `Total`, `Hospitalized`, `Recovered`, `Deceased`, `Mask`, `Sanitizer`, `Oxygen`, `State`, and the zone columns.

## 🤝 Contributing

Suggestions and improvements are welcome. Open an issue or submit a pull request.

## 📜 License

This project is for educational purposes.

---
Made with ❤️ using Python and Dash
