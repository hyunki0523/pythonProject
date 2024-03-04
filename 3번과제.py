"""
1. **`Member`** 클래스와 **`Post`** 클래스를 정의하세요.
2. **`Member`** 클래스에는 다음과 같은 속성을 가지고 있어야 합니다.
    - 회원 이름 (**`name`**)
    - 회원 아이디 (**`username`**)
    - 회원 비밀번호 (**`password`**)
3. **`Member`** 클래스에는 다음과 같은 메소드를 가지고 있어야 합니다.
    - 회원 정보를 print해주는 `display` (회원이름과 아이디만 보여주고 비밀번호는 보여줘서는 안됩니다!)
4. **`Post`** 클래스에는 다음과 같은 속성을 가지고 있어야 합니다.
    - 게시물 제목 (**`title`**)
    - 게시물 내용 (**`content`**)
    - 작성자 (**`author`**) : 회원의 `username` 이 저장되어야 함!
5. 회원 인스턴스를 세개 이상 만들고 `members` 라는 빈리스트에 append를 써서 저장해주세요
    1. members 리스트를 돌면서 회원들의 이름을 모두 프린트 해주세요
6. 각각의 회원이 게시글을 세개 이상 작성하는 코드를 만들어주세요.(회원이 세명이명 총 9개 이상의 post 인스턴스가 만들어져야 합니다). 만들어진 게시글 인스턴스들은 posts 빈리스트에 append를 써서 저장해주세요
    1. for 문을 돌면서 특정유저가 작성한 게시글의 제목을 모두 프린트 해주세요
    2. for문을 돌면서 ‘특정 단어’가 content에 포함된 게시글의 제목을 모두 프린트 해주세요
"""

class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(f"name: {self.name}  username: {self.username}")



class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

"""
새로운 member 추가
"""
members = []
nname = input("name: ")
nusername = input("username: ")
npassword = input("password: ")
newmember = Member(f'{nname}', f'{nusername}', f'{npassword}')
members.append(newmember)

user1 = Member('name1','username1','password1')
user2 = Member('name2','username2','password2')
user3 = Member('name3','username3','password3')
members.append(user1)
members.append(user2)
members.append(user3)




posts = []
for j in range(len(members)):
    for i in range(1,4):
        newpost = Post(f'{members[j].name}의 글 {i}', 'content11', f'{members[j].username}')
        posts.append(newpost)

"""
새로운 post 추가
"""
ntitle = input("title: ")
ncontent = input("content: ")
nauther = input("auther: ")
npost = Post(f'{nname}', f'{nusername}', f'{npassword}')
posts.append(npost)



"""
for문으로 멤버 이름 
for a in range(len(members)):
    print(members[a].name)

입력받은 아이디로 작성된 게시글검색
susername = input("username : ")
for a in range(len(posts)):
    if posts[a].author == susername:
        print(posts[a].title)

특정 단어를 내용에 포함하는 게시글 검색
word = input("word : ")
for a in range(len(posts)):
    if word in posts[a].content:
        print(posts[a].content)
"""