import pandas as pd
import csv
import re
import datetime
counter = 1
now = datetime.datetime.now()
today = now.date()
tomorrow = datetime.date.today() + datetime.timedelta(days=1)

csv= r'./temp.csv'

def user_input():
    user_input = input("Enter Message\n")
    add(user_input)
    

def add(input_string):
    Status = '[]'
    items = re.search(r"(.*?(?P<Project>\+\w+).*?)?(?P<DueDate>today|tomorrow|\d+.\d+.\d{2,}?).*?"
                      r"(?P<Message>(.*?)(?P<Context>(@\w+)).*)",
                      input_string, re.I)
    # testing
    # print(items.group('project'))
    # print(items.group('date'))
    # print(items.group('context'))
    # print(items.group('message'))
    try:
        if items.group('Project') is not None:
            Project = items.group('Project')
        else:
            Project = ""

        if items.group('DueDate') is None:
            DueDate = ""
        else:
            if items.group('DueDate') == 'today':
                DueDate = str(today)
            elif items.group('DueDate') == 'tomorrow':
                DueDate = str(tomorrow)
            else:
                DueDate = items.group('DueDate')
        if items.group('Context') is not None:
            Context = items.group('Context')
        else:
            Context = ""
        if items.group('Message') is not None:
            Message = items.group('Message')
        else:
            Project = ""
    except ValueError:
        print(e+" :Invalid Syntax")
    df = pd.read_csv(csv)
    data = [(Status, Project, DueDate, Context, Message)]
    # print(data)
    data_frame = pd.DataFrame(data=data, columns=['Status', 'Project', 'DueDate', 'Context', 'Message'])
    try:
        with open(csv, 'a') as csv_file:
            data_frame.to_csv(csv_file, header=False, index=False)
        print(data_frame.to_string(index=False))
    except FileNotFoundError as e:
        print(e)

def show(inp):
    data = pd.read_csv(csv)  #path
    df = pd.DataFrame(data=data)
    df.index +=1
    x = df.groupby(inp)  #takes the column name
    for name, group in x:
        print(name)
        print(group.to_string())


def delete(task_number):
    data = pd.read_csv(csv)  #path
    df = pd.DataFrame(data=data)
    df.index +=1
    df.drop(df.index[task_number]-1, inplace=True)
    df.to_csv(csv, index=False)
    print(df.to_string())


def complete(task_number):
    data = pd.read_csv(csv) #path
    df = pd.DataFrame(data=data)
    df.index +=1
    df.loc[task_number, 'Status'] = "[Done]"
    data.to_csv(csv,index=False)
    print(df.to_string())


def extend(task_number, date):
    data = pd.read_csv(csv)  #path
    df = pd.DataFrame(data=data)
    df.index +=1
    if date == 'today':
        data.loc[task_number, 'DueDate'] = today
    elif date == 'tomorrow':
        data.loc[task_number, 'DueDate'] = tomorrow
    else:
        data.loc[task_number, 'DueDate'] = date
    data.to_csv(csv,index=False)
    print(df.to_string())


def overdue():
    data = pd.read_csv(csv)  #path
    df = pd.DataFrame(data=data)
    df.index +=1
    df=df[df.Status != '[Done]']
    x = df.groupby("DueDate") # column name
    for date, group in x:
        if datetime.datetime.strptime(date, "%Y-%m-%d").date() <= today:
            print(group.to_string())

