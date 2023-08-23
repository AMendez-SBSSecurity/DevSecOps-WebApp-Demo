from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from collections import defaultdict
import config
import csv

app = Flask(__name__)
app.config.from_object(config)

#Function to see the app
def show():
    show = config.SHOW_APP
    return show
show_app = show()
name_items_menu = app.config["TEXT_NAME_ITEM_MENU"]
@app.route('/')
def index():
    message_empty_page = app.config["TEXT_EMPTY_PAGE"]
    #If show_app is true, the application will display with the table like default view
    if show_app:
        csv_data = []
        with open('static/data.csv', 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                csv_data.append(row)
        return render_template('table.html', active_page='table', csv_data=csv_data,show_app=show_app,message_empty_page=message_empty_page,name_items_menu=name_items_menu)
    else:
        return render_template('index.html', show_app=show_app,message_empty_page=message_empty_page,name_items_menu=name_items_menu)
@app.route('/table')
def table():
    title_table = app.config["TEXT_TITLE_CONTENT_TABLE"]
    csv_data = []
    with open('static/data.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            csv_data.append(row)
    return render_template('table.html', active_page='table',csv_data=csv_data,show_app=show_app,title_table=title_table,name_items_menu=name_items_menu)
@app.route('/charts')
def charts():
    title_chart = app.config["TEXT_TITLE_CONTENT_CHART"]
    data = []
    with open('static/data.csv', 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)

    menu_item_totals = defaultdict(int)
    for item in data:
        menu_item_totals[item['menu_item']] += 1

    menu_items = list(menu_item_totals.keys())
    menu_item_counts = list(menu_item_totals.values())
    return render_template('charts.html', data={'menu_items': menu_items, 'menu_item_counts': menu_item_counts},active_page= 'charts',show_app=show_app, name_items_menu=name_items_menu,title_chart=title_chart)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    new_index = 1
    print(id)
    lines = []
    deleted = False
    with open('static/data.csv', 'r',encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        lines.append(header)
        for row in reader:
            if id == int(row[0]):
                deleted = True
            else:
                row[0] = new_index
                lines.append(row)
                new_index+=1
    if deleted:
        print("Item deleted successfully")
    else:
        print("Item not found")
    print(lines)
    with open('static/data.csv', 'w', newline='',encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(lines)
    return redirect(url_for('table'))

if __name__ == '__main__':
    app.run(debug=True)
