import csv, os
from backend.models import Task

current_dir = os.path.dirname(os.path.abspath(__file__))
target_dir = os.path.join(current_dir, os.pardir)
print(target_dir)
def run():
    currtask = Task.objects.all()
    order_id = 0
    for task in currtask:
        if order_id < task.order:
            order_id = task.order
    order_id+=1
    with open(os.path.join(target_dir,'extra_tasks.csv'), "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            task = Task(order=order_id,title=row[0], description=row[1])
            order_id+=1
            task.save()