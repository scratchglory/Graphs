import random


class Queue:
    def __init__(self):
        self.storage = []

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if (self.size()) > 0:
            return self.storage.pop(0)
        else:
            return None

    def size(self):
        return len(self.storage)


class User:
    def __init__(self, name):
        self.name = name

    # print the names of the objects
    def __repr__(self):
        return f'User({repr(self.name)})'


class SocialGraph:
    def __init__(self):
        # self.last_id = 0
        # self.users = {}
        # self.friendships = {}
        self.reset()

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            # undirected because it is bidirectional which defaults to undirect
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    # create a reset
    def reset(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        # self.last_id = 0
        # self.users = {}
        # self.friendships = {}
        self.reset()
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(f"User {i}")

        # Create friendships
        possible_friendships = []

        # go through all users we have so far
        for user_id in self.users:
            # the same friendship as user 1 to user 2 and vice versa
            for friend_id in range((user_id + 1), self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # random package has a shuffle command
        random.shuffle(possible_friendships)
        # because we are bidirections, each user has the avg friend, but everytime we add friend it is +2, so divide by 2 to counteract the self adding friendship
        for i in range(num_users * avg_friendships // 2):
            friendships = possible_friendships[i]
            self.add_friendship(friendships[0], friendships[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        q = Queue()
        q.enqueue([user_id])

        while q.size() > 0:
            path = q.dequeue()
            # print("path", path)
            newUserId = path[-1]
            if newUserId not in visited:
                visited[newUserId] = path
                for friendId in self.friendships[newUserId]:
                    if friendId not in visited:
                        new_path = list(path)
                        new_path.append(friendId)
                        q.enqueue(new_path)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print("USERS:", sg.users)
    print("FRIENDHIPS:", sg.friendships)
    connections = sg.get_all_social_paths(1)
    print("CONNECTIONS:", connections)
