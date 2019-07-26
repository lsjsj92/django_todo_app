from django.shortcuts import render, redirect
from .models import TodoList
from .forms import TodoForm
from django.views import generic
from django.http import JsonResponse
from datetime import datetime, timedelta
import json

#board view
class Todo_board(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        #Reserved.objects.filter(client=client_id).order_by('-check_in')
        template_name = 'todo_board/todo_board_list.html'
        #기한 없는 일정, 마감 안된 애들
        todo_list_no_endDate = TodoList.objects.all().filter(end_date__isnull=True, is_complete=0).order_by('priority')
        #기한 있고, 마감이 안된 애들
        todo_list_endDate_non_complete = TodoList.objects.all().filter(end_date__isnull=False, is_complete=0).order_by('priority')
        #마김이 된 애들
        todo_list_endDate_complete = TodoList.objects.all().filter(is_complete=1).order_by('end_date')
        today = datetime.now()
        # deadline is close
        close_end_day = []
        #over time
        over_end_day = []
        for i in todo_list_endDate_non_complete:
            e_day = str(i.end_date).split("-")
            end_day = datetime(int(e_day[0]), int(e_day[1]), int(e_day[2]))
            if (end_day - today).days < -1: over_end_day.append(i.title)
            if (end_day - today).days >= -1 and (end_day - today).days < 3: close_end_day.append(i.title)
        return render(request, template_name, {"todo_list_endDate_non_complete": todo_list_endDate_non_complete, "todo_list_endDate_complete": todo_list_endDate_complete, "todo_list_no_endDate": todo_list_no_endDate, 'close_end_day': close_end_day, 'over_end_day':over_end_day})

#todo_detail view
class Todo_board_detail(generic.DetailView):
    model = TodoList
    template_name = 'todo_board/todo_board_detail.html'
    context_object_name = 'todo_list'

#todo_update view
class Todo_board_update(generic.UpdateView):
    model = TodoList
    form_class = TodoForm
    template_name = 'todo_board/todo_board_update.html'
    success_url = '/board/'

    def form_valid(self, form):
        form.save()
        return render(self.request, 'todo_board/todo_board_success.html', {"message": "일정을 업데이트 했습니다"})

# todo_delete view
class Todo_board_delete(generic.DeleteView):
    model = TodoList
    success_url = '/board/'
    context_object_name = 'todo_list'

# when write new todo_list
# post -> when click "save"
# get -> just view a template
def check_post(request):
    template_name = 'todo_board/todo_board_success.html'
    if request.method == "POST":
        if str(request.path).split("/board/")[1].split("/")[0] == "insert":
            form = TodoForm(request.POST)
            if form.is_valid():
                message = "일정을 추가하였습니다."
                if len(request.POST.get('title')) < 2:
                    message = "제목은 2글자 이상으로 입력해주세요!"
                else:
                    todo = form.save(commit=False)
                    todo.todo_save()
                return render(request, template_name, {"message": message})
        elif str(request.path).split("/board/")[1].split("/")[0] == "save_prioirity":
            todo_list = json.loads(request.POST['todo_dict'])
            for key, value in todo_list.items():
                if key == "None" : continue
                todo_selected = TodoList.objects.get(pk=key)
                todo_selected.priority = value
                todo_selected.save()
            return JsonResponse({'text': '저장되었습니다.'})
        elif str(request.path).split("/board/")[1].split("/")[0] == "is_complete":
            pk = request.POST['data']
            return_value = checkbox_event(pk, True)
            return JsonResponse(return_value)
        elif str(request.path).split("/board/")[1].split("/")[0] == "is_non_complete":
            pk = request.POST['data']
            return_value = checkbox_event(pk, False)
            return JsonResponse(return_value)
    else:
        template_name = 'todo_board/todo_board_insert.html'
        form = TodoForm
        return render(request, template_name, {"form" : form})

def checkbox_event(pk, is_check):
    todo_selected = TodoList.objects.get(pk=pk)
    if is_check == True:
        todo_selected.is_complete = 1
        todo_selected.priority = None
    else :
        todo_selected.is_complete = 0
    todo_selected.save()
    return_value = {'text': '저장되었습니다.'}
    return return_value

