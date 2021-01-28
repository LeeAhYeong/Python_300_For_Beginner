movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']

for data in ['스플릿', '배트맨']:
    if data in movie_rank :
        movie_rank.remove(data)

print(movie_rank)

# for-in : range(), list, dict.key() ~
# 추가 : append, insert
# 삭제 : remove, pop, del 명령어