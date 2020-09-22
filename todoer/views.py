from collections import Counter
from datetime import timedelta

from django.utils.timezone import now
from django.views.generic import TemplateView

from todoer.models import Task


class Home(TemplateView):
    template_name = 'home.html'


class WeekScores(TemplateView):
    template_name = 'weekscores.html'

    def get_context_data(self, **kwargs):
        today = now().date()
        a_week_ago = today - timedelta(days=7)
        total = Counter()
        completed = Counter()
        for task in Task.objects.filter(date__gte=a_week_ago, date__lt=today).order_by('order'):
            total[task.template] += 1
            if task.completed:
                completed[task.template] += 1

        scores = []
        for template in total:
            scores.append({'name': template.name, 'completed': completed[template], 'total': total[template]})

        context = super().get_context_data(**kwargs)
        context['scores'] = scores
        context['overall'] = f'{sum(completed.values())}/{sum(total.values())}'
        context['percent'] = f'{round(sum(completed.values())/sum(total.values()) * 100)}%'
        return context
