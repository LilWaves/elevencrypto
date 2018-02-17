from django.views.generic import TemplateView
#from fusioncharts import FusionCharts

class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'
