from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']
engine = create_engine(db_connection_string,
                       connect_args={'ssl': {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def row2dict(row, columns):
  """
   Convert an SQLAlchemy row object to a Python dictionary.

   :param row: SQLAlchemy row object
   :return: Python dictionary
   """
  return {column: value for column, value in zip(columns, row)}


def load_jobs_from_db():
  with engine.connect() as conn:
    query = text("select * from jobs")
    result = conn.execute(query)
    columns = result.keys()

  rows = [row2dict(row, columns) for row in result]
  jobs = [row_dict for row_dict in rows]
  return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(f"SELECT * FROM jobs WHERE id = :val"),
                          {"val": id})
    columns = result.keys()
  rows = [row2dict(row, columns) for row in result]
  return None if len(rows) == 0 else rows[0]


def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text(
      "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)"
    )

    conn.execute(
      query, {
        'job_id': job_id,
        'full_name': data['full_name'],
        'email': data['email'],
        "linkedin_url": data['linkedin_url'],
        "education": data['education'],
        "work_experience": data['work_experience'],
        "resume_url": data['resume_url']
      })
