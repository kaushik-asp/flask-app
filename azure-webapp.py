from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		print(request.form)
		data = request.form
		# Logic to store the data in the database
		resp_dict = { 'success': 'true' }
		return jsonify(resp_dict)

	elif request.method == 'GET':
		# return render_template('index.html')
		return app.send_static_file('index.html')


if __name__ == '__main__':
	app.run(debug=True)