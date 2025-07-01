import gradio as gr
from ted_recommender import TEDRecommender

# Load the model
recommender = TEDRecommender("TED.csv")

def get_recommendations(text):
    results = recommender.recommend(text)
    return [(row['title'], row['url']) for _, row in results.iterrows()]

iface = gr.Interface(
    fn=get_recommendations,
    inputs=gr.Textbox(lines=3, label="Enter a TED Talk topic or description"),
    outputs=gr.Dataframe(headers=["Title", "Link"]),
    title="TED Talk Recommender",
    description="Get recommended TED Talks based on your input!"
)

if __name__ == "__main__":
    iface.launch()