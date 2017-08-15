from graphic.render import render_test
from sound.echo import echo_test

# 패키지 내에 각 모듈끼리 namespace를 활용하여 서로를 호출하는 방법
# from game.graphic.render import render_test           절대 참조 방식으로, game/graphic 폴더 내 render라는 모듈 내 render_test 함수를 import함
# from .render import render_test                       현재 파일이 있는 위치 (game이라는 현재 디렉토리 내) graphic 이라는 폴더 내 render 모듈을 호출
# from ..sound.render import render_test                현재 파일이 있는 위치에서의 game이라는 부모폴더 내 sound 폴더 내 render 모듈을 호출

if __name__ == "__main__":
    render_test()
    echo_test()
