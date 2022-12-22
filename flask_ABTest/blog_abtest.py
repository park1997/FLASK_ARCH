from flask import Flask
from flask import jsonify           # data를 front로 리턴할때 json형태로 보내기 위해
from flask import request           # argument를 받으려면 이런 함수를 써야함, http request를 가져오기 위해
from flask import render_template   # html페이지 return할때 필요함
from flask import make_response     # http 코드 넘겨주기위해

from flask_login import LoginManager    # 맨처음에 세션관리를 등록해줘야함
from flask_login import current_user    # 객체로 로그인된 유저정보를 언제든 참조할수있는 객체
from flask_login import login_required  # 로그인 된 사용자만 access하기 위해
from flask_login import login_user      # 로그인된 해당 객체를 로그인 유저 객체에 넘겨줘야 그다음부터 세션이 만들어지고 해당 세션으로 통신하게끔 구성함
from flask_login import logout_user     # 로그아웃을 할때는 해당 객체를 로그아웃 객체에 넘겨주면됨

from blog_control.user_mgmt import User

from flask_cors import CORS     # flask와 view와같이 백앤드와 프론트앤드가 다른 서버를 쓴다고하면 동일한 웹서버로의 request는 괜찮은데, 웹브라우저상에서 다른 웹서버에다가 스크립트를 기반으로해서 요청하는건 지원안함, 이를 지원하기 위해 도메인 헤더를 넣는 라이브러임


from blog_view import blog

import os   # auuth2 와 같이 보안로그인을 하기위해 사용할 것

# https 만을 지원하는 기능을 http에서 테스트할 때 필요한 설정
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

app = Flask(__name__, static_url_path="/static")
CORS(app)
# 암호화 난수임, 매번 다른 값으로 해야하는데 그동안 설정된 세션은 날라가기때문에 고정된 값으로 함
app.secret_key = "dave_server"

app.register_blueprint(blog.blog_abtest, url_prefix="/blog")

login_maneger = LoginManager()
login_maneger.init_app(app)
login_maneger.session_protection = "strong"

# user_id를 통해 User객체 가져오기
@login_maneger.user_loader
def load_user(user_id):
    return User.get(user_id)

# 로그인이 안된 사용자가 로그인이 된 사용자만 접근할수있는 api들을 request했을경우, 에러가나면서 이 함수가 호출이 된다. 
@login_maneger.unauthorized_handler
def unauthorized():
    return make_response(jsonify(success = False), 401) # 401은 허용이 안되었다는 뜻


if __name__== "__main__":
    app.run(host = "0.0.0.0", port = 8080, debug = True)




