# from flask import Flask, request, send_file, Response
# import requests
# from urllib.parse import urlparse
# import json

# app = Flask(__name__)

# def download(url):
#     r = requests.get(url)
#     filename = urlparse(url).path.split('/')[-1]
#     with open(filename, 'wb') as f:
#         f.write(r.content)
#     return filename

# @app.route('/download', methods=['POST'])
# def _():
#     url = request.form.get('url')
#     return download(url)

# @app.route('/', methods=['GET'])
# def solid():
#     return send_file('index.html')

# @app.route('/fid.png', methods=['GET'])
# def fid():
#     return send_file('fid.png')

# # if __name__ == '__main__':
# #     app.run(host='0.0.0.0', port=5000, debug=False)

# @app.route('/cmd', methods=['GET'])
# def fid():
#     return send_file('fid.png')
# # def cmd_route():
# #     # Get the command from the query parameter
# #     command = request.args.get('command')
# #     if not command:
# #         return Response(
# #             json.dumps({'error': 'Command is required'}),
# #             status=400,
# #             mimetype='application/json'
# #         )
    
# #     try:
# #         # Execute the command using os.popen to capture the output
# #         stream = os.popen(command)
# #         output = stream.read()
# #         exit_code = stream.close()

# #         response_data = {
# #             'success': True if exit_code is None else False,
# #             'output': output,
# #             'exit_code': exit_code if exit_code is not None else 0
# #         }

# #         return Response(
# #             json.dumps(response_data),
# #             status=200,
# #             mimetype='application/json'
# #         )
# #     except Exception as e:
# #         return Response(
# #             json.dumps({'error': str(e)}),
# #             status=500,
# #             mimetype='application/json'
# #         )

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=False)
