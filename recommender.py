import pandas as pd

def recommend_product(query_data):
    df=pd.read_csv('products.csv')

    if query_data["price"]:
        budget = int(query_data["price"].replace("k","000"))
        df = df[df["price"] <= budget]

    if "16gb" in query_data["text"].lower():
        df = df[df["ram"] == "16GB"]

        top_products = df.head(3).to_dict(orient="records")
        response = "Here are some recommendation:\n"
        for p in top_products:
            response += f"- {p['name']} — Rs.{p['price']} | {p['battery']}\n"
        return response