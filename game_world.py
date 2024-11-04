#world = []  # 단일 계층 구조
# world[0]에는 백그라운드 객체들 즉 맨 아래에 그려야 할 객체들
#world[1] 에는 포어라운드 객체들 위에 그려야 할 객체들
world =[[],[],[]]

def add_object(o,depth):
    world[depth].append(o)

def update():
    for layer in world:
        for o in layer:
            o.update()
def render():
    for layer in world:
        for o in layer:
            o.draw()

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return # 지우는 미션은 달성, 다른 요소는 더이상 체크할 필요 없음
    print('에러 : 존재하지 않는 객체를 지운다니..?')