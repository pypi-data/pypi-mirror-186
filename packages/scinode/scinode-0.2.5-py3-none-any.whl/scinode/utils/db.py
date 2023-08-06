def copy_item(name, item, db):
    """Copy one item in the collection

    Args:
        name (str): new name of the ite
        item (dict): data of the item
        db (collection): _description_
    """
    import uuid
    import copy

    data = copy.deepcopy(item)
    data.pop("_id")
    data["name"] = name
    uuid = str(uuid.uuid1())
    data["uuid"] = uuid
    insert_one(data, db)


def insert_one(item, db):
    """add one item to database

    Args:
        item (dict): _description_
    """
    if db.count_documents({}) == 0:
        index = 1
    else:
        index = db.find().sort("index", -1).limit(1)[0]["index"] + 1
    item.update({"index": index})
    db.insert_one(item)


def update_one(item, db, key="uuid"):
    """update one item to database

    Args:
        item (dict): _description_
    """
    query = {key: item[key]}
    newvalues = {"$set": item}
    db.update_one(query, newvalues)


def push_message(query, db, items):
    """push message to database

    Args:
        item (dict): _description_
    """
    newvalues = {"$push": items}
    db.update_one(query, newvalues)
