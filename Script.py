#! /usr/bin/env python
import argparse
from ToDo import add, delete, complete, show, extend, overdue
task_number = 0
date_number = 1

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="Todo")
    parser.add_argument("todo", help="todo please provide options total 6")
    parser.add_argument("-overdue", help="prints overdue and old tasks")
    parser.add_argument("-extend", nargs=2, help="-extend task DueDate")
    parser.add_argument("-complete", help="-extend task DueDate", type=int)
    parser.add_argument("-add", help="todo -add in string", type=str)
    parser.add_argument("-delete",  help="-delete and task-number", type=int)
    parser.add_argument("-list",
                        help="list options 4 fields",
                        type=str, default="I")
    args = parser.parse_args()
    if args.add:
        add_to_todo = args.add
        add(add_to_todo)
    elif args.delete:
        delete = args.delete
        delete(delete)
    elif args.extend:
        extend_todo = args.extend
        task_number = int(extend_todo[task_number])
        extend_to_date = extend_todo[date_number]
        extend(task_number, extend_to_date)
    elif args.complete:
        comp=args.complete
        complete(comp)
    elif args.list:
        showing = args.list
        # print(e)
        show(showing)
    elif args.overdue:
        past = args.overdue
        overdue()




