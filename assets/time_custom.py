import datetime


def time_bm(timezone):
    now = datetime.datetime.utcnow()

    if timezone is None:
        return now
    else:
        time_offsets = [int(value) for value in timezone.split(':')]
        if len(time_offsets) == 2:
            now += datetime.timedelta(hours=time_offsets[0],
                                      minutes=time_offsets[1] * (-1 if (time_offsets[0] < 0) else 1))
        else:
            now += datetime.timedelta(hours=time_offsets[0])
        final_time = str(now)[11:16]
        return final_time