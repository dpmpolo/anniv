from django.shortcuts import render
from django.views.generic import ListView
from challenge.models import GoalInstance, Goal
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datetime import date
from collections import defaultdict
import random


# Create your views here.

class LoggedInMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)

class GoalInstanceView(LoggedInMixin, ListView):
    model = GoalInstance
    template_name = 'goalinstance_list.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(GoalInstanceView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['new_goal'] = self.new_goal
        return context

    def _new_goal(self):
        # find the number of times that we have used each goal
        all_goals = GoalInstance.objects.filter(user=self.request.user)
        choices = Goal.objects.all()
        
        if len(all_goals) > 0:
            goal_dict = defaultdict(lambda x: 0)
            for goal_inst in all_goals:
                goal_dict[goal_inst.goal] += 1

            # find the most number of times we have used any goal            
            high = max(goal_dict.values())

            # we can pick from all goals that haven't been used the most
            choices = [x for x in choices if goal_dict[x] != high]

        new_goal = random.choice(choices)

        # woohoo its our new goal
        gi = GoalInstance(goal=new_goal, user=self.request.user, started=date.today())
        gi.save()
        return gi
 
    def get_queryset(self):
        self.new_goal = False
        today = date.today().toordinal()
        sunday = today - (today % 7)
        sunday = date.fromordinal(sunday)
        try:
            current_goal = GoalInstance.objects.filter(user=self.request.user, started__gt=sunday)
            if len(current_goal) == 0:
                self.new_goal = True
                #pick a new goal
                self._new_goal()
                current_goal = GoalInstance.objects.filter(user=self.request.user, started__gt=sunday)

        except IndexError:
            return None
        return current_goal
