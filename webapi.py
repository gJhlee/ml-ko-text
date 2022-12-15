from flask import Flask, request
from text_generate import generate
from text_summary import summary
from time import time

app = Flask(__name__)

@app.route("/api/generate")
def generate_api():
	start_time = time()
	text = request.args['text']
	print("---> input text")
	print(text);

	next_text = generate(text);

	print("---> next text")
	print(next_text)

	elapsed_time = time() - start_time
	return f"""<h1>요약</h1>
	<p>걸린시간: {round(elapsed_time, 2)}s</p>
	<h2>원본 텍스트</h2>
	<p>{text}</p>
	<h2>다음 텍스트</h2>
	<p>{next_text}</p>"""


@app.route("/api/summary")
def summary_api():
	start_time = time()
	text = request.args['text']
	print("---> input text")
	print(text);
	inputs = ["summarize: " + text]
	predicted_title = summary(text)
	print("---> summarized text")
	print(predicted_title)

	elapsed_time = time() - start_time
	return f"""<h1>요약</h1>
	<p>걸린시간: {round(elapsed_time, 2)}s</p>
	<p><b>{predicted_title}</b></p>
	<h2>원본 텍스트</h2>
	<p>{text}</p>"""


if __name__ == '__main__':
    app.run()
