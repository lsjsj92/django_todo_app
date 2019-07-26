import requests

def get_data(type, datas=None):
    if type == "list":
        data = (requests.get('http://localhost:8000/todo_list/')).json()
    if type == "detail":
        data = (requests.get('http://localhost:8000/todo_list/'+str(datas['pk'])+"/")).json()
    if type == "delete":
        data = requests.delete('http://localhost:8000/todo_list/' + str(datas['pk']) + '/delete/', data=datas)
        data = "일정을 삭제하였습니다."
    if type == "create":
        data = requests.post('http://localhost:8000/todo_list/create/', data=datas)
        data = "일정을 추가하였습니다."
    if type == "update":
        data = requests.put('http://localhost:8000/todo_list/'+str(datas['pk'])+'/update/', data=datas)
        data = "일정을 업데이트하였습니다."
    return data
