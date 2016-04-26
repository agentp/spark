# myapp/util/assets.py

from flask.ext.assets import Bundle, Environment
from app import app

bundles = {
    'common_js': Bundle(
        '../../node_modules/react/dist/react.min.js',
        output='gen_files/bundle/common.js'
    ),
    'hello_js': Bundle(
        'gen_files/gulp/hello.js',
        output='gen_files/bundle/hello.js'
    ),
}

assets = Environment(app)

assets.register(bundles)
