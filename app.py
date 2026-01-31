import os
from flask import Flask
from pymongo import MongoClient
import redis

app = Flask(__name__)

mongo_client = MongoClient(os.getenv("MONGO_URI"))
db = mongo_client.ml_db

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT")),
    decode_responses=True
)
