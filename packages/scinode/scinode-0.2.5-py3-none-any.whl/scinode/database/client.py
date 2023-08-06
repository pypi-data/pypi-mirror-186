import pymongo
from scinode.profile.profile import profile_datas

scinode_client = pymongo.MongoClient(profile_datas["db_address"])
scinodedb = scinode_client[profile_datas["db_name"]]
db_nodetree = scinodedb["nodetree"]
db_node = scinodedb["node"]
