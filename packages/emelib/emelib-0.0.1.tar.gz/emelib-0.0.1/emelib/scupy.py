from task_struct import Task
from typing import Union
import json
import pathlib





def load_all_tasks():
    all_tasks = []
    with open(pathlib.Path(pathlib.Path(pathlib.Path.cwd(), "task_struct", "tasks_base.json"))) as f:
        for row in f:
            all_tasks.append(Task.deserialize(json.loads(row)))
    return all_tasks


def get_task_by_id(id: int) -> Union[Task, str]:
    all_tasks = load_all_tasks()
    for task in all_tasks:
        if task.id == id:
            return task
    return "NO TASK WITH THAT WORD, CHECK IT"


def find_by_word(word: str):
    all_tasks = load_all_tasks()
    for task in all_tasks:
        task_words = task.task_text.split(" ")
        task_words = [w.lower() for w in task_words]
        if word in task_words:
            print(task.id, task.task_text)
