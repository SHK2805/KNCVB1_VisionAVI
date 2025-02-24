from scene_data import get_scenes_by_time, get_detections_by_scene

scenes = get_scenes_by_time("2024-08-12 12:00:00", "2024-08-12 13:00:00")
print("🔹 Scenes in given time range:", scenes)


scene_id = 1  
detections = get_detections_by_scene(scene_id)
print("🔹 Objects detected in scene:", detections)
 