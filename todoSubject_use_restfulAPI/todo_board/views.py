from django.shortcuts import render, redirect
from .models import TodoList
from .forms import TodoForm
from .get_data import get_data
from django.views import generic
from django.http import JsonResponse
from datetime import datetime, timedelta
import json

#board view
class Todo_board(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        datas = get_data("list")
        todo_list_no_endDate, todo_list_endDate_non_complete, todo_list_endDate_complete, close_end_day, over_end_day = [],[],[],[],[]
        for data in datas:
            if data['end_date'] is None and data['is_complete'] == 0: todo_list_no_endDate.append(data)
            elif data['end_date'] is not None and data['is_complete'] == 0: todo_list_endDate_non_complete.append(data)
            elif data['is_complete'] == 1 : todo_list_endDate_complete.append(data)
        todo_list_no_endDate = sorted(todo_list_no_endDate, key=lambda x: x['priority'] if x['priority'] is not None else 0, reverse=False)
        todo_list_endDate_non_complete = sorted(todo_list_endDate_non_complete, key=lambda x: x['priority'] if x['priority'] is not None else 0, reverse=False)
        todo_list_endDate_complete = sorted(todo_list_endDate_complete, key=lambda x: x['end_date'] if x['end_date'] is not None else '0000-00-00', reverse=True)

        template_name = 'todo_board/todo_board_list.html'
        today = datetime.now()
        # deadline is close
        close_end_day = []
        #over time
        over_end_day = []
        for i in todo_list_endDate_non_complete:
            e_day = str(i["end_date"]).split("-")
            end_day = datetime(int(e_day[0]), int(e_day[1]), int(e_day[2]))
            if (end_day - today).days < -1: over_end_day.append(i["title"])
            if (end_day - today).days >= -1 and (end_day - today).days < 3: close_end_day.append(i["title"])
        return render(request, template_name, {"todo_list_endDate_non_complete": todo_list_endDate_non_complete, "todo_list_endDate_complete": todo_list_endDate_complete, "todo_list_no_endDate": todo_list_no_endDate, 'close_end_day': close_end_day, 'over_end_day':over_end_day})

#todo_detail view
class Todo_board_detail(generic.DetailView):
    def get(self, request, *args, **kwargs):
        datas = {
            'pk': self.kwargs['pk']
        }
        datas = get_data("detail", datas=datas)
        return render(self.request, 'todo_board/todo_board_detail.html', {"todo_list": datas})

#todo_update view
class Todo_board_update(generic.UpdateView):
    model = TodoList
    form_class = TodoForm
    template_name = 'todo_board/todo_board_update.html'
    success_url = '/board/'
    def form_valid(self, form):
        datas = {
            'title': self.request.POST.get('title'),
            'content': self.request.POST.get('title'),
            'end_date': self.request.POST.get('end_date'),
            'pk' : self.kwargs['pk']
        }
        datas = get_data("update", datas=datas)
        return render(self.request, 'todo_board/todo_board_success.html', {"message": datas})


# when write new todo_list
# post -> when click "save"
# get -> just view a template
def check_post(request, pk=None):
    template_name = 'todo_board/todo_board_success.html'
    # when POST
    if request.method == "POST":
        # when data isnert
        if str(request.path).split("/board/")[1].split("/")[0] == "insert":
            form = TodoForm(request.POST)
            if form.is_valid():
                if len(request.POST.get('title')) < 2:
                    datas = "제목은 2글자 이상으로 입력해주세요!"
                else:
                    datas = {
                        'title':request.POST.get('title'),
                        'content' : request.POST.get('content'),
                        'end_date' : request.POST.get('end_date'),
                        'is_complete': 0
                    }
                    datas = get_data("create", datas=datas)
                return render(request, template_name, {"message": datas})

        # when data save priority
        elif str(request.path).split("/board/")[1].split("/")[0] == "save_prioirity":
            todo_list = json.loads(request.POST['todo_dict'])
            for key, value in todo_list.items():
                if key == "None" : continue
                # too slow..
                datas = get_data("detail", datas={'pk': key})
                datas['priority'] = value
                datas['pk'] = datas.pop('no')
                datas = get_data("update", datas=datas)
            return JsonResponse({'text': '저장되었습니다.'})
        #when check checkbox to complete
        elif str(request.path).split("/board/")[1].split("/")[0] == "is_complete":
            pk = request.POST['data']
            return_value = checkbox_event(pk, True)
            return JsonResponse(return_value)
        #when uncheck checkbox complete
        elif str(request.path).split("/board/")[1].split("/")[0] == "is_non_complete":
            pk = request.POST['data']
            return_value = checkbox_event(pk, False)
            return JsonResponse(return_value)
    # GET
    else:
        if str(request.path).split("/board/")[1].split("/")[0] == "insert":
            template_name = 'todo_board/todo_board_insert.html'
            form = TodoForm
            return render(request, template_name, {"form" : form})
        # confirm delete
        if str(request.path).split("/board/")[1].split("/")[1] == "delete":
            datas = get_data("detail", datas={'pk':pk})
            template_name = 'todo_board/todolist_confirm_delete.html'
            return render(request, template_name, {'todo_list':datas})
        # delete
        if str(request.path).split("/board/")[1].split("/")[1] == "delete_complete":
            datas = get_data("delete", datas={'pk': pk})
            return render(request, template_name, {'message':datas})

def checkbox_event(pk, is_check):
    datas = get_data("detail", datas={'pk': pk})
    datas['pk'] = datas.pop('no')
    if is_check == True:
        datas['is_complete'] = 1
    else:
        datas['is_complete'] = 0
    datas = get_data("update", datas=datas)
    return_value = {'text': '저장되었습니다.'}
    return return_value