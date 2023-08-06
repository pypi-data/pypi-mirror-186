<%!
import datetime
%>\
<%inherit file="/site.mako" />\
<h2>${translate('I18n')}</h2>

<% date = datetime.datetime(2021, 1, 1) %>\
<pre class="bg-light border rounded p-3">
date = datetime.datetime(2021, 1, 1)                                        # 01/01/2021 00:00:00

format_date(date)                                                           # ${format_date(date)}
format_datetime(date)                                                       # ${format_datetime(date)}
format_date(date, format='long')                                            # ${format_date(date, format='long')}
format_datetime(date, date_format='long')                                   # ${format_datetime(date, date_format='long')}
format_datetime(date, date_format='short')                                  # ${format_datetime(date, date_format='short')}
format_datetime(date, date_format='short', time_format='short')             # ${format_datetime(date, date_format='short', time_format='short')}
format_datetime(localtoutc(date), date_format='short', time_format='short') # ${format_datetime(localtoutc(date), date_format='short', time_format='short')}
format_datetime(utctolocal(date), date_format='short', time_format='short') # ${format_datetime(utctolocal(date), date_format='short', time_format='short')}
format_time(date)                                                           # ${format_time(date)}
format_time(date, format='short')                                           # ${format_time(date, format='short')}

format_decimal(1.01)                                                        # ${format_decimal(1.01)}

translate('Title')                                                          # ${translate('Title')}

% for num in range(4):
pluralize('{0} article', '{0} articles', ${num}).format(${num})                       # ${pluralize('{0} article', '{0} articles', num).format(num)}
% endfor
</pre>
