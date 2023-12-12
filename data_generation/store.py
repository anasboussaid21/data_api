from datetime import date

import numpy as np

from data_generation.camera import VisitCamera


class StoreCamera:
    def __init__(
        self,
        name: str,
        avg_visit: int,
        std_visit: int,
        perc_malfunction: float = 0,
        perc_break: float = 0,
    ) -> None:
        """Initialize a store"""
        self.name = name
        self.cameras = list()

        # To always get the same result when asking for the same store
        seed = np.sum(list(self.name.encode("ascii")))
        np.random.seed(seed=seed)

        # 80/20: most people take the main entrance, and so on ;)
        traffic_percentage = [0.48, 0.30, 0.05, 0.03, 0.01, 0.02, 0.10, 0.01]
        np.random.shuffle(traffic_percentage)

        # Initialisation of the store's cameras
        # To keep things simple, we assume each store has eight cameras
        # Otherwise we would need to dynamically create traffic_percentages that sum to 1
        for i in range(8):
            camera = VisitCamera(
                int(traffic_percentage[i] * avg_visit),
                int(traffic_percentage[i] * std_visit),
                perc_malfunction,
                perc_break,
            )

            self.cameras.append(camera)

    def get_camera_traffic(self, camera_id: int, business_date: date) -> int:
        """Return the traffic for one camera at a date"""
        return self.cameras[camera_id].get_visit_count(business_date)

    def get_store_traffic(self, business_date: date) -> int:
        """Return the traffic for all cameras of the store at a date"""
        visit = 0
        for i in range(8):
            visit += self.cameras[i].get_visit_count(business_date)
        return visit
