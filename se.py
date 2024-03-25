# Model# Model
class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def complete(self):
        self.completed = True

# View
class TaskView:
    def show_tasks(self, tasks):
        print("Tasks:")
        for index, task in enumerate(tasks):
            status = "X" if task.completed else " "
            print(f"{index + 1}. [{status}] {task.description}")

# Controller
class TaskController:
    def __init__(self):
        self.tasks = []
        self.view = TaskView()

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            task.complete()

    def show_tasks(self):
        self.view.show_tasks(self.tasks)

# Usage
if __name__ == "__main__":
    controller = TaskController()
    controller.add_task("Learn Python")
    controller.add_task("Write code")
    controller.add_task("Eat lunch")

    controller.show_tasks()

    
    controller.complete_task(0)

    controller.show_tasks()

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def complete(self):
        self.completed = True

# View
class TaskView:
    def show_tasks(self, tasks):
        print("Tasks:")
        for index, task in enumerate(tasks):
            status = "X" if task.completed else " "
            print(f"{index + 1}. [{status}] {task.description}")

# Controller
class TaskController:
    def __init__(self):
        self.tasks = []
        self.view = TaskView()

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            task.complete()

    def show_tasks(self):
        self.view.show_tasks(self.tasks)

# Usage
if __name__ == "__main__":
    controller = TaskController()
    controller.add_task("Learn Python")
    controller.add_task("Write code")
    controller.add_task("Eat lunch")

    controller.show_tasks()

    
    controller.complete_task(0)

    controller.show_tasks()
