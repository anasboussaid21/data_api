from datetime import date

from data_generation.store import StoreCamera


def create_app() -> dict:
    """
    Create the available camera in our API
    5 stores, with each 8 cameras
    Each stores has a different number of people coming to it
    As well as different break and malfunction percentages
    (Not realistic, but we keep things simple)
    """

    store_name = ["Marjane", "Carrefour", "Zara", "MoroccoMall", "Decathlon"]
    store_avg_visit = [9000, 7000, 2500, 50000, 4000]
    store_std_visit = [500, 800, 500, 400, 100]
    perc_malfunction = [0.05, 0.05, 0.05, 0.05, 0.05]
    perc_break = [0.03, 0.03, 0.05, 0.02, 0]

    store_dict = dict()

    for i in range(len(store_name)):
        store_dict[store_name[i]] = StoreCamera(
            store_name[i],
            store_avg_visit[i],
            store_std_visit[i],
            perc_malfunction[i],
            perc_break[i],
        )
    return store_dict
