from scene_data import store_scene, store_object_detection, store_scene_description
scene_id = store_scene(
    timestamp="2024-08-12 12:30:00",
    location="Library",
    resolution="1920x1080",
    camera_id="Cam_001"
)
print(f"Scene stored with ID: {scene_id}")


store_object_detection(scene_id, "Person", [100, 200, 150, 250], 0.95)
store_object_detection(scene_id, "Book", [300, 400, 350, 450], 0.89)


store_scene_description(scene_id, "A person is standing near bookshelves.")

print(" Scene metadata, detections, and description are stored")

     