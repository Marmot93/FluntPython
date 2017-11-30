import datetime
import textwrap
import time

# available_clocks = [
#     ('clock', time.clock),
#     ('monotonic', time.monotonic),
#     ('perf_counter', time.perf_counter),
#     ('process_time', time.process_time),
#     ('time', time.time),
# ]
#
# for clock_name, func in available_clocks:
#     print(textwrap.dedent('''\
#     {name}:
#         adjustable    : {info.adjustable}
#         implementation: {info.implementation}
#         monotonic     : {info.monotonic}
#         resolution    : {info.resolution}
#         current       : {current}
#     ''').format(
#         name=clock_name,
#         info=time.get_clock_info(clock_name),
#         current=func())
#     )

# unix
print(time.time())
# str time
print(time.ctime())
# str time
print(time.asctime())
# struct_time to unix
print(time.mktime(time.localtime()))
# format
print(time.strftime('%Y-%m-%d %H:%M:%S'))
# str to struct_time
print(time.strptime("2017-11-28 15:09:44", '%Y-%m-%d %H:%M:%S'))

print(datetime.datetime.strptime("2017-11-28" + " 23:59:59", "%Y-%m-%d %H:%M:%S"))

