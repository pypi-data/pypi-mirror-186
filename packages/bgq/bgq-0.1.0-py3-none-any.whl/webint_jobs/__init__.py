""""""

import importlib

import web

app = web.application(
    __name__,
    prefix="jobs",
    args={
        "job_module": r"[\w.]+",
        "job_object": r"\w+",
        "job_arghash": r"\w+",
        "job_run_id": r"\!+",
    },
    model={
        "job_signatures": {
            "module": "TEXT",
            "object": "TEXT",
            "args": "BLOB",
            "kwargs": "BLOB",
            "arghash": "TEXT",
            "unique": ("module", "object", "arghash"),
        },
        "job_runs": {
            "job_signature_id": "INTEGER",
            "job_id": "TEXT UNIQUE",
            "created": """DATETIME NOT NULL
                          DEFAULT(STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW'))""",
            "started": "DATETIME",
            "finished": "DATETIME",
            "start_time": "REAL",
            "run_time": "REAL",
            "status": "INTEGER",
            "output": "TEXT",
        },
        "job_schedules": {
            "job_signature_id": "INTEGER",
            "minute": "TEXT",
            "hour": "TEXT",
            "day_of_month": "TEXT",
            "month": "TEXT",
            "day_of_week": "TEXT",
            "unique": (
                "job_signature_id",
                "minute",
                "hour",
                "day_of_month",
                "month",
                "day_of_week",
            ),
        },
    },
)


@app.control(r"")
class Jobs:
    """"""

    def get(self):
        active = web.tx.db.select(
            "job_runs AS jr",
            join="job_signatures AS js ON js.rowid = jr.job_signature_id",
            where="started IS NOT NULL AND finished IS NULL",
        )
        finished = web.tx.db.select(
            "job_runs AS jr",
            join="job_signatures AS js ON js.rowid = jr.job_signature_id",
            where="finished IS NOT NULL",
            order="finished DESC",
            limit=20,
        )
        return app.view.index(active, finished)


@app.control(r"slow")
class SlowJobs:
    """"""

    def get(self):
        duration = web.form(duration=60).duration
        slowest = web.tx.db.select(
            "job_runs AS jr",
            join="job_signatures AS js ON js.rowid = jr.job_signature_id",
            where="finished IS NOT NULL AND run_time > ?",
            vals=[duration],
            order="run_time DESC",
        )
        return app.view.slow(slowest)


@app.control(r"schedules")
class Schedules:
    """"""

    def get(self):
        schedules = web.tx.db.select(
            "job_schedules AS sc",
            join="job_signatures AS si ON si.rowid = sc.job_signature_id",
        )
        return app.view.schedules(schedules)


@app.control(r"{job_module}")
class ByModule:
    """"""

    def get(self, job_module):
        jobs = web.tx.db.select(
            "job_signatures",
            what="rowid AS id, *",
            where="module = ?",
            vals=[job_module],
        )
        return app.view.by_module(job_module, jobs)


@app.control(r"{job_module}/{job_object}")
class ByObject:
    """"""

    def get(self, job_module, job_object):
        callable = getattr(importlib.import_module(job_module), job_object)
        jobs = web.tx.db.select(
            "job_signatures",
            what="rowid AS id, *",
            where="module = ? AND object = ?",
            vals=[job_module, job_object],
        )
        return app.view.by_object(job_module, job_object, callable, jobs)


@app.control(r"{job_module}/{job_object}/{job_arghash}")
class Job:
    """"""

    def get(self, job_module, job_object, job_arghash):
        callable = getattr(importlib.import_module(job_module), job_object)
        job = web.tx.db.select(
            "job_signatures",
            what="rowid AS id, *",
            where="module = ? AND object = ? AND arghash LIKE ?",
            vals=[job_module, job_object, job_arghash + "%"],
        )[0]
        runs = web.tx.db.select(
            "job_runs",
            where="job_signature_id = ?",
            vals=[job["id"]],
            order="finished DESC",
            limit=100,
        )
        total = web.tx.db.select(
            "job_runs",
            what="count(*) AS count",
            where="job_signature_id = ?",
            vals=[job["id"]],
            order="finished DESC",
        )[0]["count"]
        return app.view.job(job_module, job_object, callable, job, runs, total)


@app.control(r"{job_module}/{job_object}/{job_arghash}/{job_run_id}")
class JobRun:
    """"""

    def get(self, job_module, job_object, job_arghash, job_run_id):
        callable = getattr(importlib.import_module(job_module), job_object)
        job = web.tx.db.select(
            "job_signatures",
            what="rowid AS id, *",
            where="module = ? AND object = ? AND arghash LIKE ?",
            vals=[job_module, job_object, job_arghash + "%"],
        )[0]
        run = web.tx.db.select(
            "job_runs",
            what="rowid, *",
            where="job_id = ?",
            vals=[job_run_id],
            order="finished DESC",
        )[0]
        return app.view.run(job_module, job_object, callable, job, run)
