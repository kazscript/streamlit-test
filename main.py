import streamlit as st
import pandas as pd
import os

# ページタイトルの設定
st.set_page_config(page_title="ToDo App", page_icon=":memo:", layout="wide")

# ファイルが存在しない場合は作成する
if not os.path.exists("tasks.csv"):
    with open("tasks.csv", "w") as f:
        f.write("task\n")

# CSVファイルを読み込む
df = pd.read_csv("tasks.csv")

# セッションステートの初期化
if "tasks" not in st.session_state:
    st.session_state.tasks = df["task"].tolist()

# サイドバーにタスクの入力フォームを表示
task = st.sidebar.text_input("Add Task")

# タスクを追加するためのボタン
if st.sidebar.button("Add"):
    st.session_state.tasks.append(task)

    # CSVファイルに書き込む
    pd.DataFrame({"task": st.session_state.tasks}).to_csv("tasks.csv", index=False)

# タスクリストの表示
st.header("Task List")
if not st.session_state.tasks:
    st.write("No tasks yet.")
else:
    for i, task in enumerate(st.session_state.tasks):
        st.write(f"{i+1}. {task}")

# クリアボタン
if st.button("Clear All"):
    st.session_state.tasks = []

    # CSVファイルを空にする
    pd.DataFrame({"task": st.session_state.tasks}).to_csv("tasks.csv", index=False)
