# Simple PM2 Dashboard

간단한 PM2 재시작을 위한 대시보드입니다.

## Requirements

- Python 3.11.11
- pm2

## Installation

```bash
cd simple-pm2-dashboard
python -m venv venv
source venv/bin/activate # Windows는 venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```bash
streamlit run app.py
```

## 참고 문서

- [터미널 출력을 가져오는 방법]("https://csatlas.com/python-subprocess-run-stdout-stderr/")
- pandas dataframe
- [streamlit dataframe](https://docs.streamlit.io/develop/api-reference/data/st.dataframe)
