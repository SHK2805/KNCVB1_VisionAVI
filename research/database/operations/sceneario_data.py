import json
from db_connection import get_db_connection


def store_scene(timestamp, location, resolution, camera_id):
    conn = get_db_connection()
    if conn is None:
        return None

    cursor = conn.cursor()
    query = """
        INSERT INTO Scenes (timestamp, location, resolution, camera_id)
        VALUES (%s, %s, %s, %s) RETURNING scene_id;
    """
    cursor.execute(query, (timestamp, location, resolution, camera_id))
    scene_id = cursor.fetchone()[0]  
    conn.commit()
    cursor.close()
    conn.close()
    
    return scene_id 



def store_object_detection(scene_id, object_label, bounding_box, confidence):
    conn = get_db_connection()
    if conn is None:
        return

    cursor = conn.cursor()
    query = """
        INSERT INTO ObjectDetections (scene_id, object_label, bounding_box, confidence)
        VALUES (%s, %s, %s, %s);
    """
    cursor.execute(query, (scene_id, object_label, json.dumps(bounding_box), confidence))
    conn.commit()
    cursor.close()
    conn.close()



def store_scene_description(scene_id, description):
    conn = get_db_connection()
    if conn is None:
        return

    cursor = conn.cursor()
    query = """
        INSERT INTO SceneDescriptions (scene_id, description)
        VALUES (%s, %s);
    """
    cursor.execute(query, (scene_id, description))
    conn.commit()
    cursor.close()
    conn.close()



#ToQuery Data from PostgreSQL



def get_scenes_by_time(start_time, end_time):
    conn = get_db_connection()
    if conn is None:
        return []

    cursor = conn.cursor()
    query = """
        SELECT * FROM Scenes
        WHERE timestamp BETWEEN %s AND %s;
    """
    cursor.execute(query, (start_time, end_time))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return results


def get_detections_by_scene(scene_id):
    conn = get_db_connection()
    if conn is None:
        return []

    cursor = conn.cursor()
    query = """
        SELECT * FROM ObjectDetections
        WHERE scene_id = %s;
    """
    cursor.execute(query, (scene_id,))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return results
