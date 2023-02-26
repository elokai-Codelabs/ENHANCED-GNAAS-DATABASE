# from django.http import JsonResponse
# from myapp.models import MyModel

# def chart_data(request):
#     data = {}
#     for item in MyModel.objects.all():
#         category = item.category
#         if category not in data:
#             data[category] = 0
#         data[category] += 1
#     return JsonResponse(data)


# {% extends "base.html" %}

# {% block content %}
#     <h1>My Chart</h1>
#     <canvas id="myChart"></canvas>
# {% endblock %}

# {% block scripts %}
#     <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
#     <script>
#         fetch("{% url 'chart_data' %}")
#             .then(response => response.json())
#             .then(data => {
#                 var ctx = document.getElementById('myChart').getContext('2d');
#                 var myChart = new Chart(ctx, {
#                     type: 'bar',
#                     data: {
#                         labels: Object.keys(data),
#                         datasets: [{
#                             label: 'Count',
#                             data: Object.values(data),
#                             backgroundColor: 'rgba(255, 99, 132, 0.2)',
#                             borderColor: 'rgba(255, 99, 132, 1)',
#                             borderWidth: 1
#                         }]
#                     },
#                     options: {
#                         scales: {
#                             y: {
#                                 beginAtZero: true
#                             }
#                         }
#                     }
#                 });
#             });
#     </script>
# {% endblock %}




