#Ref: https://huggingface.co/beomi/kykim-gpt3-kor-small_based_on_gpt2


print("Loading modules ....")
from transformers import pipeline
from time import time

print("Loading models ....")
_pipe = pipeline('text-generation', model='beomi/kykim-gpt3-kor-small_based_on_gpt2')

def generate(text):
	return _pipe(text)


if __name__ == '__main__':

	print("Start API Server ...")
	from flask import Flask, request

	app = Flask(__name__)

	@app.route("/api/generate")
	def generate():
		start_time = time()
		text = request.args['text']
		print("---> input text")
		print(text);

		next_text = pipe(text);

		print("---> next text")
		print(next_text)

		elapsed_time = time() - start_time
		return f"""<h1>요약</h1>
		<p>걸린시간: {round(elapsed_time, 2)}s</p>
		<h2>원본 텍스트</h2>
		<p>{text}</p>
		<h2>다음 텍스트</h2>
		<p>{next_text}</p>"""

	app.run()