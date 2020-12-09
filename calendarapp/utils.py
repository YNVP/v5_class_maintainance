# calendarapp/utils.py

from datetime import datetime, timedelta,date
from calendar import HTMLCalendar
from .models import Event
from calendarapp.helper import get_current_user

class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, events):
		events_per_day = events.filter(start_time__day=day)
		d = ''

		for event in events_per_day:
		    d += f'''<li class="btn btn-dark" style='margin-left:10px;'> {event.get_html_url} </li>'''

		if day != 0:
		    if d=='':
		        return f'''<td><button type="button" class="btn btn-primary" data-toggle="modal" data-target='#day{day}' style='height:40px;width:40px;' disabled><span class='date' style='font-weight:bold;font-size:2.5vh;'>{day}</span></button></td>'''
		    else:
		        datecheck = date(self.year,self.month,day)
		        currday = date.today()
		        if datecheck < currday:
		            return f'''<td><button type="button" class="btn btn-danger" style='height:40px;width:40px;'><span class='date' style='font-weight:bold;font-size:2.5vh;'>{day}</span></button>'''
		        else:
		            return f'''<td><button type="button" class="btn btn-success" data-toggle="modal" data-target='#day{day}' style='height:40px;width:40px;'><span class='date' style='font-weight:bold;font-size:2.5vh;'>{day}</span></button>
                			            <div class="modal fade" id='day{day}' tabindex="-1" role="dialog" aria-labelledby='{day}label' aria-hidden="true" >
                                          <div class="modal-dialog" role="document" >
                                            <div class="modal-content" style="color: white; border-radius:15px; background-image: linear-gradient(to top left,#EF6DA0,#EE8E6B);">
                                              <div class="modal-header">
                                                <h5 class="modal-title" id="exampleModalLabel">Placements</h5>
                                                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                                  <span aria-hidden="true">&times;</span>
                                                </button>
                                              </div>
                                              <div class="modal-body">
                                                    {d}
                                              </div>
                                              <div class="modal-footer">
                                                <small>Please report your CR or Moderator if you got selected in any of CRDs.</small>
                                                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                                              </div>
                                            </div>
                                          </div></td>'''
		return '<td></td>'

	# formats a week as a tr
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)

		cal = f'<table style="margin: 20px;">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, events)}\n'
		cal+=f'</table>'
		return cal