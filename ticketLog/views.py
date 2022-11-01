from django.shortcuts import render
from django.views import View
from datetime import datetime
from ticketLog.models import Sections, Days, Ticket


# Create your views here.
class Home(View):
    def get(self, request):
        print(Days.choices)
        return render(request, "home.html", {"days": Days.choices, "sections": Sections.choices})

    def post(self, request):
        print(Days.choices)
        # extract form data from POST
        try:
            section = request.POST["section"]
            print(section)

            # convert datetime-local string to a Python datetime
            dateTime = datetime.strptime(request.POST["dateTime"], "%Y-%m-%dT%H:%M")
            print(dateTime)

            dayOfWeek = Days[dateTime.strftime("%A")].value
            print(dayOfWeek)

            # instantiate and save a Ticket
            Ticket.objects.create(section=section, dateTime=dateTime, dayOfWeek=dayOfWeek)
            msg = "Ticket created successfully"

        except ValueError:
            msg = "Invalid section, date, or time"

        return render(request, "home.html", {"days": Days.choices, "sections": Sections.choices, "msg": msg})


class History(View):
    def get(self, request):
        return render(request, "history.html", {"days": Days.choices, "sections": Sections.choices})

    def post(self, request):
        # extract day and section from POST
        day = request.POST["day"]
        section = request.POST["section"]
        # query (filter) for tickets
        tickets = Ticket.objects.filter(dayOfWeek=day, section=section)
        print(tickets)
        # render a response (with a table of matching tickets)
        return render(request, "history.html", {"days": Days.choices, "sections": Sections.choices, "tickets": tickets})
