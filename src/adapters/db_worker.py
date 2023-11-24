import os

import psycopg2

from src.entity.course import Course


class DBworker:

    def get_best_course(self, user_id, get=10):
        conn = psycopg2.connect(
            dbname=os.environ.get('db_name'),
            user=os.environ.get('db_user'),
            password=os.environ.get('db_password'),
            host=os.environ.get('db_host'),
            port=os.environ.get('db_port')
        )
        sql_get_preferenses_courses = """
            select *
            from courses,
            limit 40;
        """
        response = []

        try:
            cur = conn.cursor()
            cur.execute(sql_get_preferenses_courses)
            results = cur.fetchall()

            for row in results:
                response.append(Course(
                    embedding=row[0]
                ))

        except Exception as e:
            print("Database connection or execution issue:", e)

        finally:
            cur.close()
            return response


    @staticmethod
    def get_course():
        conn = psycopg2.connect(
            dbname=os.environ.get('db_name'),
            user=os.environ.get('db_user'),
            password=os.environ.get('db_password'),
            host=os.environ.get('db_host'),
            port=os.environ.get('db_port')
        )
        sql = """
                    select embedding
                    from courses,
                    limit 40;
                """
        response = []

        try:
            cur = conn.cursor()
            cur.execute(sql)
            results = cur.fetchall()

            for row in results:
                response.append(Course(
                    embedding=row[0]
                ))

        except Exception as e:
            print("Database connection or execution issue:", e)

        finally:
            cur.close()
            return response


if __name__ == "__main__":
    os.environ['host'] = '26.191.10.163'
    os.environ['user'] = 'postgres'
    os.environ['password'] = 'admin'
    os.environ['db'] = 'ufa_hack_2023'
    os.environ['port'] = '5432'

    conn = psycopg2.connect(
        dbname=os.environ.get('db_name'),
        user=os.environ.get('db_user'),
        password=os.environ.get('db_password'),
        host=os.environ.get('db_host'),
        port=os.environ.get('db_port')
    )
    sql = """
                        select embedding
                        from courses,
                        limit 40;
                    """
    response = []

    try:
        cur = conn.cursor()
        cur.execute(sql)
        results = cur.fetchall()

        for row in results:
            response.append(Course(
                embedding=row[0]
            ))

        print(response)
    except Exception as e:
        print("Database connection or execution issue:", e)

    finally:
        cur.close()