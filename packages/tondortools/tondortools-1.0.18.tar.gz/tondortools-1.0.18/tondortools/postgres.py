#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json
from contextlib import contextmanager
from datetime import datetime

import psycopg2
import psycopg2.extras


@contextmanager
def create_tr_cursor(connection_params):
    """Create cursor in a new transaction."""
    connection = psycopg2.connect(**connection_params)
    try:
        # psycopg2 does transaction using with statement.
        with connection:
            with connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                cursor.execute("SET timezone TO 'UTC';")
            # Give the application a new empty cursor.
            with connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                yield cursor
    finally:
        connection.close()


def submit_simple_job(job_name, tool_ident, job_step_params, task_list, connection_params,
                      worker_group="main", set_submitted=True, description=None):
    job_step_params = json.dumps(job_step_params)
    with create_tr_cursor(connection_params) as cursor:
        sql = "BEGIN;"
        cursor.execute(sql)

        if description is not None:
            sql = ("INSERT INTO supervisor_Job (name, description) VALUES (%s, %s) RETURNING id;")
            cursor.execute(sql, [job_name, description])
        else:
            sql = ("INSERT INTO supervisor_Job (name) VALUES (%s) RETURNING id;")
            cursor.execute(sql, [job_name])
        job_id = cursor.fetchone()[0]

        sql = ("INSERT INTO supervisor_JobStep (job_id, tool_ident, params, worker_group)"
               " VALUES (%s, %s, %s, %s)"
               " RETURNING id;")
        cursor.execute(sql, [job_id, tool_ident, job_step_params, worker_group])
        job_step_id = cursor.fetchone()[0]

        for task_param in task_list:
            sql = ("INSERT INTO supervisor_Task (job_step_id, params) VALUES (%s, %s);")
            cursor.execute(sql, [job_step_id, task_param])

        if set_submitted:
            sql = ("UPDATE supervisor_Job SET submitted = %s WHERE id = %s;")
            cursor.execute(sql, [datetime.utcnow(), job_id])

        sql = "COMMIT;"
        cursor.execute(sql)
    return job_id

def update_simple_job(country_code, sitecode,   connection_params, task_list, product):
                                 

    with create_tr_cursor(connection_params) as cursor:
        sql = "BEGIN;"
        cursor.execute(sql)

        for task_param in task_list:
            sql = ("INSERT INTO cop4n2k_jobmonitor (country, sitecode, productcode, year) VALUES (%s, %s, %s, %s);")
            cursor.execute(sql, [country_code, sitecode,  product, task_param])


        sql = "COMMIT;"
        cursor.execute(sql)
 


def set_submitted(job_id, connection_params):
    with create_tr_cursor(connection_params) as cursor:
        sql = ("UPDATE supervisor_Job SET submitted = %s WHERE id = %s;")
        cursor.execute(sql, [datetime.utcnow(), job_id])
