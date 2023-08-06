from datetime import timedelta, datetime
import time
from voip_shifts.bot import bot
from rq.job import get_current_job
from sqlalchemy import and_, select
from tzlocal import get_localzone
import telnyx
from telnyx.error import InvalidParametersError

import subprocess

from voip_shifts.models import *
from voip_shifts.config import Config, log, session, rq



class Shifts():
    def __init__(self, employee_id:str, client_id:str, service_id:str, 
                start_date:datetime, end_date:datetime, minutes_time_delta:int, 
                active:bool, skip:bool, source_phone:str, destination_phone:str) -> None:
        self.sip_server = Config.SIP_SERVER
        self.password = Config.SIP_PASSWORD
        self.username = Config.SIP_USERNAME
        self.employee_id = employee_id
        self.client_id = client_id
        self.service_id = service_id
        self.minutes_time_delta = minutes_time_delta
        self.start_date = start_date
        self.end_date = end_date
        self.active = active
        self.skip = skip
        self.source_phone = source_phone
        self.destination_phone = destination_phone
        self.on_shift_call = f"1WWWWWWW{self.client_id}WWWWW"
        self.off_shift_call = f"2WWWWWWW{self.client_id}WWWWW{self.service_id}WWWWWWW1WWW0WWWWW"

    def is_callable(self, datetime_:datetime) -> bool:
        if datetime.now(get_localzone()) < datetime_ + timedelta(minutes=10):
            return True
        return False

    def get_printable_time(self, date_time:datetime) -> str:
        return date_time.strftime("%m_%d_%y_%I:%M_%p")

    def shift_call(self, type_of_call) -> None:
        current_job_id = get_current_job().id
        timetable = session.scalar(
            select(TimetableModel).filter(
                TimetableModel.job_id==current_job_id
            )
        )
        if self.skip is True or timetable is None:
            log.info("Call skiped or timetable is None")
            return None
        datetime_ = self.start_date if type_of_call is self.on_shift_call else self.end_date
        if not self.is_callable(datetime_):
            msg = f"""<b>Emploee {self.employee_id} shift call with {self.client_id}, \
                       service:{self.service_id} at {datetime_} UTC will not be executed \
                       {datetime.utcnow().strftime('%m-%d-%y-%I:%M')}</b>"""
            log.info(msg)
            bot.send_messages(msg)
            return None

        if Config.MODE == "prod":
            call = telnyx.Call
            call.create(connection_id="2021741919184356464", to=f"+1{self.destination_phone}", from_=f"+1{self.source_phone}")
            time.sleep(8)
            for i in range(10):
                time.sleep(1)
                try:
                    call.send_dtmf(digits=f"W4WWWWWW{self.employee_id}WWWWWWWW2WWWWWW{type_of_call}")
                except InvalidParametersError:
                    log.warning(f"Call not answered yet")
                    log.warning(f"Try again")
                else:
                    break
            if type_of_call is self.on_shift_call:
                time.sleep(48)
            else:
                time.sleep(68)
            try:
                call.hangup()
            except Exception as e:
                log.info(f"hangup error with {e}")

        msg = f"""Employee {self.employee_id} is {'On shift Call' if type_of_call is self.on_shift_call else 'Off shift call'} \
                  with {self.client_id}, service:{self.service_id} at {datetime.utcnow()} UTC0"""
        try:
            bot.send_messages(msg)
        except Exception as e:
            log.info("Don't send message")
        log.info(f"Shift call executed {current_job_id}")
        daily_report = session.scalar(
            select(DailyReportModel).filter(and_(
                DailyReportModel.company_id==timetable.company_id,
                DailyReportModel.date==timetable.date
            ))
        )

        if daily_report is None:
            daily_report = DailyReportModel(
                call_count = 0,
                date = datetime_.date(),
                company_id = timetable.company_id,
            )
            session.add(daily_report)
            session.flush()
        daily_report.call_count += 1

        if type_of_call is self.on_shift_call:
            job = rq.enqueue_at(
                self.end_date + (datetime.now(get_localzone()) - self.start_date),
                self.shift_call,
                self.off_shift_call
            )
            log.info(f"Off shift call is in queue with {job.id}")
            timetable.job_id = job.id

        try:
            session.commit()
        except Exception as e:
            log.error(f"Commit don't exist. Exception is {e}")
            session.rollback()
            bot.send_messages(f"EXCEPTION: {e}")
        else:
            log.info(f"Data recorded")
        finally:
            session.close()
