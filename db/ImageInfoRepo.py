"""
Add, Delete, Update, Search on table test_image
"""
# !/usr/bin/env python3

from db import mysql

class ImageInfo:
    """Entity Class to Table test_image"""
    pk = -1
    name = ""

    def __init__(self, _pk, _name):
        self.pk = _pk
        self.name = _name

    def json(self):
        return {"id": self.pk, "name": self.name}


def new(image):
    if isinstance(image, dict):
        return ImageInfo(image['id'], image['name'])
    elif isinstance(image, ImageInfo):
        return ImageInfo(image.pk, image.name)


def find_all_from_db(return_json):

    conn = mysql.get_conn()
    cursor = conn.cursor()

    # SQL 插入语句
    sql = "select id,name from test_image"
    images = []

    try:
        # 执行sql语句
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            if return_json is True:
                images.append({"id": row[0], "name": row[1]})
            else:
                images.append(new({"id": row[0], "name": row[1]}))

    except Exception as e:
        raise e

    finally:
        conn.close()

    return images


if __name__ == '__main__':
    print(find_all_from_db(True))
