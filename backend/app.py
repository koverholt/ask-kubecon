import json
import os
import re
from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain.retrievers import GoogleVertexAIMultiTurnSearchRetriever

app = Flask(__name__)
cors = CORS(app)

project_id = "kubecon-gen-ai"
location = "global"
data_store_id = "ask-kubecon_1698683635501"

retriever = GoogleVertexAIMultiTurnSearchRetriever(
    project_id=project_id,
    data_store_id=data_store_id,
    engine_data_type=0,
    max_documents=5,
    max_extractive_answer_count=5,
    get_extractive_answers=True,
)


@app.route("/", methods=["GET", "POST"])
def search():
    if request.method == "GET":
        return 200

    if request.method == "POST":
        request_json = request.get_json(silent=True)
        if request_json and "query" in request_json:
            message = request_json["query"]

        results = retriever.get_relevant_documents(query)
        print(results)

        return results

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
