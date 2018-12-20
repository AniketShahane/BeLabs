from django.shortcuts import render, redirect
from .models import Goal
# Create your views here.
def goal(request):
    if request.method == "POST":
        goal = request.POST['goal']
        print('look below')
        print(goal)
        new_goal = Goal(goal=goal, writer=request.user)
        new_goal.save()
        return redirect('dashboard')

def delgoal(request, goal_id):
    if request.method == "POST":
        goal = Goal.objects.get(id=goal_id)
        goal.delete()
        return redirect('dashboard')
