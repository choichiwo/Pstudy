토요일 파이썬 특강
IDE(Integrated Development Environment) 통합개발환경
자료형 (리스트, 튜플, 세트, 딕셔너리) !!!!! 공통점 변수 하나에 여러값 저장

CRUD = create read update delete  생성 조회 수정 지우는것 

http://3.134.55.142/ncs/ncs.php?class=ncs6&namer=최치원

리스트(List): 배열(Array) a=[1,2.3] 동질성 데이터 index(순서)0부터 부여 불러올때  a[0:3] 이유는 [시작index:끝index+1] [ :2],[1: ] 공백은 시작부터나 끝까지 len(a) length줄인말 길이확인, 리스트는 값이 중복되어 들어갈수 있음, 다른 타입에 데이터를 넣을 수 있음. .append(추가내용) 끝에추가 .insert(위치,추가내용) 중간에추가 .extend() 추가는 a+b와 비슷하나 다른점은 a값 자체를 a+b형태로 변환시킴 
제거하기 del 리스트명[인덱스] (특정 인덱스만 제거) , 리스트명.pop(인덱스)  (만약 인덱스를 부여안하면 마지막인덱스 적용) , 리스트명.remove(데이터) (해당데이터 제거), 리스트.clear() (모든 값을 제거), a.add(넣을값): 넣으면 마지막인덱스에 들어감 
CRUD해당
for i in List:

튜플(Tuple): () data전달용 수정불가? 
CRD해당
for i in Tuple:

세트(Set): {} 중복X, 순서X(no index) 
합집합: union,| 교집합: intersect, & 차집합:minus, -
CUD해당
for i in Set:

딕셔너리(Dictionary): {키:값}  {'key':'value'}형태로  저장 및 전달용으로 많이 사용
key중복X value중복은 가능,      값을찾을때 인데스 입력이 아님 key값을 넣어야됨 예: n=a['age']
CRUD해당
for x,y in Didt.items():

for x,y in a.items():
    print(x,y)

for x in a:
    print(a[x])


집합을 만드는 방법 예시: a = {1, 2, 3}


class1[0]['eng'] = 리스트안에 여러가지 딕셔너리들이 있을때 원하는 값을 구할떄 

함수(function) : def 함수이름()
1.less code
2.elegance code (가독성, 간단)

routine 반복적으로 단순한 작업