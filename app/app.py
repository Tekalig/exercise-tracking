import streamlit as st
import asyncio
from components.post_workout import post_workout
from components.get_workout import get_workout
from components.update_workout import update_workout
from components.delete_workout import delete_workout

async def fetch_workouts():
    return await get_workout()

def display_workouts():
    workouts = asyncio.run(fetch_workouts())
    if not workouts:
        st.write("No workouts available.")
        return

    # Column headers
    col1, col2, col3, col4, col5, col6, col7 = st.columns([1, 2, 2, 2, 2, 1, 1])
    col1.write("ID")
    col2.write("Date")
    col3.write("Time")
    col4.write("Exercise")
    col5.write("Duration")
    col6.write("Edit")
    col7.write("Delete")

    for workout in workouts:
        col1, col2, col3, col4, col5, col6, col7 = st.columns([1, 2, 2, 2, 2, 1, 1])
        col1.write(workout["id"])
        col2.write(workout["date"])
        col3.write(workout["time"])
        col4.write(workout["exercise"])
        col5.write(workout["duration"])

        if col6.button("✏️", key=f"edit_{workout['id']}"):
            st.session_state.selected_workout = workout
            st.session_state.edit_mode = True

        if col7.button("🗑️", key=f"delete_{workout['id']}"):
            delete_workout(workout["id"])
            st.experimental_rerun()

        if st.session_state.get("edit_mode") and st.session_state.selected_workout["id"] == workout["id"]:
            updated_data = {
                "exercise": st.text_input("Exercise", workout["exercise"]),
                "duration": st.text_input("Duration", workout["duration"]),
            }
            update_workout(workout["id"], updated_data)
            st.session_state.edit_mode = False
            st.experimental_rerun()

st.title("Workout Tracker")

exercise_input = st.text_input("Exercise")

def add_workout():
    if exercise_input:
        post_workout({"exercise": exercise_input})
        st.experimental_rerun()

if st.button("Add Workout"):
    add_workout()

display_workouts()
