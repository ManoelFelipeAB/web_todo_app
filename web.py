import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    new_todo = st.session_state.new_todo + "\n"
    if new_todo:
        todos.append(new_todo)
        functions.write_todos(todos)
        st.session_state.new_todo = ""

st.title("My Todo App")
st.subheader("This is my todo app.")

# Initialize session state for checkboxes
if "checkboxes" not in st.session_state:
    st.session_state.checkboxes = {}

for index, todo in enumerate(todos):
    cleaned_todo = todo.strip()  # Remove newline characters
    checkbox_state = st.session_state.checkboxes.get(cleaned_todo, False)
    checkbox = st.checkbox(cleaned_todo, key=f"todo_{index}", value=checkbox_state)
    st.session_state.checkboxes[cleaned_todo] = checkbox
    if checkbox:
        todos.remove(todo)  # Remove from list
        functions.write_todos(todos)
        st.experimental_rerun()  # Trigger a rerun to update the display

st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key='new_todo')
