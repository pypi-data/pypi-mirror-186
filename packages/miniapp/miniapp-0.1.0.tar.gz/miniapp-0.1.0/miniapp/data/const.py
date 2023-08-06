"""
Constants.
"""

ROW_ID = "_id"                  # name of built-in, always unique, always present row identifier

QUERY_LT = "$lt"
QUERY_LE = "$lte"
QUERY_GT = "$gt"
QUERY_GE = "$gte"
QUERY_NE = "$ne"
QUERY_IN = "$in"
QUERY_AND = "$and"
QUERY_OR = "$or"
QUERY_NOT = "$not"
QUERY_EXISTS = "$exists"
QUERY__ALL = (QUERY_LT, QUERY_LE, QUERY_GT, QUERY_GE, QUERY_NE, QUERY_IN, QUERY_AND, QUERY_OR, QUERY_NOT, QUERY_EXISTS)

UPDATE_SET = "$set"             # update command to set fields, i.e. {"$set": {"x.y.z": 1}}
UPDATE_UNSET = "$unset"         # update command to delete fields
UPDATE_PUSH = "$push"           # update command: append to list
UPDATE_INC = "$inc"             # update command: increment by, i.e. {"$inc": {"x.y.z": 1}}
UPDATE__ALL = (UPDATE_SET, UPDATE_UNSET, UPDATE_PUSH, UPDATE_INC)
