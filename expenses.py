import argparse
import json
import os
from storage import load_data, save_data

DATA_FILE = 'expenses.json'

def add_category(args):
    data = load_data()
    if args.category in data['categories']:
        print(f"Категория {args.category} уже есть")
    else:
        data['categories'].append(args.category)
        save_data(data)
        print(f"Категория {args.category} успешно добавлена.")

def add_expense(args):
    data = load_data()
    
    try:
        cost = float(args.cost)
    except ValueError:
        print("Ошибка: Стоимость должна быть числом.")
        return

    if args.category not in data['categories']:
        print(f"Ошибка: Категории '{args.category}' не существует.")
        return

    new_expense = {
        "cost": cost,
        "category": args.category,
        "name": args.name
    }
    data['expenses'].append(new_expense)
    save_data(data)
    print(f"Добавлен расход: {args.name} ({cost})")  

def list_expenses(args):
    data = load_data()
    expenses = data['expenses']
    
    if args.category:
        expenses = [e for e in expenses if e['category'] == args.category]

    for e in expenses:
        print(f"[{e['category']}] {e['name']}: {e['cost']}")