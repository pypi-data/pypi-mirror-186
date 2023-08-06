"""A simple asynchronous background job queue."""

from gevent import monkey

monkey.patch_all()

import argparse  # noqa: E402
import importlib  # noqa: E402
import pathlib  # noqa: E402
import time  # noqa: E402
import traceback  # noqa: E402

import gevent.queue  # noqa: E402
import pendulum  # noqa: E402
import sqlyte  # noqa: E402
import txt  # noqa: E402
import web  # noqa: E402
import webcli  # noqa: E402

# XXX queue = gevent.queue.PriorityQueue()
worker_count = 20
main = txt.application("webqueue", __doc__)


def handle_job(host, job_run_id, db, cache_db, browser):
    """Handle a freshly dequeued job."""
    # TODO handle retries
    web.tx.host.name = host
    web.tx.host.db = db
    web.tx.host.cache = webcli.cache(db=cache_db)
    web.tx.browser = browser
    job = web.tx.db.select(
        "job_runs AS r",
        what="s.rowid, *",
        join="job_signatures AS s ON s.rowid = r.job_signature_id",
        where="r.job_id = ?",
        vals=[job_run_id],
    )[0]
    if job["started"]:
        return
    web.tx.db.update(
        "job_runs",
        where="job_id = ?",
        vals=[job_run_id],
        what="started = STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW')",
    )
    _module = job["module"]
    _object = job["object"]
    _args = web.load(job["args"])
    _kwargs = web.load(job["kwargs"])
    print(
        f"{host}/{_module}:{_object}",
        *(_args + list(f"{k}={v}" for k, v in _kwargs.items())),
        sep="\n  ",
        flush=True,
    )
    status = 0
    try:
        output = getattr(importlib.import_module(_module), _object)(*_args, **_kwargs)
    except Exception as err:
        status = 1
        output = str(err)
        traceback.print_exc()
    web.tx.db.update(
        "job_runs",
        vals=[status, output, job_run_id],
        what="finished = STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW'), status = ?, output = ?",
        where="job_id = ?",
    )
    run = web.tx.db.select("job_runs", where="job_id = ?", vals=[job_run_id])[0]
    st, rt = run["started"] - run["created"], run["finished"] - run["started"]
    web.tx.db.update(
        "job_runs",
        where="job_id = ?",
        what="start_time = ?, run_time = ?",
        vals=[
            f"{st.seconds}.{st.microseconds}",
            f"{rt.seconds}.{rt.microseconds}",
            job_run_id,
        ],
    )
    # XXX print(flush=True)


def run_scheduler(browser):
    """Check all schedules every minute and enqueue any scheduled jobs."""
    while True:
        now = pendulum.now()
        if now.second:
            time.sleep(0.9)
            continue
        # TODO schedule_jobs()
        time.sleep(1)


def schedule_jobs(browser):
    """Check schedule and enqueue jobs if necessary."""
    # TODO support for days of month, days of week
    print("checking schedule")
    # for host in get_hosts():
    #     web.tx = canopy.contextualize(host)
    #     jobs = web.tx.db.select("job_schedules AS sch",
    #                         join="""job_signatures AS sig ON
    #                                 sch.job_signature_id = sig.rowid""")
    #     for job in jobs:
    #         run = True
    #         minute = job["minute"]
    #         hour = job["hour"]
    #         month = job["month"]
    #         if minute[:2] == "*/":
    #             if now.minute % int(minute[2]) == 0:
    #                 run = True
    #             else:
    #                 run = False
    #         if hour[:2] == "*/":
    #             if now.hour % int(hour[2]) == 0 and now.minute == 0:
    #                 run = True
    #             else:
    #                 run = False
    #         if month[:2] == "*/":
    #             if now.month % int(month[2]) == 0 and now.hour == 0 \
    #                and now.minute == 0:
    #                 run = True
    #             else:
    #                 run = False
    #         if run:
    #             canopy.enqueue(getattr(importlib.import_module(job["module"]),
    #                                    job["object"]))
    # time.sleep(.9)


@main.register()
class Run:
    """Run the job queue."""

    def setup(self, add_arg):
        add_arg(
            "--browser",
            action=argparse.BooleanOptionalAction,
            help="include a web browser",
        )

    def run(self, stdin, log):
        """Serve the queue."""
        browser = None
        if self.browser:
            browser = web.agent.Firefox()
            # TODO gevent.spawn(run_scheduler, browser)

        def run_worker(domain, db, cache_db, browser):
            while True:
                for job in db.select("job_runs", where="started is null"):
                    handle_job(domain, job["job_id"], db, cache_db, browser)
                time.sleep(0.5)

        for db_filename in pathlib.Path().glob("site-*.db"):
            domain = db_filename.stem.removeprefix("site-")
            log.info(f"Watching for jobs at: {domain}")
            sqldb = sqlyte.db(f"site-{domain}.db")
            cache_db = sqlyte.db(f"cache-{domain}.db")
            for _ in range(worker_count):
                gevent.spawn(run_worker, domain, sqldb, cache_db, browser)
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:  # TODO capture supervisord's kill signal
            if self.browser:
                browser.quit()
