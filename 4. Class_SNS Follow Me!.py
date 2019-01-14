# -*- coding: utf-8 -*-
#class
print("\n----------------------------------- #Follw Me!")
class User:
    # Initial setting
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.following_list = []    # 이 유저가 팔로우하는 유저 리스트
        self.followers_list = []    # 이 유저를 팔로우하는 유저 리스트

    # follow
    def follow(self, another_user):
        # I follow another
        self.following_list.append(another_user)

        # another follows me
        another_user.followers_list.append(self)

    # total # of following
    def num_following(self):
        return len(self.following_list)

    # total # of followers
    def num_followers(self):
        return len(self.followers_list)

# Create users
user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
user3 = User("Taeho", "taeho@codeit.kr", "123abc")
user4 = User("Lisa", "lisa@codeit.kr", "abc123")

# Test
user1.follow(user2)
user1.follow(user3)
user2.follow(user1)
user2.follow(user3)
user2.follow(user4)
user4.follow(user1)

print(user1.name, user1.num_followers(), user1.num_following())
print(user2.name, user2.num_followers(), user2.num_following())
print(user3.name, user3.num_followers(), user3.num_following())
print(user4.name, user4.num_followers(), user4.num_following())